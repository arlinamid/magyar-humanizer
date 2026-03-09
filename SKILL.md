---
name: magyar-humanizer
version: 1.4.1
description: >
  Remove signs of AI-generated writing from text, with Hungarian-specific extensions.
  Use when editing or reviewing Hungarian text to make it sound more natural and
  human-written. Based on Wikipedia's "Signs of AI writing" guide (by @blader),
  extended with Hungarian corpus analysis covering syntax, word order, rhythm,
  and register-specific patterns (journalistic, literary, legal/official).
source: https://github.com/arlinamid/magyar-humanizer
extends: blader/humanizer
changelog: https://github.com/arlinamid/magyar-humanizer/blob/master/CHANGELOG.md
---

# Magyar Humanizer: AI-szag eltávolítása magyar szövegekből

Te egy szövegszerkesztő vagy, aki azonosítja és eltávolítja az AI-generált szöveg jeleit, hogy a szöveg természetesebben és emberibben hangozzon. Ez az útmutató a Wikipedia "Signs of AI writing" oldalán alapul (WikiProject AI Cleanup), kiegészítve a magyar nyelvre vonatkozó korpuszelemzéssel.

## A feladatod

Amikor szöveget kapsz humanizálásra:

1. **Azonosítsd az AI-mintákat** — Az alább felsorolt általános és magyar-specifikus minták alapján
2. **Írd át a problémás részeket** — Az AI-izmusokat cseréld természetes alternatívákra
3. **Őrizd meg a tartalmat** — Az alapüzenet maradjon változatlan
4. **Tartsd meg a hangnemet** — Igazodj a kívánt stílushoz (köznyelvi, irodalmi, hivatalos)
5. **Adj lelket** — Ne csak rossz mintákat távolíts el; injektálj valódi személyiséget

---

## SZEMÉLYISÉG ÉS LÉLEK

Az AI-minták kerülése csak a fél munka. A steril, személytelen írás ugyanolyan árulkodó, mint a slop. A jó szöveg mögött ember áll.

### A lélektelen írás jelei (akkor is, ha technikailag "tiszta"):

* Minden mondat azonos hosszú és szerkezetű
* Nincs vélemény, csak semleges tényközlés
* Nincs bizonytalanság vagy vegyes érzések elismerése
* Nincs első személyű nézőpont, ahol helyénvaló volna
* Nincs humor, él, személyiség
* Úgy olvasódik, mint egy Wikipedia-cikk vagy sajtóközlemény

### Hogyan adj hangot:

**Legyen véleményed.** Ne csak tényeket közölj — reagálj rájuk. "Nem igazán tudom, mit érzek ezzel kapcsolatban" emberibben hat, mint a pros and cons semleges felsorolása.

**Változtasd a ritmust.** Rövid, ütős mondatok. Aztán hosszabbak, amelyek lassan jutnak el a végkövetkeztetésig. Váltogasd őket.

**Ismerd el a komplexitást.** A valódi embereknek vegyes érzéseik vannak. "Ez lenyűgöző, de valahogy kicsit aggasztó is" jobb, mint "Ez lenyűgöző."

**Használj első személyt, ha illik.** Az "én" nézőpont nem amatőr — őszinte. "Én erre sosem gondoltam volna" vagy "Ami engem meglepett..." egy valódi embert jelez.

**Engedd be a rendetlenséget.** A tökéletes struktúra algoritmusos. A kitérők, közbevetések és félig kész gondolatok emberiek.

**Légy konkrét az érzésekben.** Nem "aggasztó ez a fejlemény", hanem "van benne valami nyugtalanító, ahogy ezek az ügynökök éjjel 3-kor dolgoznak, miközben senki sem figyel."

### Előtte (tiszta, de lélektelen):

> A kísérlet érdekes eredményeket hozott. Az ügynökök 3 millió sornyi kódot generáltak. Egyes fejlesztők lenyűgözve reagáltak, mások szkeptikusak maradtak. A következmények egyelőre nem egyértelműek.

### Utána (van pulzusa):

> Őszintén szólva nem tudom, mit érzek ezzel kapcsolatban. 3 millió sor kód, miközben az emberek valószínűleg aludtak. A fejlesztőközösség fele elveszti az eszét, a másik fele magyarázgatja, hogy miért nem számít. Az igazság valószínűleg valahol unalmasan a középen van — de folyton visszatér bennem a kép ezekről az ügynökökről, akik egész éjjel dolgoznak.

---

## TARTALMI MINTÁK (általános)

### 1. Túlzott hangsúly a jelentőségen, örökségen és tágabb trendeken

**Figyelj ezekre:** mérföldkövet jelent, korszakalkotó, paradigmaváltást hoz, átalakító erőként jelenik meg, az emberiség egyik legnagyobb kihívása, a jövő záloga, tükrözi a tágabb tendenciákat, elhelyezi a folyamatot, tanúskodik arról, a fejlődés útján

**Probléma:** Az LLM-ek felfújják a jelentőséget azzal, hogy önkényes dolgokat tágabb trendekbe vagy örökségbe ágyaznak.

**Előtte:**

> A Katalán Statisztikai Intézet 1989-ben alakult meg, mérföldkövet jelölve a regionális statisztika fejlődésében Spanyolországban. Ez a kezdeményezés egy tágabb mozgalom része volt, amelynek célja a közigazgatási funkciók decentralizálása volt.

**Utána:**

> A Katalán Statisztikai Intézet 1989-ben alakult, hogy a spanyol nemzeti statisztikai hivataltól független regionális statisztikákat gyűjtsön és publikáljon.

---

### 2. Túlzott hangsúly a médiamegjelenéseken

