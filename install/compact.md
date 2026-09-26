<!-- synced-with: SKILL.md@2.2.0 sha256:60137c36a312 -->
# Magyar Humanizer – kompakt szabálykészlet

Magyar szöveg humanizálása: az AI-generált írás jeleinek felismerése és eltávolítása. A teljes skill (SKILL.md) sűrített változata méretkorlátos szabályfájlokhoz.

## Két alapszabály

1. **Tartalmi hűség.** Nem kerülhet a szövegbe új tény, szám, forrás, idézet, név, esemény, személyes élmény, vélemény vagy érzés, ami az eredetiben nincs. A minták javítása egyszerűsítés vagy törlés; ahol a szerző saját részlete kellene, hagyj `[ide jöhet egy saját példa: …]` jelölést, és sorold fel a kimenetben.
2. **Műfaj.** Előbb döntsd el: publicisztika/esszé, széppróza, közösségi médiás poszt, blog, hivatalos szöveg. Szépprózában a szereplői beszéd, a nyelvjárás és a szleng marad; posztban a tegezés és a szleng is – emoji viszont semmilyen műfajban nem marad.

## Három réteg, mindig, ebben a sorrendben

| Réteg | Hatókör | Mikor |
|-------|---------|-------|
| **A – általános (1–26)** | mondat, bekezdés | mindig, elsőként |
| **B – magyar (M1–M9)** | mondat, bekezdés | mindig, az A után |
| **C – stilometriai (S1–S10)** | **teljes szöveg** | mindig, záró passzként |

**A leggyakoribb hiba:** „a szöveg magyar, tehát a magyar réteg elég”. A B réteg kiegészítés, nem önálló lista – ha csak azt futtatod, bennmarad a „mérföldkövet jelent”, a „szakértők szerint”, a három félkövér bekezdésenként, az emojis fejléc. A „magyar” a szöveg nyelvét jelöli, nem azt, melyik réteget használd.

---

## A réteg – általános minták

1. **Felfújt jelentőség** – „mérföldkövet jelent”, „paradigmaváltás”, „a jövő záloga”, „korszakalkotó”, „tükrözi a tágabb tendenciákat” → mondd meg konkrétan, mi változott
2. **Médiamegjelenés-halmozás** – forráslisták, követőszámok kontextus nélkül → törlendő vagy egy konkrét hivatkozásra szűkítendő
3. **Odabiggyesztett igeneves tagmondat** – „kiemelve, hogy…”, „biztosítva…”, „tükrözve…”, „hozzájárulva…” → törlendő
4. **Reklámnyelv** – „élénk”, „gazdag”, „lélegzetelállító”, „a szívében”, „büszkén kínál”, „úttörő”, „kötelező látványosság”
5. **Homályos hivatkozás** – „szakértők szerint”, „iparági jelentések szerint”, „megfigyelők szerint” → konkrét forrás vagy törlés
6. **Formulaszerű „Kihívások és kilátások” fejezet** → konkrét eseményekre cserélendő
7. **AI-szókincs** – kulcsfontosságú, kulcsszerepet játszik, kiemelkedő, hangsúlyozva, elősegítve, ösztönözve, mélységes, meghatározó, aláhúzva, összetettsége, érintettség, élénk, kiválóság, zökkenőmentes, betekintést nyújt. A sűrűség dönt; szakszóként („fenntartható fejlődés”) marad.
8. **Létige-kerülés** – „szolgál alapul”, „funkcionál”, „büszkélkedik”, „testesíti meg”, „minősül” → „van” / „egy”
9. **Negatív párhuzamosság** – „nem csak… hanem…”, „nem pusztán… hanem…” túlhasználat
10. **Erőltetett hármas felsorolás** – mindenből három elem
11. **Elegáns variáció** – ugyanarra a dologra folyton új szinonima (főszereplő / főhős / központi figura / hős)
12. **Hamis tartomány** – „X-től Y-ig”, ahol X és Y nem áll közös skálán
13. **Title Case fejléc** – magyarul csak az első szó és a tulajdonnevek nagybetűsek
14. **Angol idézőjel** – `"…"` vagy `“…”` helyett `„…”`; belső idézet `»…«`; kódban marad az egyenes
15. **Gondolatjel** – mondaton belül 2+, vagy három egymás utáni mondatban → ritkítandó; magyarul szóközös nagykötőjel ` – `, nem angol `—`
16. **Félkövér-túlhasználat** – bekezdésenként 3+ kiemelés, rövidítések mind félkövérben
17. **Alcímes felsorolás** – `* **Szó:** ugyanaz a szó folytatja a mondatot` → prózává
18. **Emojik** → mindig törlendők, Facebook- és LinkedIn-posztban is
19. **Chatbot-töredék** – „Remélem, segít!”, „Természetesen!”, „Íme…”, „adjon tudtomra”
20. **Tudásvágási nyilatkozat** – „a rendelkezésre álló információk alapján”, „bár a részletek korlátozottak”
21. **Szikofantikus hangnem** – „Nagyszerű kérdés!”, „Teljesen igaza van!”
22. **Töltelékfrázis** – „annak érdekében, hogy” → „hogy”; „ezen a ponton” → „most”; „fontos megjegyezni, hogy” → törlendő
23. **Túlzott fedezés** – „talán esetlegesen felvethető lenne, hogy némi hatással lehet”
24. **Általános pozitív zárómondat** – „a jövő fényesnek ígérkezik”, „izgalmas idők közelednek”
25. **Kétszavas drámai ütés** – két egymás utáni 1–3 szavas mondat hatásvadász célból. Teszt: ha elvehető és a szöveg ugyanannyit mond, sablon.
26. **Narratív fordulópontjelző / wow-kérés** – „itt jön a lényeg”, „ekkor változott meg minden”, „ha ez nem cool, nem tudom mi az”

