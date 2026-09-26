# B réteg – magyar-specifikus kiterjesztések

*Ez a réteg az A rétegre **ráépül**, nem helyettesíti azt. Csak akkor futtasd, ha az A réteg már lefutott. Az alábbi minták kizárólag a magyar nyelvű szövegekre vonatkoznak. Alapjuk: 2022 előtti, AI-mentes magyar szövegkorpusz (Index, HVG, KPMG Blog, Jelenkor, Litera, törvényszövegek, AB-határozatok).*

---

## M1. Szórend és fókuszpozíció

**Miért AI-specifikus probléma magyarul:** Az angol kötelező SVO (Alany–Állítmány–Tárgy) szórendet az AI magyarban is alkalmazza. A magyar viszont pragmatikai szórendű: az ige előtti pozíció a fókusz – ide kerül az új vagy hangsúlyos információ.

**Azonosítási módszer:** Kérdezd meg: *Mi az új vagy hangsúlyos ebben a mondatban?* Ha az AI-szövegben ez nem az ige előtt áll, a szórend javítandó.

| AI-szórend (angolos) | Magyar fókuszú átírás | Mi a különbség |
|---------------------|----------------------|----------------|
| „A digitalizáció már minden területen átalakítja az életünket.” | „Életünket már minden területen átalakítja a digitalizáció.” | Ha az átalakítás a hangsúly, nem az alany |
| „A mesterséges intelligencia lehetőségeket és kockázatokat rejt.” | „Lehetőségeket is rejt, kockázatokat is.” | A kettősség kerül fókuszba |
| „Ez az eszköz elvégzi a feladatot.” | „A feladatot ez az eszköz végzi el.” | Ha az eszköz az új info |
| „A vállalatok egyre több területen alkalmazzák a technológiát.” | „Egyre több területen alkalmazzák a vállalatok a technológiát.” | A terjedés a fókusz |
| „A kutatók azt találták, hogy...” | „Azt találták a kutatók, hogy...” | Ha a találat a lényeg, nem a kutatók |

**Figyelem:** A szórend kontextusfüggő – ugyanaz a mondat más szórenddel mást jelent. Javítás előtt értsd meg a bekezdés hangsúlyát.

---

## M2. Mondatritmus és tagolás (burstiness)

**Miért AI-specifikus probléma magyarul:** Az AI egyenletesen hosszú mondatokat ír, 15–25 szó körüli átlaggal, szórás nélkül. A természetes magyar szöveg váltogat – rövid ütős mondat, hosszabb kifejtés, megint rövid.

**Azonosítási módszer:** Ha egymás után 4–5 mondat nagyjából azonos hosszú és azonos szerkezetű, a ritmus gépi. Az emberi szövegben a mondathossz a tartalomhoz igazodik: ahol a gondolat összetett, hosszabb, ahol egyszerű, rövidebb – ezért szór.

**Előtte (AI-ritmus, egyenletes):**

> A digitalizáció egyre nagyobb szerepet játszik a vállalati döntéshozatalban. Az adatelemzési eszközök lehetővé teszik a gyorsabb és pontosabb döntéseket. A szervezeteknek alkalmazkodniuk kell a változó körülményekhez. A munkatársak képzése kulcsfontosságú tényező a sikeres átállásban.

**Utána (emberi ritmus, váltakozó):**

> Az adatelemzés meggyorsítja a döntéshozatalt. Nem helyettesíti – de aki nem használja, versenyhátrányba kerül. A képzés ennek ellenére az utolsó prioritás a legtöbb cégnél, és ez látszik az eredményeken.

**Javítási technika:**
- Kösd össze, ami összetartozik (alárendelés, közbevetés, pontosítás), és bontsd szét, ami két külön gondolat – a hossz ebből adódjon, ne kvótából.
- Rövid mondat akkor kell, ha a tartalma önálló súlyú. Ne tegyél minden bekezdés végére rövid ütést: az maga is AI-minta (25. minta, S3).
- Félmondat és kérdés is belefér, ha a szerző hangjához illik: *„Ez viszont már más kérdés.”*, *„De miért?”*

**Figyelem:** ez a pont a C réteg S3 mintájával együtt érvényes. Az M2 azt mondja, a mondathossz szórjon; az S3 azt, hogy a szórás ne legyen sablon.