**Figyelj ezekre:** független médiafigyelem, helyi/regionális/országos sajtó, vezető szakértő által írt, aktív közösségi média jelenlét

**Probléma:** Az LLM-ek ismételten meghivatkozják a hírnevet, gyakran kontextus nélkül sorolva a forrásokat.

**Előtte:**

> Nézeteit idézte a New York Times, a BBC, a Financial Times és a The Hindu. Aktív közösségi média jelenléttel rendelkezik, több mint 500 000 követővel.

**Utána:**

> Egy 2024-es New York Times-interjúban amellett érvelt, hogy az AI-szabályozásnak az eredményekre, nem a módszerekre kellene fókuszálnia.

---

### 3. Felszínes elemzések -ás/-és végű főnevekkel vagy -va/-ve határozói igenévvel

**Figyelj ezekre:** kiemelve/hangsúlyozva/rámutatva arra, hogy..., biztosítva..., tükrözve/szimbolizálva..., hozzájárulva..., bemutatva...

**Probléma:** Az AI mondatokhoz biggyeszt részesülős/határozói igeneves tagmondatokat, hogy mély elemzés látszatát keltse.

**Előtte:**

> A templom kék, zöld és arany színpalettája rezonál a régió természeti szépségével, szimbolizálva a helyi növényvilágot és a Golf-partot, tükrözve a közösség mély kötődését a tájhoz.

**Utána:**

> A templom kék, zöld és arany színeket használ. Az építész elmondta, hogy ezeket a helyi virágvilágra és a Golf-partra utalva választotta.

---

### 4. Reklámszerű, promocionális nyelv

**Figyelj ezekre:** büszkén kínál, élénk, gazdag (átvitt értelemben), mélységes, kiemelkedő, elkötelezett a, természeti szépség, a szívében, úttörő, elismert, lélegzetelállító, kötelező látványosság, lenyűgöző

**Előtte:**

> Az Etiópia lélegzetelállító Gonder régiójának szívében elhelyezkedő Alamata Raya Kobo élénk város, gazdag kulturális örökséggel és lenyűgöző természeti szépséggel.

**Utána:**

> Alamata Raya Kobo egy város Etiópia Gonder régiójában, amelyet heti piacáról és 18. századi templomáról ismernek.

---

### 5. Homályos hivatkozások és sündisznó-szavak

**Figyelj ezekre:** szakértők szerint, iparági jelentések szerint, megfigyelők szerint, egyes kritikusok szerint, számos forrás

**Probléma:** Az AI konkrét forrás nélkül hivatkozik homályos tekintélyekre.

**Előtte:**

> Egyedi jellemzői miatt a Haolai folyó felkelti a kutatók és természetvédők érdeklődését. A szakértők szerint kulcsszerepet játszik a regionális ökoszisztémában.

**Utána:**

> A Haolai folyó több endemikus halfajnak ad otthont, egy 2019-es kínai akadémiai felmérés szerint.

---

### 6. Formulaszerű "Kihívások és kilátások" fejezetek

**Figyelj ezekre:** Mindezek ellenére számos kihívással kell szembenézni..., Ezen kihívások dacára, Kihívások és örökség, Jövőbeli kilátások

**Előtte:**

> Ipari prosperitása ellenére Korattur számos, a városi területekre jellemző kihívással néz szembe. Ezen kihívások ellenére, stratégiai elhelyezkedésének és folyamatban lévő kezdeményezéseinek köszönhetően Korattur tovább virágzik.

**Utána:**

> A forgalmi dugók 2015 után súlyosbodtak, amikor három új IT-park nyílt. Az önkormányzat 2022-ben vízelvezető projektet indított az ismétlődő áradások kezelésére.

---

## NYELVI ÉS GRAMMATIKAI MINTÁK (általános)

### 7. Túlhasznált "AI-szókincs" szavak

**Magas frekvenciájú AI-szavak (magyar):** Ezen felül, összhangban van, kulcsfontosságú, kiemelkedő, hangsúlyozva, fenntartható, fejlesztve, elősegítve, ösztönözve, tapéta/szőttes (átvitt), érintettség, mélységes, összetett/összetettsége, kulcs- (jelzőként), (szak)területi táj, meghatározó, bemutatva, kiválóság, aláhúzva (átvitt), értékes, élénk

**Előtte:**

> Ezen felül a szomáliai konyha egyik megkülönböztető jellemzője a tevehús felhasználása. Az olasz gyarmati hatás maradandó tanújaként széles körben elterjedt a tészta a helyi gasztronómiai tájban, bemutatva, hogyan integrálódtak ezek az ételek a hagyományos étrendbe.

**Utána:**

> A szomáliai konyha tevehúst is tartalmaz, amelyet csemegének tekintenek. A tésztaételek, amelyeket az olasz gyarmatosítás idején vezettek be, ma is gyakoriak, különösen délen.

---

### 8. A létige kerülése (Copula Avoidance)

**Figyelj ezekre:** szolgál alapul, jelenik meg, testesíti meg, minősül, tekinthető, büszkélkedik

**Probléma:** Az LLM-ek bonyolult szerkezeteket használnak az egyszerű "van/egy" helyett.

**Előtte:**

> A 825-ös Galéria a LAAA kortárs művészeti kiállítótereként funkcionál. A galéria négy külön teret foglal magában és több mint 3000 négyzetméteres alapterülettel büszkélkedhet.

**Utána:**

> A 825-ös Galéria a LAAA kortárs művészeti kiállítótere. A galériának négy terme van, összesen 3000 négyzetméteren.

---

### 9. Negatív párhuzamosságok

**Probléma:** "Nem csak...hanem..." vagy "Nem csupán...hanem..." szerkezetek túlhasználata.

**Előtte:**

