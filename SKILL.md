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

A `references/` és a `dict/` útvonalak ehhez a SKILL.md-hez képest értendők. Ahol lent `<skill-mappa>` áll, oda ennek a fájlnak a mappáját írd (abszolút úttal), mert a parancsok a felhasználó munkamappájából indulnak, nem innen. Ha a host nem adja meg a skill útvonalát: az a mappa, ahonnan ezt a SKILL.md-t beolvastad; ha az sem ismert, keresd meg a `name: magyar-humanizer` fejlécű SKILL.md-t, vagy kérdezd meg a felhasználót.

---

## Két alapszabály, ami minden réteg előtt áll

**1. Tartalmi hűség: nem adsz hozzá tényt.** Humanizálás közben nem kerülhet a szövegbe új adat, szám, forrás, idézet, név, esemény vagy személyes élmény, ami az eredetiben nincs benne. A mintafájlok „Utána” példái nem adnak hozzá tényt; az egyetlen konkrétum, ami bennük megjelenik, a „Szerzői háttér” jelölésű rész, és azt a példa szerint a szerző adta. Ha egy minta javításához konkrétum kellene (homályos hivatkozás, 5. minta; „szerintem”-szindróma, S8; kitérő, S1), és az eredetiben nincs:

- használd, amit a szerző a szövegben vagy a beszélgetésben megadott;
- ha nincs ilyen, egyszerűsíts vagy törölj (a „szakértők szerint” kimarad, nem forrássá válik);
- ha a hiány a szöveg érthetőségét vagy hitelességét rontja, és a szerző valószínűleg tud mit írni, hagyj a helyén rövid jelölést – `[ide jöhet egy saját példa: …]` – és a kimenetben sorold fel ezeket; ne szórd tele a szöveget, szövegenként néhány jelölés a legtöbb.

Ugyanez érvényes a véleményre és az érzelemre: a szerző nevében nem találsz ki álláspontot vagy érzést. A kitalált tény egy humanizált szövegben rosszabb, mint az AI-szag – a szerző a saját neve alatt közli.

**Logikai viszonyok.** A tényeken túl a viszonyok sem változhatnak: tagadás, ok és következmény, fokozás, feltétel, ellentét, nyomaték. Összevonás vagy kihagyás után olvasd vissza: ugyanazt állítja-e, ugyanolyan erősen? Két tipikus hiba: a kihagyott tagadás megfordítja a mondatot (*„Egy szoftver nem ad megértést, egy tanfolyam gyakorlatot”* azt jelenti, hogy a tanfolyam ad; helyesen *„… egy tanfolyam gyakorlatot sem”*), és az enyhébb szó gyengíti az állítást (*„nem az a kérdés, hogy van-e pénz”* ≠ *„kevésbé fontos, hogy van-e pénz”*). A véleményjelölő (*szerintem*, *úgy gondolom*) csak arra az állításra vonatkozzon, amelyre az eredetiben: összevonáskor ne terjedjen ki az eredetileg ténymondatra, és a vélemény se váljon ténnyé. A fokozás is viszony: a „nem csupán X, hanem Y” (Y több) ne legyen „X, de egyben Y is”; helyes: „X-nél több: Y”. A mód is: kérdésből ne legyen kötelezettség („mennyibe kerül?” → „tisztázni kell…”), kijelentésből kérdés, és fordítva. A szerző tartalmas felsorolásának (három konkrét előny) elemei összevonáskor sem hagyhatók el; csak az ismétlő, töltelék elem. Erősség: a „mellékes”, „nem számít” egyenértékű a „nem az számít” erősségével; a „kevésbé fontos”, „is számít” gyengébb.

**Kötőszó és alcím.** Kötőszót (pedig, így, ezért, tehát, mert) csak akkor adj hozzá, ha az eredeti ugyanazt a viszonyt fejezi ki: a „pedig” ellentétet, az „így” és az „ezért” következményt állít. Címet és alcímet csak a 13. minta szerint (Title Case) vagy akkor írj át, ha maga is AI-minta (*„a … világában”*); új alcímet ne találj ki, a bekezdések sorrendjét ne cseréld fel.

