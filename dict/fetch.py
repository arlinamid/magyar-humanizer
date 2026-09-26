#!/usr/bin/env python3
"""
Szótárletöltő a LibreOffice/dictionaries repóból.

A magyar mindig települ — ez a skill alapja. Telepítéskor rákérdez, kell-e
másik nyelv is, mert a skill használható más nyelvű szövegekhez is, és mert
a helyesírás-ellenőrzés csak a letöltött nyelvekre tud futni.

    python dict/fetch.py                      # interaktív
    python dict/fetch.py --lang hu_HU,en_US   # kérdés nélkül
    python dict/fetch.py --list               # mi érhető el
    python dict/fetch.py --thesaurus-only     # csak tezaurusszal bíró nyelvek

A szótárak a <adatmappa>/data/<nyelv>/ alá kerülnek (lásd dict/paths.py:
a dict/ mappa, ha írható, különben a felhasználói adatmappa), és NEM kerülnek
be a repóba (lásd .gitignore). Ennek licencokai is vannak: a magyar tezaurusz GPL-2,
amit egy MIT-licencű repóba nem vendorolunk bele.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DICT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(DICT_DIR))
from paths import DATA  # noqa: E402

REPO = "LibreOffice/dictionaries"
BRANCH = "master"
TREE_URL = f"https://api.github.com/repos/{REPO}/git/trees/{BRANCH}?recursive=1"
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/"

# A skill alapnyelve — mindig települ.
BASE_LANG = "hu_HU"

SKIP_DIRS = {".github", "util"}


# --------------------------------------------------------------- katalógus


class CatalogUnavailable(Exception):
    pass


def fetch_tree() -> list[str]:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "magyar-humanizer"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(TREE_URL, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        # Gyakori: a GitHub API korlátoz (403/429), vagy egy homokozó csak a
        # raw.githubusercontent.com-ot engedi. Ilyenkor a szabványos
        # fájlnevekkel közvetlenül próbálkozunk (guess_catalog).
        raise CatalogUnavailable(str(getattr(e, "code", "") or e))
    if data.get("truncated"):
        print("FIGYELEM: a falista csonkolt, egyes nyelvek hiányozhatnak.", file=sys.stderr)
    return [x["path"] for x in data["tree"] if x["type"] == "blob"]


def build_catalog(paths: list[str]) -> dict[str, dict]:
    """
    Nyelvenként csoportosítja a használható fájlokat.

    A LibreOffice névadása nem egységes (`de_DE_frami.dic`, `th_es_v2.dat`,
    `fr_FR/dictionaries/fr.aff`), ezért a fájlokat felderítjük, nem kitaláljuk.
    """
    cat: dict[str, dict] = {}
    for p in paths:
        parts = p.split("/")
        if len(parts) < 2 or parts[0] in SKIP_DIRS:
            continue
        lang, name = parts[0], parts[-1]
        e = cat.setdefault(lang, {"spell": {}, "thesaurus": [], "hyph": [], "readme": []})

        if name.startswith("hyph_") and name.endswith(".dic"):
            e["hyph"].append(p)
        elif name.startswith("th_") and name.endswith((".dat", ".idx")):
            e["thesaurus"].append(p)
        elif name.endswith((".dic", ".aff")):
            e["spell"].setdefault(name[:-4], {})[name[-3:]] = p
        elif name.upper().startswith("README") and name.endswith(".txt"):
            e["readme"].append(p)

    # Csak azok a helyesírási készletek maradnak, ahol .dic ÉS .aff is van
    for e in cat.values():
        e["spell"] = {k: v for k, v in e["spell"].items() if "dic" in v and "aff" in v}

    return {k: v for k, v in cat.items() if v["spell"] or v["thesaurus"]}


def summarize(cat: dict[str, dict]) -> list[tuple[str, str, bool, int]]:
    rows = []
    for lang in sorted(cat):
        e = cat[lang]
        variants = sorted(e["spell"])
        has_th = any(p.endswith(".dat") for p in e["thesaurus"])
        rows.append((lang, ", ".join(variants[:4]) + ("…" if len(variants) > 4 else ""), has_th, len(variants)))
    return rows


def _exists(path: str) -> bool:
    req = urllib.request.Request(RAW + path, method="HEAD", headers={"User-Agent": "magyar-humanizer"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 200
    except (urllib.error.URLError, TimeoutError):
        return False


def guess_catalog(langs: set[str]) -> dict[str, dict]:
    """
    Katalógus API nélkül: a LibreOffice szokásos fájlneveit próbálja a
    raw.githubusercontent.com-on (hu_HU/hu_HU.dic, en/en_US.dic,
    th_<nyelv>_v2.dat). A szokatlan nevű nyelveket így nem találja meg —
    azokhoz az API kell (GITHUB_TOKEN).
    """
    cat: dict[str, dict] = {}
    for lang in langs:
        for folder in dict.fromkeys([lang, lang.split("_")[0]]):
            dic, aff = f"{folder}/{lang}.dic", f"{folder}/{lang}.aff"
            if not (_exists(dic) and _exists(aff)):
                continue
            e = {"spell": {lang: {"dic": dic, "aff": aff}}, "thesaurus": [], "hyph": [], "readme": []}
            th = f"{folder}/th_{lang}_v2.dat"
            if _exists(th):
                e["thesaurus"].append(th)
            hyph = f"{folder}/hyph_{lang}.dic"
            if _exists(hyph):
                e["hyph"].append(hyph)
            readme = f"{folder}/README_{lang}.txt"
            if _exists(readme):
                e["readme"].append(readme)
            cat[lang] = e
            break
    return cat


# --------------------------------------------------------------- letöltés


def download(path: str, dest: Path) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(RAW + path, headers={"User-Agent": "magyar-humanizer"})
    with urllib.request.urlopen(req, timeout=120) as r:
        blob = r.read()
    dest.write_bytes(blob)
    return len(blob)


def pick_variant(variants: dict[str, dict], lang: str) -> str | None:
    """
    Egy nyelvhez több helyesírási készlet is tartozhat (es_AR, es_ES, …).
    Ha a kért kód pontosan egyezik, azt visszük; különben a nyelvkóddal
    kezdődő legrövidebb nevűt, ami rendszerint az alapváltozat.
    """
    if not variants:
        return None
    if lang in variants:
        return lang
    base = lang.split("_")[0]
    cands = [k for k in variants if k == base or k.startswith(base)]
    return min(cands, key=len) if cands else min(variants, key=len)


def install(lang: str, cat: dict[str, dict], want: set[str]) -> bool:
    key = lang if lang in cat else lang.split("_")[0]
    if key not in cat:
        print(f"  {lang}: nincs ilyen a katalógusban — kihagyva")
        return False
    e = cat[key]
    out = DATA / lang
    files, total = [], 0

    if "spell" in want:
        v = pick_variant(e["spell"], lang)
        if v:
            for ext in ("dic", "aff"):
                p = e["spell"][v][ext]
                total += download(p, out / Path(p).name)
                files.append(Path(p).name)

    if "thesaurus" in want:
        for p in e["thesaurus"]:
            if p.endswith(".dat"):
                total += download(p, out / Path(p).name)
                files.append(Path(p).name)

    if "hyph" in want:
        for p in e["hyph"][:1]:
            total += download(p, out / Path(p).name)
            files.append(Path(p).name)

    for p in e["readme"]:
        try:
            download(p, out / Path(p).name)
        except Exception:
            pass

    if not files:
        print(f"  {lang}: nem volt letölthető komponens")
        return False

    print(f"  {lang}: {', '.join(files)}  ({total / 1024 / 1024:.1f} MB)")

    if any(f.startswith("th_") for f in files):
        sys.path.insert(0, str(DICT_DIR))
        from thesaurus import build_index  # noqa: E402

        build_index(lang, quiet=True)
        print(f"  {lang}: tezaurusz-index generálva")

    manifest = DATA / "manifest.json"
    m = json.loads(manifest.read_text("utf-8")) if manifest.exists() else {}
    m[lang] = {"source": f"https://github.com/{REPO}/tree/{BRANCH}/{key}", "files": files}
    manifest.write_text(json.dumps(m, ensure_ascii=False, indent=2), "utf-8")
    return True


# --------------------------------------------------------------- interaktív


def ask(cat: dict[str, dict]) -> tuple[set[str], set[str]]:
    rows = summarize(cat)
    with_th = [r[0] for r in rows if r[2]]

    print(f"\nA magyar ({BASE_LANG}) mindig települ — ez a skill alapja.\n")
    print(f"Tezaurusszal {len(with_th)} nyelv érhető el, helyesírás-ellenőrzéssel {len(rows)}.")
    print("Szinonimakereséshez tezaurusz kell, helyesírás-ellenőrzéshez elég a szólista.\n")
    print("Tezaurusszal bíró nyelvek:")
    print("  " + ", ".join(with_th) + "\n")

    raw = input(
        "Melyik további nyelvek kellenek? (vesszővel, üres = csak magyar,\n"
        "'all-th' = az összes tezauruszos, 'list' = teljes lista): "
    ).strip()

    if raw == "list":
        cmd_list(cat)
        raw = input("\nMelyik további nyelvek kellenek? ").strip()

    if raw == "all-th":
        langs = set(with_th)
    else:
        langs = {x.strip() for x in raw.split(",") if x.strip()}
    langs.add(BASE_LANG)

    print("\nMit töltsünk le nyelvenként?")
    print("  1) helyesírás + tezaurusz   (ajánlott)")
    print("  2) csak helyesírás")
    print("  3) helyesírás + tezaurusz + elválasztás")
    choice = input("Választás [1]: ").strip() or "1"
    want = {
        "1": {"spell", "thesaurus"},
        "2": {"spell"},
        "3": {"spell", "thesaurus", "hyph"},
    }.get(choice, {"spell", "thesaurus"})

    return langs, want


def cmd_list(cat: dict[str, dict]) -> None:
    print(f"\n{'nyelv':<12} {'tezaurusz':<10} változatok")
    print("-" * 64)
    for lang, variants, has_th, _ in summarize(cat):
        print(f"{lang:<12} {'igen' if has_th else '-':<10} {variants}")
    print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", help="vesszővel elválasztott nyelvkódok (kihagyja a kérdéseket)")
    ap.add_argument("--list", action="store_true", help="elérhető nyelvek listája")
    ap.add_argument("--thesaurus-only", action="store_true", help="csak tezauruszos nyelvek telepítése")
    ap.add_argument("--no-thesaurus", action="store_true", help="csak helyesírási szólisták")
    ap.add_argument("--hyph", action="store_true", help="elválasztási minták is")
    args = ap.parse_args()

    print("Katalógus lekérése a LibreOffice/dictionaries repóból…")
    try:
        cat = build_catalog(fetch_tree())
        print(f"{len(cat)} nyelv a katalógusban.")
    except CatalogUnavailable as e:
        if args.list or args.thesaurus_only or not args.lang:
            raise SystemExit(
                f"A GitHub API nem érhető el ({e}). Listához és interaktív módhoz kell;\n"
                "  próbáld GITHUB_TOKEN-nel, vagy add meg a nyelvet: --lang hu_HU"
            )
        print(f"A GitHub API nem érhető el ({e}) — közvetlen letöltés szabványos fájlnevekkel.")
        want_langs = {x.strip() for x in args.lang.split(",") if x.strip()}
        cat = guess_catalog(want_langs)

    if args.list:
        cmd_list(cat)
        return

    if args.lang:
        langs = {x.strip() for x in args.lang.split(",") if x.strip()}
        want = {"spell"}
        if not args.no_thesaurus:
            want.add("thesaurus")
        if args.hyph:
            want.add("hyph")
    elif args.thesaurus_only:
        langs = {l for l, _, th, _ in summarize(cat) if th}
        want = {"spell", "thesaurus"}
    elif sys.stdin.isatty():
        langs, want = ask(cat)
    else:
        langs, want = {BASE_LANG}, {"spell", "thesaurus"}
        print("Nem interaktív futás — csak a magyar települ.")

    print(f"\nTelepítés: {', '.join(sorted(langs))}\n")
    failed = []
    for lang in sorted(langs):
        try:
            ok = install(lang, cat, want)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"  {lang}: letöltési hiba ({e})")
            ok = False
        if not ok:
            failed.append(lang)

    print(f"\nKész. Helye: {DATA}")
    print(f'Ellenőrzés:  python3 "{DICT_DIR / "thesaurus.py"}" stats')
    if failed:
        raise SystemExit(f"Nem sikerült: {', '.join(failed)}")


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