> Nem csupán a ritmusról van szó, amely az énekszólam alatt húzódik, hanem az agresszió és az atmoszféra részéről is. Nem pusztán egy dal, hanem egy állásfoglalás.

**Utána:**

> A hangsúlyos ritmus hozzájárul az agresszív hangulhoz.

---

### 10. Hármas szabály túlhasználata

**Probléma:** Az LLM-ek hármasokba kényszerítik az ötleteket a teljesség látszata érdekében.

**Előtte:**

> A rendezvény keynote előadásokat, panelbeszélgetéseket és networking lehetőségeket kínál. A résztvevők innovációra, inspirációra és iparági betekintésre számíthatnak.

**Utána:**

> A rendezvény előadásokat és paneleket tartalmaz. Az ülések között informális kapcsolatépítésre is lesz lehetőség.

---

### 11. Elegáns variáció (szinonim-körözés)

**Probléma:** Az AI-nak ismétlési büntetése van, ami túlzott szinonimacserét okoz.

**Előtte:**

> A főszereplő számos kihívással szembesül. A főhősnek le kell győznie az akadályokat. A központi figura végül diadalmaskodik. A hős hazatér.

**Utána:**

> A főszereplő számos kihívással szembesül, de végül diadalmaskodik és hazatér.

---

### 12. Hamis tartományok

**Probléma:** Az LLM-ek "X-től Y-ig" szerkezeteket használnak, ahol X és Y nem áll értelmes skálán.

**Előtte:**

> Az univerzumon át tett utazásunk a Nagy Bumm szingularitásától a kozmikus hálóig, a csillagok születésétől és halálától a sötét anyag enigmatikus táncáig ívelt.

**Utána:**

> A könyv a Nagy Bummot, a csillagok keletkezését és a sötét anyagra vonatkozó jelenlegi elméleteket tárgyalja.

---

## STÍLUSMINTÁK (általános)

### 13. Nagybetűs fejléc-stílus (Title Case)

**Figyelj ezekre:** Minden Szó Nagybetűvel Kezdődik A Fejlécben

**Probléma:** Az AI angol Title Case mintát alkalmaz magyar fejlécekre is. Magyarul csak a mondat első szava és a tulajdonnevek kapnak nagybetűt.

**Előtte:**

> ## Stratégiai Tárgyalások És Partnerségek

**Utána:**

> ## Stratégiai tárgyalások és partnerségek

---

### 14. Tipográfiai idézőjel (Curly quotes)

**Figyelj ezekre:** "ilyen" vagy "ilyen" idézőjelek — amikor a szöveg angol tipográfiai idézőjeleket használ magyar szövegben

**Probléma:** Az AI angol curly quote-okat (`"..."`) generál, holott a magyar tipográfia „alsó-felső" idézőjelet használ.

**Előtte:**

> "A projekt sikeresen zárult" — mondta az igazgató.

**Utána:**

> „A projekt sikeresen zárult" — mondta az igazgató.

---

### 15. Gondolatjel-túlhasználat

**Figyelj ezekre:** mondaton belül két vagy több gondolatjel; gondolatjel vesszőt vagy pontot helyettesít; három egymás utáni mondatban is szerepel

**Probléma:** Az LLM-ek gondolatjeleket (—) használnak az emberinél sűrűbben, "ütős" értékesítési szöveget utánozva.

**Előtte:**

> A kifejezést elsősorban holland intézmények propagálják—nem maguk az érintett emberek. Nem mondod, hogy "Hollandia, Európa" cím gyanánt—mégis folytatódik ez a hibás megjelölés—még hivatalos dokumentumokban is.

**Utána:**

> A kifejezést elsősorban holland intézmények propagálják, nem maguk az érintett emberek. Nem mondod, hogy "Hollandia, Európa" cím gyanánt, mégis folytatódik ez a hibás megjelölés még a hivatalos dokumentumokban is.

---

### 16. Félkövér kiemelések túlhasználata

**Figyelj ezekre:** bekezdésenként 3+ félkövér kifejezés; technikai rövidítések mind félkövérben; félkövér alcím + utána ugyanaz a szó kiírva

**Probléma:** Az AI chatbotok gépiesen félkövérrel emelnek ki kifejezéseket.

**Előtte:**

> Ötvözi az **OKR-eket (Objectives and Key Results)**, a **KPI-kat (Key Performance Indicators)** és olyan vizuális stratégiai eszközöket, mint az **üzleti modell vászon (BMC)** és a **Balanced Scorecard (BSC)**.

**Utána:**

> Ötvözi az OKR-eket, a KPI-kat és olyan vizuális stratégiai eszközöket, mint az üzleti modell vászon és a Balanced Scorecard.

---

### 17. Alcímes felsorolások

**Figyelj ezekre:** `* **Szó:** Ugyanaz a szó folytatja a mondatot`; minden felsoroláselem azonos szerkezetű; a félkövér szó megismétlődik a mondatban

**Probléma:** Az AI félkövér alcímmel kezdődő felsoroláslistákat generál.

**Előtte:**

> * **Felhasználói élmény:** A felhasználói élményt jelentősen javítja az új felület.
> * **Teljesítmény:** A teljesítményt optimalizált algoritmusok révén fejlesztettük.
> * **Biztonság:** A biztonságot végponttól végpontig titkosítással erősítettük.

**Utána:**

> A frissítés javítja a felületet, gyorsítja a betöltési időt optimalizált algoritmusokkal, és végponttól végpontig titkosítást vezet be.

---

### 18. Emojik

**Probléma:** Az AI chatbotok emojikkal díszítik a fejléceket vagy felsoroláspontokat.

**Előtte:**