**Idézet.** A szó szerinti idézetet (idézőjelben, másoktól vagy a szerzőtől) ne írd át, ne tolmácsold, akkor sem, ha AI-szagú; legfeljebb az idézőjelet igazítsd „…” alakra. Ha maga az idézet AI-jel, jelezd a kimenetben. Példa: a tanárnő szerint a dolgozat *„változatos és izgalmas kihívást jelent”* – az idézet marad szó szerint, a kimenet pedig jelzi, hogy AI-szagú, de idézet.

**Törölt hivatkozás.** Ha a „szakértők szerint”-féle hivatkozás kimarad, és a megmaradó állítás vitatható vagy tényszerű, ne hagyd forrás nélküli tényként: jelölj `[ide jöhet a forrás: …]`-t. Ha az állítás magától értetődő, elég a törlés.

**2. Műfaj és regiszter: a szabályok a szöveghez igazodnak.** Mielőtt átírsz, állapítsd meg, mi a szöveg: publicisztika/esszé, szépirodalmi próza (novella, regényrészlet), közösségi médiás poszt, blog/hírlevél, szakmai vagy hivatalos szöveg. Ugyanaz a jelenség műfajonként mást jelent: a rövid mondat a párbeszédben természetes, a tegezés és a szleng egy posztban rendben van, a nyelvjárás a szereplő szájában nem helyesírási hiba. A műfaji fájlok (lent) megmondják, hol kell eltérni a rétegek alapértelmezéseitől.

---

## Futtatási sorrend – mind a három alapréteg, mindig

| Réteg | Fájl | Mit tartalmaz | Hatókör |
|-------|------|---------------|---------|
| **A – általános** (1–26) | [references/layer-a-general.md](references/layer-a-general.md) | Nyelvfüggetlen AI-minták: felfújt jelentőség, reklámnyelv, homályos hivatkozás, AI-szókincs, gondolatjel, félkövér, emoji, chatbot-töredékek, töltelék | mondat, bekezdés |
| **B – magyar** (M1–M9) | [references/layer-b-hungarian.md](references/layer-b-hungarian.md) | Szórend, ritmus, terpeszkedés, főnevesítés, magyar klisék, regiszter, személykonzisztencia, névismétlés | mondat, bekezdés |
| **C – stilometriai** (S1–S10) | [references/layer-c-stylometric.md](references/layer-c-stylometric.md) | Gondolatvezetés szabályossága, szerkezeti ismétlődés, bináris érvelés, szemantikai körkörösség | teljes szöveg |

A három réteget mindig futtatod; hogy melyik fájlt kell hozzá beolvasnod, a szöveg hosszától függ:

- **Rövid szöveg (kb. 200 szó alatt: poszt, komment, rövid bekezdés):** a [references/checklist.md](references/checklist.md) mind a három réteg minden pontját tartalmazza. Ezt és a műfaji fájlt olvasd be; a rétegfájlt csak akkor nyisd meg, ha a lista egy pontjához példa vagy részlet kell.
- **Hosszabb szöveg (200 szó felett):** mindhárom rétegfájlt olvasd be, mielőtt átírsz. A 200 szavas ágat a teljes szöveg szószáma dönti el (fejlécekkel, pl. `wc -w`). A C réteg mutatóinak küszöbei csak 400 szó felett értelmezhetők, és ott a `metrics.py` első „szavak” értéke számít: az a mondatokban lévő szavakat számolja (fejléc, kód, jelölő nélkül), a fájl összes szavát zárójelben kiírja. A 200–400 szó közötti sávban a rétegfájlok kellenek, de a C réteget a három kérdéssel és a mutatók darabszámaival alkalmazd.

