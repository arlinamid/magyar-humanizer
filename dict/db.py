#!/usr/bin/env python3
"""
A humanizáló saját adatbázisa — amit munka közben ő maga épít.

Miért nem JSON és miért nem beégetett lista?

A korábbi `synonyms.json` két dolgot nem tudott: nem volt benne kereszt-
ellenőrzés (bármilyen elgépelt vagy rossz jelentésű javaslat bekerülhetett),
és nehezen lehetett feldolgozni. Egy beégetett lista pedig attól sem lesz jobb,
hogy hosszabb: ugyanazt a néhány esetet ismétli, és nem tanul.

Itt ezért az adatbázis a munka mellékterméke. Amikor a skill kicserél egy
fordulatot, rögzíti: mit mire, melyik minta alapján, milyen mondatban. Minden
bejegyzés átmegy a kereszt-ellenőrzésen (helyesírás, tezaurusz, kölcsönösség),
és az eredmény is eltárolódik, tehát utólag látszik, mi mennyire megbízható.

    python3 <skill-mappa>/dict/db.py init          # séma + mag betöltése
    python3 <skill-mappa>/dict/db.py add "szerepet játszik" "hat" --pattern M3
    python3 <skill-mappa>/dict/db.py scan szoveg.md  # ismert fordulatok keresése
    python3 <skill-mappa>/dict/db.py lookup "kiemelkedő"
    python3 <skill-mappa>/dict/db.py verify          # kereszt-ellenőrzések újra
    python3 <skill-mappa>/dict/db.py stats
    python3 <skill-mappa>/dict/db.py export --out dump.tsv

Az adatbázis helyét a dict/paths.py adja (a dict/ mappa, ha írható, különben
a felhasználói adatmappa; felülírható: MAGYAR_HUMANIZER_HOME).
"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import re
import sqlite3
import sys
from pathlib import Path

DICT_DIR = Path(__file__).resolve().parent
ROOT = DICT_DIR.parent
sys.path.insert(0, str(DICT_DIR))
from paths import DB as DB_PATH, IGNORE_TSV, SEED_TSV, seed_digest, skill_cmd  # noqa: E402

SKILL = ROOT / "references" / "layer-b-hungarian.md"

SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS entries (
  id            INTEGER PRIMARY KEY,
  kind          TEXT NOT NULL CHECK (kind IN ('phrase','word')),
  lang          TEXT NOT NULL DEFAULT 'hu_HU',
  source_text   TEXT NOT NULL,
  replacement   TEXT NOT NULL,
  category      TEXT,
  pattern       TEXT,
  origin        TEXT NOT NULL CHECK (origin IN ('seed','learned','manual')),
  note          TEXT,
  times_used    INTEGER NOT NULL DEFAULT 0,
  first_seen    TEXT NOT NULL,
  last_used     TEXT,
  UNIQUE (kind, lang, source_text, replacement)
);

CREATE INDEX IF NOT EXISTS idx_entries_source ON entries(lang, source_text);
CREATE INDEX IF NOT EXISTS idx_entries_pattern ON entries(pattern);

-- A kereszt-ellenőrzések eredménye. Külön táblában, mert több ellenőrzés
-- fut bejegyzésenként, és mert újra lehet futtatni őket a szótár frissülésekor.
CREATE TABLE IF NOT EXISTS checks (
  entry_id      INTEGER NOT NULL REFERENCES entries(id) ON DELETE CASCADE,
  name          TEXT NOT NULL CHECK (name IN ('spelling','thesaurus','reciprocal')),
  passed        INTEGER,
  detail        TEXT,
  checked_at    TEXT NOT NULL,
  PRIMARY KEY (entry_id, name)
);

-- Helyesírási kivételek: szavak, amiket a hunspell nem ismer, de szándékosak.
-- Ez is felhalmozódó tudás, ezért ide tartozik és nem külön szövegfájlba: így
-- van eredete, indoka és használatszáma, és ugyanúgy exportálható, mint a többi.
CREATE TABLE IF NOT EXISTS ignore_words (
  id            INTEGER PRIMARY KEY,
  word          TEXT NOT NULL,
  lang          TEXT NOT NULL DEFAULT 'hu_HU',
  reason        TEXT NOT NULL CHECK (reason IN
                  ('szakszo','tulajdonnev','marka','idegen','magyar-hianyzo','egyeb')),
  note          TEXT,
  origin        TEXT NOT NULL CHECK (origin IN ('seed','learned','manual')),
  times_seen    INTEGER NOT NULL DEFAULT 0,
  first_seen    TEXT NOT NULL,
  UNIQUE (lang, word)
);

CREATE INDEX IF NOT EXISTS idx_ignore_word ON ignore_words(lang, word);

-- Valódi előfordulások: ez adja a bizonyítékot a bejegyzés mögé.
CREATE TABLE IF NOT EXISTS contexts (
  id            INTEGER PRIMARY KEY,
  entry_id      INTEGER NOT NULL REFERENCES entries(id) ON DELETE CASCADE,
  before        TEXT NOT NULL,
  after         TEXT,
  seen_at       TEXT NOT NULL
);

-- Kulcs–érték tár: itt áll, melyik seed.tsv-változat van betöltve, hogy
-- frissítéskor a magból kikerült bejegyzéseket is el lehessen távolítani.
CREATE TABLE IF NOT EXISTS meta (
  key           TEXT PRIMARY KEY,
  value         TEXT
);

CREATE VIEW IF NOT EXISTS v_entries AS
SELECT
  e.id, e.kind, e.lang, e.source_text, e.replacement, e.category, e.pattern,
  e.origin, e.times_used, e.note,
  MAX(CASE WHEN c.name='spelling'   THEN c.passed END) AS ok_spelling,
  MAX(CASE WHEN c.name='thesaurus'  THEN c.passed END) AS ok_thesaurus,
  MAX(CASE WHEN c.name='reciprocal' THEN c.passed END) AS ok_reciprocal,
  (SELECT COUNT(*) FROM contexts x WHERE x.entry_id = e.id) AS n_contexts
FROM entries e
LEFT JOIN checks c ON c.entry_id = e.id
GROUP BY e.id;
"""


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def connect(path: Path = DB_PATH) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