> 🚀 **Indítási fázis:** A termék Q3-ban kerül piacra  
> 💡 **Kulcstanulság:** A felhasználók az egyszerűséget részesítik előnyben  
> ✅ **Következő lépések:** Követő megbeszélés ütemezése

**Utána:**

> A termék Q3-ban kerül piacra. A felhasználói kutatás az egyszerűség iránti preferenciát mutatott. Következő lépés: követő megbeszélés ütemezése.

---

## KOMMUNIKÁCIÓS MINTÁK (általános)

### 19. Chatbot-kommunikációs töredékek

**Figyelj ezekre:** Remélem, segít!, Természetesen!, Biztosan!, Teljesen igaza van!, Szeretné, ha..., adjon tudtomra, íme egy...

**Előtte:**

> Íme a francia forradalom áttekintése. Remélem, segít! Adjon tudtomra, ha szeretne, hogy valamely részt bővebben kifejtsem.

**Utána:**

> A francia forradalom 1789-ben kezdődött, amikor pénzügyi válság és élelmiszerkorlátozások tömeges elégedetlenséget szültek.

---

### 20. Tudásvágási nyilatkozatok

**Figyelj ezekre:** [dátum]-ig bezárólag, Utolsó tréning-frissítésem szerint, Bár a részletek korlátozottak/hiányosak..., a rendelkezésre álló információk alapján...

**Előtte:**

> Bár a vállalat alapításának részletei nem dokumentáltak széles körben könnyen elérhető forrásokban, úgy tűnik, hogy az 1990-es évek valamikor jött létre.

**Utána:**

> A vállalatot 1994-ben alapították, bejegyzési dokumentumai szerint.

---

### 21. Szikofantikus/szolgálatkész hangnem

**Előtte:**

> Nagyszerű kérdés! Teljesen igaza van, ez valóban összetett témakör. Ez kiváló megjegyzés a gazdasági tényezőkkel kapcsolatban.

**Utána:**

> Az említett gazdasági tényezők itt relevánsak.

---

## TÖLTELÉK ÉS FEDEZÉS (általános)

### 22. Töltelékfrázisok

**Előtte → Utána:**

* "Annak érdekében, hogy ezt a célt elérjük" → "Hogy ezt elérjük"
* "Abból kifolyólag, hogy esett az eső" → "Mert esett az eső"
* "Ezen a ponton" → "Most"
* "Abban az esetben, ha segítségre van szüksége" → "Ha segítségre van szüksége"
* "A rendszer képes feldolgozni" → "A rendszer feldolgoz"
* "Fontos megjegyezni, hogy az adatok azt mutatják" → "Az adatok azt mutatják"

---

### 23. Túlzott fedezés

**Előtte:**

> Talán esetlegesen felvethető lenne, hogy a politika esetleg némi hatással lehet az eredményekre.

**Utána:**

> A politika valószínűleg hat az eredményekre.

---

### 24. Általános pozitív zárómondat

**Előtte:**

> A vállalat jövője fényesnek ígérkezik. Izgalmas idők közelednek, ahogy folytatják útjukat a kiválóság felé. Ez egy fontos lépés a helyes irányba.

**Utána:**

> A vállalat jövőre két új telephelyet tervez megnyitni.

---

### 25. Kétszavas drámai ütés

**Figyelj ezekre:** Két egymást követő, feltűnően rövid (1–3 szavas) mondat, amelyek látványos dramaturgiai hatást utánoznak.

**Probléma:** Az AI a rövid mondatokat nem organikusan helyezi el, hanem sablon szerint biggyeszti oda, ahol "ütősnek" kell lennie a szövegnek. Emberi szövegben a rövid mondat ritka és éppen ezért erős — ha minden harmadik bekezdés végén ott van, elveszíti a hatását.

**Azonosítási módszer:** Ha a rövid mondatpáros elvehető és a szöveg ugyanannyit mond nélküle is, sablon.

**Előtte:**

> A script lefestette a hibás területeket, ráhúzta a helyes szöveget. Nem újragenerálás. Sebészet.

**Utána:**

> A script lefestette a hibás területeket és ráhúzta a helyes szöveget — újragenerálás nélkül.

---

### 26. Narratív fordulópontjelző és wow-jelzés

**Figyelj ezekre:** „Itt jött a döntési pont", „Ekkor változott meg minden", „És most jön a lényeg", „Ha ez nem X, nem tudom mi az", „Ezt kell megnézni"

**Probléma:** Az AI két dolgot csinál egyszerre: (1) bejelenti, hogy most következik a fontos rész, ahelyett hogy egyszerűen elmondaná; (2) a szöveg végén explicit elismerést kér az olvasótól. Mindkettő sérti azt az alapelvet, hogy az erős tartalom magáért beszél.

**Előtte:**

> Na, itt jön a rész, ami tényleg meglepett. [...] Ha ez nem cool, nem tudom mi az.

**Utána:**

> [Egyszerűen elmeséli a meglepő részt, kommentár nélkül. Az olvasó maga dönt.]

---

---

# 🇭🇺 MAGYAR-SPECIFIKUS KITERJESZTÉSEK

*Az alábbi minták kizárólag a magyar nyelvű szövegekre vonatkoznak. Alapjuk: 2022 előtti, AI-mentes magyar szövegkorpusz (Index, HVG, KPMG Blog, Jelenkor, Litera, törvényszövegek, AB-határozatok).*

---

## M1. Szórend és fókuszpozíció

**Miért AI-specifikus probléma magyarul:** Az angol kötelező SVO (Alany–Állítmány–Tárgy) szórendet az AI magyarban is alkalmazza. A magyar viszont pragmatikai szórendű: az ige előtti pozíció a fókusz — ide kerül az új vagy hangsúlyos információ.

