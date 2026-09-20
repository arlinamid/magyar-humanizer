#!/usr/bin/env python3
"""
MyThes tezaurusz-olvasó kereszt-ellenőrzéssel.

A LibreOffice `th_<lang>_v2.dat` fájljait olvassa. A formátum:

    UTF-8                      <- kódolás
    szó|N                      <- N jelentéscsoport
    (szófaj)|szin1|szin2|...   <- egy jelentéscsoport
    ...

A `.dat` fájlhoz nem jár index a LibreOffice repóban, ezért a `build-index`
paranccsal generáljuk: a `.idx` a szó -> bájtoffszet leképezést tárolja, így
a 2 MB-os fájlból nem kell mindent memóriába olvasni.

Használat:

    python dict/thesaurus.py lookup kulcsfontosságú
    python dict/thesaurus.py lookup kiemelkedő --verify
    python dict/thesaurus.py lookup szerep --lang hu_HU --json
    python dict/thesaurus.py build-index --lang hu_HU
    python dict/thesaurus.py stats
"""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
import unicodedata
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
DEFAULT_LANG = "hu_HU"


# --------------------------------------------------------------- segédek


def _norm(w: str) -> str:
    """Kisbetűsít és Unicode-normalizál — a .dat kulcsai így vannak tárolva."""
    return unicodedata.normalize("NFC", w.strip().lower())


def lang_dir(lang: str) -> Path:
    d = DATA / lang
    if not d.is_dir():
        raise SystemExit(
            f"Nincs letöltve: {lang}\n"
            f"  Telepítsd:  python dict/fetch.py --lang {lang}"
        )
    return d


def find_file(lang: str, prefix: str = "", suffix: str = "") -> Path | None:
    d = DATA / lang
    if not d.is_dir():
        return None
    for p in sorted(d.iterdir()):
        if p.name.startswith(prefix) and p.name.endswith(suffix):
            return p
    return None


# --------------------------------------------------------------- index


def build_index(lang: str = DEFAULT_LANG, quiet: bool = False) -> Path:
    """Végigolvassa a .dat-ot és kiírja a szó->offszet indexet."""
    dat = find_file(lang, "th_", ".dat")
    if dat is None:
        raise SystemExit(f"Nincs tezaurusz ehhez: {lang}")
    idx = dat.with_suffix(".idx")

    entries: list[tuple[str, int]] = []
    with open(dat, "rb") as f:
        encoding = f.readline().decode("ascii", "replace").strip() or "UTF-8"
        offset = f.tell()
        while True:
            raw = f.readline()
            if not raw:
                break
            line = raw.decode(encoding, "replace").rstrip("\r\n")
            # A szócikkfej az egyetlen sor, ami nem '|'-lel vagy '('-lel kezdődik
            # és a végén a jelentéscsoportok száma áll.
            if line and not line.startswith(("|", "(")):
                head, _, count = line.rpartition("|")
                if head and count.strip().isdigit():
                    entries.append((head, offset))
            offset = f.tell()

    with io.open(idx, "w", encoding="utf-8", newline="\n") as out:
        out.write(f"{encoding}\n{len(entries)}\n")
        for word, off in entries:
            out.write(f"{word}|{off}\n")

    if not quiet:
        print(f"{idx.name}: {len(entries)} szócikk indexelve")
    return idx


class Thesaurus:
    def __init__(self, lang: str = DEFAULT_LANG):
        self.lang = lang
        lang_dir(lang)
        dat = find_file(lang, "th_", ".dat")
        if dat is None:
            raise SystemExit(f"Nincs tezaurusz ehhez: {lang}")
        self.dat = dat
        self.idx = dat.with_suffix(".idx")
        if not self.idx.exists():
            build_index(lang, quiet=True)
        self.encoding, self.index = self._load_index()

    def _load_index(self) -> tuple[str, dict[str, int]]:
        index: dict[str, int] = {}
        with io.open(self.idx, encoding="utf-8") as f:
            encoding = f.readline().strip()
            f.readline()  # darabszám
            for line in f:
                word, _, off = line.rstrip("\n").rpartition("|")
                if off.isdigit():
                    index[_norm(word)] = int(off)
        return encoding, index

    def lookup(self, word: str) -> list[dict]:
        """Jelentéscsoportok listája: [{'pos': str, 'synonyms': [str, ...]}]."""
        off = self.index.get(_norm(word))
        if off is None:
            return []
        senses = []
        with open(self.dat, "rb") as f:
            f.seek(off)
            head = f.readline().decode(self.encoding, "replace").rstrip("\r\n")
            _, _, count = head.rpartition("|")
            for _ in range(int(count)):
                line = f.readline().decode(self.encoding, "replace").rstrip("\r\n")
                parts = [p for p in line.split("|")]
                pos = parts[0].strip("()") if parts and parts[0] else ""
                syns = [p.strip() for p in parts[1:] if p.strip()]
                senses.append({"pos": pos, "synonyms": syns})
        return senses

    def __contains__(self, word: str) -> bool:
        return _norm(word) in self.index


# --------------------------------------------------------------- helyesírás