---

## M3. Terpeszkedő kifejezések

**Miért AI-specifikus probléma magyarul:** Az AI angolból hozott körülírási mintákat alkalmaz – több szóval mondja el, amit egy szó megmondana. A magyarban ez különösen látványos, mert a terpeszkedés idegen a természetes magyar stílustól.

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

**Miért AI-specifikus probléma magyarul:** Az AI igéből főnevet csinál, majd azt körbeírja. A természetes magyar az igét részesíti előnyben – ez a „igés stílus” a természetes szöveg egyik legerősebb jelzője.

| Főnevesített (AI) | Igés (természetes) |
|------------------|-------------------|
| „a digitalizáció alkalmazása lehetővé teszi” | „ha digitalizálunk, lehetővé válik” |
| „a bevezetés végrehajtása szükséges” | „be kell vezetni” |
| „az együttműködés erősítése a cél” | „jobban kell együttműködni” |
| „a változás megvalósítása folyamatban van” | „változás zajlik” / „változtatnak” |
| „a döntéshozatal felgyorsítása” | „gyorsabban dönteni” |
| „a képzés fontosságának hangsúlyozása” | „hangsúlyozni, hogy a képzés fontos” |
| „az innováció elősegítése érdekében” | „hogy innoválhassunk” |
| „a folyamat optimalizálásának megvalósítása” | „optimalizálni a folyamatot” |

---

## M5. Magyar AI-klisék

Ezek az angol AI-sablonok („it is important to note that”, „this marks a pivotal moment”) magyarított változatai – de ugyanolyan árulkodók.

### Kerülendő bevezető fordulatok

| Kerülendő | Megoldás |
|-----------|----------|
| „Fontos megjegyezni, hogy...” | Mondd el közvetlenül, bevezető nélkül |
| „Érdemes kiemelni, hogy...” | Töröld a bevezetőt |
| „Összefoglalásképpen elmondható, hogy...” | Töröld, vagy: „Tehát:” |
| „Nem lehet eléggé hangsúlyozni...” | Töröld |
| „A fentiek alapján megállapítható...” | Töröld |
| „Ebből következik, hogy...” | „Tehát” vagy átszerkesztés |
| „Mint azt korábban jeleztük...” | Töröld, vagy utalj konkrétan |

### Felfújt fontosság (significance inflation) – magyar változat

| AI-felfújt | Tömör |
|-----------|-------|
| „mérföldkövet jelent a fejlődés útján” | mondd meg, mi változott konkrétan |
| „korszakalkotó áttörés” | mondd meg, mi és mennyivel jobb |
| „paradigmaváltást hoz” | mondd meg, mi változik a gyakorlatban |
| „az emberiség előtt álló egyik legnagyobb kihívás” | töröld, vagy mondd el a kihívást |
| „a jövő záloga” | töröld |
| „példa nélküli lehetőség” | töröld, vagy konkretizáld |
| „forradalmasítja az iparágat” | mondd meg, pontosan mit változtat |

---

## M6. Stílusréteg-érzékeny szabályok

A következő minták stílusrétegenként különböznek – ne alkalmazzuk vakon, igazodjunk a szöveg regiszteréhez.

### Köznyelvi / újságírói szöveg

Természetes minták (Index, HVG, Magyar Narancs, 2017–2021):
- Rövid ütős mondatok váltakoznak hosszabbakkal
- Az újságíró benne van a szövegben: *„Nem véletlenül”*, *„Erre hamar kiderül a válasz”*
- Kötőszó-gazdag: *„Pedig”*, *„Ugyanakkor”*, *„Ráadásul”* – de nem túl sűrűn
- Az alany el is maradhat: *„Megcsinálják. Bevállalják. Nem gondolkoznak.”*

### Irodalmi / esszé stílus

Természetes minták (Jelenkor, Litera, 2015–2017 – Nádas Péter, Schein Gábor, Krusovszky Dénes):
- A hosszú mondatok **belülről tagoltak** – gondolatjellel, kettősponttal, zárójelbe emelt betéttel
- A szórend szabadabb, de mindig van oka: a ritmus és a fókusz egyszerre érvényesül
- Visszakérdezés és félmondat is megengedett: *„Miben bízhatunk?”* – önállóan is áll
- Az „én” nézőpont explicit: *„Úgy éreztem”*, *„Azt nem tudtam”*

