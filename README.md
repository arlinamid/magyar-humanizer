![Magyar Humanizer Banner](banner.png)

# Magyar Humanizer

[![Version](https://img.shields.io/badge/version-1.1.0-blue?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/CHANGELOG.md)
[![Patterns](https://img.shields.io/badge/minták-24%20általános%20%2B%206%20magyar-green?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/SKILL.md)
[![Language](https://img.shields.io/badge/nyelv-magyar-red?style=flat-square)](https://github.com/arlinamid/magyar-humanizer)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/LICENSE)
[![Based on](https://img.shields.io/badge/alapja-blader%2Fhumanizer-orange?style=flat-square)](https://github.com/blader/humanizer)

> AI-szag eltávolítása magyar szövegekből — Claude Code skill

Az AI-generált szöveg jeleit azonosítja és eltávolítja, hogy a szöveg természetesebben és emberibben hangozzon. Az útmutató a Wikipedia ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) oldalán alapul (WikiProject AI Cleanup, [@blader/humanizer](https://github.com/blader/humanizer)), kiegészítve a magyar nyelvre vonatkozó korpuszelemzéssel.

---

## Mit csinál?

**24 általános minta** (az eredeti humanizer alapján, kibővítve):

- Jelentőség-felfújás, reklámszerű nyelv, homályos hivatkozások
- AI-szókincs, terpeszkedő szerkezetek, negatív párhuzamosságok
- Gondolatjel- és félkövér-túlhasználat, alcímes felsorolások
- Title Case fejlécek, tipográfiai idézőjelek
- Chatbot-töredékek, szikofantikus hangnem, általános zárómondatok
- **Második pass audit** — kötelező újraolvasás az első átírás után

**6 magyar-specifikus kiterjesztés:**

| Minta | Leírás |
|-------|--------|
| M1 | Szórend és fókuszpozíció — pragmatikai szórend helyreállítása |
| M2 | Mondatritmus (burstiness) — egyenletes AI-ritmus felváltása |
| M3 | Terpeszkedő kifejezések → tömör változatok (40+ sor) |
| M4 | Főnevesítés → visszaigésítés |
| M5 | Magyar AI-klisék listája |
| M6 | Stílusréteg-érzékeny szabályok (köznyelvi / irodalmi / hivatalos) |

---

## Telepítés

### Claude Code (ajánlott)

```bash
mkdir -p ~/.claude/skills/magyar-humanizer
curl -o ~/.claude/skills/magyar-humanizer/SKILL.md \
  https://raw.githubusercontent.com/arlinamid/magyar-humanizer/master/SKILL.md
```

### OpenClaw

```bash
mkdir -p ~/.openclaw/workspace/skills/magyar-humanizer
curl -o ~/.openclaw/workspace/skills/magyar-humanizer/SKILL.md \
  https://raw.githubusercontent.com/arlinamid/magyar-humanizer/master/SKILL.md
```

### Kézi

Töltsd le a `SKILL.md` fájlt, és másold a megfelelő skills könyvtárba.

---

## Használat

Claude Code-ban:

```
/humanizer

[szöveg ide]
```

Vagy egyszerűen:

```
Humanizáld ezt a szöveget: [szöveg]
```

A skill automatikusan aktiválódik, ha magyar szöveget kapsz humanizálásra.

---

## Stílusrétegek

A skill három regiszterben dolgozik — add meg, melyiket kéred:

- **Köznyelvi / újságírói** — Index, HVG stílus
- **Irodalmi / esszé** — Jelenkor, Litera stílus
- **Hivatalos / jogi** — törvényszöveg, AB-határozat stílus

---

## Kapcsolódó projektek

- [@blader/humanizer](https://github.com/blader/humanizer) — az eredeti skill, amin ez alapul
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — forrásanyag

---

## Hozzájárulás

Ha van egy mintád, ami nálad bevált — nyiss egy pull requestet. Bővítsük együtt.

---

## Changelog

Lásd: [CHANGELOG.md](CHANGELOG.md)

---

[![MIT License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](LICENSE)
