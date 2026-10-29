# A réteg – általános (nyelvfüggetlen) minták

*Ez a réteg mindig fut, elsőként. Forrás: Wikipedia „Signs of AI writing” (WikiProject AI Cleanup).*

> **Az „Utána” példákról.** Az „Utána” változatok nem adnak hozzá tényt: ahol az eredeti nem ad konkrétumot, a javítás egyszerűsítés, törlés vagy `[ide jöhet …]` jelölés (lásd SKILL.md, 1. alapszabály). A valódi átírásban sem maradhat olyan tény, ami az eredeti szövegben vagy a szerzőtől nem származik.

## TARTALMI MINTÁK (általános)

### 1. Túlzott hangsúly a jelentőségen, örökségen és tágabb trendeken

**Figyelj ezekre:** mérföldkövet jelent, korszakalkotó, paradigmaváltást hoz, átalakító erőként jelenik meg, az emberiség egyik legnagyobb kihívása, a jövő záloga, tükrözi a tágabb tendenciákat, elhelyezi a folyamatot, tanúskodik arról, a fejlődés útján

**Probléma:** Az LLM-ek felfújják a jelentőséget azzal, hogy önkényes dolgokat tágabb trendekbe vagy örökségbe ágyaznak.

**Előtte:**

> A Katalán Statisztikai Intézet 1989-ben alakult meg, mérföldkövet jelölve a regionális statisztika fejlődésében Spanyolországban. Ez a kezdeményezés egy tágabb mozgalom része volt, amelynek célja a közigazgatási funkciók decentralizálása volt.

**Utána:**

> A Katalán Statisztikai Intézet 1989-ben alakult Spanyolországban, a közigazgatási funkciók decentralizálásának részeként.

---

### 2. Túlzott hangsúly a médiamegjelenéseken

**Figyelj ezekre:** független médiafigyelem, helyi/regionális/országos sajtó, vezető szakértő által írt, aktív közösségi média jelenlét

**Probléma:** Az LLM-ek ismételten meghivatkozják a hírnevet, gyakran kontextus nélkül sorolva a forrásokat.

**Előtte:**

> Nézeteit idézte a New York Times, a BBC, a Financial Times és a The Hindu. Aktív közösségi média jelenléttel rendelkezik, több mint 500 000 követővel.

**Utána:**

> Nézeteit idézte többek között a New York Times. [ide jöhet egy konkrét hivatkozás: melyik cikkben, mit állított]

*(A médialista és a követőszám törölve; a konkrét hivatkozás a szerzőtől jön.)*

---

### 3. Felszínes elemzések -ás/-és végű főnevekkel vagy -va/-ve határozói igenévvel

**Figyelj ezekre:** kiemelve/hangsúlyozva/rámutatva arra, hogy..., biztosítva..., tükrözve/szimbolizálva..., hozzájárulva..., bemutatva...

**Probléma:** Az AI mondatokhoz biggyeszt részesülős/határozói igeneves tagmondatokat, hogy mély elemzés látszatát keltse.

**Előtte:**

> A templom kék, zöld és arany színpalettája rezonál a régió természeti szépségével, szimbolizálva a helyi növényvilágot és a Golf-partot, tükrözve a közösség mély kötődését a tájhoz.

**Utána:**

> A templom kék, zöld és arany színeket használ.

*(Az értelmezés törölve; ha a szerző ismeri az építész indoklását, az kerülhet a helyére.)*

---

### 4. Reklámszerű, promocionális nyelv

**Figyelj ezekre:** büszkén kínál, élénk, gazdag (átvitt értelemben), mélységes, kiemelkedő, elkötelezett a, természeti szépség, a szívében, úttörő, elismert, lélegzetelállító, kötelező látványosság, lenyűgöző

**Előtte:**

> Az Etiópia lélegzetelállító Gonder régiójának szívében elhelyezkedő Alamata Raya Kobo élénk város, gazdag kulturális örökséggel és lenyűgöző természeti szépséggel.

