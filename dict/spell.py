#!/usr/bin/env python3
"""
Helyesírás-ellenőrző a humanizált szöveghez.

A magyar erősen toldalékoló és összetételt képző nyelv, ezért a szólista-tagság
önmagában nem elég: a „kulcsfontosságú" például nem szerepel külön a .dic-ben,
a hunspell mégis helyesnek ismeri fel, mert összetételként előállítja. Ezért a
teljes hunspell motort használjuk (spylls), és csak végső esetben esünk vissza
a szólistára.

    python dict/spell.py check szoveg.md
    python dict/spell.py check - < szoveg.txt
    python dict/spell.py check szoveg.md --suggest
    python dict/spell.py word kiemelkedo --suggest
    python dict/spell.py engine

Kivételek: az adatbázisban (`python dict/db.py ignore add <szó> --reason idegen`).
"""

from __future__ import annotations

import argparse
import io
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

DICT_DIR = Path(__file__).resolve().parent
DATA = DICT_DIR / "data"
DB = DICT_DIR / "humanizer.db"
IGNORE_SEED = DICT_DIR / "seed-ignore.tsv"
DEFAULT_LANG = "hu_HU"


def _norm(w: str) -> str:
    return unicodedata.normalize("NFC", w)


# --------------------------------------------------------------- motor


def _patch_spylls() -> None:
    """
    A magyar .dic REP-mintái között van olyan, amit a spylls regexként fordít,
    de nem érvényes regex (pl. lezáratlan karakterosztály). Ilyenkor a minta
    literálként is jó — enélkül a szótár be sem töltődik.
    """
    import re as _re

    from spylls.hunspell.data import aff as aff_mod

    original = aff_mod.RepPattern.__post_init__

    def tolerant(self):
        try:
            original(self)
        except _re.error:
            self.regexp = _re.compile(_re.escape(self.pattern))

    aff_mod.RepPattern.__post_init__ = tolerant


def _base_path(lang: str) -> Path | None:
    d = DATA / lang
    if not d.is_dir():
        return None
    for p in sorted(d.glob("*.dic")):
        if p.name.startswith("hyph_"):
            continue
        if p.with_suffix(".aff").exists():
            return p.with_suffix("")
    return None


class Speller:
    """
    Három szint, ebben a sorrendben:

      hunspell  — spylls, teljes ragozás- és összetétel-kezelés (ajánlott)
      enchant   — pyenchant, ha rendszerszinten telepítve van a hu_HU
      wordlist  — puszta .dic tagság; csak szótári alakokra megbízható
    """

    def __init__(self, lang: str = DEFAULT_LANG):
        self.lang = lang
        self.engine = "none"
        self._d = None
        self._words: set[str] = set()

        base = _base_path(lang)
        if base is None:
            raise SystemExit(
                f"Nincs letöltve a(z) {lang} szótár.\n"
                f"  Telepítsd:  python dict/fetch.py --lang {lang}"
            )

        try:
            _patch_spylls()
            from spylls.hunspell import Dictionary

            self._d = Dictionary.from_files(str(base))
            self.engine = "hunspell"
            return
        except ImportError:
            pass
        except Exception as e:  # sérült vagy szokatlan szótár
            print(f"spylls betöltés sikertelen ({e}); visszaesés.", file=sys.stderr)

        try:
            import enchant

            self._d = enchant.Dict(lang)
            self.engine = "enchant"
            return
        except Exception:
            pass

        with io.open(base.with_suffix(".dic"), encoding="utf-8", errors="replace") as f:
            first = f.readline().strip()
            if not first.isdigit():
                f.seek(0)
            for line in f:
                w = line.split("/", 1)[0].split("\t", 1)[0].strip()
                if w:
                    self._words.add(_norm(w).lower())
        self.engine = "wordlist"

    @property
    def reliable(self) -> bool:
        """A szólista csak szótári alakokra megbízható — ragozott szövegre nem."""
        return self.engine in ("hunspell", "enchant")

    def check(self, word: str) -> bool:
        w = _norm(word)
        if self.engine == "hunspell":
            return bool(self._d.lookup(w))
        if self.engine == "enchant":
            return bool(self._d.check(w))
        return w.lower() in self._words

    def suggest(self, word: str, limit: int = 5) -> list[str]:
        w = _norm(word)
        try:
            if self.engine == "hunspell":
                out = []
                for s in self._d.suggest(w):
                    out.append(s)
                    if len(out) >= limit:
                        break
                return out
            if self.engine == "enchant":
                return list(self._d.suggest(w))[:limit]
        except Exception:
            pass
        return []