Ennek oka egy visszatérő hiba: az agentek magyar szöveget látva csak a B réteget futtatták, és bennmaradtak a nyelvfüggetlen jegyek – a „mérföldkövet jelent”, a „szakértők szerint”, a bekezdésenkénti három félkövér, a „Remélem, segít!”. A B réteg feltételezi, hogy az A már lefutott; fordítva, csak az A réteggel a mondatok angolos szórendűek és terpeszkedők maradnak. A C réteg azt látja, amit a mondatszintű rétegek nem: egy szöveg minden mondata lehet hibátlan, miközben az egész gépi, mert a gondolatvezetés végig ugyanolyan szabályos. A „magyar” a kérésben a szöveg nyelvét jelöli, nem azt, melyik réteget futtasd.

### Műfaji rétegek – ha a szöveg olyan

| Fájl | Mikor olvasd |
|------|--------------|
| [references/publicisztika.md](references/publicisztika.md) | vélemény, esszé, tárca, hangvezérelt próza |
| [references/publicisztika-audit.md](references/publicisztika-audit.md) | publicisztikai átírás után, záró ellenőrzésként |
| [references/publicisztika-sources.md](references/publicisztika-sources.md) | ha 2020 előtti magyar mintaszövegek kellenek a hanghoz |
| [references/szepproza.md](references/szepproza.md) | novella, regényrészlet, mese, bármilyen elbeszélő próza párbeszéddel vagy anélkül |
| [references/kozossegi-media.md](references/kozossegi-media.md) | Facebook-, LinkedIn-, Instagram-poszt, komment, rövid hírlevél |
| [references/blog.md](references/blog.md) | blogbejegyzés, hosszabb hírlevél, ismeretterjesztő vagy szakmai-személyes cikk |
| [references/hivatalos.md](references/hivatalos.md) | közlemény, tájékoztató, szabályzat, hivatalos levél, ügyfélértesítés |

**Besorolás.** Személyes, alcímes esszé (tagolt, saját történetekkel): `blog.md`. Ha érvelő, véleményes is – vagyis van olyan mondata, amely valamit kér vagy tilt (*kellene*, *ideje*, *nem szabad*), vagy két lehetőség közül az egyiket védi –, olvasd mellé a `publicisztika.md`-t, és a végén futtasd a `publicisztika-audit.md`-t.

**Hivatalos, jogi és szakmai szöveg.** A B réteg M6 pontja az irányadó (blog és hírlevél esetén annak köznyelvi szakasza; részletek: `hivatalos.md`, `blog.md`): ahol ütközik valamelyik A vagy B mintával, az M6 dönt; a többi A-minta (reklámnyelv, chatbot-töredék, emoji) változatlanul érvényes.

### Szükség szerint

| Fájl | Mire |
|------|------|
| [references/voice.md](references/voice.md) | ha az átírt szöveg steril lett: mi kerüljön az eltávolított minták helyére – a szerző hangja, nem kitalált személyiség |
| [references/checklist.md](references/checklist.md) | a teljes ellenőrzőlista, mind a három rétegre és a műfajokra; rövid szövegnél ez helyettesíti a rétegfájlokat |
| [references/examples.md](references/examples.md) | végigvezetett példák, rétegenként; csak ha példa kell |

---

## A feladatod

Az eszközök fájlt várnak (a `spell.py` és a `metrics.py` stdinről is: `-`). Az eredeti és az átírt szöveget a rendszer ideiglenes mappájába mentsd, és a végén töröld.

0. **Eszközök ellenőrzése.** Futtasd (csak olvas, nem telepít):

   ```bash
   python3 "<skill-mappa>/dict/ensure.py" --check
   ```

   (Windowson `python`.) Ha minden megvan, lépj tovább. Ha valami hiányzik, mondd meg a felhasználónak, mit telepítene a bootstrap: a `spylls` pip-csomagot (szükség esetén `--user`, majd `--break-system-packages` kapcsolóval), a magyar helyesírási szótárat és tezauruszt a GitHubról, és a munka-adatbázist. **Csak a jóváhagyása után** futtasd kapcsoló nélkül: `python3 "<skill-mappa>/dict/ensure.py"`. Ha ugyanebben a munkamenetben már jóváhagyta, nem kérdezel újra. Ha a kimenet szerint csak az adatbázis magja elavult („a mag elavult”), a kapcsoló nélküli futtatás csak helyben importál, hálózat nélkül: ezt nem kell jóváhagyatni. A letöltött fájlok a `dict/` mappába kerülnek, ha az írható, különben a felhasználói adatmappába (`~/.local/share/magyar-humanizer`). Ha a szövegben más nyelvű szakszavak is vannak: `--lang hu_HU,en_US`.

   Ha a felhasználó nemet mond, vagy a bootstrap nem sikerül (nincs hálózat, nincs pip), attól még humanizálj: a helyesírást ilyenkor magad olvasod végig kétszer, és a kimenetben jelzed, hogy a gépi ellenőrzés nem futott, és miért.