**Utána:**

> Alamata Raya Kobo egy város Etiópia Gonder régiójában.

---

### 5. Homályos hivatkozások és sündisznó-szavak

**Figyelj ezekre:** szakértők szerint, iparági jelentések szerint, megfigyelők szerint, egyes kritikusok szerint, számos forrás

**Probléma:** Az AI konkrét forrás nélkül hivatkozik homályos tekintélyekre. Ha a hivatkozás kimarad, és a megmaradó állítás vitatható vagy tényszerű, jelölj `[ide jöhet a forrás: …]`-t, ne hagyd forrás nélküli tényként.

**Előtte:**

> Egyedi jellemzői miatt a Haolai folyó felkelti a kutatók és természetvédők érdeklődését. A szakértők szerint kulcsszerepet játszik a regionális ökoszisztémában.

**Utána:**

> A Haolai folyó felkelti a kutatók és természetvédők érdeklődését, és része a regionális ökoszisztémának.

*(A „szakértők szerint” kimarad; forrás csak akkor kerül be, ha a szerző megadja.)*

---

### 6. Formulaszerű „Kihívások és kilátások” fejezetek

**Figyelj ezekre:** Mindezek ellenére számos kihívással kell szembenézni..., Ezen kihívások dacára, Kihívások és örökség, Jövőbeli kilátások

**Előtte:**

> Ipari prosperitása ellenére Korattur számos, a városi területekre jellemző kihívással néz szembe. Ezen kihívások ellenére, stratégiai elhelyezkedésének és folyamatban lévő kezdeményezéseinek köszönhetően Korattur tovább virágzik.

**Utána:**

> Korattur ipari város, amely számos, a városi területekre jellemző kihívással néz szembe. [ide jöhet a szerzőtől: melyek ezek a kihívások, és mit tettek ellenük]

---

## NYELVI ÉS GRAMMATIKAI MINTÁK (általános)

### 7. Túlhasznált „AI-szókincs” szavak

**Magas frekvenciájú AI-szavak (magyar):** Ezen felül, összhangban van, kulcsfontosságú, kulcsszerepet játszik, kiemelkedő, hangsúlyozva, fejlesztve, elősegítve, ösztönözve, kárpit/szőttes (átvitt: „a kultúra kárpitja”), érintettség, mélységes, összetett/összetettsége, kulcs- (jelzőként), táj (átvitt: „a gasztronómiai tájban”), meghatározó, bemutatva, kiválóság, aláhúzva (átvitt), értékes, élénk, zökkenőmentes, betekintést nyújt, egyedülálló, „utazás” (átvitt: „ez az utazás”), „a … világában” („a mesterséges intelligencia világában”)

**Mikor nem AI-jel:** a szó a sűrűségtől és a szereptől lesz gyanús, nem önmagától. Szakszóként maradjon, ha a szó a szakma kötött kifejezésének része („fenntartható fejlődés”, „fenntartható jövő”, „fenntartható közlekedés”, „szignifikáns eltérés” statisztikában, „összetett szó” nyelvtanban); üres jelzőként ne („fenntartható megoldás”, „fenntartható szemlélet”, „szignifikáns javulás”). Egy-egy előfordulás egy különben természetes szövegben nem ok a cserére. Cserélni ott kell, ahol a szó üres nyomatékot ad, vagy ahol ugyanabban a bekezdésben több ilyen torlódik.

**Előtte:**

> Ezen felül a szomáliai konyha egyik megkülönböztető jellemzője a tevehús felhasználása. Az olasz gyarmati hatás maradandó tanújaként széles körben elterjedt a tészta a helyi gasztronómiai tájban, bemutatva, hogyan integrálódtak ezek az ételek a hagyományos étrendbe.

**Utána:**

> A szomáliai konyha tevehúst is használ. A tészta az olasz gyarmati hatás nyomán terjedt el a helyi étrendben.

