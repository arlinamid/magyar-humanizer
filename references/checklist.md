# Gyors ellenőrző lista — mind a három réteg

**Ez a lista egyben van. Nem szabad csak a B szakaszát végigfutni.**

### Bootstrap — mielőtt bármit átírnál

- [ ] Lefuttattad a `python dict/ensure.py`-t (vagy `--check` után OK a szótár + adatbázis)?
- [ ] Ha angol/más nyelvű szakszavakra is kell motor: `python dict/ensure.py --lang hu_HU,en_US`?

### A réteg — általános (1–26) · mondatszint

- [ ] Van „mérföldkövet jelent", „paradigmaváltás", „a jövő záloga" típusú felfújt jelentőség? → konkretizálandó (1.)
- [ ] Van kontextus nélküli médiafelsorolás vagy követőszám? → törlendő (2.)
- [ ] Vannak odabiggyesztett -va/-ve határozói igeneves tagmondatok („kiemelve, hogy…")? → törlendő (3.)
- [ ] Van reklámnyelv: „élénk", „lélegzetelállító", „a szívében", „büszkén kínál"? → cserélendő (4.)
- [ ] Van „szakértők szerint" konkrét forrás nélkül? → konkretizálandó (5.)
- [ ] Van „Kihívások és kilátások" típusú formulaszerű fejezet? → átírandó (6.)
- [ ] Vannak AI-szókincs szavak: „kulcsfontosságú", „elősegítve", „aláhúzva", „mélységes"? → cserélendő (7.)
- [ ] Van létige-kerülés: „szolgál alapul", „büszkélkedik", „funkcionál"? → egyszerűsítendő (8.)
- [ ] Van „nem csak… hanem…" túlhasználat? → egyszerűsítendő (9., lásd még S2)
- [ ] Van kényszerített hármas felsorolás? → egyszerűsítendő (10.)
- [ ] Van szinonim-körözés ugyanarra a dologra? → egységesítendő (11.)
- [ ] Van hamis „X-től Y-ig" tartomány? → átírandó (12.)
- [ ] Vannak Title Case fejlécek? → kisbetűsítendő (13.)
- [ ] Angol tipográfiai idézőjel („…") szerepel? → „…" alakra cserélendő (14.)
- [ ] Gondolatjel-túlhasználat (mondaton belül 2+, vagy 3 egymás utáni mondatban)? → ritkítandó (15.)
- [ ] Bekezdésenként 3+ félkövér kiemelés? → ritkítandó (16.)
- [ ] Van `* **Szó:** Ugyanaz a szó folytatja` típusú alcímes felsorolás? → prózává írandó (17.)
- [ ] Vannak emojik fejlécben vagy felsoroláspontban? → törlendő (18.)
- [ ] Van chatbot-töredék: „Remélem, segít!", „Természetesen!", „Íme…"? → törlendő (19.)
- [ ] Van tudásvágási nyilatkozat: „a rendelkezésre álló információk alapján"? → törlendő (20.)
- [ ] Van szikofantikus hangnem: „Nagyszerű kérdés!", „Teljesen igaza van"? → törlendő (21.)
- [ ] Vannak töltelékfrázisok: „annak érdekében, hogy", „ezen a ponton"? → tömörítendő (22.)
- [ ] Van túlzott fedezés: „talán esetlegesen felvethető"? → egyszerűsítendő (23.)
- [ ] Van általános pozitív zárómondat: „a jövő fényesnek ígérkezik"? → törlendő (24.)
- [ ] Van kétszavas drámai ütés-páros? → felülvizsgálandó (25., lásd még S3)
- [ ] Van „itt jön a lényeg" bejelentés vagy wow-kérés a végén? → törlendő (26., lásd még S7)

### B réteg — magyar (M1–M9) · mondatszint

- [ ] Az alany minden mondatban az első szó? → szórend vizsgálandó (M1)
- [ ] Van egymás után 4+ azonos hosszúságú mondat? → ritmus javítandó (M2)
- [ ] Szerepel „kerül", „történik", „valósul meg" terpeszkedő szerkezetben? → igésítendő (M3)
- [ ] Az igék helyett főnév + segédige szerepel? → visszaigésítendő (M4)
- [ ] Van „fontos megjegyezni", „érdemes kiemelni", „összefoglalásképpen"? → törölhető (M5)
- [ ] Illeszkedik a szöveg a saját regiszteréhez (köznyelvi / irodalmi / hivatalos)? (M6)
- [ ] Első személyű szövegben logikailag lehetséges-e minden érzés és reakció? (M7)
- [ ] Van T/1 igealak eredménymondatban (csökkentettük, stabilizáltuk)? → E/1-re cserélendő (M8)
- [ ] Van E/1 névmás + T/1 ige ellentmondás („én értettük")? → grammatikai javítás (M8)
- [ ] Van E/3 ige ott, ahol az alany maga cselekedett („mondja" → „mondom")? → E/1-re cserélendő (M8)
- [ ] Bekezdésenként 2+ névismétlés egyértelmű alannyal? → névmással kiváltandó (M9)
- [ ] Jelenetenként 20+ névhasználat? → szisztematikus vizsgálat (M9)

### C réteg — stilometriai (S1–S10) · a TELJES szövegen, egyszerre

- [ ] Minden bekezdésnek egyértelmű, rövid „dolga" van, egyik sem lóg ki? → kitérő beépítendő (S1)
- [ ] Hány „nem az… hanem…" szerkezet van 1000 szavanként? 4 felett átírandó (S2)
- [ ] Van mondatkezdő „Hanem" 3-nál többször? → átírandó (S2)
- [ ] Az 1–3 szavas mondatok aránya 8% felett van? → visszaolvasztandó (S3)
- [ ] Van 2-nél több retorikai kérdéssor, azonos dramaturgiai helyen? → prózává írandó (S4)
- [ ] Van 3+ elemű azonos vázú mondatsorozat? → a harmadiknál megtörendő (S5)
- [ ] Hány kérdés kap kétpólusú felépítést? → köztes eset megnevezendő (S6)
- [ ] A bekezdések 40%-ánál több kezdődik átvezető formulával? → változatosítandó (S7)
- [ ] Több a véleményjelölő („szerintem"), mint a konkrét tapasztalati elem? → tapasztalatra cserélendő (S8)
- [ ] A központi tétel 4-nél többször tér vissza új tartalom nélkül? → törlendő vagy feltöltendő (S9)
- [ ] Van pontokba szedhető mondatsorozat folyó szövegbe rejtve? → prózává vagy listává írandó (S10)
- [ ] Lefuttattad a stilometriai mutatótáblát? Három vagy több kilógó érték = mintázat

### Eszközök — a visszaadás előtt

- [ ] Lefutott a helyesírás-ellenőrzés az átírt szövegen? (`python dict/spell.py check <fájl> --suggest`)
- [ ] Minden találatot megnéztél: javítva vagy `python dict/db.py ignore add …`-dal felvéve?
- [ ] A szinonimacseréknél kölcsönös párt választottál, és nem léptél át jelentéscsoportot? (`thesaurus.py lookup --verify`)
- [ ] Rögzítetted a cseréket az adatbázisban? (`python dict/db.py add …`)

---