**Lélek:** a steril szöveg is árulkodó, de a hangot a szerző anyagából hozd vissza (saját részletei, fordulatai, megszólítása) – véleményt, érzést, élményt nem írsz a nevében.

---

## B réteg – magyar-specifikus minták

- **M1 Szórend.** A magyar pragmatikai szórendű: az **ige előtti pozíció a fókusz**. Az angolos „alany elöl mindig” séma gépi. Kérdezd: mi az új információ? Az kerüljön az ige elé. *„A vállalatok egyre több területen alkalmazzák a technológiát” → „Egyre több területen alkalmazzák a vállalatok a technológiát.”*
- **M2 Ritmus (burstiness).** Az AI egyforma hosszú és szerkezetű mondatokat ír. A hossz a tartalomból jöjjön: kösd össze, ami összetartozik, bontsd szét, ami külön gondolat. Ne kvótából, és ne tegyél minden bekezdés végére rövid ütést (25. minta, S3).
- **M3 Terpeszkedés.** kérdésként merül fel → felmerül · elvégzésre kerül → elvégzik · megvalósításra kerül → megvalósul · abban az esetben, ha → ha · rámutat arra, hogy → jelzi · szerepet játszik → hat / számít · tekintettel arra, hogy → mivel · annak érdekében, hogy → hogy · az a tény, hogy → az / hogy · rendelkezésre áll → megvan
- **M4 Főnevesítés → ige.** „a bevezetés végrehajtása szükséges” → „be kell vezetni” · „a döntéshozatal felgyorsítása” → „gyorsabban dönteni” · „az innováció elősegítése érdekében” → „hogy innoválhassunk”
- **M5 Magyar AI-klisék.** Törlendő bevezetők: „Fontos megjegyezni, hogy”, „Érdemes kiemelni, hogy”, „Összefoglalásképpen elmondható”, „Nem lehet eléggé hangsúlyozni”, „A fentiek alapján megállapítható”, „Mint azt korábban jeleztük”
- **M6 Regiszter.** *Köznyelvi/újságírói:* váltakozó mondathossz, kötőszó-gazdag (Pedig, Ugyanakkor, Ráadásul), az alany elmaradhat. *Irodalmi:* hosszú, de belülről tagolt mondatok (gondolatjel, kettőspont, zárójeles betét), explicit „én”. *Hivatalos:* hosszú mondatok logikai ragozással, az ige **mindig cselekvő** („kizárja”, nem „kizárásra kerül”); jogalap → tényállás → következmény.
- **M7 Első személyű logikai ellentmondás.** Aki maga cselekedett, nem lepődhet meg azon, hogy ő csinálja – csak az eredményen. „bedobtam a képet – ami engem is meglepett” → „bedobtam a képet. Meglepett, hogy ilyen pontosan jött ki.”
- **M8 Személy-inkonzisztencia.** E/1 narrációban: `én értettük` → `én értettem` · `csökkentettük` → `csökkentettem` (ha a szerző egyedül csinálta) · `Hatkor keltem, felöltözik` → `felöltöztem`. Ha az ige alanya harmadik személy vagy dolog („a gyár mondja”), az E/3 helyes.
- **M9 Névismétlés.** Close third personben a név bekezdésenként 2+ előfordulása egyértelmű alany mellett felesleges → névmás vagy alanyi ragozás. Tartsd meg, ha előtte más volt az alany, időugrás után, vagy ha hangsúlyt hordoz.