---

### 8. A létige kerülése (Copula Avoidance)

**Figyelj ezekre:** szolgál alapul, jelenik meg, testesíti meg, minősül, tekinthető, büszkélkedik

**Probléma:** Az LLM-ek bonyolult szerkezeteket használnak az egyszerű „van/egy” helyett.

**Előtte:**

> A 825-ös Galéria a LAAA kortárs művészeti kiállítótereként funkcionál. A galéria négy külön teret foglal magában és több mint 3000 négyzetméteres alapterülettel büszkélkedhet.

**Utána:**

> A 825-ös Galéria a LAAA kortárs művészeti kiállítótere. A galériának négy külön tere van, összesen több mint 3000 négyzetméteren.

---

### 9. Negatív párhuzamosságok

**Probléma:** „Nem csak...hanem...” vagy „Nem csupán...hanem...” szerkezetek túlhasználata. Javításnál a fokozás marad: „nem csupán X, hanem Y” → „X-nél több: Y”, nem „X is, Y is”.

**Előtte:**

> Nem csupán a ritmusról van szó, amely az énekszólam alatt húzódik, hanem az agresszió és az atmoszféra részéről is. Nem pusztán egy dal, hanem egy állásfoglalás.

**Utána:**

> A hangsúlyos ritmus agresszívvá teszi a hangulatot.

---

### 10. Hármas szabály túlhasználata

**Probléma:** Az LLM-ek hármasokba kényszerítik az ötleteket a teljesség látszata érdekében.

**Mikor nem AI-jel:** ha a szerző valóban három dolgot sorol fel, és mindhárom tartalmas. A gyanú ott kezdődik, ahol mindenből három van, vagy a harmadik elem töltelék. Összevonáskor a tartalmas elemeket ne dobd el; csak az ismétlő, töltelék elemet hagyd el.

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

**Probléma:** Az LLM-ek „X-től Y-ig” szerkezeteket használnak, ahol X és Y nem áll értelmes skálán.

**Előtte:**

> Az univerzumon át tett utazásunk a Nagy Bumm szingularitásától a kozmikus hálóig, a csillagok születésétől és halálától a sötét anyag enigmatikus táncáig ívelt.

**Utána:**

> A könyv a Nagy Bummot, a csillagok keletkezését és a sötét anyagra vonatkozó jelenlegi elméleteket tárgyalja.

---

## STÍLUSMINTÁK (általános)

### 13. Nagybetűs fejléc-stílus (Title Case)

**Figyelj ezekre:** Minden Szó Nagybetűvel Kezdődik A Fejlécben

**Probléma:** Az AI angol Title Case mintát alkalmaz magyar fejlécekre is. Magyarul csak a mondat első szava és a tulajdonnevek kapnak nagybetűt. A fejlécet csak ennyire írd át; új alcímet ne találj ki, a sorrendet ne változtasd.

**Előtte:**

> ## Stratégiai Tárgyalások És Partnerségek

**Utána:**

> ## Stratégiai tárgyalások és partnerségek

---

### 14. Angol idézőjel magyar szövegben

**Figyelj ezekre:** `“ilyen”` (angol tipográfiai) vagy `"ilyen"` (egyenes, gépi) idézőjel magyar szövegben; `'ilyen'` egyszeres idézőjel belső idézetként.

**Probléma:** Az AI az angol idézőjelet viszi át a magyarba. A magyar szabály (AkH. 12. kiadás, az idézőjel szabályai): nyitó idézőjel lent (`„`, U+201E), záró fent, 9-es alakban (`”`, U+201D). Idézeten belüli idézet: `»…«`. Az aposztróf `’` (U+2019), nem egyenes `'`.

**Előtte:**

> "A projekt sikeresen zárult" — mondta az igazgató.

**Utána:**

> „A projekt sikeresen zárult” – mondta az igazgató.