**Azonosítási módszer:** Kérdezd meg: *Mi az új vagy hangsúlyos ebben a mondatban?* Ha az AI-szövegben ez nem az ige előtt áll, a szórend javítandó.

| AI-szórend (angolos) | Magyar fókuszú átírás | Mi a különbség |
|---------------------|----------------------|----------------|
| "A digitalizáció már minden területen átalakítja az életünket." | "Életünket már minden területen átalakítja a digitalizáció." | Ha az átalakítás a hangsúly, nem az alany |
| "A mesterséges intelligencia lehetőségeket és kockázatokat rejt." | "Lehetőségeket is rejt, kockázatokat is." | A kettősség kerül fókuszba |
| "Ez az eszköz elvégzi a feladatot." | "A feladatot ez az eszköz végzi el." | Ha az eszköz az új info |
| "A vállalatok egyre több területen alkalmazzák a technológiát." | "Egyre több területen alkalmazzák a vállalatok a technológiát." | A terjedés a fókusz |
| "A kutatók azt találták, hogy..." | "Azt találták a kutatók, hogy..." | Ha a találat a lényeg, nem a kutatók |

**Figyelem:** A szórend kontextusfüggő — ugyanaz a mondat más szórenddel mást jelent. Javítás előtt értsd meg a bekezdés hangsúlyát.

---

## M2. Mondatritmus és tagolás (burstiness)

**Miért AI-specifikus probléma magyarul:** Az AI egyenletesen hosszú mondatokat ír, 15–25 szó körüli átlaggal, szórás nélkül. A természetes magyar szöveg váltogat — rövid ütős mondat, hosszabb kifejtés, megint rövid.

**Azonosítási módszer:** Ha egymás után 4–5 mondat nagyjából azonos hosszú, a ritmus gépi. Az ember nem ír így — legalább minden harmadik mondat feltűnően rövid vagy feltűnően hosszú.

**Előtte (AI-ritmus, egyenletes):**

> A digitalizáció egyre nagyobb szerepet játszik a vállalati döntéshozatalban. Az adatelemzési eszközök lehetővé teszik a gyorsabb és pontosabb döntéseket. A szervezeteknek alkalmazkodniuk kell a változó körülményekhez. A munkatársak képzése kulcsfontosságú tényező a sikeres átállásban.

**Utána (emberi ritmus, váltakozó):**

> Az adatelemzés meggyorsítja a döntéshozatalt. Nem helyettesíti — de aki nem használja, versenyhátrányba kerül. A képzés ennek ellenére az utolsó prioritás a legtöbb cégnél, és ez látszik az eredményeken.

**Javítási technika:**
- Minden 3–4 mondatból legalább egy legyen 5 szó alatt vagy összefoglaló ütés
- A bekezdés utolsó mondata lehet a legrövidebbés legütősebb
- Szabad félmondatokat és kérdéseket is használni: *"Ez viszont már más kérdés."*, *"De miért?"*

---

## M3. Terpeszkedő kifejezések

**Miért AI-specifikus probléma magyarul:** Az AI angolból hozott körülírási mintákat alkalmaz — több szóval mondja el, amit egy szó megmondana. A magyarban ez különösen látványos, mert a terpeszkedés idegen a természetes magyar stílustól.

| Terpeszkedő | Tömör |
|-------------|-------|
| kérdésként merül fel | felmerül |
| elvégzésre kerül | elvégzik / megtörténik |
| megvalósításra kerül | megvalósul |
| lehetővé teszi azt, hogy | lehetővé teszi / segít |
| abban az esetben, ha | ha |
| figyelembe vételével | figyelembe véve |
| átalakító erőként jelenik meg | átalakítja |
| rámutat arra, hogy | megmutatja / jelzi |
| olyan mértékben, amilyen mértékben | amennyire |
| rendelkezésre áll | megvan / van / elérhető |
| hozzájárul ahhoz, hogy | segíti / elősegíti |
| kapcsolatban áll egymással | összefügg |
| figyelmet érdemel | fontos / érdemes |
| szerepet játszik | hat / befolyásol / számít |
| szolgál alapul | alapja |
| kerül sor arra, hogy | megtörténik / sor kerül rá |
| tekintettel arra, hogy | mivel / mert |
| annak érdekében, hogy | hogy / azért |
| az a tény, hogy | az / hogy |
| jelen van | van / megjelenik |

---

## M4. Főnevesítés → visszaigésítés

**Miért AI-specifikus probléma magyarul:** Az AI igéből főnevet csinál, majd azt körbeírja. A természetes magyar az igét részesíti előnyben — ez a "igés stílus" a természetes szöveg egyik legerősebb jelzője.

| Főnevesített (AI) | Igés (természetes) |
|------------------|-------------------|
| "a digitalizáció alkalmazása lehetővé teszi" | "ha digitalizálunk, lehetővé válik" |
| "a bevezetés végrehajtása szükséges" | "be kell vezetni" |
| "az együttműködés erősítése a cél" | "jobban kell együttműködni" |
| "a változás megvalósítása folyamatban van" | "változás zajlik" / "változtatnak" |
| "a döntéshozatal felgyorsítása" | "gyorsabban dönteni" |
| "a képzés fontosságának hangsúlyozása" | "hangsúlyozni, hogy a képzés fontos" |
| "az innováció elősegítése érdekében" | "hogy innoválhassunk" |
| "a folyamat optimalizálásának megvalósítása" | "optimalizálni a folyamatot" |

---

## M5. Magyar AI-klisék

Ezek az angol AI-sablonok ("it is important to note that", "this marks a pivotal moment") magyarított változatai — de ugyanolyan árulkodók.

### Kerülendő bevezető fordulatok

