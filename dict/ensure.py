#!/usr/bin/env python3
"""
Bootstrap: szótár + adatbázis, ha még nincs.

A skill első lépése. Nem interaktív — a magyar mindig települ.
Ha a szövegben más nyelv is van, hívja újra:  python dict/ensure.py --lang en_US

    python dict/ensure.py
    python dict/ensure.py --lang hu_HU,en_US
    python dict/ensure.py --check   # csak jelent, nem telepít
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

DICT_DIR = Path(__file__).resolve().parent
DATA = DICT_DIR / "data"
DB = DICT_DIR / "humanizer.db"
BASE_LANG = "hu_HU"


def _has_spell(lang: str) -> bool:
    d = DATA / lang
    if not d.is_dir():
        return False
    for p in d.glob("*.dic"):
        if p.name.startswith("hyph_"):
            continue
        if p.with_suffix(".aff").exists():
            return True
    return False


def _has_thesaurus(lang: str) -> bool:
    d = DATA / lang
    if not d.is_dir():
        return False
    return any(d.glob("th_*.dat"))


def _db_ready() -> bool:
    if not DB.exists():
        return False
    try:
        import sqlite3

        con = sqlite3.connect(DB)
        n = con.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
        con.close()
        return n > 0
    except Exception:
        return False


def _spylls_ok() -> bool:
    try:
        import spylls  # noqa: F401

        return True
    except ImportError:
        return False


def status(langs: list[str]) -> dict:
    return {
        "spylls": _spylls_ok(),
        "db": _db_ready(),
        "langs": {
            lang: {"spell": _has_spell(lang), "thesaurus": _has_thesaurus(lang)}
            for lang in langs
        },
    }


def _run(cmd: list[str]) -> int:
    print("+", " ".join(cmd))
    return subprocess.call(cmd, cwd=str(DICT_DIR.parent))


def ensure(langs: list[str], *, check_only: bool = False) -> int:
    langs = list(dict.fromkeys([BASE_LANG, *langs]))
    st = status(langs)
    missing_langs = [
        lang
        for lang, info in st["langs"].items()
        if not info["spell"] or not info["thesaurus"]
    ]

    print("magyar-humanizer dict bootstrap")
    print(f"  spylls:     {'OK' if st['spylls'] else 'HIÁNYZIK'}")
    print(f"  adatbázis:  {'OK' if st['db'] else 'HIÁNYZIK'}  ({DB.name})")
    for lang, info in st["langs"].items():
        spell = "OK" if info["spell"] else "HIÁNYZIK"
        th = "OK" if info["thesaurus"] else "HIÁNYZIK"
        print(f"  {lang}:      helyesírás {spell}, tezaurusz {th}")

    if check_only:
        ok = st["spylls"] and st["db"] and not missing_langs
        return 0 if ok else 1

    rc = 0

    if not st["spylls"]:
        rc = _run([sys.executable, "-m", "pip", "install", "spylls"]) or rc

    if missing_langs:
        rc = (
            _run(
                [
                    sys.executable,
                    str(DICT_DIR / "fetch.py"),
                    "--lang",
                    ",".join(missing_langs),
                ]
            )
            or rc
        )

    if not st["db"]:
        # import létrehozza a sémát, betölti a seed.tsv / seed-ignore.tsv magot,
        # és lefuttatja a kereszt-ellenőrzést.
        rc = _run([sys.executable, str(DICT_DIR / "db.py"), "import"]) or rc

    st2 = status(langs)
    if not (st2["spylls"] and st2["db"] and not [
        lang
        for lang, info in st2["langs"].items()
        if not info["spell"] or not info["thesaurus"]
    ]):
        print("FIGYELEM: a bootstrap után is hiányzik valami.", file=sys.stderr)
        return 1

    print("Kész — szótár és adatbázis használható.")
    return rc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--lang",
        default=BASE_LANG,
        help="vesszővel elválasztott nyelvkódok (a magyar mindig benne van)",
    )
    ap.add_argument("--check", action="store_true", help="csak ellenőrzés, telepítés nélkül")
    args = ap.parse_args()
    langs = [x.strip() for x in args.lang.split(",") if x.strip()]
    return ensure(langs, check_only=args.check)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
