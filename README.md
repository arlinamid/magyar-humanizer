![Magyar Humanizer Banner](banner.png)

# Magyar Humanizer

[![Version](https://img.shields.io/badge/version-2.2.0-blue?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/CHANGELOG.md)
[![Patterns](https://img.shields.io/badge/minták-26%20%2B%209%20%2B%2010-green?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/SKILL.md)
[![Install](https://img.shields.io/badge/npx-skills%20add-black?style=flat-square)](https://github.com/vercel-labs/skills)
[![Language](https://img.shields.io/badge/nyelv-magyar-red?style=flat-square)](https://github.com/arlinamid/magyar-humanizer)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](https://github.com/arlinamid/magyar-humanizer/blob/master/LICENSE)

> AI-szag eltávolítása magyar szövegekből – agent skill Claude Code-hoz, Codexhez, Cursorhoz és társaikhoz

```bash
npx skills add arlinamid/magyar-humanizer
```

---

## Három réteg, mindig mind a három

Ez a skill v2.0-tól **három kötelező rétegből** áll, és ez a lényege:

| Réteg | Mit tartalmaz | Hatókör |
|-------|---------------|---------|
| **A – általános** (1–26) | Nyelvfüggetlen AI-minták: felfújt jelentőség, reklámnyelv, homályos hivatkozás, AI-szókincs, gondolatjel, félkövér, emoji, chatbot-töredékek | mondat, bekezdés |
| **B – magyar** (M1–M9) | Szórend, ritmus, terpeszkedés, főnevesítés, magyar klisék, regiszter, személykonzisztencia, névismétlés | mondat, bekezdés |
| **C – stilometriai** (S1–S10) | Gondolatvezetés szabályossága, szerkezeti ismétlődés, bináris érvelés, szemantikai körkörösség | **teljes szöveg** |

**A B réteg kiegészítés, nem helyettesítés.** A v1 leggyakoribb hibája az volt, hogy az agent meglátta a magyar szöveget, és csak a magyar rétegen futott végig – ettől bennmaradt a „mérföldkövet jelent”, a „szakértők szerint” és a három félkövér kiemelés bekezdésenként. A v2 a sorrendet kötelezővé teszi, és egy záró réteg-audittal kikényszeríti.

---

## Mit ad hozzá a C réteg?

Az A és B réteg mondatokat javít. A C réteg **arányokat mér** – mert egy szöveg minden egyes mondata lehet természetes, miközben a szöveg egésze gépi.

| Minta | Leírás |
|-------|--------|
| S1 | Feltűnően szabályos gondolatvezetés – minden bekezdésnek egyértelmű dolga van, semmi nem lóg ki |
| S2 | A „nem az… hanem…” szerkezet túlhasználata, a mondatkezdő „Hanem” |
| S3 | Rövid mondatok mint rendszer – a nyomatékosítás sablonná válik |
| S4 | Retorikai kérdések halmozása, mindig ugyanabban a dramaturgiai szerepben |
| S5 | Azonos vázú mondatsorozatok – a párhuzam tovább tart, mint ameddig ember fenntartaná |
| S6 | Két pólusra egyszerűsített érvelés, a köztes esetek eltüntetése |
| S7 | Az átmenetek túlzott jelölése – a szöveg a saját szerkezetét magyarázza |
| S8 | „Szerintem”-szindróma – a személyességet jelölő hordozza tapasztalat helyett |
| S9 | Szemantikai körkörösség – ugyanaz a tétel négyszer, új tartalom nélkül |
| S10 | Felsorolások folyó szövegbe rejtve |

A réteghez **mérhető mutatótábla** is tartozik: mondathossz-szórás, rövid mondatok aránya, „hanem”-sűrűség, véleményjelölő/tapasztalat arány. Egyetlen kilógó érték semmit nem jelent – **három vagy több egyszerre már mintázat.**

---

## Telepítés

### npx skills (ajánlott)

```bash
npx skills add arlinamid/magyar-humanizer
```

Felismeri a gépen lévő agenteket és felajánlja a telepítést. Konkrét célok:

```bash
npx skills add arlinamid/magyar-humanizer --agent claude-code codex cursor
npx skills add arlinamid/magyar-humanizer -g       # globálisan
npx skills update magyar-humanizer                 # frissítés
```

Támogatott: **Claude Code** (CLI és Desktop), **OpenAI Codex CLI**, **Cursor**, **Windsurf**, **GitHub Copilot**, **Gemini CLI / Antigravity**, **Cline**, **Zed**. Mindegyik a teljes SKILL.md-t kapja.

### Kézzel

```bash
git clone https://github.com/arlinamid/magyar-humanizer ~/.claude/skills/magyar-humanizer
```

### Régi, szabályfájl-alapú beállításokhoz

Ha az agented még nem ismeri a skill-mappát és csak szabályfájlt olvas, az `install/` transzpilere legenerálja a méretkorlátos formátumokat (Cursor `.mdc`, Windsurf rule, Copilot instructions, Gemini TOML, `AGENTS.md`):

```bash
node install/build.js --all
```

Részletek: [install/README.md](install/README.md)

---

## Beépített eszközök

A `dict/` mappában öt offline eszköz. Egyik sem igényel API-kulcsot.

```bash
python dict/ensure.py       # szótár + tezaurusz + spylls + adatbázis, ha hiányzik
python dict/fetch.py        # kézi letöltés — rákérdez, mely nyelvek kellenek
```

A szótárak a [LibreOffice/dictionaries](https://github.com/LibreOffice/dictionaries) repóból jönnek. A magyar mindig települ; tezaurusz 29 nyelvhez, helyesírási szótár 66-hoz érhető el.

### Helyesírás-ellenőrzés – kötelező lépés

```bash
python dict/spell.py check szoveg.md --suggest
```

Nem opcionális segédeszköz: az átírás közben keletkezik a legtöbb elgépelés, mert szavakat cserélsz és mondatokat szerkesztesz át. A skill ellenőrizetlen szöveget nem ad vissza.

Teljes hunspell motorral fut, nem szólistával. Ez a magyarban nem finomhangolás: a „kulcsfontosságú” nem szerepel külön a szótárfájlban, a hunspell összetételként állítja elő – szólistával téves hibának látszana, és a ragozott alakok tömegesen buknának.

### Tezaurusz – kereszt-ellenőrzéssel

```bash
python dict/thesaurus.py lookup kiemelkedő --verify
```

A LibreOffice magyar tezaurusza 21 687 szócikket és 30 500 jelentéscsoportot tartalmaz. A `--verify` minden jelöltről megmondja, hogy valódi szó-e, melyik jelentéscsoportból jött, és **kölcsönös-e** a szinonimaviszony:

```
kiemelkedő -> kiváló    helyesírás: rendben   tezaurusz: rendben   kölcsönös: rendben
kiemelkedő -> sárcipő   helyesírás: rendben   tezaurusz: rendben   kölcsönös: FIGYELEM
```

A „sárcipő” valódi szó, és szerepel is a tezauruszban – csak éppen semmi köze a „kiemelkedő”-höz. Egyedül a kölcsönösség fogja meg. Pontosan ez hiányzott a korábbi JSON-alapú megoldásból.

### Adatbázis – amit a skill maga épít

```bash
python dict/db.py add "szerepet játszik" "hat" --pattern M3 --context "…"
python dict/db.py scan szoveg.md
python dict/db.py verify
```

A `humanizer.db` (SQLite) nem beégetett lista: az induló készlet csak mag, a tartalom a munkából jön. Minden bejegyzés átmegy a kereszt-ellenőrzésen, és az eredmény eltárolódik, tehát utólag is látszik, mi mennyire megbízható. A verziókövetett forma a `dict/seed.tsv` – bináris SQLite-ot nem commitolunk, mert nem olvasható a diffje.

Részletek és licencek: [dict/README.md](dict/README.md)

---

## Használat

A skill automatikusan aktiválódik, ha magyar szöveg humanizálásáról van szó. Explicit hívás Claude Code-ban:

```
/magyar-humanizer

[szöveg ide]
```

A kimenet az átírt szöveg, és a változtatások **rétegenként bontva** (A / B / C) – így látszik, hogy mind a három lefutott.

---

## Fájlszerkezet

```
magyar-humanizer/
├── SKILL.md              — a skill magja: kötelező sorrend, eszközök, kimenet
├── CHANGELOG.md          — fejlesztési napló
├── references/           — A/B/C rétegek, publicisztika, ellenőrzőlista, példák
├── dict/
│   ├── README.md         — eszközök, kereszt-ellenőrzés, licencek
│   ├── ensure.py         — bootstrap: telepít, ha hiányzik
│   ├── fetch.py          — szótárletöltő (interaktív nyelvválasztás)
│   ├── spell.py          — helyesírás-ellenőrzés (spylls / hunspell)
│   ├── thesaurus.py      — MyThes tezaurusz kereszt-ellenőrzéssel
│   ├── db.py             — a skill saját SQLite adatbázisa
│   ├── paths.py          — hová kerülnek a szótárak és az adatbázis
│   ├── seed.tsv          — szócsere-mag (verziókövetett)
│   ├── seed-ignore.tsv   — helyesírási kivételek magja
│   └── data/             — letöltött szótárak (gitignore-olt)
└── install/
    ├── README.md         — telepítési útmutató agentenként
    ├── build.js          — transzpiler a szabályfájl-formátumokhoz
    ├── compact.md        — kézzel sűrített változat (drift-ellenőrzéssel)
    └── dist/             — generált kimenetek (gitignore-olt)
```

---

## Műfajok és stílusrétegek

- **Köznyelvi / újságírói** – Index, HVG, Magyar Narancs stílus
- **Irodalmi / esszé, publicisztika** – Jelenkor, Litera, WMN, 24.hu stílus (`references/publicisztika.md`)
- **Szépirodalmi próza** – novella, regényrészlet, párbeszéd-tipográfia, nyelvjárás (`references/szepproza.md`)
- **Közösségi média** – Facebook-, LinkedIn-poszt: horog-nyitány, emojis lista, hashtag-halmaz, kommentvadász zárás (`references/kozossegi-media.md`)
- **Hivatalos / jogi** – törvényszöveg, AB-határozat stílus

Minden műfajban érvényes a **tartalmi hűség** szabálya: a humanizálás nem ad hozzá tényt, forrást, számot, véleményt vagy élményt, ami az eredetiben nincs – ahol a szerző saját részlete kellene, jelölést hagy.

---

## Korlátok

Ez szövegszerkesztő eszköz, nem detektor-megkerülő. Az automatikus MI-detektorok százalékos értéke nem szerzőségi bizonyíték: emberi szöveget is minősítenek gépinek, és gépi szöveg is átcsúszik rajtuk. Jelentős tartalmi MI-közreműködésnél szakmailag és etikailag helyes jelezni a használatot; aki a szöveget a neve alatt közli, felelős az adatokért és a hivatkozásokért. Az EU MI-rendelet 50. cikk (4) bekezdése szerint jelezni kell a nyilvánosság közérdekű tájékoztatására közzétett MI-generált szöveget (2026. augusztus 2-tól alkalmazandó) – érdemi emberi felülvizsgálat esetén nem szükséges.

---

## Források

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) – az A réteg alapja (WikiProject AI Cleanup)
- [@blader/humanizer](https://github.com/blader/humanizer) – az eredeti skill
- 2022 előtti magyar korpusz (Index, HVG, Magyar Narancs, Jelenkor, Litera, törvényszövegek, AB-határozatok) – a B réteg alapja
- [Caimelot: Az MI-használat felismerhető nyomai – mit mutat meg a stilometria?](https://caimelot.blogspot.com/2026/09/az-mi-hasznalat-felismerheto-nyomai-mit.html) (2026) – a C réteg alapja
- [LibreOffice/dictionaries](https://github.com/LibreOffice/dictionaries) – hunspell + MyThes tezaurusz (offline)
- [vercel-labs/skills](https://github.com/vercel-labs/skills) – a telepítéshez használt skills CLI

---

## Hozzájárulás

Ha van egy mintád, ami nálad bevált – nyiss egy pull requestet. Bővítsük együtt.

Changelog: [CHANGELOG.md](CHANGELOG.md)

---

[![MIT License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](LICENSE)