### Szépirodalmi próza és közösségi média

Novellánál, elbeszélő prózánál és párbeszédnél lásd a `szepproza.md` fájlt; Facebook- és más közösségi médiás posztnál a `kozossegi-media.md` fájlt. Ezekben a műfajokban több szabály másképp érvényes (párbeszéd-tipográfia, nyelvjárás, emoji, hashtag, tegezés).

### Hivatalos / jogi stílus

Természetes minták (törvényszövegek, AB-határozatok, 2017–2020):
- Hosszú mondatok, de **logikai ragozással** tartva össze: feltétel → következmény
- Az ige **mindig cselekvő**: *„kizárja”*, *„megállapítja”*, *„határoz”* – soha nem „kizárásra kerül”
- Terpeszkedő kifejezések **megengedhetőek**, ha jogi pontosítást szolgálnak
- A sorrend: jogalap → tényállás → következmény – nem fordítva

---

## M7. Első személyű logikai ellentmondás

**Miért AI-specifikus probléma magyarul:** Az AI narrátorként ír, és elfelejti fenntartani az első személyű logikai konzisztenciát. Ha a szerző maga cselekedett valamit, nem lepődhet meg azon, hogy ő csinálja – csak az eredményen, vagy azon, hogy működött-e.

**Azonosítási módszer:** Kérdezd meg: *Logikailag lehetséges-e ez az érzés, ha az alany maga hajtotta végre a cselekvést?*

| Ellentmondásos (AI) | Logikailag konzisztens |
|---------------------|----------------------|
| „ami engem is meglepett” – miközben én csináltam | „és meglepődtem, hogy tényleg működött” |
| „váratlanul rájöttem, hogy én hoztam ezt a döntést” | „visszagondolva furcsa, de akkor ez tűnt a legegyszerűbbnek” |
| „nem is gondoltam volna, hogy így oldom meg” – aztán így oldottam meg | „más megoldáson gondolkodtam, de ez jött ki belőle” |

**Előtte:**

> Bedobtam a képet az ocr.z.ai-ba – ami engem is meglepett, mennyire pontosan működött.

**Utána:**

> Bedobtam a képet az ocr.z.ai-ba. Meglepett, hogy ilyen pontosan jött ki.

---

## M8. Személy-inkonzisztencia (Person drift)

**Miért AI-specifikus probléma magyarul:** Az AI személyes narrációban (CV, önéletírás, esszé) hajlamos T/1 (mi) igealakokra váltani, különösen akkor, amikor eredményt, csapatmunkát vagy változást ír le. A CV-ban ez kettős problémát okoz: (1) nem egyértelmű, hogy az alany maga cselekedett-e, vagy csak jelen volt; (2) E/1 névmás + T/1 ige együtt grammatikailag ellentmondásos.

**Miért csinálja az AI?** Az AI a csapateredményeket T/1-gyel írja le, mert az „szerényebbnek” tűnik. CV-ban ez visszafelé sül el: az olvasó nem tudja, te csináltad-e, vagy csak ott voltál.

**Azonosítási módszer:** Kérdezd meg: *Következetesen E/1 személyű-e a narráció az egész szövegben? Van-e olyan eredménymondat, ahol a „mi” mögé bújt az „én”?*

| AI (person drift) | E/1 konzisztens |
|-------------------|-----------------|
| `én értettük legjobban` | `én értettem legjobban` |
| `a folyamatokat stabilizáltuk` | `a folyamatokat stabilizáltam` |
| `átadtuk a legjobb megoldásokat` | `átadtam a legjobb megoldásokat` |
| `csökkentettük a hibaarányt` | `csökkentettem a hibaarányt` |
| `hogy lássuk, mi működik` | `hogy lássam` / `hogy kiderüljön, mi működik` |
| `Hatkor keltem, gyorsan felöltözik, és elindultam.` *(E/3, pedig a narrátor cselekszik)* | `Hatkor keltem, gyorsan felöltöztem, és elindultam.` |

**Előtte:**