def get_speller(lang: str = DEFAULT_LANG):
    """
    A helyesírás-ellenőrzés a dict/spell.py motorját használja (teljes hunspell),
    nem puszta szólista-tagságot. A magyarban ez nem finomhangolás: a
    „kulcsfontosságú" nincs benne külön a .dic-ben, mert a hunspell
    összetételként állítja elő — szólistával téves hibának látszana.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        from spell import Speller

        return Speller(lang)
    except SystemExit:
        raise
    except Exception:
        return None


# --------------------------------------------------------------- ellenőrzés


def verify(th: Thesaurus, word: str, spell=None) -> dict:
    """
    Kereszt-ellenőrzés — ezt a JSON-alapú adatbázis nem tudta:

    1. helyesírás  — szótári alak-e a jelölt (hunspell .dic)
    2. kölcsönösség — a jelölt szócikkében visszajön-e az eredeti szó
    3. jelentéscsoport — melyik jelentésből jött, milyen szófajjal

    A kölcsönösség a legerősebb jel: az egyirányú kapcsolat gyakran csak laza
    asszociáció, a kölcsönös viszont valódi szinonimapár.
    """
    senses = th.lookup(word)
    out = {"word": word, "lang": th.lang, "found": bool(senses), "senses": []}
    for sense in senses:
        checked = []
        for cand in sense["synonyms"]:
            back = th.lookup(cand)
            reciprocal = any(
                _norm(word) == _norm(s) for grp in back for s in grp["synonyms"]
            )
            checked.append(
                {
                    "synonym": cand,
                    "spelled": spell.check(cand) if spell else None,
                    "reciprocal": reciprocal,
                    "in_thesaurus": cand in th,
                }
            )
        out["senses"].append({"pos": sense["pos"], "candidates": checked})
    return out


# --------------------------------------------------------------- kimenet


def print_lookup(th: Thesaurus, word: str, spell, do_verify: bool):
    senses = th.lookup(word)
    if not senses:
        print(f"'{word}' — nincs a tezauruszban ({th.lang}).")
        if spell and not spell.check(word):
            print("  A szó a helyesírási szótárban sincs meg — elgépelés?")
        print("  A tezaurusz szótári alakokat tárol: told vissza alapalakra.")
        return

    print(f"{word}  ({th.lang}, {len(senses)} jelentéscsoport)\n")
    for i, sense in enumerate(senses, 1):
        label = f"  {i}. " + (f"({sense['pos']}) " if sense["pos"] else "")
        if not do_verify:
            print(label + ", ".join(sense["synonyms"]))
            continue
        print(label.rstrip())
        for cand in sense["synonyms"]:
            back = th.lookup(cand)
            recip = any(
                _norm(word) == _norm(s) for grp in back for s in grp["synonyms"]
            )
            ok_spell = spell.check(cand) if spell else None
            marks = []
            marks.append("kölcsönös" if recip else "egyirányú")
            if ok_spell is False:
                marks.append("HELYESÍRÁS: nincs a szótárban")
            print(f"       {cand:<28} {', '.join(marks)}")
        print()

    if do_verify:
        print(
            "  A kölcsönös pár megbízhatóbb csere. Az egyirányú gyakran laza\n"
            "  asszociáció — cserélés előtt nézd meg a jelentéscsoportot."
        )


def cmd_stats(args):
    if not DATA.is_dir():
        raise SystemExit("Nincs letöltött szótár. Futtasd: python dict/fetch.py")
    langs = sorted(p.name for p in DATA.iterdir() if p.is_dir())
    if not langs:
        raise SystemExit("Nincs letöltött szótár. Futtasd: python dict/fetch.py")
    print(f"{'nyelv':<12} {'tezaurusz':>10} {'helyesírás':>12}  fájlok")
    for lang in langs:
        try:
            th = Thesaurus(lang)
            n_th = f"{len(th.index):,}".replace(",", " ")
        except SystemExit:
            n_th = "-"
        try:
            sp = get_speller(lang)
            n_sp = sp.engine if sp else "-"
        except SystemExit:
            n_sp = "-"
        files = len([p for p in (DATA / lang).iterdir() if p.is_file()])
        print(f"{lang:<12} {n_th:>10} {n_sp:>12}  {files}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("lookup", help="szinonimák keresése")
    p.add_argument("word")
    p.add_argument("--lang", default=DEFAULT_LANG)
    p.add_argument("--verify", action="store_true", help="kereszt-ellenőrzés")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("build-index", help="tezaurusz-index generálása")
    p.add_argument("--lang", default=DEFAULT_LANG)

    sub.add_parser("stats", help="letöltött szótárak")

    args = ap.parse_args()

    if args.cmd == "build-index":
        build_index(args.lang)
    elif args.cmd == "stats":
        cmd_stats(args)
    else:
        th = Thesaurus(args.lang)
        spell = get_speller(args.lang)
        if args.json:
            print(json.dumps(verify(th, args.word, spell), ensure_ascii=False, indent=2))
        else:
            print_lookup(th, args.word, spell, args.verify)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
