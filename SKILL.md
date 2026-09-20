---
name: magyar-humanizer
version: 2.1.1
description: >
  Remove signs of AI-generated writing from Hungarian text. Runs a mandatory
  three-layer pass: a language-independent general layer (1-26, from Wikipedia's
  "Signs of AI writing"), a Hungarian-specific layer (M1-M9, from Hungarian corpus
  analysis), and a stylometric whole-text layer (S1-S10). All three always run, in
  order - the Hungarian and stylometric layers are ADDITIONS to the general layer,
  never replacements. Adds an opinion-writing (publicisztika) layer for essays and
  columns, and a mandatory spell-check step. On first use bootstraps LibreOffice
  dictionaries and the local SQLite database via dict/ensure.py if missing. Use
  when editing, reviewing or rewriting Hungarian text so it sounds natural and
  human-written.
source: https://github.com/arlinamid/magyar-humanizer
extends: blader/humanizer
changelog: https://github.com/arlinamid/magyar-humanizer/blob/master/CHANGELOG.md
install: install/README.md
---

# Magyar Humanizer: AI-szag eltávolítása magyar szövegekből

Te egy szövegszerkesztő vagy, aki azonosítja és eltávolítja az AI-generált szöveg jeleit, hogy a szöveg természetesebben és emberibben hangozzon.

---

## ⚠️ KÖTELEZŐ FUTTATÁSI SORREND — ezt olvasd el, mielőtt egyetlen mondatot átírnál

### A három alapréteg — mindig mind a három

| Réteg | Fájl | Mit tartalmaz | Hatókör |
|-------|------|---------------|---------|
| **A — általános** (1–26) | [references/layer-a-general.md](references/layer-a-general.md) | Nyelvfüggetlen AI-minták: felfújt jelentőség, reklámnyelv, homályos hivatkozás, AI-szókincs, gondolatjel, félkövér, emoji, chatbot-töredékek, töltelék | mondat, bekezdés |
| **B — magyar** (M1–M9) | [references/layer-b-hungarian.md](references/layer-b-hungarian.md) | Szórend, ritmus, terpeszkedés, főnevesítés, magyar klisék, regiszter, személykonzisztencia, névismétlés | mondat, bekezdés |
| **C — stilometriai** (S1–S10) | [references/layer-c-stylometric.md](references/layer-c-stylometric.md) | Gondolatvezetés szabályossága, szerkezeti ismétlődés, bináris érvelés, szemantikai körkörösség | **teljes szöveg** |

> **Ezt a három fájlt mindig beolvasod, mind a hármat, mielőtt átírnál.** Nem válogatsz közülük. A lentebbi „szükség szerint olvasd" **kizárólag a feltételes rétegekre** vonatkozik, az alaprétegre soha.

### A leggyakoribb hiba, amit el kell kerülnöd

> **„A szöveg magyar, tehát a magyar réteg elég."** — Ez hibás. A B réteg **kiegészítés**, nem önálló ellenőrzőlista.

Ha csak a B réteget futtatod, bennmaradnak a nyelvfüggetlen AI-jegyek: a „mérföldkövet jelent", a „szakértők szerint", a három félkövér kiemelés bekezdésenként, az emojis fejléc, a „Remélem, segít!". Ezek magyarul pontosan ugyanolyan árulkodók, mint angolul — a B réteg viszont nem foglalkozik velük, mert azt feltételezi, hogy az A réteg már lefutott.

Fordítva is igaz: ha csak az A réteget futtatod magyar szövegen, a mondatok angolos szórendűek és terpeszkedők maradnak.

**A C réteg pedig olyat lát meg, amit egyik mondatszintű réteg sem:** egy szöveg minden mondata lehet hibátlan, miközben a szöveg *egésze* gépi — mert a gondolatvezetés végig ugyanolyan szabályos, mert minden ellentét ugyanabba a retorikai keretbe kerül, mert ugyanaz a tétel négyszer tér vissza. A C réteget nem lehet mondatonként futtatni: **végig kell olvasni az egész szöveget, és a mintázat sűrűségét kell mérni.**

**Ha a felhasználó csak annyit mond, hogy „humanizáld" vagy „magyar":** futtasd mind a hármat. A „magyar" a szöveg nyelvét jelöli, nem azt, melyik réteget használd.

### Feltételes rétegek — csak ha a szöveg olyan

| Réteg | Fájl | Mikor olvasd |
|-------|------|--------------|
| Publicisztika | [references/publicisztika.md](references/publicisztika.md) | vélemény, esszé, tárca, hangvezérelt próza |
| Publicisztika-audit | [references/publicisztika-audit.md](references/publicisztika-audit.md) | publicisztikai átírás **után**, záró ellenőrzésként |
| Publicisztika-források | [references/publicisztika-sources.md](references/publicisztika-sources.md) | ha konkrét 2020 előtti magyar mintaszövegek kellenek |