# --------------------------------------------------------------- szöveg


FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
URL = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+")
MD_LINK_TARGET = re.compile(r"\]\([^)]*\)")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
HTML_TAG = re.compile(r"</?[a-zA-Z][^>]*>")
# Azonosítók és fájlnevek: `hu_HU`, `build.js`, `dict/data` — ezek nem szavak,
# és szétvágva értelmetlen töredékeket adnának ("hu", "ben", "md").
IDENTIFIER = re.compile(r"\S*[_/\\]\S*|\b[\w-]+(?:\.[\w-]+)+")
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
# A számjegyet is beleveszzük, hogy az „1989-ben", „Q3-ban", „2-nél" EGY token
# legyen. Külön nem szabad vágni: a puszta toldalék („ben", „nél") téves
# hibaként jelenne meg. A számot tartalmazó tokent utána kihagyjuk.
WORD = re.compile(r"[^\W_]+(?:%?[-'’][^\W_]+)*", re.UNICODE)
HAS_DIGIT = re.compile(r"\d")
# Csupa nagybetűs rövidítés: AI, MI, LLM, CV, KPI — magyar szövegben toldalékot
# kötőjellel kapnak (AI-szag, LLM-ek), és a hunspell nem ismeri őket
ABBREV = re.compile(r"\A[A-ZÁÉÍÓÖŐÚÜŰ]{2,}\Z")


def load_ignore(lang: str = DEFAULT_LANG) -> set[str]:
    """
    A kivételeket az adatbázis tárolja, nem szövegfájl: így van eredete,
    indoka és használatszáma minden szónak, és ugyanúgy kereshető, mint a
    többi felhalmozott tudás.

    Közvetlenül sqlite3-mal olvasunk, nem a `db` modulon át — az importálja
    innen a `Speller`-t, tehát a modulszintű import körkörös lenne.
    """
    out: set[str] = set()
    if DB.exists():
        try:
            con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
            try:
                out = {
                    _norm(w).lower()
                    for (w,) in con.execute(
                        "SELECT word FROM ignore_words WHERE lang=?", (lang,)
                    )
                }
            finally:
                con.close()
        except sqlite3.Error:
            pass

    # Ha az adatbázis még nincs felépítve, a verziókövetett mag is megteszi.
    if not out and IGNORE_SEED.exists():
        with io.open(IGNORE_SEED, encoding="utf-8") as f:
            header = None
            for line in f:
                if line.startswith("#") or not line.strip():
                    continue
                parts = line.rstrip("\n").split("\t")
                if header is None:
                    header = parts
                    continue
                if parts and parts[0]:
                    out.add(_norm(parts[0]).lower())
    return out


def iter_words(text: str, skip_code: bool = True, skip_frontmatter: bool = True):
    """(sorszám, szó) párokat ad vissza, a nem szövegszerű részeket kihagyva."""
    offset = 0
    if skip_frontmatter:
        m = FRONTMATTER.match(text)
        if m:
            # A frontmatter gépi metaadat, jellemzően angolul — nem szöveg
            offset = text[: m.end()].count("\n")
            text = text[m.end() :]
    text = HTML_COMMENT.sub(" ", text)
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1 + offset):
        if skip_code and FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if skip_code:
            line = INLINE_CODE.sub(" ", line)
        line = MD_LINK_TARGET.sub(" ", line)
        line = URL.sub(" ", line)
        line = HTML_TAG.sub(" ", line)
        line = IDENTIFIER.sub(" ", line)
        for m in WORD.finditer(line):
            # Idézőjel vagy zárójel után kötőjellel kapcsolt toldalék:
            # „kiemelkedő"-höz, (M3)-at. A kötőjel előtti rész nem szó, ezért a
            # regex csak a toldalékot fogja meg — az pedig önmagában értelmetlen.
            if m.start() > 0 and line[m.start() - 1] == "-":
                continue
            yield lineno, m.group(0)