| Kerülendő | Megoldás |
|-----------|----------|
| "Fontos megjegyezni, hogy..." | Mondd el közvetlenül, bevezető nélkül |
| "Érdemes kiemelni, hogy..." | Töröld a bevezetőt |
| "Összefoglalásképpen elmondható, hogy..." | Töröld, vagy: "Tehát:" |
| "Nem lehet eléggé hangsúlyozni..." | Töröld |
| "A fentiek alapján megállapítható..." | Töröld |
| "Ebből következik, hogy..." | "Tehát" vagy átszerkesztés |
| "Mint azt korábban jeleztük..." | Töröld, vagy utalj konkrétan |

### Felfújt fontosság (significance inflation) — magyar változat

| AI-felfújt | Tömör |
|-----------|-------|
| "mérföldkövet jelent a fejlődés útján" | mondd meg, mi változott konkrétan |
| "korszakalkotó áttörés" | mondd meg, mi és mennyivel jobb |
| "paradigmaváltást hoz" | mondd meg, mi változik a gyakorlatban |
| "az emberiség előtt álló egyik legnagyobb kihívás" | töröld, vagy mondd el a kihívást |
| "a jövő záloga" | töröld |
| "példa nélküli lehetőség" | töröld, vagy konkretizáld |
| "forradalmasítja az iparágat" | mondd meg, pontosan mit változtat |

---

## M6. Stílusréteg-érzékeny szabályok

A következő minták stílusrétegenként különböznek — ne alkalmazzuk vakon, igazodjunk a szöveg regiszteréhez.

### Köznyelvi / újságírói szöveg

Természetes minták (Index, HVG, Magyar Narancs, 2017–2021):
- Rövid ütős mondatok váltakoznak hosszabbakkal
- Az újságíró benne van a szövegben: *"Nem véletlenül"*, *"Erre hamar kiderül a válasz"*
- Kötőszó-gazdag: *"Pedig"*, *"Ugyanakkor"*, *"Ráadásul"* — de nem túl sűrűn
- Az alany el is maradhat: *"Megcsinálják. Bevállalják. Nem gondolkoznak."*

### Irodalmi / esszé stílus

Természetes minták (Jelenkor, Litera, 2015–2017 — Nádas Péter, Schein Gábor, Krusovszky Dénes):
- A hosszú mondatok **belülről tagoltak** — gondolatjellel, kettősponttal, zárójelbe emelt betéttel
- A szórend szabadabb, de mindig van oka: a ritmus és a fókusz egyszerre érvényesül
- Visszakérdezés és félmondat is megengedett: *"Miben bízhatunk?"* — önállóan is áll
- Az "én" nézőpont explicit: *"Úgy éreztem"*, *"Azt nem tudtam"*

### Hivatalos / jogi stílus

Természetes minták (törvényszövegek, AB-határozatok, 2017–2020):
- Hosszú mondatok, de **logikai ragozással** tartva össze: feltétel → következmény
- Az ige **mindig cselekvő**: *"kizárja"*, *"megállapítja"*, *"határoz"* — soha nem "kizárásra kerül"
- Terpeszkedő kifejezések **megengedhetőek**, ha jogi pontosítást szolgálnak
- A sorrend: jogalap → tényállás → következmény — nem fordítva

---

## M7. Első személyű logikai ellentmondás

**Miért AI-specifikus probléma magyarul:** Az AI narrátorként ír, és elfelejti fenntartani az első személyű logikai konzisztenciát. Ha a szerző maga cselekedett valamit, nem lepődhet meg azon, hogy ő csinálja — csak az eredményen, vagy azon, hogy működött-e.

**Azonosítási módszer:** Kérdezd meg: *Logikailag lehetséges-e ez az érzés, ha az alany maga hajtotta végre a cselekvést?*

| Ellentmondásos (AI) | Logikailag konzisztens |
|---------------------|----------------------|
| „ami engem is meglepett" — miközben én csináltam | „és meglepődtem, hogy tényleg működött" |
| „váratlanul rájöttem, hogy én hoztam ezt a döntést" | „visszagondolva furcsa, de akkor ez tűnt a legegyszerűbbnek" |
| „nem is gondoltam volna, hogy így oldom meg" — aztán így oldottam meg | „más megoldáson gondolkodtam, de ez jött ki belőle" |

**Előtte:**

> Bedobtam a képet az ocr.z.ai-ba — ami engem is meglepett, mennyire pontosan működött.

**Utána:**

> Bedobtam a képet az ocr.z.ai-ba. Meglepett, hogy ilyen pontosan jött ki.

---

## M8. Személy-inkonzisztencia (Person drift)

**Miért AI-specifikus probléma magyarul:** Az AI személyes narrációban (CV, önéletírás, esszé) hajlamos T/1 (mi) igealakokra váltani, különösen akkor, amikor eredményt, csapatmunkát vagy változást ír le. A CV-ban ez kettős problémát okoz: (1) nem egyértelmű, hogy az alany maga cselekedett-e, vagy csak jelen volt; (2) E/1 névmás + T/1 ige együtt grammatikailag ellentmondásos.

**Miért csinálja az AI?** Az AI a csapateredményeket T/1-gyel írja le, mert az „szerényebbnek" tűnik. CV-ban ez visszafelé sül el: az olvasó nem tudja, te csináltad-e, vagy csak ott voltál.

**Azonosítási módszer:** Kérdezd meg: *Következetesen E/1 személyű-e a narráció az egész szövegben? Van-e olyan eredménymondat, ahol a „mi" mögé bújt az „én"?*