1. **Olvasd végig a teljes szöveget**, mielőtt bármit átírnál:
   * döntsd el a műfajt és a regisztert (2. alapszabály); ha van a műfajhoz fájl (lásd fent), olvasd be most: a kivételei a 2–4. lépésre is érvényesek, nem csak az 5.-re;
   * nézd meg, mi a szerző saját hangja (szóhasználat, mondathossz, tegez vagy magáz, mennyire személyes), és ezt őrizd meg;
   * csak azt írd át, ami minta; ami természetesen szól, hagyd érintetlenül, és nem cél minden rétegben változtatni;
   * ha a szerző saját, következetes szokása (pl. gondolatjel, rövid mondat) ütközik egy mintával, a szokás marad: hibának a gépies sűrűség és ismétlődés számít; jelezd, ha ezért hagytál valamit. Kivétel az emoji: a 18. minta a szerző szokása esetén is érvényes.
2. **A réteg (1–26).** Az általános minták. Ha az eszközök megvannak, előbb futtasd az eredeti szövegen: `python3 "<skill-mappa>/dict/db.py" scan <fájl>`. A találatok jelöltek, nem kötelező cserék (lásd Adatbázis).
3. **B réteg (M1–M9).** A már javított szövegen a magyar nyelvspecifikus ellenőrzés. Szócserénél lásd lent a tezauruszt – de csak akkor cserélj szót, ha maga a szó a probléma; puszta változatosság kedvéért ne (11. minta).
4. **C réteg (S1–S10).** Olvasd újra az átírt szöveget egészben, és mérd a mintázatok sűrűségét: `python3 "<skill-mappa>/dict/metrics.py" <fájl>` (szépprózában `--skip-dialogue` kapcsolóval). A szkript közelítést ad; a tapasztalati elemeket, a központi tétel ismétlését és a bekezdések „dolgát” te ítéled meg. A küszöbök 400 szó felett értelmezhetők (lásd fent); alatta a C réteg három kérdésével dolgozz (a C réteg elején és a `checklist.md`-ben).
   **Ritmus (M2).** Ha a mondathossz szórása ±4 alá esik (80 szó felett, a 400 szavas küszöbtől függetlenül), az átírás maga hozott egyenletes ritmust: kösd össze és bontsd szét a mondatokat a tartalom szerint. A szórást hosszú (20+ szavas) mondat beillesztésével is emelheted, nem csak rövid mondattal; az S3 8%-os korlátja marad.
5. **Műfaji záró ellenőrzés**, ha van műfaji fájl: nézd át vele az eredményt, publicisztikánál a végén a `publicisztika-audit.md`-vel.
6. **Ellenőrizd az eredményt:**
   * hangosan olvasva természetesen szól, és a szerzőre hasonlít, nem egy általános „jó stílusra”;
   * változatos a mondatszerkezet, de nem sablonosan váltogat (M2 + S3 együtt, a végleges szövegen mérve);
   * nem került bele új tény, forrás, szám vagy élmény, és nem változott a mondatok logikai viszonya: tagadás, ok, fokozás, feltétel (1. alapszabály);
   * illik a műfajhoz és a regiszterhez;
   * első személyű szövegben az igék E/1-ben állnak, ahol a narrátor egyedül cselekszik; ha nem derül ki, hogy egyedül csinálta-e, hagyd T/1-ben, és jelezd (M8);
   * a személyesség tapasztalatból jön, nem „szerintem”-jelölőből (S8);
   * a magyar tipográfia rendben van: „…” idézőjel, gondolatjelként szóközös nagykötőjel (–), magyar nagybetűs írás a címekben (13–15. minta);
   * nincs benne semmi, ami még gépi hangzású (második olvasás) – ha van, írd át;
   * mind a három alapréteg lefutott – ha csak a magyaron mentél végig, kezdd újra az A réteggel.