# --------------------------------------------------------------- ellenőrzés


_tools = {}


def tools(lang: str = "hu_HU"):
    """A helyesírás- és tezaurusz-motor lusta betöltése (a hunspell ~3 s)."""
    if lang in _tools:
        return _tools[lang]
    speller = thes = None
    # A Speller/Thesaurus SystemExit-tel jelzi, ha nincs letöltött szótár —
    # itt ez nem végzetes: az ellenőrzés az adott mezőt n.a.-n hagyja.
    try:
        from spell import Speller

        speller = Speller(lang)
    except (Exception, SystemExit):
        pass
    try:
        from thesaurus import Thesaurus

        thes = Thesaurus(lang)
    except (Exception, SystemExit):
        pass
    _tools[lang] = (speller, thes)
    return _tools[lang]


def run_checks(con: sqlite3.Connection, entry_id: int, verbose: bool = False) -> dict:
    """
    Három kereszt-ellenőrzés minden bejegyzésre:

      spelling   — a javasolt csere minden szava valódi szó-e (teljes hunspell)
      thesaurus  — szerepel-e a csere a tezauruszban szócikként (egyszavas eseteknél)
      reciprocal — kölcsönös-e a szinonimaviszony: a csere a forrásszó
                   csoportjában ÉS a forrásszó a csere csoportjában is szerepel.
                   Ez a legerősebb jel, mert az egyirányú kapcsolat gyakran csak
                   laza asszociáció.

    A fordulatoknál (több szó) a tezaurusz nem alkalmazható — ott a mező NULL
    marad, nem pedig „bukott". Ez fontos: a hiányzó adat nem hiba.
    """
    row = con.execute("SELECT * FROM entries WHERE id=?", (entry_id,)).fetchone()
    if row is None:
        raise SystemExit(f"Nincs ilyen bejegyzés: {entry_id}")
    speller, thes = tools(row["lang"])
    out = {}

    # Az útmutató jellegű javaslat („mondd meg, mi változott") nem csere,
    # tehát nincs mit helyesírás szerint ellenőrizni rajta.
    guidance = row["replacement"].startswith(("mondd", "töröld", "[")) or len(
        row["replacement"].split()
    ) > 6

    if speller and not guidance:
        words = re.findall(r"[^\W\d_]+", row["replacement"])
        bad = [w for w in words if not speller.check(w) and not speller.check(w.lower())]
        out["spelling"] = (not bad, ", ".join(bad) if bad else f"motor: {speller.engine}")

    if thes and row["kind"] == "word":
        cand = row["replacement"].strip()
        src = row["source_text"].strip()
        out["thesaurus"] = (cand in thes, "" if cand in thes else "nincs a tezauruszban")

        # A kölcsönösség csak akkor értelmezhető, ha a FORRÁSSZÓ is szerepel a
        # tezauruszban. Ha nem, a válasz „nem tudjuk", nem pedig „rossz" — a
        # skill épp az olyan AI-klisékkel dolgozik (kulcsfontosságú, mélységes),
        # amelyek szándékosan hiányoznak a szótárból.
        senses = thes.lookup(src)
        if not senses:
            out["reciprocal"] = (None, "a forrásszó nincs a tezauruszban — nem értelmezhető")
        else:
            fwd = any(cand.lower() == s.lower() for g in senses for s in g["synonyms"])
            back = any(
                src.lower() == s.lower() for g in thes.lookup(cand) for s in g["synonyms"]
            )
            recip = fwd and back
            detail = (
                "" if recip
                else "nem szerepel a forrásszó jelentéscsoportjában" if not fwd
                else "egyirányú: a csere szócikkében nincs vissza a forrásszó"
            )
            out["reciprocal"] = (recip, detail)

    for name, (passed, detail) in out.items():
        con.execute(
            "INSERT INTO checks (entry_id,name,passed,detail,checked_at) VALUES (?,?,?,?,?) "
            "ON CONFLICT(entry_id,name) DO UPDATE SET passed=excluded.passed, "
            "detail=excluded.detail, checked_at=excluded.checked_at",
            (entry_id, name, None if passed is None else (1 if passed else 0), detail, now()),
        )
    con.commit()
    if verbose:
        for k, (p, d) in out.items():
            print(f"    {k:<11} {_flag(None if p is None else int(bool(p)))}  {d}")
    return out