### Mindig hasznos

| Fájl | Mire |
|------|------|
| [references/voice.md](references/voice.md) | személyiség és lélek — mi kerüljön az eltávolított minták helyére |
| [references/checklist.md](references/checklist.md) | a teljes ellenőrzőlista, mind a három rétegre |
| [references/examples.md](references/examples.md) | végigvezetett példák, rétegenként |

---

## A feladatod

0. **Bootstrap — mielőtt bármit átírnál.** Ha a szótár vagy az adatbázis hiányzik, telepítsd / hozd létre. **Ne kérdezz rá, futtasd:**

   ```bash
   python dict/ensure.py
   ```

   Ez ellenőrzi a `spylls` csomagot, a `dict/data/hu_HU` helyesírási szótárat + tezauruszt, és a `dict/humanizer.db` adatbázist. Ami hiányzik, azt telepíti / létrehozza (`fetch.py` + `db.py import`). Ha a szövegben angol (vagy más) szakszavak is vannak, és azokra is kell motor:

   ```bash
   python dict/ensure.py --lang hu_HU,en_US
   ```

   Csak ellenőrzés telepítés nélkül: `python dict/ensure.py --check`. Ha a bootstrap hibával tér vissza, **ne humanizálj tovább** — javítsd előbb.

1. **Olvasd végig a teljes bemeneti szöveget**, mielőtt bármit átírnál. A C réteg csak így működik.
2. **A réteg (1–26).** Futtasd végig az általános mintákat. Ez mindig az első lépés a bootstrap után, akkor is, ha a szöveg magyar.
3. **B réteg (M1–M9).** A már javított szövegen futtasd a magyar nyelvspecifikus ellenőrzést. Szóalternatívákhoz a tezauruszt használd, és a kölcsönös párokat részesítsd előnyben.
4. **C réteg (S1–S10).** Olvasd újra az immár átírt szöveget **egészben**, és mérd a szerkezeti mintázatok sűrűségét a stilometriai mutatótáblával. Itt nem mondatokat keresel, hanem arányokat.
5. **Feltételes réteg**, ha a szöveg publicisztikai: a `publicisztika.md` irányelvei, majd a végén a `publicisztika-audit.md`.
6. **Ellenőrizd az eredményt:**
   * Hangosan olvasva természetesen szól
   * Változatos mondatszerkezetet használ — de nem sablonosan váltogat (M2 + S3 együtt)
   * Konkrét részleteket ad homályos állítások helyett
   * Megfelel a szöveg stílusrétegének (köznyelvi / irodalmi / hivatalos / publicisztikai)
   * **Első személyű szövegben:** minden ige E/1 — nincs T/1 „eredménybújtatás", nincs E/3 perspektívaváltás (M8)
   * **A személyessége tapasztalatból jön, nem jelölőből** — több a konkrét részlet, mint a „szerintem" (S8)
7. **Második pass — „Nyilvánvalóan AI" audit:** olvasd újra. Van-e benne bármi, ami még mindig nyilvánvalóan AI-generált hangzású? Ha igen, írd át.
8. **Helyesírás-ellenőrzés — kötelező.** Lásd lent. **Ellenőrizetlen szöveget ne adj vissza.**
9. **Rögzítés.** Amit cseréltél, vedd fel az adatbázisba.
10. **Réteg-audit:** ellenőrizd, hogy **mind a három alapréteget** lefuttattad-e. Ha csak a magyar rétegen mentél végig, kezdd elölről az A réteggel.
11. Add meg az átírt verziót.

---

## Eszközök

Offline eszközök a `dict/` mappában. Egyik sem igényel API-kulcsot.

```bash
python dict/ensure.py                 # KÖTELEZŐ első lépés — telepít, ha hiányzik
python dict/ensure.py --check         # csak ellenőriz
python dict/fetch.py --lang hu_HU     # kézi szótárletöltés
pip install spylls                    # a teljes hunspell motorhoz (az ensure is megteszi)
```

### 1. Helyesírás-ellenőrzés — KÖTELEZŐ LÉPÉS

**Nem opcionális segédeszköz, hanem a folyamat része.**

```bash
python dict/spell.py check szoveg.md --suggest
```

Az átírás közben keletkezik a legtöbb elgépelés és rossz toldalékolás, mert épp akkor cserélsz szavakat és szerkesztesz át mondatokat. Minden találatot nézz meg: vagy javítsd, vagy — ha szándékos (angol szakszó, név) — vedd fel kivételnek: `python dict/db.py ignore add <szó> --reason idegen|tulajdonnev|marka|szakszo`.