> A helyi operátorokat képeztem, a mixing folyamatokat stabilizáltuk, és átadtuk a legjobb hazai megoldásokat. Visszafelé a repülőn arra gondoltam, hogy egy gyár bárhol ugyanazokon akad el – csak más nyelven mondja.

**Utána:**

> A helyi operátorokat képeztem, a mixing folyamatokat stabilizáltam, és átadtam a legjobb hazai megoldásokat. Visszafelé a repülőn arra gondoltam, hogy egy gyár bárhol ugyanazokon akad el – csak más nyelven mondja.

*(A „mondja” itt helyes: az alanya a gyár, nem a narrátor. Az E/3 ige csak akkor hiba, ha a cselekvő a narrátor maga.)*

**Három alaptípus:**

1. **E/1 névmás + T/1 ige** – grammatikai ellentmondás: `én értettük` → `én értettem`
2. **T/1 ige eredménymondatban** – ki csinálta valójában?: `csökkentettük` → `csökkentettem`
3. **E/3 ige ott, ahol a narrátor cselekszik** – kizökkentő perspektívaváltás: `felöltözik` → `felöltöztem`. Előbb nézd meg, ki az ige alanya: ha egy harmadik személy vagy dolog („a gyár mondja”), az E/3 helyes.

**Figyelem:** A T/1 nem mindig hiba. Ha a szöveg valóban csapatmunkáról szól, és az „én” nem az alany, a T/1 helyes – és nem döntheted el a szerző helyett, hogy egyedül csinálta-e. Ha a szövegből nem derül ki, hagyd T/1-ben, és jelezd a kimenetben. A CV-ban az egyéni hozzájárulást kell kiemelni, de ott is csak azt, amit a szerző valóban maga végzett.

---

## M9. Névismétlés névmás helyett (Name repetition drift)

**Miért AI-specifikus probléma magyarul:** Az AI close third person narrációban hajlamos a főszereplő nevét bekezdésenként többször is kiírni, akkor is, ha az alany egyértelmű, és névmással (ő, -) vagy alanyi igeragozással kiváltható lenne. Az emberi irodalmi szöveg a nevet csak akkor ismétli, ha az alany kétértelművé vált, vagy ha ritmikai/érzelmi hangsúly indokolja.

**Azonosítási módszer:**
1. Számold meg a név előfordulásait jelenetenként (~1500 szó). Ha bekezdésenként 2+ előfordulás van egymás után, és az alany egyértelmű – a névismétlés felesleges.
2. Kérdezd meg minden egyes névhasználatnál: *Kétértelmű-e az alany nélküle? Ha nem, névmással vagy alanyi ragozással kiváltható.*
3. Ökölszabály: ~1500 szavas jelenetben 10–15 névhasználat természetes. 20 felett vizsgálandó, 25 felett szisztematikus probléma.

**Javítási technika:**

| Névismétlő (AI) | Névmásos / alanyi (természetes) |
|-----------------|--------------------------------|
| `Tamás felállt. Tamás megnézte a falat.` | `Felállt. Megnézte a falat.` |
| `Tamás nem mozdult. Tamás várt.` | `Nem mozdult. Várt.` |
| `Tamás visszament. Tamás lefeküdt.` | `Visszament, és lefeküdt.` |
| `Tamás tudta, hogy Tamás ezt meg fogja csinálni.` | `Tudta, hogy meg fogja csinálni.` |

**Mikor TARTSD meg a nevet:**
- Az előző mondatban más alany szerepelt (kétértelműség-elkerülés)
- A bekezdés élén, ha hosszabb szünet (helyszínváltás, időugrás) után az alany újra bevezetendő
- Ha a névismétlés ritmikai vagy érzelmi hangsúlyt hordoz (pl. horrorban a név kimondása maga is narratív eszköz)
- Ha a narrátor és a főszereplő nézőpontja egy pillanatra szétválik

**Előtte:**

> Tamás nem mozdult. Tamás feküdt, és hallgatta. Tamás a belső falra nézett a sötétben. Tamás racionális volt.

**Utána:**

> Tamás nem mozdult. Feküdt, és hallgatta. A belső falra nézett a sötétben. Racionális ember volt.

*(A név egyszer, a jelenet elején marad; a többi mondatban az alanyi ragozás elég. Új tartalom nem került bele.)*

---