# --------------------------------------------------------------- műveletek


def add_entry(
    con: sqlite3.Connection,
    source_text: str,
    replacement: str,
    *,
    kind: str | None = None,
    category: str | None = None,
    pattern: str | None = None,
    origin: str = "learned",
    note: str | None = None,
    context: str | None = None,
    lang: str = "hu_HU",
    check: bool = True,
) -> int:
    kind = kind or ("word" if len(source_text.split()) == 1 else "phrase")
    cur = con.execute(
        "INSERT INTO entries (kind,lang,source_text,replacement,category,pattern,origin,note,"
        "times_used,first_seen,last_used) VALUES (?,?,?,?,?,?,?,?,0,?,NULL) "
        "ON CONFLICT(kind,lang,source_text,replacement) DO NOTHING",
        (kind, lang, source_text, replacement, category, pattern, origin, note, now()),
    )
    if cur.rowcount:
        entry_id = cur.lastrowid
    else:
        entry_id = con.execute(
            "SELECT id FROM entries WHERE kind=? AND lang=? AND source_text=? AND replacement=?",
            (kind, lang, source_text, replacement),
        ).fetchone()["id"]

    if origin == "learned":
        con.execute(
            "UPDATE entries SET times_used = times_used + 1, last_used = ? WHERE id = ?",
            (now(), entry_id),
        )
    if context:
        con.execute(
            "INSERT INTO contexts (entry_id,before,after,seen_at) VALUES (?,?,?,?)",
            (entry_id, context, None, now()),
        )
    con.commit()
    if check:
        run_checks(con, entry_id)
    return entry_id


# --------------------------------------------------------------- seed


SECTIONS = {
    "## M3. Terpeszkedő kifejezések": ("terpeszkedo", "M3"),
    "### Kerülendő bevezető fordulatok": ("bevezeto", "M5"),
    # A „Felfújt fontosság” tábla szándékosan nincs itt: a jobb oldala utasítás
    # („töröld”, „mondd meg, mi változott”), nem beírható csere.
}
ROW = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")
SEP = re.compile(r"^\|[\s:|-]+\|$")
SKIP_FIRST_COL = {"terpeszkedő", "kerülendő", "ai-felfújt"}