**Kivétel:** kódban, parancsban, fájlnévben és URL-ben az egyenes idézőjel marad.

---

### 15. Gondolatjel-túlhasználat

**Figyelj ezekre:** mondaton belül két vagy több gondolatjel; gondolatjel vesszőt vagy pontot helyettesít; három egymás utáni mondatban is szerepel; angol hosszú kötőjel (`—`, em dash) magyar szövegben, főleg szóköz nélkül.

**Probléma:** Az LLM-ek az emberinél sűrűbben használnak gondolatjelet, „ütős” értékesítési szöveget utánozva – és magyarul is az angol formát írják. A magyar gondolatjel a nagykötőjel (`–`, U+2013), mindkét oldalán szóközzel (AkH. 12. kiadás, a gondolatjel szabályai); a szóköz nélküli `—` angol tipográfia, magyar szövegben önmagában is árulkodó. Szépprózában a párbeszéd sorát is nagykötőjel vezeti be (`– Hová mész? – kérdezte.`).

**Javítás:** a gondolatjelek többsége vessző, kettőspont, zárójel vagy új mondat lesz; ami marad, az ` – ` alakú.

**Előtte:**

> A kifejezést elsősorban holland intézmények propagálják—nem maguk az érintett emberek. Nem mondod, hogy "Hollandia, Európa" cím gyanánt—mégis folytatódik ez a hibás megjelölés—még hivatalos dokumentumokban is.

**Utána:**

> A kifejezést elsősorban holland intézmények propagálják, nem maguk az érintett emberek. Nem mondod, hogy „Hollandia, Európa” cím gyanánt, mégis folytatódik ez a hibás megjelölés, még a hivatalos dokumentumokban is.

---

### 16. Félkövér kiemelések túlhasználata

**Figyelj ezekre:** bekezdésenként 3+ félkövér kifejezés; technikai rövidítések mind félkövérben; félkövér alcím + utána ugyanaz a szó kiírva

**Probléma:** Az AI chatbotok gépiesen félkövérrel emelnek ki kifejezéseket.

**Mikor nem AI-jel:** szakmai dokumentum, felhasználói felület feliratai, a szerző saját, következetes kiemelése.

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

> A frissítés javítja a felületet, optimalizált algoritmusokkal a teljesítményt, és végponttól végpontig titkosítást vezet be.

---

### 18. Emojik

**Probléma:** Az AI chatbotok emojikkal díszítik a fejléceket, a felsoroláspontokat és a mondatvégeket.

**Szabály:** a kimenetben nincs emoji – semmilyen műfajban, Facebook- és LinkedIn-posztban sem. Az emoji mondaton belül, sor elején, címsorban vagy a szöveg végén gyűjtve (🚀✨🔥) egyaránt törlendő; ha a jelentést hordozta (pl. 🤯 = meglepődtem), azt szóval mondd ki, de csak ha az eredeti ezt valóban kifejezte.

**Előtte:**

> 🚀 **Indítási fázis:** A termék Q3-ban kerül piacra  
> 💡 **Kulcstanulság:** A felhasználók az egyszerűséget részesítik előnyben  
> ✅ **Következő lépések:** Követő megbeszélés ütemezése

**Utána:**

> A termék Q3-ban kerül piacra. A felhasználók az egyszerűséget részesítik előnyben. Következő lépés: követő megbeszélés ütemezése.

---

## KOMMUNIKÁCIÓS MINTÁK (általános)

### 19. Chatbot-kommunikációs töredékek

**Figyelj ezekre:** Remélem, segít!, Természetesen!, Biztosan!, Teljesen igaza van!, Szeretné, ha..., adjon tudtomra, íme egy...

**Előtte:**

> Íme a francia forradalom áttekintése. Remélem, segít! Adjon tudtomra, ha szeretne, hogy valamely részt bővebben kifejtsem.

**Utána:**

> [Csak az áttekintés tartalma marad; az „Íme…” bevezető, a „Remélem, segít!” és a felajánlás törölve.]