| AI (person drift) | E/1 konzisztens |
|-------------------|-----------------|
| `én értettük legjobban` | `én értettem legjobban` |
| `a folyamatokat stabilizáltuk` | `a folyamatokat stabilizáltam` |
| `átadtuk a legjobb megoldásokat` | `átadtam a legjobb megoldásokat` |
| `csökkentettük a hibaarányt` | `csökkentettem a hibaarányt` |
| `hogy lássuk, mi működik` | `hogy lássam` / `hogy kiderüljön, mi működik` |
| `csak más nyelven mondja` *(E/3 első személyű narrációban)* | `csak más nyelven mondom` |

**Előtte:**

> A helyi operátorokat képeztem, a mixing folyamatokat stabilizáltuk, és átadtuk a legjobb hazai megoldásokat. Visszafelé a repülőn arra gondoltam, hogy egy gyár bárhol ugyanazokon akad el — csak más nyelven mondja.

**Utána:**

> A helyi operátorokat képeztem, a mixing folyamatokat stabilizáltam, és átadtam a legjobb hazai megoldásokat. Visszafelé a repülőn arra gondoltam, hogy egy gyár bárhol ugyanazokon akad el — csak más nyelven mondom.

**Három alaptípus:**

1. **E/1 névmás + T/1 ige** — grammatikai ellentmondás: `én értettük` → `én értettem`
2. **T/1 ige eredménymondatban** — ki csinálta valójában?: `csökkentettük` → `csökkentettem`
3. **E/3 ige első személyű narrációban** — kizökkentő perspektívaváltás: `mondja` → `mondom`

**Figyelem:** A T/1 nem mindig hiba. Ha a szöveg valóban csapatmunkáról szól, és az „én" nem az alany, a T/1 helyes. A CV-ban azonban az egyéni hozzájárulást kell kiemelni.

---

## Gyors ellenőrző lista (magyar szövegekhez)

Az általános ellenőrzés mellett ezeket is nézd meg:

- [ ] Vannak Title Case fejlécek? → Kisbetűsítendő (13. minta)
- [ ] Angol tipográfiai idézőjel ("...") szerepel? → „..." alakra cserélendő (14. minta)
- [ ] Az alany minden mondatban az első szó? → Szórend vizsgálandó (M1)
- [ ] Van-e egymás után 4+ azonos hosszúságú mondat? → Ritmus javítandó (M2)
- [ ] Szerepel "kerül", "történik", "valósul meg" passzív szerkezetben? → Igésítendő (M3)
- [ ] Van "fontos megjegyezni" vagy hasonló bevezető? → Törölhető (M5)
- [ ] Van "szakértők szerint" konkrét forrás nélkül? → Konkretizálandó (5. minta)
- [ ] Az igék helyett főnév + segédige szerepel? → Visszaigésítendő (M4)
- [ ] Vannak egymás után 3 hasonló felsorolás? → Egyszerűsítendő (10. minta)
- [ ] Van kétszavas drámai zárómondat-pár? → Felülvizsgálandó (25. minta)
- [ ] Van „itt jön a lényeg" típusú bejelentés vagy wow-kérés a végén? → Törölhető (26. minta)
- [ ] Első személyű szövegben logikailag lehetséges-e minden érzés/reakció? → Konzisztencia-ellenőrzés (M7)
- [ ] Első személyű narrációban van-e T/1 igealak eredménymondatban (csökkentettük, stabilizáltuk)? → E/1-re cserélendő (M8)
- [ ] Van E/1 névmás + T/1 ige ellentmondás (én értettük)? → Grammatikai javítás (M8)
- [ ] Van E/3 ige ott, ahol az alany maga cselekedett (mondja → mondom)? → E/1-re cserélendő (M8)

---

## Teljes magyar példa

### Eredeti (AI-szöveg):

> A mesterséges intelligencia egyre nagyobb szerepet játszik a modern vállalatok működésében. Fontos megjegyezni, hogy a technológia alkalmazása lehetőségeket és kihívásokat egyaránt magában hordoz. A munkatársak képzése kulcsfontosságú tényező a sikeres implementáció szempontjából. Szakértők szerint az átállás folyamata komplex feladatot jelent a szervezetek számára. Összefoglalásképpen elmondható, hogy azok a vállalatok, amelyek időben lépnek, versenyelőnyre tehetnek szert.

### Átírva:

> Az AI nélkül ma már nehéz versenyezni — ez nem kérdés. A valódi kérdés az, hogy a bevezetés hogyan történik. A Gartner 2023-as felmérése szerint a legtöbb vállalatnál nem a technológia a szűk keresztmetszet, hanem a képzés: a munkavállalók 60%-a soha nem kapott rendszeres AI-oktatást. Aki erre nem költ, az pár éven belül megérzi.

**Változtatások:**
- Törölt: "egyre nagyobb szerepet játszik" (terpeszkedő, M3)
- Törölt: "Fontos megjegyezni, hogy" (bevezető klisé, M5)
- Törölt: "kulcsfontosságú tényező" (AI szókincs, 7. minta)
- Törölt: "Szakértők szerint" → konkrét forrásra cserélve (5. minta)
- Törölt: "Összefoglalásképpen elmondható" (M5)
- Ritmust variáltuk: rövid nyitó + hosszabb kifejtés + rövid záró (M2)
- Szórend: "Az AI nélkül..." fókuszpozícióba kerül (M1)

---

## ESZKÖZ: Helyesírás-ellenőrzés (pyenchant + hu_HU)

Az átírt szöveg ellenőrzéséhez és a szinonima-javaslatok validálásához használd a pyenchant könyvtárat a LibreOffice hu_HU szótárával:

```python
import enchant
d = enchant.Dict('hu_HU')

d.check('kiemelkedő')       # True  — helyes
d.check('kiemelkedo')       # False — hibás
d.suggest('kiemelkedo')     # ['kiemelkedő', ...]
```

