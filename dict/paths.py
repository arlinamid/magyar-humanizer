#!/usr/bin/env python3
"""
Közös útvonalak: hol vannak a letöltött szótárak és a munka-adatbázis.

A verziókövetett mag (seed.tsv, seed-ignore.tsv) mindig a dict/ mappában
marad. A letöltött szótárak és a humanizer.db viszont írható helyet kívánnak,
a skill mappája pedig sok telepítésben csak olvasható (claude.ai, plugin,
rendszerszintű másolat). Sorrend:

  1. MAGYAR_HUMANIZER_HOME környezeti változó, ha be van állítva
  2. a dict/ mappa, ha írható (fejlesztői klón, ~/.claude/skills/ alatti másolat)
  3. felhasználói mappa: $XDG_DATA_HOME/magyar-humanizer
     (alapból ~/.local/share/magyar-humanizer; Windowson %LOCALAPPDATA%)

Ha egy korábbi futás már a dict/ alá töltött le, az ott marad érvényes.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

DICT_DIR = Path(__file__).resolve().parent
SEED_TSV = DICT_DIR / "seed.tsv"
IGNORE_TSV = DICT_DIR / "seed-ignore.tsv"


def _writable(d: Path) -> bool:
    try:
        d.mkdir(parents=True, exist_ok=True)
        probe = d / ".write-test"
        probe.write_text("", "utf-8")
        probe.unlink()
        return True
    except OSError:
        return False


def _user_dir() -> Path:
    if sys.platform.startswith("win"):
        base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
    else:
        base = os.environ.get("XDG_DATA_HOME") or str(Path.home() / ".local" / "share")
    return Path(base) / "magyar-humanizer"


def home() -> Path:
    env = os.environ.get("MAGYAR_HUMANIZER_HOME")
    if env:
        p = Path(env).expanduser()
        p.mkdir(parents=True, exist_ok=True)
        return p
    # Korábbi telepítés a skill mappájában: használjuk tovább.
    if (DICT_DIR / "data").is_dir() or (DICT_DIR / "humanizer.db").exists():
        if _writable(DICT_DIR):
            return DICT_DIR
    if _writable(DICT_DIR):
        return DICT_DIR
    u = _user_dir()
    u.mkdir(parents=True, exist_ok=True)
    return u


HOME = home()
DATA = HOME / "data"
DB = HOME / "humanizer.db"


def skill_cmd(script: str) -> str:
    """Parancs a felhasználói üzenetekhez — abszolút úttal, hogy bárhonnan fusson."""
    return f'python3 "{DICT_DIR / script}"'