Teljes hunspell motorral fut, nem szólistával. Ez a magyarban nem finomhangolás: a „kulcsfontosságú" nem szerepel külön a szótárfájlban, a hunspell összetételként állítja elő — szólistával téves hibának látszana, és a ragozott alakok tömegesen buknának.

### 2. Tezaurusz — szinonimakeresés kereszt-ellenőrzéssel

```bash
python dict/thesaurus.py lookup kiemelkedő --verify
```

21 687 szócikk, 30 500 jelentéscsoport, szófaji címkékkel. A `--verify` megmondja, hogy a jelölt valódi szó-e, melyik jelentésből jött, és **kölcsönös-e** a viszony.

**A kölcsönösség a legfontosabb.** Az egyirányú kapcsolat gyakran csak laza asszociáció. Cserélés előtt nézd meg — és soha ne lépj át jelentéscsoportot. A tezaurusz **szótári alakokat** tárol: keresés előtt told vissza alapalakra (`kulcsfontosságúnak` → `kulcsfontosságú`).

### 3. Adatbázis — amit a skill maga épít

```bash
python dict/db.py scan szoveg.md          # ismert fordulatok a szövegben
python dict/db.py add "<eredeti>" "<csere>" --pattern <minta> --context "<mondat>"
```

A `dict/humanizer.db` tárolja, mit mire cseréltünk, melyik minta alapján, milyen mondatban. Az induló készlet csak mag; a valódi tartalom a munkából jön. **Amikor cserélsz, rögzítsd.** Minden bejegyzés automatikusan átmegy a kereszt-ellenőrzésen:

```
#35  kiemelkedő -> kiváló   helyesírás: rendben   tezaurusz: rendben   kölcsönös: rendben
#36  kiemelkedő -> sárcipő  helyesírás: rendben   tezaurusz: rendben   kölcsönös: FIGYELEM
```

A második sor mutatja, miért kell a kölcsönösség: a „sárcipő" valódi szó, szerepel is a tezauruszban — csak éppen semmi köze a „kiemelkedő"-höz.

Részletek: [dict/README.md](dict/README.md)

---

## Önfejlesztés

Ha olyan visszatérő magyar AI-mintát vagy átírási heurisztikát veszel észre, amit egyik réteg sem fed le, annak helye van a skill memóriájában. A feltételeket és a formátumot lásd: [references/self-improvement.md](references/self-improvement.md), a jegyzetek helye: [references/evolution-notes.md](references/evolution-notes.md).

Röviden: csak akkor jegyezd fel, ha a minta legalább kétszer előfordult vagy nyilvánvalóan általánosítható, 2–6 sorban leírható, és még nincs benne a rétegfájlokban. Felhasználói szöveget ne másolj bele.

A szócseréket ne ide írd, hanem az adatbázisba (`dict/db.py add`) — az jobban kereshető, és át is megy a kereszt-ellenőrzésen.

---

## Kimeneti formátum

Add meg:

1. Az átírt szöveget
2. A változtatások rövid összefoglalóját — **rétegenként bontva** (A / B / C), hogy látszódjon, mind a három lefutott
3. Ha a C réteg mutatótáblájában maradt kilógó érték, jelezd, és mondd meg, miért hagytad benne
4. A helyesírás-ellenőrzés eredményét: hány találat volt, mit javítottál, mit vettél fel kivételnek

---

## Telepítés

```bash
npx skills add arlinamid/magyar-humanizer
```

A [skills CLI](https://github.com/vercel-labs/skills) a SKILL.md szabványt használja, és egyben kezeli a Claude Code-ot (CLI és Desktop), az OpenAI Codex CLI-t, a Cursort, a Windsurfot, a GitHub Copilotot, a Gemini CLI-t, a Cline-t és a Zedet. Mindegyik a teljes csomagot kapja, a `references/` mappával együtt.

Részletek és a szabályfájl-alapú visszaesési réteg: [install/README.md](install/README.md)

---

## Források

**A réteg (általános):** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) — eredeti skill: [@blader/humanizer](https://github.com/blader/humanizer)

**B réteg (magyar-specifikus):** 2022 előtti (AI-mentes) magyar szövegkorpusz elemzése — Index, HVG, KPMG Blog, Magyar Narancs (2017–2021); Jelenkor, Litera.hu (2015–2017); 2017. évi I. törvény (Kp.), alkotmánybírósági határozatok (2018–2020).

**C réteg (stilometriai):** Caimelot: [Az MI-használat felismerhető nyomai — mit mutat meg a stilometria?](https://caimelot.blogspot.com/2026/09/az-mi-hasznalat-felismerheto-nyomai-mit.html) (2026).

**Publicisztika réteg:** 2020 előtti magyar véleményszövegek elemzése — WMN, 24.hu, Qubit, HVG. A konkrét darabokat lásd: [references/publicisztika-sources.md](references/publicisztika-sources.md)
