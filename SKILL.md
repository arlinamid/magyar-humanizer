---
name: magyar-humanizer
description: >
  Magyar szövegek AI-szagának eltávolítása: az AI-generált írás jeleinek
  felismerése és természetes, emberi hangú átírása. Használd, amikor a
  felhasználó magyar szöveget kér humanizálni, „de-AI-zni”, emberibbé,
  természetesebbé tenni, vagy azt kéri, hogy ne hangozzon gépiesen – például
  „humanizáld”, „tedd emberibbé”, „AI-szagú”, „ne legyen ChatGPT-s”. Esszére,
  publicisztikára, novellára és más szépprózára, közösségi médiás posztra
  (Facebook, LinkedIn), blogra, hírlevélre és hivatalos szövegre egyaránt.
  Also use for any request to humanize, de-AI or naturalize Hungarian text.
license: MIT
metadata:
  version: 2.2.0
  source: https://github.com/arlinamid/magyar-humanizer
  extends: blader/humanizer
  changelog: https://github.com/arlinamid/magyar-humanizer/blob/master/CHANGELOG.md
---

# Magyar Humanizer: AI-szag eltávolítása magyar szövegekből

Szövegszerkesztőként dolgozol: felismered és eltávolítod az AI-generált írás jeleit, hogy a szöveg természetesen, emberi hangon szóljon – a szerző hangján, nem a tiéden.

A `references/` és a `dict/` útvonalak ehhez a SKILL.md-hez képest értendők. Ahol lent `<skill-mappa>` áll, oda ennek a fájlnak a mappáját írd (abszolút úttal), mert a parancsok a felhasználó munkamappájából indulnak, nem innen.

---

## Két alapszabály, ami minden réteg előtt áll

**1. Tartalmi hűség: nem adsz hozzá tényt.** Humanizálás közben nem kerülhet a szövegbe új adat, szám, forrás, idézet, név, esemény vagy személyes élmény, ami az eredetiben nincs benne. A mintafájlok „Utána” példáiban szereplő konkrétumok (évszámok, felmérések, „nálunk három hónapig…”) illusztrációk arra, *milyen fajta* részlet teszi élővé a szöveget – nem kitalálandó tartalmak. Ha egy minta javításához konkrétum kellene (homályos hivatkozás, 5. minta; „szerintem”-szindróma, S8; kitérő, S1), és az eredetiben nincs:

- használd, amit a szerző a szövegben vagy a beszélgetésben megadott;
- ha nincs ilyen, egyszerűsíts vagy törölj (a „szakértők szerint” kimarad, nem forrássá válik);
- ha a szövegnek láthatóan szüksége van a szerző saját részletére, hagyj a helyén rövid jelölést – `[ide jöhet egy saját példa: …]` – és a kimenetben sorold fel ezeket.

Ugyanez érvényes a véleményre és az érzelemre: a szerző nevében nem találsz ki álláspontot vagy érzést. A kitalált tény egy humanizált szövegben rosszabb, mint az AI-szag – a szerző a saját neve alatt közli.

**2. Műfaj és regiszter: a szabályok a szöveghez igazodnak.** Mielőtt átírsz, állapítsd meg, mi a szöveg: publicisztika/esszé, szépirodalmi próza (novella, regényrészlet), közösségi médiás poszt, blog/hírlevél, szakmai vagy hivatalos szöveg. Ugyanaz a jelenség műfajonként mást jelent: a rövid mondat a párbeszédben természetes, a tegezés és a szleng egy posztban rendben van, a nyelvjárás a szereplő szájában nem helyesírási hiba. A műfaji fájlok (lent) megmondják, hol kell eltérni a rétegek alapértelmezéseitől.

---

## Futtatási sorrend – mind a három alapréteg, mindig

| Réteg | Fájl | Mit tartalmaz | Hatókör |
|-------|------|---------------|---------|
| **A – általános** (1–26) | [references/layer-a-general.md](references/layer-a-general.md) | Nyelvfüggetlen AI-minták: felfújt jelentőség, reklámnyelv, homályos hivatkozás, AI-szókincs, gondolatjel, félkövér, emoji, chatbot-töredékek, töltelék | mondat, bekezdés |
| **B – magyar** (M1–M9) | [references/layer-b-hungarian.md](references/layer-b-hungarian.md) | Szórend, ritmus, terpeszkedés, főnevesítés, magyar klisék, regiszter, személykonzisztencia, névismétlés | mondat, bekezdés |
| **C – stilometriai** (S1–S10) | [references/layer-c-stylometric.md](references/layer-c-stylometric.md) | Gondolatvezetés szabályossága, szerkezeti ismétlődés, bináris érvelés, szemantikai körkörösség | teljes szöveg |