---

## C réteg – stilometriai minták (a TELJES szövegen)

Az A és B réteg mondatokat javít, a C réteg **arányokat mér**. Minden mondat lehet hibátlan, miközben a szöveg egésze gépi. **Az alapkérdés sosem az, hogy van-e benne ilyen alakzat, hanem hogy milyen sűrűn és milyen következetesen tér vissza.** Egyetlen minta önmagában semmit nem jelent – három vagy több egyszerre már mintázat.

- **S1 Feltűnően szabályos gondolatvezetés.** Minden bekezdésnek egyértelmű dolga van, minden átmenet ki van mondva. → hagyj ki egy átvezetést; a szerző kitérőit, nem tökéletes példáit ne simítsd ki.
- **S2 „Nem az… hanem…” túlhasználat.** Magyar sajátosság: a **mondatkezdő „Hanem”**. Küszöb: 1000 szavanként 2 rendben, 4 felett átírandó; 3+ mondatkezdő „Hanem” sablon.
- **S3 Rövid mondat mint rendszer.** Nem az a baj, hogy van rövid mondat, hanem hogy **aránytalanul sok mondat kap nyomatékosító szerepet**, mindig a hosszú magyarázat után. Küszöb: 1–3 szavas mondatok 8% felett. → tartsd meg a legerősebbet, a többit olvaszd vissza.
- **S4 Retorikai kérdések halmozása.** Kérdéssor, majd rövid összegzés, többször ugyanabban a szerepben. Egy kérdéssor rendben, kettő vizsgálandó. → rendezd vissza mondatokba.
- **S5 Azonos vázú mondatsorozatok.** 3+ egymást követő mondat azonos szintaktikai sémával („Ha X… Ha Y… Ha Z…”). Emberi szövegben a harmadiknál megtörik a minta. → tartsd meg kettőig, a harmadiknál változtass hosszt vagy ékelj be közbevetést.
- **S6 Bináris érvelés.** Minden helyzet két pólusra osztva. → nevezd meg a köztes esetet, ha a szerző anyagában ott van.
- **S7 Az átmenetek túlzott jelölése.** „És itt jön be…”, „Ezen a ponton érdemes megállni”. Küszöb: a bekezdések 40%-a felett. → keverj többféle átmenetet, vagy hagyd el a bejelentést.
- **S8 „Szerintem”-szindróma.** A személyességet tapasztalat hordozza, nem jelölő. Ha több a véleményjelölő, mint a konkrét tapasztalati elem, a személyesség díszlet. → a szerző meglévő részleteit emeld előre; újat ne találj ki.
- **S9 Szemantikai körkörösség.** A központi tétel 3–4 újrafogalmazásban tér vissza új tartalom nélkül. Kérdés minden ismétlésnél: hoz-e új példát, következményt vagy ellenérvet? → tartsd meg az elsőt és a legerősebbet, a többit töröld vagy töltsd fel.
- **S10 Rejtett felsorolás.** Rövid, azonos szerkezetű mondatsor, ami valójában lista („Türelmes. Mindig elérhető. Nem fárad el.”). Teszt: ha veszteség nélkül pontokba szedhető, rejtett lista. → vagy vállald fel listaként, vagy írd vissza valódi prózává, és hagyj el legalább egy elemet.

### Stilometriai önellenőrzés

| Mutató | Természetes | Gyanús |
|--------|-------------|--------|
| Mondathossz szórása | ±8 szó felett | ±4 szó alatt |
| 1–3 szavas mondatok | 0–8% | 10% felett |
| Kérdő mondatok | 0–5% | 8% felett vagy tömbökben |
| „nem az… hanem…” / 1000 szó | 0–2 | 4 felett |
| Mondatkezdő „Hanem” | 0–1 | 3 felett |
| Azonos vázú sorozatok (3+ elem) | 0–1 | 3 felett |
| Átvezető formulával kezdődő bekezdés | 0–20% | 40% felett |
| Véleményjelölő / tapasztalati elem | 1 alatt | 1 felett |
| A központi tétel újrafogalmazásai | 1–2 | 4 felett, új tartalom nélkül |