def _clean(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    s = s.strip().strip("„”\"'")
    # A táblákban a fordulat gyakran folytatásjellel áll („Fontos megjegyezni,
    # hogy…"); a kereséshez a jel nem kell, különben sosem illeszkedne.
    return re.sub(r"\s*(\.\.\.|…)\s*$", "", s).strip()


def parse_skill(skill: Path = SKILL) -> list[tuple[str, str, str, str]]:
    label = pattern = None
    header_seen = False
    out = []
    for line in skill.read_text("utf-8").split("\n"):
        if line.startswith(("## ", "### ")):
            hit = SECTIONS.get(line.strip())
            label, pattern = hit if hit else (None, None)
            header_seen = False
            continue
        if label is None:
            continue
        if SEP.match(line):
            header_seen = True
            continue
        m = ROW.match(line)
        if not m:
            if not line.strip() and header_seen:
                label = None
            continue
        if not header_seen:
            continue
        src, dst = _clean(m.group(1)), _clean(m.group(2))
        if src and dst and src.lower() not in SKIP_FIRST_COL:
            out.append((label, pattern, src, dst))
    return out


def cmd_seed(args):
    """
    Induló készlet a B réteg M3/M5 tábláiból — hogy az adatbázis ne nulláról induljon.

    Ez NEM igazságforrás, csak mag: `origin='seed'`. A valódi tartalom onnan jön,
    hogy a skill munka közben rögzíti, mit cserélt (`origin='learned'`).
    """
    con = connect(args.db)
    rows = parse_skill()
    if not rows:
        raise SystemExit(f"Nem találtam táblázatsort itt: {SKILL} — változott a szerkezet?")
    before = con.execute("SELECT COUNT(*) c FROM entries").fetchone()["c"]
    for label, pattern, src, dst in rows:
        add_entry(
            con, src, dst, category=label, pattern=pattern, origin="seed",
            check=not args.no_check,
        )
    after = con.execute("SELECT COUNT(*) c FROM entries").fetchone()["c"]
    print(f"{len(rows)} sor a B rétegből, {after - before} új bejegyzés (összesen {after}).")
    if args.no_check:
        print("Kereszt-ellenőrzés kihagyva. Futtatás: python dict/db.py verify")


# --------------------------------------------------------------- CLI


EXPORT_COLS = ["kind", "lang", "source_text", "replacement", "category",
               "pattern", "origin", "times_used", "note"]


def dump_seed(con: sqlite3.Connection, path: Path = SEED_TSV) -> int:
    """
    Szöveges mag a repóhoz. Az .db maga nem kerül verziókövetésbe: bináris,
    ütközésnél nem olvasható a diff, és nem lehet összefésülni. A TSV igen.
    """
    rows = con.execute(
        f"SELECT {','.join(EXPORT_COLS)} FROM entries ORDER BY pattern, source_text, replacement"
    ).fetchall()
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("# A humanizáló adatbázisának szöveges magja.\n")
        f.write("# Újraépítés:  python dict/db.py import\n")
        f.write("# Frissítés:   python dict/db.py dump\n")
        f.write("\t".join(EXPORT_COLS) + "\n")
        for r in rows:
            f.write("\t".join("" if r[c] is None else str(r[c]) for c in EXPORT_COLS) + "\n")
    return len(rows)


def load_seed(con: sqlite3.Connection, path: Path = SEED_TSV) -> int:
    if not path.exists():
        return 0
    n = 0
    with io.open(path, encoding="utf-8") as f:
        header = None
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if header is None:
                header = parts
                continue
            row = dict(zip(header, parts))
            con.execute(
                "INSERT INTO entries (kind,lang,source_text,replacement,category,pattern,"
                "origin,note,times_used,first_seen) VALUES (?,?,?,?,?,?,?,?,?,?) "
                "ON CONFLICT(kind,lang,source_text,replacement) DO NOTHING",
                (row["kind"], row["lang"], row["source_text"], row["replacement"],
                 row.get("category") or None, row.get("pattern") or None,
                 row.get("origin") or "seed", row.get("note") or None,
                 int(row.get("times_used") or 0), now()),
            )
            n += 1
    con.commit()
    return n


def _seed_keys(path: Path = SEED_TSV) -> set[tuple[str, str, str, str]]:
    keys = set()
    with io.open(path, encoding="utf-8") as f:
        header = None
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\r\n").split("\t")
            if header is None:
                header = parts
                continue
            row = dict(zip(header, parts))
            keys.add((row["kind"], row["lang"], row["source_text"], row["replacement"]))
    return keys


def prune_seed(con: sqlite3.Connection, path: Path = SEED_TSV) -> int:
    """
    Törli a `seed` eredetű bejegyzéseket, amelyek kikerültek a seed.tsv-ből.

    A betöltés csak beszúr (`ON CONFLICT DO NOTHING`), így egy frissítés után a
    magból szándékosan törölt, hibás cserék a régi adatbázisban tovább élnének.
    A `learned` és `manual` bejegyzésekhez nem nyúlunk: azok a felhasználóéi.
    """
    if not path.exists():
        return 0
    keep = _seed_keys(path)
    stale = [
        r["id"]
        for r in con.execute(
            "SELECT id, kind, lang, source_text, replacement FROM entries WHERE origin='seed'"
        )
        if (r["kind"], r["lang"], r["source_text"], r["replacement"]) not in keep
    ]
    con.executemany("DELETE FROM entries WHERE id=?", [(i,) for i in stale])
    con.commit()
    return len(stale)


def seed_is_current(con: sqlite3.Connection, path: Path = SEED_TSV) -> bool:
    row = con.execute("SELECT value FROM meta WHERE key='seed_digest'").fetchone()
    return bool(row) and row["value"] == seed_digest(path)


def mark_seed_loaded(con: sqlite3.Connection, path: Path = SEED_TSV) -> None:
    con.execute(
        "INSERT INTO meta (key, value) VALUES ('seed_digest', ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
        (seed_digest(path),),
    )
    con.commit()


IGNORE_COLS = ["word", "lang", "reason", "origin", "times_seen", "note"]


def add_ignore(con, word, *, reason="egyeb", note=None, origin="learned",
               lang="hu_HU") -> int:
    cur = con.execute(
        "INSERT INTO ignore_words (word,lang,reason,note,origin,times_seen,first_seen) "
        "VALUES (?,?,?,?,?,0,?) ON CONFLICT(lang,word) DO UPDATE SET "
        "times_seen = times_seen + 1",
        (word, lang, reason, note, origin, now()),
    )
    con.commit()
    return cur.lastrowid


def load_ignore_words(con, lang="hu_HU") -> set[str]:
    return {
        r["word"].lower()
        for r in con.execute("SELECT word FROM ignore_words WHERE lang=?", (lang,))
    }


def dump_ignore(con, path: Path = IGNORE_TSV) -> int:
    rows = con.execute(
        f"SELECT {','.join(IGNORE_COLS)} FROM ignore_words ORDER BY reason, word"
    ).fetchall()
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Helyesírási kivételek — az adatbázis verziókövetett magja.\n")
        f.write("# Újraépítés:  python dict/db.py import\n")
        f.write("\t".join(IGNORE_COLS) + "\n")
        for r in rows:
            f.write("\t".join("" if r[c] is None else str(r[c]) for c in IGNORE_COLS) + "\n")
    return len(rows)


def load_ignore_seed(con, path: Path = IGNORE_TSV) -> int:
    if not path.exists():
        return 0
    n = 0
    with io.open(path, encoding="utf-8") as f:
        header = None
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if header is None:
                header = parts
                continue
            r = dict(zip(header, parts))
            con.execute(
                "INSERT INTO ignore_words (word,lang,reason,note,origin,times_seen,first_seen) "
                "VALUES (?,?,?,?,?,?,?) ON CONFLICT(lang,word) DO NOTHING",
                (r["word"], r.get("lang") or "hu_HU", r.get("reason") or "egyeb",
                 r.get("note") or None, r.get("origin") or "seed",
                 int(r.get("times_seen") or 0), now()),
            )
            n += 1
    con.commit()
    return n


def cmd_ignore(args):
    con = connect(args.db)
    if args.action == "add":
        if not args.word:
            raise SystemExit("Adj meg legalább egy szót.")
        for w in args.word:
            add_ignore(con, w, reason=args.reason, note=args.note, origin=args.origin,
                       lang=args.lang)
        # Nem írjuk automatikusan a verziókövetett seed-ignore.tsv-be: abba
        # csak az kerüljön, amit a karbantartó tudatosan kiad (`dump`) —
        # különben a felhasználói szövegek nevei bekerülnének a repóba.
        print(f"{len(args.word)} szó felvéve ({args.reason}).")
    elif args.action == "remove":
        for w in args.word:
            con.execute("DELETE FROM ignore_words WHERE LOWER(word)=LOWER(?)", (w,))
        con.commit()
        print(f"{len(args.word)} szó törölve.")
    else:
        rows = con.execute(
            "SELECT * FROM ignore_words WHERE (? IS NULL OR reason=?) ORDER BY reason, word",
            (args.reason_filter, args.reason_filter),
        ).fetchall()
        if not rows:
            print("A kivétellista üres.")
            return
        cur = None
        for r in rows:
            if r["reason"] != cur:
                cur = r["reason"]
                print(f"\n[{cur}]")
            note = f"  — {r['note']}" if r["note"] else ""
            print(f"  {r['word']}{note}")
        print(f"\nösszesen: {len(rows)}")


def cmd_init(args):
    con = connect(args.db)
    n = con.execute("SELECT COUNT(*) c FROM entries").fetchone()["c"]
    if n == 0 and SEED_TSV.exists():
        load_seed(con)
        load_ignore_seed(con)
        mark_seed_loaded(con)
        n = con.execute("SELECT COUNT(*) c FROM entries").fetchone()["c"]
        print(f"{SEED_TSV.name} betöltve.")
    print(f"{args.db} kész — {n} bejegyzés.")


def cmd_dump(args):
    con = connect(args.db)
    n = dump_seed(con)
    m = dump_ignore(con)
    print(f"{SEED_TSV.name}: {n} bejegyzés, {IGNORE_TSV.name}: {m} kivétel kiírva.")


def cmd_import(args):
    con = connect(args.db)
    before = con.execute("SELECT COUNT(*) c FROM entries").fetchone()["c"]
    load_seed(con)
    load_ignore_seed(con)
    removed = prune_seed(con)
    mark_seed_loaded(con)
    after = con.execute("SELECT COUNT(*) c FROM entries").fetchone()["c"]
    ign = con.execute("SELECT COUNT(*) c FROM ignore_words").fetchone()["c"]
    print(f"{after - before + removed} új bejegyzés, {removed} elavult mag-bejegyzés törölve "
          f"(összesen {after}), {ign} kivétel.")
    if not args.no_check:
        for r in con.execute("SELECT id FROM entries"):
            run_checks(con, r["id"])
        print("Kereszt-ellenőrzés lefutott.")


def cmd_add(args):
    con = connect(args.db)
    eid = add_entry(
        con, args.source, args.replacement,
        category=args.category, pattern=args.pattern, origin=args.origin,
        note=args.note, context=args.context, check=not args.no_check,
    )
    row = con.execute("SELECT * FROM v_entries WHERE id=?", (eid,)).fetchone()
    print(f"#{eid}  {row['source_text']} -> {row['replacement']}  "
          f"({row['origin']}, {row['times_used']}x)")
    _print_checks(row, indent="  ")


def _flag(v):
    return "rendben" if v == 1 else ("FIGYELEM" if v == 0 else "n.a.")


def _print_checks(row, indent=""):
    print(f"{indent}helyesírás: {_flag(row['ok_spelling'])}   "
          f"tezaurusz: {_flag(row['ok_thesaurus'])}   "
          f"kölcsönös: {_flag(row['ok_reciprocal'])}")


def cmd_lookup(args):
    con = connect(args.db)
    rows = con.execute(
        "SELECT * FROM v_entries WHERE source_text LIKE ? OR replacement LIKE ? "
        "ORDER BY times_used DESC, source_text",
        (f"%{args.text}%", f"%{args.text}%"),
    ).fetchall()
    if not rows:
        print(f"'{args.text}' — nincs az adatbázisban.")
        return
    for r in rows:
        print(f"#{r['id']}  [{r['pattern'] or '-'}/{r['category'] or '-'}] "
              f"{r['source_text']} -> {r['replacement']}   "
              f"({r['origin']}, {r['times_used']}x, {r['n_contexts']} példa)")
        _print_checks(r, indent="      ")


def cmd_scan(args):
    con = connect(args.db)
    text = sys.stdin.read() if args.path == "-" else Path(args.path).read_text("utf-8", errors="replace")
    lines = text.split("\n")
    rows = con.execute("SELECT * FROM v_entries ORDER BY LENGTH(source_text) DESC").fetchall()

    hits = []
    for r in rows:
        src = r["source_text"]
        if "..." in src or "…" in src:
            continue  # sablon („nem csupán ... hanem”), nem szó szerinti fordulat
        # Egyszavas bejegyzésnél a toldalékolt alak is találat
        # („kulcsfontosságúnak”, „elősegítette”). Fordulatnál csak a szó szerinti
        # alak: a belső ragozást („szerepet játszott”) regex nem kezeli
        # megbízhatóan, azt a B réteg olvasása fogja meg.
        tail = r"\w*" if r["kind"] == "word" else ""
        pat = re.compile(r"(?<!\w)" + re.escape(src) + tail + r"(?!\w)", re.IGNORECASE)
        for n, line in enumerate(lines, 1):
            for m in pat.finditer(line):
                hits.append((n, m.start() + 1, r))
    hits.sort(key=lambda h: (h[0], h[1]))

    label = "<stdin>" if args.path == "-" else args.path
    if args.tsv:
        print("sor\toszlop\tminta\tkategoria\tfordulat\tjavaslat")
        for n, col, r in hits:
            print(f"{n}\t{col}\t{r['pattern'] or ''}\t{r['category'] or ''}\t"
                  f"{r['source_text']}\t{r['replacement']}")
        return 0
    if not hits:
        print(f"{label} — nincs ismert fordulat az adatbázisból.")
        return 0
    print("Ezek jelöltek, nem kötelező cserék: csak ott cserélj, ahol a szó a")
    print("szövegben valóban AI-jel (7. minta), és a csere jelentése illik.\n")

    # Egy előforduláshoz több jelölt is tartozhat — egy helyen, egy sorban
    # mutatjuk őket, különben a kimenet olvashatatlan. A megerősített
    # (kölcsönös) jelölt kerül előre, mert az a megbízhatóbb csere.
    grouped: dict[tuple, list] = {}
    for n, col, r in hits:
        grouped.setdefault((n, col, r["source_text"], r["pattern"]), []).append(r)

    print(f"{label} — {len(grouped)} előfordulás:\n")
    for (n, col, src, pattern), cands in grouped.items():
        cands.sort(key=lambda r: (r["ok_reciprocal"] != 1, -(r["times_used"] or 0)))
        print(f"  {n}:{col:<4} [{pattern or '-'}] {src}")
        for r in cands[: args.limit]:
            mark = " (kölcsönös)" if r["ok_reciprocal"] == 1 else ""
            used = f" [{r['times_used']}x]" if r["times_used"] else ""
            print(f"          -> {r['replacement']}{mark}{used}")
        if len(cands) > args.limit:
            print(f"             … és még {len(cands) - args.limit}")
    return 1 if args.strict else 0


def cmd_verify(args):
    con = connect(args.db)
    ids = [r["id"] for r in con.execute("SELECT id FROM entries ORDER BY id")]
    if not ids:
        raise SystemExit(f"Üres adatbázis. Futtasd: {skill_cmd('db.py')} init")
    print(f"{len(ids)} bejegyzés ellenőrzése…")
    for i in ids:
        run_checks(con, i)
    bad = con.execute(
        "SELECT * FROM v_entries WHERE ok_spelling = 0 OR ok_thesaurus = 0 OR ok_reciprocal = 0"
    ).fetchall()
    if not bad:
        print("Minden bejegyzés átment.")
        return 0
    print(f"\n{len(bad)} bejegyzés bukott legalább egy ellenőrzésen:\n")
    for r in bad:
        print(f"  #{r['id']}  {r['source_text']} -> {r['replacement']}")
        _print_checks(r, indent="        ")
    print("\n  A bukott tezaurusz/kölcsönösség nem feltétlenül hiba: szerkesztői\n"
          "  döntés is lehet. A bukott helyesírás viszont mindig javítandó.")
    return 1 if args.strict else 0


def cmd_stats(args):
    con = connect(args.db)
    t = con.execute(
        "SELECT origin, kind, COUNT(*) n, SUM(times_used) used FROM entries "
        "GROUP BY origin, kind ORDER BY origin, kind"
    ).fetchall()
    if not t:
        raise SystemExit(f"Üres adatbázis. Futtasd: {skill_cmd('db.py')} init")
    print(f"{'eredet':<10} {'típus':<8} {'darab':>7} {'használat':>10}")
    for r in t:
        print(f"{r['origin']:<10} {r['kind']:<8} {r['n']:>7} {r['used'] or 0:>10}")
    c = con.execute(
        "SELECT SUM(ok_spelling=1) s, SUM(ok_thesaurus=1) t, SUM(ok_reciprocal=1) r, "
        "COUNT(*) n FROM v_entries"
    ).fetchone()
    print(f"\nkereszt-ellenőrzés: helyesírás {c['s'] or 0}/{c['n']}, "
          f"tezaurusz {c['t'] or 0}/{c['n']}, kölcsönös {c['r'] or 0}/{c['n']}")
    ctx = con.execute("SELECT COUNT(*) n FROM contexts").fetchone()["n"]
    print(f"rögzített előfordulás: {ctx}")


def cmd_export(args):
    con = connect(args.db)
    rows = con.execute("SELECT * FROM v_entries ORDER BY pattern, source_text").fetchall()
    cols = ["id", "kind", "pattern", "category", "source_text", "replacement",
            "origin", "times_used", "ok_spelling", "ok_thesaurus", "ok_reciprocal"]
    out = io.StringIO()
    out.write("\t".join(cols) + "\n")
    for r in rows:
        out.write("\t".join("" if r[c] is None else str(r[c]) for c in cols) + "\n")
    if args.out:
        Path(args.out).write_text(out.getvalue(), "utf-8")
        print(f"{args.out}: {len(rows)} sor")
    else:
        sys.stdout.write(out.getvalue())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", type=Path, default=DB_PATH)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="séma létrehozása").set_defaults(fn=cmd_init)

    p = sub.add_parser("seed", help="induló készlet a SKILL.md tábláiból")
    p.add_argument("--no-check", action="store_true")
    p.set_defaults(fn=cmd_seed)

    p = sub.add_parser("add", help="csere rögzítése")
    p.add_argument("source")
    p.add_argument("replacement")
    p.add_argument("--pattern", help="melyik minta: M3, M5, 7, S2 …")
    p.add_argument("--category")
    p.add_argument("--note")
    p.add_argument("--context", help="a mondat, amiben előfordult")
    p.add_argument("--origin", default="learned", choices=["learned", "manual", "seed"])
    p.add_argument("--no-check", action="store_true")
    p.set_defaults(fn=cmd_add)

    p = sub.add_parser("lookup", help="mit tudunk erről")
    p.add_argument("text")
    p.set_defaults(fn=cmd_lookup)

    p = sub.add_parser("scan", help="ismert fordulatok keresése szövegben")
    p.add_argument("path")
    p.add_argument("--tsv", action="store_true")
    p.add_argument("--strict", action="store_true")
    p.add_argument("--limit", type=int, default=4, help="jelölt / előfordulás")
    p.set_defaults(fn=cmd_scan)

    p = sub.add_parser("verify", help="kereszt-ellenőrzések újrafuttatása")
    p.add_argument("--strict", action="store_true")
    p.set_defaults(fn=cmd_verify)

    p = sub.add_parser("ignore", help="helyesírási kivételek kezelése")
    p.add_argument("action", nargs="?", default="list", choices=["list", "add", "remove"])
    p.add_argument("word", nargs="*")
    p.add_argument("--reason", default="egyeb",
                   choices=["szakszo", "tulajdonnev", "marka", "idegen",
                            "magyar-hianyzo", "egyeb"])
    p.add_argument("--reason-filter", dest="reason_filter", default=None)
    p.add_argument("--lang", default="hu_HU")
    p.add_argument("--note")
    p.add_argument("--origin", default="learned", choices=["learned", "manual", "seed"])
    p.set_defaults(fn=cmd_ignore)

    sub.add_parser("stats", help="összesítés").set_defaults(fn=cmd_stats)
    sub.add_parser("dump", help="szöveges mag kiírása (dict/seed.tsv) — karbantartói lépés").set_defaults(fn=cmd_dump)

    p = sub.add_parser("import", help="szöveges mag betöltése")
    p.add_argument("--no-check", action="store_true")
    p.set_defaults(fn=cmd_import)

    p = sub.add_parser("export", help="TSV kimenet")
    p.add_argument("--tsv", action="store_true", help="alapértelmezett formátum")
    p.add_argument("--out")
    p.set_defaults(fn=cmd_export)

    args = ap.parse_args()
    sys.exit(args.fn(args) or 0)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