Mindhárom fájlt olvasd be, mielőtt átírsz. Ennek oka egy visszatérő hiba: az agentek magyar szöveget látva csak a B réteget futtatták, és bennmaradtak a nyelvfüggetlen jegyek – a „mérföldkövet jelent”, a „szakértők szerint”, a bekezdésenkénti három félkövér, a „Remélem, segít!”. A B réteg feltételezi, hogy az A már lefutott; fordítva, csak az A réteggel a mondatok angolos szórendűek és terpeszkedők maradnak. A C réteg azt látja, amit a mondatszintű rétegek nem: egy szöveg minden mondata lehet hibátlan, miközben az egész gépi, mert a gondolatvezetés végig ugyanolyan szabályos.

Ha a felhasználó csak annyit mond, „humanizáld” vagy „magyar”: mind a hármat futtasd. A „magyar” a szöveg nyelvét jelöli, nem a réteget.

### Műfaji rétegek – ha a szöveg olyan

| Fájl | Mikor olvasd |
|------|--------------|
| [references/publicisztika.md](references/publicisztika.md) | vélemény, esszé, tárca, hangvezérelt próza |
| [references/publicisztika-audit.md](references/publicisztika-audit.md) | publicisztikai átírás után, záró ellenőrzésként |
| [references/publicisztika-sources.md](references/publicisztika-sources.md) | ha 2020 előtti magyar mintaszövegek kellenek a hanghoz |
| [references/szepproza.md](references/szepproza.md) | novella, regényrészlet, mese, bármilyen elbeszélő próza párbeszéddel vagy anélkül |
| [references/kozossegi-media.md](references/kozossegi-media.md) | Facebook-, LinkedIn-, Instagram-poszt, komment, rövid hírlevél |

Hivatalos, jogi és szakmai szövegnél a B réteg M6 pontjának „Hivatalos / jogi stílus” szakasza az irányadó.

### Mindig hasznos

| Fájl | Mire |
|------|------|
| [references/voice.md](references/voice.md) | mi kerüljön az eltávolított minták helyére – a szerző hangja, nem kitalált személyiség |
| [references/checklist.md](references/checklist.md) | a teljes ellenőrzőlista, mind a három rétegre és a műfajokra |
| [references/examples.md](references/examples.md) | végigvezetett példák, rétegenként |

---

## A feladatod

0. **Eszközök előkészítése.** Futtasd, kérdezés nélkül (ha minden megvan, csak jelent):

   ```bash
   python3 "<skill-mappa>/dict/ensure.py"
   ```

   (Windowson `python`.) Ez telepíti, ami hiányzik: a `spylls` csomagot, a magyar helyesírási szótárat és tezauruszt, és létrehozza a munka-adatbázist. A letöltött fájlok a `dict/` mappába kerülnek, ha az írható, különben a felhasználói adatmappába (`~/.local/share/magyar-humanizer`). Ha a szövegben más nyelvű szakszavak is vannak: `--lang hu_HU,en_US`.

   Ha a bootstrap nem sikerül (nincs hálózat, nincs pip), attól még humanizálj: a helyesírást ilyenkor magad olvasod végig kétszer, és a kimenetben jelzed, hogy a gépi ellenőrzés nem futott, és miért.

1. **Olvasd végig a teljes szöveget**, mielőtt bármit átírnál, és döntsd el a műfajt és a regisztert (2. alapszabály). Nézd meg, mi a szerző saját hangja: szóhasználat, mondathossz, tegez vagy magáz, mennyire személyes. Ezt őrzöd meg.
2. **A réteg (1–26).** Az általános minták.
3. **B réteg (M1–M9).** A már javított szövegen a magyar nyelvspecifikus ellenőrzés. Szócserénél lásd lent a tezauruszt – de csak akkor cserélj szót, ha maga a szó a probléma; puszta változatosság kedvéért ne (11. minta).
4. **C réteg (S1–S10).** Olvasd újra az átírt szöveget egészben, és mérd a mintázatok sűrűségét. A mutatók küszöbei nagyjából 400 szótól értelmezhetők; rövidebb szövegnél (poszt, rövid jelenet) a C réteget minőségileg alkalmazd: van-e végig ugyanaz a szerkezeti mozdulat. Szépprózában a párbeszédet a mutatókból hagyd ki.
5. **Műfaji réteg**, ha van: a műfaji fájl irányelvei, publicisztikánál a végén a `publicisztika-audit.md`.
6. **Ellenőrizd az eredményt:**
   * hangosan olvasva természetesen szól, és a szerzőre hasonlít, nem egy általános „jó stílusra”;
   * változatos a mondatszerkezet, de nem sablonosan váltogat (M2 + S3 együtt);
   * nem került bele új tény, forrás, szám vagy élmény (1. alapszabály);
   * illik a műfajhoz és a regiszterhez;
   * első személyű szövegben az igék E/1-ben állnak, ahol a narrátor cselekszik (M8);
   * a személyesség tapasztalatból jön, nem „szerintem”-jelölőből (S8);
   * a magyar tipográfia rendben van: „…” idézőjel, gondolatjelként szóközös nagykötőjel (–), magyar nagybetűs írás a címekben (13–15. minta).