**Három vagy több kilógó érték = mintázat.** A legerősebb ellenőrzés, ha van rá mód: hasonlítsd a szerző korábbi írásaihoz – nem az a kérdés, „emberinek” látszik-e, hanem hogy eltér-e a szerző kialakult nyelvi szokásaitól.

---

## Eszközök

A `dict/` mappában offline eszközök; a parancsokat a skill mappájának abszolút útjával futtasd (`<skill-mappa>`). **Első lépés:** `python3 "<skill-mappa>/dict/ensure.py"` – telepíti a magyar szótárat + tezauruszt, létrehozza a `humanizer.db`-t, és telepíti a `spylls`-t, ha hiányzik. Ha nem sikerül, a humanizálás folytatható: a helyesírást olvasd végig magad, és jelezd, hogy a gépi ellenőrzés nem futott.

- **Helyesírás-ellenőrzés – kötelező lépés.** `python3 "<skill-mappa>/dict/spell.py" check <fájl> --suggest`. Átírás közben keletkezik a legtöbb elgépelés. Ellenőrizetlen szöveget ne adj vissza. Ami szándékosan nem magyar szó: `db.py ignore add <szó> --reason …` (nyelvjárást, szlenget, egyszeri nevet ne).
- **Tezaurusz.** `thesaurus.py lookup <szó> --verify` – 21 687 szócikk, jelentéscsoportokkal. A `--verify` megmondja, kölcsönös-e a szinonimapár. **Kölcsönös párt válassz, és ne lépj át jelentéscsoportot.** A tezaurusz szótári alakokat tárol, tehát told vissza alapalakra.
- **Adatbázis.** `db.py scan <fájl>` megkeresi az ismert fordulatokat; `db.py add "<eredeti>" "<csere>" --pattern <minta>` rögzíti, amit cseréltél. Minden bejegyzés átmegy a kereszt-ellenőrzésen (helyesírás, tezaurusz, kölcsönösség).

---

## Folyamat

0. **Eszközök:** `python3 "<skill-mappa>/dict/ensure.py"` – kérdés nélkül. Ha nem sikerül, folytasd, és a kimenetben jelezd.
1. Olvasd végig a **teljes** szöveget, mielőtt bármit átírnál; döntsd el a műfajt és a szerző hangját
2. A réteg (1–26) – elsőként, akkor is, ha a szöveg magyar
3. B réteg (M1–M9) – a már javított szövegen
4. C réteg (S1–S10) – olvasd újra **egészben**, és mérd a mutatótáblát (kb. 400 szótól; rövid szövegnél minőségileg, szépprózában párbeszéd nélkül)
5. „Nyilvánvalóan AI” audit: maradt-e bármi, ami még mindig gépi hangzású?
6. **Helyesírás-ellenőrzés:** `python3 "<skill-mappa>/dict/spell.py" check <fájl> --suggest`, majd visszaolvasás – a létező, de rossz szót („egyenlőre/egyelőre”) a gép nem látja
7. Rögzítés: az általánosítható szócseréket `db.py add "<eredeti>" "<csere>" --pattern <minta>` – felhasználói mondatot nem
8. Réteg-audit: mind a három lefutott? Ha csak a magyar, kezdd elölről
9. Add vissza az átírt szöveget (posztnál markdown nélkül), a változtatásokat **rétegenként bontva** (A / B / C), a `[ide jöhet…]` jelöléseket és a helyesírás-ellenőrzés eredményét

## Korlátok

Ez szövegszerkesztő eszköz, nem detektor-megkerülő. Az automatikus MI-detektorok százalékos értéke nem szerzőségi bizonyíték: emberi szöveget is minősítenek gépinek és fordítva. Jelentős tartalmi MI-közreműködésnél szakmailag és etikailag helyes jelezni a használatot; aki a szöveget a neve alatt közli, felelős az adatokért és a hivatkozásokért. Az EU MI-rendelet 50. cikk (4) bekezdése szerint jelezni kell a nyilvánosság közérdekű tájékoztatására közzétett MI-generált szöveget (2026. augusztus 2-tól alkalmazandó); érdemi emberi felülvizsgálat esetén nem szükséges.

## Források

A réteg: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) · [@blader/humanizer](https://github.com/blader/humanizer) – B réteg: 2022 előtti magyar korpusz (Index, HVG, Magyar Narancs, Jelenkor, Litera, törvényszövegek, AB-határozatok) – C réteg: [Caimelot: Az MI-használat felismerhető nyomai](https://caimelot.blogspot.com/2026/09/az-mi-hasznalat-felismerheto-nyomai-mit.html) (2026)