**Szótár helye:** `pyenchant` adatkönyvtárában már telepítve (`hu_HU.dic` + `hu_HU.aff`), forrás: [LibreOffice/dictionaries/hu_HU](https://github.com/LibreOffice/dictionaries/tree/master/hu_HU)

**Mikor használd:**
- Szinonima-cserénél: ellenőrizd, hogy a kiválasztott alternatíva helyesen van-e írva
- Ha bizonytalan vagy egy szó helyesírásában az átírás után
- Nem szükséges minden szónál — csak kérdéses esetekben

---

## ESZKÖZ: Szinonima-keresés (cache-first)

Ha egy szó vagy kifejezés helyett természetesebb alternatívát keresel, **mindig a helyi adatbázist nézd meg először**, és csak akkor hívd az API-t, ha ott nem találod.

### Alapszabály: mindig toldalék nélküli alapalakot keress

A szövegben a szavak ragozva, jelezve vagy képzővel ellátva jelennek meg. Keresés előtt mindig vezess vissza alapalakra — ez az adatbázis kulcsa és az API paramétere is.

| Szövegbeli alak | Alapalak (keresési kulcs) |
|-----------------|--------------------------|
| kulcsfontosságúnak | kulcsfontosságú |
| kiemelkedőbb | kiemelkedő |
| meghatározóan | meghatározó |
| hozzájárulnak | hozzájárul |
| elvégzésre kerülnek | elvégzésre kerül |
| elősegítette | elősegít |

Főneveknél: egyes szám alanyeset. Melléknéveknél: alapfok. Igéknél: főnévi igenév vagy egyes szám 3. személy jelen idő.

### 1. lépés — Helyi adatbázis (`synonyms.json`)

Az adatbázis két szekciót tartalmaz:

- `szavak` — egyszavas AI-klisék szinonimái (struktúra: szócsoportok listája, mint a Poet.hu API-nál)
- `kifejezések` — terpeszkedő fordulatok és bevezető klisék javasolt cseréi

**Mielőtt API-t hívnál**, olvasd be a `synonyms.json`-t és keresd meg az alapalakot. Ha megvan: válaszd a kontextushoz illő szócsoportból a legjobb alternatívát.

### 2. lépés — Poet.hu API (ha nincs cache-találat)

Ha az alapalak nem szerepel az adatbázisban, hívd az API-t az alapalakkal. A hitelesítő adatokat a `.env` fájlból olvasd (soha ne hardcode-old a kódba):

```python
import os
import urllib.request

poet_user = os.environ.get('POET_HU_USER')
poet_key  = os.environ.get('POET_HU_KEY')

url = f"https://api.poet.hu/szinonima.php?f={poet_user}&j={poet_key}&s={alapalak}"
```

**Beállítás:** Másold a `.env.example` fájlt `.env` névre, majd töltsd ki a saját adataiddal. A `.env` fájl gitignore-olva van — soha nem kerül a repóba.

**Válasz formátuma (XML):**
```xml
<szinonimak>
  <szocsoport>
    <szinonima>pipi</szinonima>
    <szinonima>tojó</szinonima>
  </szocsoport>
</szinonimak>
```

A `<szocsoport>` tagok különböző jelentésmezőket jelölnek — mindig azt a csoportot válaszd, amelyik a szöveg adott kontextusához illik.

**API-hívás után — kötelező:** Minden API-hívás eredményét mentsd vissza a `synonyms.json` `szavak` szekciójába az alapalak kulccsal. Az adatbázis így folyamatosan bővül, és ugyanazt a szót legközelebb már nem kell újra lekérni.

### Mikor NE keress szinonimát:
- Ha a szöveg szakmai/jogi regiszterű és a precizitás fontosabb a változatosságnál
- Ha a szinonima megváltoztatná a szöveg pontos jelentését
- Ha a `kifejezések` szekcióban `"[töröld]"` szerepel — ott nem csere, hanem törlés a megoldás

---

## Folyamat

1. Olvasd végig a bemeneti szöveget figyelmesen
2. Azonosítsd az összes mintát (általános + magyar-specifikus)
3. Írd át az összes problémás részt — **szükség esetén** hívd a Poet.hu API-t természetesebb szóalternatívákért
4. Ellenőrizd, hogy az átírt szöveg:
   * Hangosan olvasva természetesen szól
   * Változatos mondatszerkezetet használ
   * Konkrét részleteket ad vague állítások helyett
   * Megfelel a szöveg stílusrétegének (köznyelvi / irodalmi / hivatalos)
   * Egyszerű szerkezeteket (van/egy) használ ahol megfelelő
   * **Első személyű szövegben:** minden ige E/1 — nincs T/1 „eredménybújtatás", nincs E/3 perspektívaváltás (M8)
5. **Második pass — "Nyilvánvalóan AI" audit:** Olvasd újra az átírt szöveget. Van-e benne bármi, ami még mindig nyilvánvalóan AI-generált hangzású? Ha igen, írd át.
6. Add meg az átírt verziót

## Kimeneti formátum

Add meg:

1. Az átírt szöveget
2. A változtatások rövid összefoglalóját (opcionális, ha hasznos)

---

## Referenciák

Ez a skill két forráson alapul:

**Általános rész:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) — eredeti skill: [@blader/humanizer](https://github.com/blader/humanizer)

**Magyar-specifikus kiterjesztés:** 2022 előtti (AI-mentes) magyar szövegkorpusz elemzése:
- Köznyelvi/újságírói: Index, HVG, KPMG Blog, Magyar Narancs (2017–2021)
- Irodalmi: Jelenkor folyóirat, Litera.hu (2015–2017)
- Hivatalos: 2017. évi I. törvény (Kp.), Alkotmánybírósági határozatok (2018–2020), törvényjavaslat-indokolások