7. **Helyesírás-ellenőrzés.** Futtasd az átírt szövegen:

   ```bash
   python3 "<skill-mappa>/dict/spell.py" check <fájl> --suggest
   ```

   Minden találatot nézz meg. A szándékos nyelvjárás, szleng, szereplői beszéd és az egyszeri tulajdonnév maradhat – ezeket ne javítsd és ne vedd fel kivételnek, csak említsd a jelentésben. A szövegben többször szereplő szakszó vagy márka felvételét javasold a jelentésben; ha a felhasználó jóváhagyja, a válasz után: `python3 "<skill-mappa>/dict/db.py" ignore add <szó> --reason szakszo|marka|idegen|tulajdonnev`.

   A helyesírás-ellenőrző a létező, de rossz szót nem veszi észre („hangulhoz” a „hangulathoz” helyett, „kétértelmes” a „kétértelmű” helyett, „egyenlőre” az „egyelőre” helyett, „fáradság” a „fáradtság” helyett), és nem látja a rossz egybe- és különírás egy részét sem. Ezért az ellenőrzés után a szöveget még egyszer olvasd vissza, kifejezetten erre figyelve.
8. **Újramérés és kiadás.** Ha az 5–7. lépésben még szerkesztettél, mérj újra a `metrics.py`-val a végleges szövegen: a jelentésben szereplő mutatók a kiadott szövegé legyenek. Add vissza az átírt szöveget (lásd Kimeneti formátum).
9. **Rögzítés – a válasz után.** Ha egy szó- vagy fordulatcsere általánosítható (egy AI-klisé és a természetes megfelelője), a válaszban javasold a felvételét (eredeti → csere, minta). Ha a felhasználó jóváhagyja, futtasd: `python3 "<skill-mappa>/dict/db.py" add "<eredeti>" "<csere>" --pattern <minta>` (a minta pl. `M3`, `S2`, `7`). Stilisztikai mondat-átírást és a felhasználó szövegéből vett mondatot ne rögzíts – az adatbázis szócserék gyűjteménye, nem a felhasználói szövegek archívuma.

---

## Eszközök

Offline eszközök a `dict/` mappában, API-kulcs nélkül. Mindegyik bármelyik mappából futtatható abszolút úttal. A parancsokban `python3` áll; ahol csak `python` van (Windows), azt használd.

```bash
python3 "<skill-mappa>/dict/ensure.py" --check    # első lépés – csak ellenőriz
python3 "<skill-mappa>/dict/ensure.py"            # telepít, ami hiányzik (jóváhagyással)
python3 "<skill-mappa>/dict/spell.py" check szoveg.md --suggest
python3 "<skill-mappa>/dict/thesaurus.py" lookup kiemelkedő --verify
python3 "<skill-mappa>/dict/db.py" scan szoveg.md
python3 "<skill-mappa>/dict/db.py" add "<eredeti>" "<csere>" --pattern <minta>   # jóváhagyással
python3 "<skill-mappa>/dict/metrics.py" szoveg.md [--skip-dialogue]
```

### Helyesírás-ellenőrzés

Teljes hunspell-motorral fut, nem szólistával. Ez a magyarban szükséges: a „kulcsfontosságú” nem szerepel külön a szótárfájlban, a hunspell összetételként állítja elő, és a ragozott alakokat is így ismeri fel. Ha a gépen van rendszer-`hunspell` program, azt használja (ez a legpontosabb); különben a `spylls` csomagot, amely néhány helyes alakot tévesen elutasít (pl. „ellenőrzi”) – ilyenkor a találatot a saját nyelvtudásoddal bíráld el. A `#hashtageket`, `@említéseket`, URL-eket, kódrészleteket és a gyakori rövidítéseket (pl., stb., kb.) kihagyja.