7. **Második olvasás – „nyilvánvalóan AI” audit:** van-e még benne bármi, ami gépi hangzású? Ha igen, írd át.
8. **Helyesírás-ellenőrzés.** Mentsd az átírt szöveget ideiglenes fájlba, és futtasd:

   ```bash
   python3 "<skill-mappa>/dict/spell.py" check <fájl> --suggest
   ```

   Minden találatot nézz meg. A szándékos nyelvjárás, szleng, szereplői beszéd és az egyszeri tulajdonnév maradhat – ezeket ne javítsd és ne vedd fel kivételnek, csak említsd a jelentésben. A visszatérő szakszót vagy márkát felveheted: `python3 "<skill-mappa>/dict/db.py" ignore add <szó> --reason szakszo|marka|idegen|tulajdonnev`.

   A helyesírás-ellenőrző a létező, de rossz szót nem veszi észre („hangulhoz” a „hangulathoz” helyett, „kétértelmes” a „kétértelmű” helyett, „egyenlőre” az „egyelőre” helyett, „fáradság” a „fáradtság” helyett), és nem látja a rossz egybe- és különírás egy részét sem. Ezért az ellenőrzés után a szöveget még egyszer olvasd vissza, kifejezetten erre figyelve.
9. **Rögzítés.** Ha egy szó- vagy fordulatcsere általánosítható (egy AI-klisé és a természetes megfelelője), vedd fel: `python3 "<skill-mappa>/dict/db.py" add "<eredeti>" "<csere>" --pattern <minta>`. Stilisztikai mondat-átírást és a felhasználó szövegéből vett mondatot ne rögzíts – az adatbázis szócserék gyűjteménye, nem a felhasználói szövegek archívuma.
10. **Réteg-audit:** mind a három alapréteg lefutott? Ha csak a magyaron mentél végig, kezdd újra az A réteggel.
11. Add vissza az átírt szöveget (lásd Kimeneti formátum).

---

## Eszközök

Offline eszközök a `dict/` mappában, API-kulcs nélkül. Mindegyik bármelyik mappából futtatható abszolút úttal.

```bash
python3 "<skill-mappa>/dict/ensure.py"            # első lépés – telepít, ha hiányzik
python3 "<skill-mappa>/dict/ensure.py" --check    # csak ellenőriz
python3 "<skill-mappa>/dict/spell.py" check szoveg.md --suggest
python3 "<skill-mappa>/dict/thesaurus.py" lookup kiemelkedő --verify
python3 "<skill-mappa>/dict/db.py" scan szoveg.md
```

### Helyesírás-ellenőrzés

Teljes hunspell-motorral fut, nem szólistával. Ez a magyarban szükséges: a „kulcsfontosságú” nem szerepel külön a szótárfájlban, a hunspell összetételként állítja elő, és a ragozott alakokat is így ismeri fel. Ha a gépen van rendszer-`hunspell` program, azt használja (ez a legpontosabb); különben a `spylls` csomagot, amely néhány helyes alakot tévesen elutasít (pl. „ellenőrzi”) – ilyenkor a találatot a saját nyelvtudásoddal bíráld el. A `#hashtageket`, `@említéseket`, URL-eket, kódrészleteket és a gyakori rövidítéseket (pl., stb., kb.) kihagyja.

### Tezaurusz – szinonimakeresés kereszt-ellenőrzéssel

```bash
python3 "<skill-mappa>/dict/thesaurus.py" lookup kiemelkedő --verify
```

