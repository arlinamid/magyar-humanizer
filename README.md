![Magyar Humanizer Banner](banner.png)

# Magyar Humanizer

[![Version](https://img.shields.io/badge/version-1.4.1-blue?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/CHANGELOG.md)
[![Patterns](https://img.shields.io/badge/minták-26%20általános%20%2B%208%20magyar-green?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/SKILL.md)
[![Language](https://img.shields.io/badge/nyelv-magyar-red?style=flat-square)](https://github.com/arlinamid/magyar-humanizer)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/LICENSE)
[![Based on](https://img.shields.io/badge/alapja-blader%2Fhumanizer-orange?style=flat-square)](https://github.com/blader/humanizer)

> AI-szag eltávolítása magyar szövegekből — Claude Code skill

Az AI-generált szöveg jeleit azonosítja és eltávolítja, hogy a szöveg természetesebben és emberibben hangozzon. Az útmutató a Wikipedia ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) oldalán alapul (WikiProject AI Cleanup, [@blader/humanizer](https://github.com/blader/humanizer)), kiegészítve a magyar nyelvre vonatkozó korpuszelemzéssel.

---

## Mit csinál?

**26 általános minta** (az eredeti humanizer alapján, kibővítve):

- Jelentőség-felfújás, reklámszerű nyelv, homályos hivatkozások
- AI-szókincs, terpeszkedő szerkezetek, negatív párhuzamosságok
- Gondolatjel- és félkövér-túlhasználat, alcímes felsorolások
- Title Case fejlécek, tipográfiai idézőjelek
- Chatbot-töredékek, szikofantikus hangnem, általános zárómondatok
- Kétszavas drámai ütés, narratív fordulópontjelzők
- **Második pass audit** — kötelező újraolvasás az első átírás után

**8 magyar-specifikus kiterjesztés (M1–M8):**

| Minta | Leírás |
|-------|--------|
| M1 | Szórend és fókuszpozíció — pragmatikai szórend helyreállítása |
| M2 | Mondatritmus (burstiness) — egyenletes AI-ritmus felváltása |
| M3 | Terpeszkedő kifejezések → tömör változatok (40+ eset) |
| M4 | Főnevesítés → visszaigésítés |
| M5 | Magyar AI-klisék és felfújt fontosság |
| M6 | Stílusréteg-érzékeny szabályok (köznyelvi / irodalmi / hivatalos) |
| M7 | Első személyű logikai ellentmondás |
| M8 | Személy-inkonzisztencia — T/1 igék E/1 narrációban (CV, önéletírás) |

---

## Beépített eszközök

### Szinonima-keresés (cache-first)

A `synonyms.json` fájl 51 AI-klisé és 22 terpeszkedő kifejezés helyi adatbázisa. Ha a szó megvan benne, nem kell API-t hívni. Ha nincs, a Poet.hu szinonimaszótár API tölti ki, és az eredmény visszaíródik az adatbázisba.

```
szó → synonyms.json → (ha nincs) → Poet.hu API → visszamentés
```

A Poet.hu API hitelesítő adatait a `.env` fájlban kell megadni (lásd `.env.example`).

### Helyesírás-ellenőrzés (pyenchant + hu_HU)

A `dict/` könyvtár a LibreOffice hivatalos Magyar hunspell szótárát tartalmazza. A `pyenchant` könyvtárral használható:

```python
import enchant
d = enchant.Dict('hu_HU')
d.check('kiemelkedő')      # True
d.suggest('kiemelkedo')    # ['kiemelkedő', ...]
```

---

## Telepítés

### Claude Code (ajánlott)

```bash
# Klónozd a teljes repót a skills könyvtárba:
git clone https://github.com/arlinamid/magyar-humanizer \
  ~/.claude/skills/magyar-humanizer
```

Vagy csak a SKILL.md, ha a többi eszközre nincs szükséged:

```bash
mkdir -p ~/.claude/skills/magyar-humanizer
curl -o ~/.claude/skills/magyar-humanizer/SKILL.md \
  https://raw.githubusercontent.com/arlinamid/magyar-humanizer/master/SKILL.md
```

### Poet.hu API beállítása (opcionális)

A szinonima-kereső cache-first módban működik — az API nélkül is használható, de az adatbázisból hiányzó szavakhoz szükséges.

```bash
cp .env.example .env
# Töltsd ki a .env fájlt a saját Poet.hu adataiddal
# Regisztráció: https://poet.hu/api
```

### Helyesírás-ellenőrzés beállítása (opcionális)

```bash
pip install pyenchant
# Másold a szótárfájlokat a pyenchant hunspell könyvtárába
# Részletes útmutató: dict/README.md
```

---

## Használat

Claude Code-ban a skill automatikusan aktiválódik, ha magyar szöveg humanizálásáról van szó. Explicit hívás:

```
/magyar-humanizer

[szöveg ide]
```

---

## Fájlszerkezet

```
magyar-humanizer/
├── SKILL.md          — fő skill (v1.4.1), összes minta és eszköz
├── synonyms.json     — helyi szinonima-adatbázis (bővül minden API-hívásnál)
├── CHANGELOG.md      — teljes fejlesztési napló
├── .env.example      — Poet.hu API credentials sablon
├── .gitignore        — .env kizárva
└── dict/
    ├── README.md     — forrás, licenc, telepítési útmutató
    ├── hu_HU.dic     — LibreOffice Magyar szótár (~1.7 MB, LGPL-2.1/MPL-2.0)
    └── hu_HU.aff     — LibreOffice Magyar ragozási szabályok (~2.2 MB)
```

---

## Stílusrétegek

- **Köznyelvi / újságírói** — Index, HVG stílus
- **Irodalmi / esszé** — Jelenkor, Litera stílus
- **Hivatalos / jogi** — törvényszöveg, AB-határozat stílus

---

## Kapcsolódó projektek

- [@blader/humanizer](https://github.com/blader/humanizer) — az eredeti skill, amin ez alapul
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — forrásanyag
- [Poet.hu szinonimaszótár](https://poet.hu) — Magyar szinonima API
- [LibreOffice/dictionaries](https://github.com/LibreOffice/dictionaries/tree/master/hu_HU) — hu_HU hunspell szótár forrása

---

## Hozzájárulás

Ha van egy mintád, ami nálad bevált — nyiss egy pull requestet. Bővítsük együtt.

---

## Changelog

Lásd: [CHANGELOG.md](CHANGELOG.md)

---

[![MIT License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](LICENSE)