### Tezaurusz – szinonimakeresés kereszt-ellenőrzéssel

`thesaurus.py lookup <szó> --verify` (lásd fent). 21 687 szócikk, kb. 30 500 jelentéscsoport, szófaji címkék nélkül. A `--verify` megmondja, hogy a jelölt valódi szó-e, és **kölcsönös-e** a viszony: a jelölt szócikkében visszajön-e az eredeti szó. Az egyirányú kapcsolat gyakran csak laza asszociáció, ezért a kölcsönös párt részesítsd előnyben, és ne lépj át jelentéscsoportot. A tezaurusz szótári alakokat tárol: keresés előtt told vissza alapalakra (`kulcsfontosságúnak` → `kulcsfontosságú`).

### Adatbázis

A `db.py scan` az ismert AI-fordulatokat keresi a szövegben, a `db.py add` rögzíti a jóváhagyott cserét (lásd fent). A `scan` a toldalékolt és tőváltozó alakokat (mérföldkő → mérföldkövet), a kifejezések ragozott alakjait (jelent → jelentett) és a hézagos mintákat („nem csupán … hanem”, egy mondaton belül) is megtalálja, és cserejelölteket mutat – ezek javaslatok, nem kötelező cserék. Csak ott cserélj, ahol a szó a szövegben valóban AI-jel; szakszóként („fenntartható fejlődés/jövő”, „szignifikáns eltérés” statisztikában) maradjon, üres jelzőként („fenntartható megoldás”) ne. Minden bejegyzés átmegy a kereszt-ellenőrzésen:

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
2. A változtatások rövid összefoglalója **rétegenként** (A / B / C, és a műfaji réteg, ha volt), hogy látszódjon, mind lefutott. Rövid szövegnél ez néhány sor. Ahol egy rétegben nem volt teendő, írd: „nincs változtatás”.
3. Ha a C réteg mutatói közül maradt kilógó érték, jelezd, és mondd meg, miért hagytad benne.
4. A `[ide jöhet…]` jelölések listája, ha hagytál ilyet – ezeket a szerzőnek kell kitöltenie –, és a bizonytalan döntések (pl. T/1 meghagyva, M8; kivont felhívás, K7).
5. A helyesírás-ellenőrzés eredménye: hány találat volt, mit javítottál, mit hagytál szándékosan (nyelvjárás, név), vagy hogy a gépi ellenőrzés nem futott, és miért.
6. Az adatbázisba javasolt szócserék és kivételek, valamint az `evolution-notes.md`-be javasolt minta (lásd Önfejlesztés), ha vannak – a felhasználó jóváhagyására várva.

---

## Források

Telepítés: [install/README.md](install/README.md).

**A réteg (általános):** [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) – eredeti skill: [@blader/humanizer](https://github.com/blader/humanizer)

**B réteg (magyar-specifikus):** 2022 előtti (AI-mentes) magyar szövegek olvasása, minőségi megfigyelés – Index, HVG, KPMG Blog, Magyar Narancs (2017–2021); Jelenkor, Litera.hu (2015–2017); 2017. évi I. törvény (Kp.), alkotmánybírósági határozatok (2018–2020).

**C réteg (stilometriai):** Caimelot: [Az MI-használat felismerhető nyomai – mit mutat meg a stilometria?](https://caimelot.blogspot.com/2026/09/az-mi-hasznalat-felismerheto-nyomai-mit.html) (2026).

**Publicisztika réteg:** 2020 előtti magyar véleményszövegek – WMN, 24.hu, Qubit, HVG. A darabok: [references/publicisztika-sources.md](references/publicisztika-sources.md)

**Tipográfia:** A magyar helyesírás szabályai (AkH. 12. kiadás) – idézőjel, gondolatjel, címek nagybetűs írása.