---

### 20. Tudásvágási nyilatkozatok

**Figyelj ezekre:** [dátum]-ig bezárólag, Utolsó tréning-frissítésem szerint, Bár a részletek korlátozottak/hiányosak..., a rendelkezésre álló információk alapján...

**Előtte:**

> Bár a vállalat alapításának részletei nem dokumentáltak széles körben könnyen elérhető forrásokban, úgy tűnik, hogy az 1990-es évek valamikor jött létre.

**Utána:**

> A vállalat az 1990-es években jött létre.

*(A pontos év csak akkor kerülhet be, ha a szerző megadja.)*

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

* „Annak érdekében, hogy ezt a célt elérjük” → „Hogy ezt elérjük”
* „Abból kifolyólag, hogy esett az eső” → „Mert esett az eső”
* „Ezen a ponton” → „Most”
* „Abban az esetben, ha segítségre van szüksége” → „Ha segítségre van szüksége”
* „A rendszer képes feldolgozni az adatokat” → „A rendszer feldolgozza az adatokat”
* „Fontos megjegyezni, hogy az adatok azt mutatják” → „Az adatok azt mutatják”

---

### 23. Túlzott fedezés

**Előtte:**

> Talán esetlegesen felvethető lenne, hogy a politika esetleg némi hatással lehet az eredményekre.

**Utána:**

> A politika valószínűleg hat az eredményekre.

---

### 24. Általános pozitív zárómondat

**Ha a zárómondat az egyetlen összefoglaló tézis,** ne töröld: egyszerűsítsd kijelentő mondattá, aforisztikus kép és ellentétpár nélkül. A tartalom a szerzőé, csak a csillogás törlendő.

**Előtte:**

> A vállalat jövője fényesnek ígérkezik. Izgalmas idők közelednek, ahogy folytatják útjukat a kiválóság felé. Ez egy fontos lépés a helyes irányba.

**Utána:**

> [A pozitív zárómondatok törölve; ha a szerző ismeri a vállalat konkrét terveit, azok kerülhetnek a helyükre.]

---

### 25. Kétszavas drámai ütés

**Figyelj ezekre:** Két egymást követő, feltűnően rövid (1–3 szavas) mondat, amelyek látványos dramaturgiai hatást utánoznak.

**Probléma:** Az AI a rövid mondatokat nem organikusan helyezi el, hanem sablon szerint biggyeszti oda, ahol „ütősnek” kell lennie a szövegnek. Emberi szövegben a rövid mondat ritka és éppen ezért erős – ha minden harmadik bekezdés végén ott van, elveszíti a hatását.

**Azonosítási módszer:** Ha a rövid mondatpáros elvehető és a szöveg ugyanannyit mond nélküle is, sablon.

**Előtte:**

> A script lefestette a hibás területeket, ráhúzta a helyes szöveget. Nem újragenerálás. Sebészet.

**Utána:**

> A script lefestette a hibás területeket, majd újragenerálás nélkül ráhúzta a helyes szöveget.

---

### 26. Narratív fordulópontjelző és wow-jelzés

**Figyelj ezekre:** „Itt jött a döntési pont”, „Ekkor változott meg minden”, „És most jön a lényeg”, „Ha ez nem X, nem tudom, mi az”, „Ezt kell megnézni”

**Probléma:** Az AI két dolgot csinál egyszerre: (1) bejelenti, hogy most következik a fontos rész, ahelyett hogy egyszerűen elmondaná; (2) a szöveg végén explicit elismerést kér az olvasótól. Mindkettő sérti azt az alapelvet, hogy az erős tartalom magáért beszél.

**Előtte:**

> Na, itt jön a rész, ami tényleg meglepett. [...] Ha ez nem cool, nem tudom, mi az.

**Utána:**

> [Egyszerűen elmeséli a meglepő részt, kommentár nélkül. Az olvasó maga dönt.]