def _acceptable(word: str, sp: Speller, ignore: set[str]) -> bool:
    key = _norm(word).lower()
    if key in ignore or len(word) == 1:
        return True
    if HAS_DIGIT.search(word):  # „1989-ben", „Q3-ban" — szám, nem szó
        return True
    if ABBREV.match(word):
        return True
    # Rövidítés + kötőjeles toldalék: „LLM-ek", „CV-ban", „KPI-kat", „AI-szag".
    # A kötőjel utáni rész toldalék vagy utótag, nem önálló szó — ha az első
    # tag rövidítés, a szó rendben van.
    head, sep, tail = word.partition("-")
    if sep and (ABBREV.match(head) or head.lower() in ignore) and tail:
        return True
    if sp.check(word):
        return True
    # Mondatkezdő nagybetű miatt kisbetűvel is megnézzük
    if word[:1].isupper() and sp.check(word.lower()):
        return True
    # Kötőjeles összetétel: minden tag külön elfogadható-e? Ez kezeli a magyar
    # „AI-szag", „LLM-ek", „CV-ban" alakokat, ahol a rövidítés kapja a toldalékot.
    if "-" in word:
        parts = [p for p in word.split("-") if p]
        if len(parts) > 1 and all(
            p.lower() in ignore or ABBREV.match(p) or sp.check(p) or sp.check(p.lower())
            for p in parts
        ):
            return True
    return False


def check_text(text: str, sp: Speller, ignore: set[str], skip_code: bool = True) -> dict:
    seen: dict[str, dict] = {}
    total = 0
    for lineno, word in iter_words(text, skip_code):
        total += 1
        key = _norm(word).lower()
        if _acceptable(word, sp, ignore):
            continue
        e = seen.setdefault(key, {"word": word, "count": 0, "lines": []})
        e["count"] += 1
        if len(e["lines"]) < 5:
            e["lines"].append(lineno)
    return {"total_words": total, "unknown": seen}


# --------------------------------------------------------------- CLI


def cmd_check(args):
    if args.path == "-":
        text = sys.stdin.read()
        label = "<stdin>"
    else:
        p = Path(args.path)
        if not p.exists():
            raise SystemExit(f"Nincs ilyen fájl: {p}")
        text = p.read_text("utf-8", errors="replace")
        label = str(p)

    sp = Speller(args.lang)
    result = check_text(text, sp, load_ignore(), skip_code=not args.include_code)
    unknown = result["unknown"]

    print(f"{label} — {result['total_words']} szó, motor: {sp.engine}")
    if not sp.reliable:
        print(
            "  FIGYELEM: szólista-visszaesés. Ez csak szótári alakokra megbízható,\n"
            "  ragozott alakokat tévesen hibásnak jelöl. Telepítsd:  pip install spylls"
        )

    if not unknown:
        print("  Nincs ismeretlen szó.")
        return 0

    print(f"  {len(unknown)} ismeretlen szó:\n")
    for e in sorted(unknown.values(), key=lambda x: (-x["count"], x["word"])):
        lines = ", ".join(str(n) for n in e["lines"])
        more = "…" if e["count"] > len(e["lines"]) else ""
        head = f"  {e['word']:<28} {e['count']}x  (sor: {lines}{more})"
        if args.suggest:
            s = sp.suggest(e["word"])
            head += "  ->  " + (", ".join(s) if s else "nincs javaslat")
        print(head)

    print(
        "\n  Ami szándékos (angol szakszó, név, márka), vedd fel kivételnek:"
        "\n    python dict/db.py ignore add <szó> --reason idegen|tulajdonnev|marka|szakszo"
    )
    return 1 if args.strict else 0


def cmd_word(args):
    sp = Speller(args.lang)
    ok = sp.check(args.word)
    print(f"{args.word}: {'helyes' if ok else 'NEM ismert'}  (motor: {sp.engine})")
    if not ok and args.suggest:
        s = sp.suggest(args.word)
        print("  javaslat: " + (", ".join(s) if s else "nincs"))
    return 0 if ok else 1


def cmd_engine(args):
    sp = Speller(args.lang)
    print(f"nyelv:  {sp.lang}")
    print(f"motor:  {sp.engine}")
    print(f"megbízható ragozott alakokra: {'igen' if sp.reliable else 'nem'}")
    if not sp.reliable:
        print("\n  pip install spylls   — ezzel lesz teljes ragozás- és összetétel-kezelés")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", default=DEFAULT_LANG)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check", help="fájl vagy stdin ellenőrzése")
    p.add_argument("path")
    p.add_argument("--suggest", action="store_true", help="javaslatok a hibás szavakhoz")
    p.add_argument("--include-code", action="store_true", help="kódblokkok is")
    p.add_argument("--strict", action="store_true", help="hibakóddal lép ki, ha van találat")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("word", help="egyetlen szó ellenőrzése")
    p.add_argument("word")
    p.add_argument("--suggest", action="store_true")
    p.set_defaults(fn=cmd_word)

    sub.add_parser("engine", help="melyik motor aktív").set_defaults(fn=cmd_engine)

    args = ap.parse_args()
    sys.exit(args.fn(args) or 0)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