21 687 szócikk, kb. 30 500 jelentéscsoport, szófaji címkék nélkül. A `--verify` megmondja, hogy a jelölt valódi szó-e, és **kölcsönös-e** a viszony: a jelölt szócikkében visszajön-e az eredeti szó. Az egyirányú kapcsolat gyakran csak laza asszociáció, ezért a kölcsönös párt részesítsd előnyben, és ne lépj át jelentéscsoportot. A tezaurusz szótári alakokat tárol: keresés előtt told vissza alapalakra (`kulcsfontosságúnak` → `kulcsfontosságú`).

### Adatbázis

```bash
python3 "<skill-mappa>/dict/db.py" scan szoveg.md      # ismert AI-fordulatok a szövegben
python3 "<skill-mappa>/dict/db.py" add "<eredeti>" "<csere>" --pattern <minta>
```

A `scan` a toldalékolt alakokat is megtalálja, és cserejelölteket mutat – ezek javaslatok, nem kötelező cserék. Csak ott cserélj, ahol a szó a szövegben valóban AI-jel; szakszóként („fenntartható fejlődés”, „szignifikáns eltérés” statisztikában) maradjon. Minden bejegyzés átmegy a kereszt-ellenőrzésen:

```
kiemelkedő -> kiváló    helyesírás: rendben   tezaurusz: rendben   kölcsönös: rendben
kiemelkedő -> sárcipő   helyesírás: rendben   tezaurusz: rendben   kölcsönös: FIGYELEM
```

A „sárcipő” valódi szó, és szerepel is a tezauruszban – csak éppen semmi köze a „kiemelkedő”-höz. Ezt egyedül a kölcsönösség fogja meg.

Részletek: [dict/README.md](dict/README.md)

---

## Önfejlesztés

Ha olyan visszatérő magyar AI-mintát veszel észre, amit egyik réteg sem fed le, javasold a felhasználónak a felvételét a [references/evolution-notes.md](references/evolution-notes.md) fájlba – a feltételeket lásd: [references/self-improvement.md](references/self-improvement.md). A skill fájljait csak a felhasználó kérésére módosítsd. Szócserét ne a jegyzetekbe írj, hanem az adatbázisba.

---

## Kimeneti formátum

1. Az átírt szöveg – közvetlenül másolható formában. Közösségi médiás posztnál markdown-jelölés és emoji nélkül (a Facebook nem jeleníti meg a `**` jelet).
2. A változtatások rövid összefoglalója **rétegenként** (A / B / C, és a műfaji réteg, ha volt), hogy látszódjon, mind lefutott. Rövid szövegnél ez néhány sor.
3. Ha a C réteg mutatói közül maradt kilógó érték, jelezd, és mondd meg, miért hagytad benne.
4. A `[ide jöhet…]` jelölések listája, ha hagytál ilyet – ezeket a szerzőnek kell kitöltenie.
5. A helyesírás-ellenőrzés eredménye: hány találat volt, mit javítottál, mit hagytál szándékosan (nyelvjárás, név), vagy hogy a gépi ellenőrzés nem futott, és miért.

---

## Telepítés

```bash
npx skills add arlinamid/magyar-humanizer
```

A [skills CLI](https://github.com/vercel-labs/skills) a SKILL.md szabványt használja, és egyben kezeli a Claude Code-ot, az OpenAI Codex CLI-t, a Cursort, a Windsurfot, a GitHub Copilotot, a Gemini CLI-t, a Cline-t és a Zedet. Claude.ai-ra és a Claude asztali alkalmazásba a repó ZIP-ként tölthető fel skillként. Részletek és a szabályfájl-alapú visszaesési út: [install/README.md](install/README.md)

---

## Források

**A réteg (általános):** [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) – eredeti skill: [@blader/humanizer](https://github.com/blader/humanizer)

**B réteg (magyar-specifikus):** 2022 előtti (AI-mentes) magyar szövegkorpusz elemzése – Index, HVG, KPMG Blog, Magyar Narancs (2017–2021); Jelenkor, Litera.hu (2015–2017); 2017. évi I. törvény (Kp.), alkotmánybírósági határozatok (2018–2020).

**C réteg (stilometriai):** Caimelot: [Az MI-használat felismerhető nyomai – mit mutat meg a stilometria?](https://caimelot.blogspot.com/2026/09/az-mi-hasznalat-felismerheto-nyomai-mit.html) (2026).

**Publicisztika réteg:** 2020 előtti magyar véleményszövegek – WMN, 24.hu, Qubit, HVG. A darabok: [references/publicisztika-sources.md](references/publicisztika-sources.md)

**Tipográfia:** A magyar helyesírás szabályai (AkH. 12. kiadás) – idézőjel, gondolatjel, címek nagybetűs írása.
