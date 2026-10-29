#!/usr/bin/env python3
"""
Stilometriai mutatók a C réteghez (references/layer-c-stylometric.md).

    python3 <skill-mappa>/dict/metrics.py szoveg.md
    python3 <skill-mappa>/dict/metrics.py - < szoveg.txt
    python3 <skill-mappa>/dict/metrics.py szoveg.md --skip-dialogue
    python3 <skill-mappa>/dict/metrics.py szoveg.md --json

Közelítés, nem ítélet: a szkript a számolható mutatókat adja. A tapasztalati
elemet (S8), a központi tétel újrafogalmazását (S9), a bekezdések „dolgát” (S1)
és a rejtett listát (S10) a skill olvasója ítéli meg. A küszöbök heurisztikák;
kb. 400 szó alatt csak tájékoztatók. Kilépési kód mindig 0 (hibás bemenetnél 2).
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

MIN_WORDS = 400

ABBR = (
    "pl|stb|kb|ún|ill|ca|dr|vö|ld|sz|nr|ifj|id|prof|özv|kft|zrt|tel|ford|old|"
    "hrsz|ker|krt|fsz|em|évf"
)
DOT = "\u0001"  # védett pont: rövidítés, sorszám, monogram

# A bekezdés elején álló bejelentő / sorszámozó formulák (S7). A köznapi
# kötőszavak (Pedig, Ugyanakkor, Ráadásul) szándékosan nincsenek köztük.
FORMULAS = (
    "és itt", "itt jön", "ezen a ponton", "ez azért", "összefoglalva",
    "összefoglalásképpen", "végül", "először", "másodszor", "harmadszor",
    "egyrészt", "másrészt", "továbbá", "mindezek alapján", "ebből következik",
    "fontos megjegyezni", "érdemes kiemelni", "nem véletlen",
)
OPINION = (
    "szerintem", "úgy gondolom", "úgy látom", "úgy érzem", "meggyőződésem",
    "véleményem szerint", "én azt látom",
)

# Fordított szembeállítás: „X, nem Y” / „Az számít, hogy X, nem az, hogy Y” (az S2 másik alakja).
INVERSE = re.compile(r"[,;]\s+nem\s+\w+")

WORD = re.compile(r"\w+(?:[-’']\w+)*", re.UNICODE)


def clean(text: str, skip_dialogue: bool) -> tuple[list[str], int]:
    """Bekezdések listája jelölés nélkül; a kihagyott párbeszédsorok száma."""
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    lines, skipped = [], 0
    for line in text.splitlines():
        if re.match(r"^\s*#{1,6}\s", line):
            continue
        if re.match(r"^\s*(?:[#@]\w[\w-]*\s*)+$", line):
            continue  # csak hashtagekből / említésekből álló sor: nem mondat
        if skip_dialogue and re.match(r"^\s*[–—-]\s", line):
            skipped += 1
            continue
        line = re.sub(r"^\s*(?:>\s*|[*+\-]\s+|\d+[.)]\s+)", "", line)
        lines.append(re.sub(r"\*\*|__|\*", "", line))
    paras = [
        " ".join(p.split())
        for p in re.split(r"\n\s*\n", "\n".join(lines))
        if p.strip()
    ]
    return paras, skipped


def protect(s: str) -> str:
    s = re.sub(rf"\b({ABBR})\.", rf"\1{DOT}", s, flags=re.IGNORECASE)
    s = re.sub(r"\b([A-ZÁÉÍÓÖŐÚÜŰ])\.(?=\s)", rf"\1{DOT}", s)
    s = re.sub(r"\b([IVXLC]+)\.(?=\s+\d)", rf"\1{DOT}", s)  # római szám + sorszám: „(II. 20.)”
    s = re.sub(r"(\d+)\.(?=\s+§)", rf"\1{DOT}", s)  # „8. §”
    s = re.sub(r"(\d+)\.(?=\s+\([IVXLC\d])", rf"\1{DOT}", s)  # „12/2025. (II. 20.)”
    # sorszám + záró jel + kisbetű: „20.) önkormányzati”, „2025. március”
    return re.sub(r"(\d+)\.(?=[)\]»”\"’]*\s+[a-záéíóöőúüű])", rf"\1{DOT}", s)


def sentences(par: str) -> list[str]:
    out = re.findall(
        r".+?(?:[.!?…]+[\"”»’)\]]*(?=\s|$)|$)", protect(par), flags=re.DOTALL
    )
    return [x.replace(DOT, ".").strip() for x in out if x.strip()]


def words(s: str) -> list[str]:
    return [w.lower() for w in WORD.findall(s) if not w.strip("_") == ""]


def grade(value: float, ok_max: float, bad_min: float) -> str:
    """rendben, ha value <= ok_max; gyanús, ha value > bad_min; különben határeset."""
    if value <= ok_max:
        return "rendben"
    return "gyanús" if value > bad_min else "határeset"


def runs(keys: list[str], min_len: int) -> list[tuple[int, int, str]]:
    """Egymást követő azonos kulcsok sorozatai: (kezdő sorszám, hossz, kulcs)."""
    found, i = [], 0
    while i < len(keys):
        j = i
        while j + 1 < len(keys) and keys[j + 1] == keys[i] and keys[i]:
            j += 1
        if j - i + 1 >= min_len:
            found.append((i + 1, j - i + 1, keys[i]))
        i = j + 1
    return found


def analyse(text: str, skip_dialogue: bool = False) -> dict:
    paras, skipped = clean(text, skip_dialogue)
    sents: list[str] = []
    for p in paras:
        sents.extend(sentences(p))
    toks = [words(s) for s in sents]
    lens = [len(t) for t in toks]
    n_words = sum(lens)
    n = len(sents)
    per_1000 = 1000 / n_words if n_words else 0

    mean = statistics.fmean(lens) if lens else 0.0
    sd = statistics.pstdev(lens) if len(lens) > 1 else 0.0
    short = sum(1 for k in lens if 1 <= k <= 3)
    questions = [s.rstrip("\"”»’)] ").endswith("?") for s in sents]

    # A határozott névelő nem számít kezdőszónak: „A döntéshozók… A kerékpáros…” nem azonos váz.
    first = [
        (t[0] + " " + t[1]) if len(t) > 1 and t[0] in ("a", "az") else (t[0] if t else "")
        for t in toks
    ]
    initial_hanem = sum(1 for f in first if f == "hanem")
    nem_hanem = 0
    for i, t in enumerate(toks):
        start = 0
        for pos, w in enumerate(t):
            if w != "hanem":
                continue
            # Az összevont „nem X, és nem Y, hanem Z” több szembeállításnak számít (legfeljebb 3).
            negs = sum(1 for x in t[start:pos] if x in ("nem", "nemcsak"))
            if negs:
                nem_hanem += min(negs, 3)
            else:
                prev = toks[i - 1] if i else []
                if "nem" in prev or "nemcsak" in prev:
                    nem_hanem += 1
            start = pos + 1

    inverse = 0
    for s in sents:
        low_s = s.lower()
        m_inv = INVERSE.search(low_s)
        # csak akkor, ha a mondatban nincs „hanem” (azt a fenti számláló viszi), és a vessző előtt még nem volt „nem”
        if m_inv and "hanem" not in low_s and not re.search(r"\bnem\b", low_s[: m_inv.start()]):
            inverse += 1

    q_blocks = runs(["q" if q else "" for q in questions], 3)
    same_start = runs(first, 3)

    formula_pars = [
        p
        for p in paras
        if re.sub(r"^[\"„»’(\s–-]+", "", p).lower().startswith(FORMULAS)
    ]
    low = text.lower()
    opinion = sum(low.count(m) for m in OPINION)

    return {
        "szavak": n_words,
        "szavak_a_fájlban": len(WORD.findall(text)),
        "mondatok": n,
        "bekezdések": len(paras),
        "kihagyott_párbeszédsor": skipped,
        "átlagos_mondathossz": round(mean, 1),
        "mondathossz_szórása": round(sd, 1),
        "rövid_mondat_arány_%": round(100 * short / n, 1) if n else 0.0,
        "kérdő_mondat_arány_%": round(100 * sum(questions) / n, 1) if n else 0.0,
        "kérdéssorok": len(q_blocks),
        "nem_hanem_/1000_szó": round(nem_hanem * per_1000, 1),
        "nem_hanem_db": nem_hanem,
        "inverz_szembeállítás_db": inverse,
        "szembeállítás_db": nem_hanem + inverse,
        "szembeállítás_/1000_szó": round((nem_hanem + inverse) * per_1000, 1),
        "mondatkezdő_hanem": initial_hanem,
        "azonos_kezdésű_sorozatok": len(same_start),
        "formulával_induló_bekezdés_%": (
            round(100 * len(formula_pars) / len(paras), 1) if paras else 0.0
        ),
        "véleményjelölők": opinion,
        "_részletek": {
            "azonos_kezdés": [
                f"{s}. mondattól {k} mondat „{w}” szóval kezdődik"
                for s, k, w in same_start
            ],
            "kérdéssor": [f"{s}. mondattól {k} kérdés egymás után" for s, k, _ in q_blocks],
            "formulás_bekezdés": [p[:60] for p in formula_pars],
        },
    }


def table(m: dict) -> list[tuple[str, str, str, str, str]]:
    short = m["rövid_mondat_arány_%"]
    sd = m["mondathossz_szórása"]
    mean = m["átlagos_mondathossz"]
    sd_state = "rendben" if sd >= 8 else "gyanús" if sd < 4 else "határeset"
    mean_state = "gyanús" if 15 <= mean <= 19 and sd < 4 else "információ"
    few = m["szavak"] < MIN_WORDS  # rövid szövegen az ezer szavankénti arány félrevezet: darabszám az irányadó
    nh = m["szembeállítás_db"]
    nh_rate = m["szembeállítás_/1000_szó"]
    return [
        ("Átlagos mondathossz (szó)", f"{mean}", "önmagában nem jel", "15–19 és alacsony szórás", mean_state),
        ("Mondathossz szórása", f"±{sd}", "±8 felett", "±4 alatt", sd_state),
        ("1–3 szavas mondatok", f"{short}%", "0–8%", "10% felett", grade(short, 8, 10)),
        ("Kérdő mondatok", f"{m['kérdő_mondat_arány_%']}%", "0–5%", "8% felett", grade(m["kérdő_mondat_arány_%"], 5, 8)),
        ("Kérdéssorok (3+ kérdés)", f"{m['kérdéssorok']}", "0–1", "2 felett", grade(m["kérdéssorok"], 1, 2)),
        (
            "szembeállítás („nem… hanem”, „X, nem Y”)",
            f"{nh} db" if few else f"{nh_rate} / 1000 szó ({nh} db)",
            "legfeljebb 1 db" if few else "0–2 / 1000 szó",
            "3 db vagy több" if few else "4 felett / 1000 szó",
            grade(nh, 1, 2) if few else grade(nh_rate, 2, 4),
        ),
        ("Mondatkezdő „Hanem”", f"{m['mondatkezdő_hanem']}", "0–1", "3 felett", grade(m["mondatkezdő_hanem"], 1, 2)),
        ("Azonos kezdésű sorozatok (3+)", f"{m['azonos_kezdésű_sorozatok']}", "0–1", "3 felett", grade(m["azonos_kezdésű_sorozatok"], 1, 3)),
        ("Formulával induló bekezdés", f"{m['formulával_induló_bekezdés_%']}%", "0–20%", "40% felett", grade(m["formulával_induló_bekezdés_%"], 20, 40)),
    ]


def render(m: dict) -> str:
    rows = table(m)
    head = ("Mutató", "Érték", "Természetes", "Gyanús", "Állapot")
    w = [max(len(r[i]) for r in [head, *rows]) for i in range(5)]
    fmt = "  ".join(f"{{:<{x}}}" for x in w)
    out = [
        "magyar-humanizer – stilometriai mutatók (közelítés)",
        f"szavak: {m['szavak']}"
        + (f" (a fájlban összesen {m['szavak_a_fájlban']})" if m["szavak_a_fájlban"] != m["szavak"] else "")
        + f" · mondatok: {m['mondatok']} · bekezdések: {m['bekezdések']}"
        + (f" · kihagyott párbeszédsor: {m['kihagyott_párbeszédsor']}" if m["kihagyott_párbeszédsor"] else ""),
    ]
    if m["szavak"] < MIN_WORDS:
        out.append(
            f"FIGYELEM: {MIN_WORDS} szó alatt a küszöbök nem értelmezhetők, az értékek csak tájékoztatók"
            " (a szószám a mondatokban lévő szavakat jelenti: fejléc, kód és jelölő nélkül)."
            " A mondathossz szórása (M2) 80 szó felett ettől függetlenül érvényes."
            " Használd a C réteg három kérdését."
        )
    out += ["", fmt.format(*head), fmt.format(*("-" * x for x in w))]
    out += [fmt.format(*r) for r in rows]
    bad = sum(1 for r in rows if r[4] == "gyanús")
    if m["szavak"] < MIN_WORDS:
        out += ["", f"Gyanús mutató: {bad} ({MIN_WORDS} szó alatt csak tájékoztató; a C réteg három kérdése dönt)."]
    else:
        out += ["", f"Gyanús mutató: {bad}. Három vagy több egyszerre már mintázat."]
    for title, key in (
        ("Azonos kezdésű sorozatok", "azonos_kezdés"),
        ("Kérdéssorok", "kérdéssor"),
        ("Formulával induló bekezdések", "formulás_bekezdés"),
    ):
        items = m["_részletek"][key]
        if items:
            out.append(f"{title}: " + "; ".join(items[:5]))
    out += [
        "",
        f"Véleményjelölő („szerintem” stb.): {m['véleményjelölők']}. "
        "A tapasztalati elemeket (megnevezett helyzet, időpont, szám, név, saját tévedés) számold meg kézzel (S8): "
        "ha több a jelölő, a személyesség díszlet.",
        "Kézzel ítélendő még: a bekezdések „dolga” (S1), a központi tétel újrafogalmazása (S9), a rejtett lista (S10).",
    ]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="szövegfájl, vagy - a standard bemenethez")
    ap.add_argument("--skip-dialogue", action="store_true", help="a gondolatjellel kezdődő párbeszédsorok kihagyása (széppróza)")
    ap.add_argument("--json", action="store_true", help="géppel olvasható kimenet")
    args = ap.parse_args()

    try:
        text = sys.stdin.read() if args.file == "-" else Path(args.file).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Nem olvasható a bemenet: {e}", file=sys.stderr)
        return 2
    m = analyse(text, args.skip_dialogue)
    if not m["mondatok"]:
        print("A bemenetben nincs elemezhető mondat.", file=sys.stderr)
        return 2
    if args.json:
        m["állapot"] = {r[0]: r[4] for r in table(m)}
        print(json.dumps(m, ensure_ascii=False, indent=2))
    else:
        print(render(m))
    return 0


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if sys.stderr.encoding and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    if sys.stdin.encoding and sys.stdin.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
