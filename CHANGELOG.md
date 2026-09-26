# Magyar Humanizer — Fejlesztési napló

## Kiadatlan

- `db.py import`: törli a `seed.tsv`-ből kikerült `seed` eredetű bejegyzéseket (a `learned`/`manual` érintetlen). Eddig egy frissítés után a v2.2.0-ban törölt hibás cserék („elmúlás → kaszás”, „pirul → irul-pirul”) a meglévő adatbázisokban tovább éltek. Az adatbázis tárolja a betöltött mag ujjlenyomatát; az `ensure.py` eltérésnél magától importál, a `--check` ilyenkor 1-gyel lép ki.
- `spell.py`: a motor neve pontos — `hunspell` a rendszerprogram, `spylls` a Python-implementáció (eddig a spylls is „hunspell”-ként jelent meg, így a téves találatai megbízhatónak látszottak). Spylls esetén a kimenet figyelmeztet a hamis hibákra.
- `db.py seed`: a „Felfújt fontosság” tábla kulcsa törölve — a jobb oldala utasítás, nem csere (a gondolatjel-javítás óta amúgy sem illeszkedett).
- `install/compact.md`: újraszinkronizálva és rövidítve; a Windsurf-kimenet 12 036 karakterről a 12 000-es korlát alá került, a build ismét hiba nélkül fut.

## v2.2.0 (2026-09-26)

### Összefoglalás

Teljes audit a v2.1.1-en: tartalmi hűség szabály, két új műfaji réteg (széppróza, közösségi média), tipográfiai és nyelvtani javítások a mintafájlokban, és hibajavítások az eszközökben.

### 1. Tartalmi hűség

- Új alapszabály a SKILL.md elején: humanizálás közben nem kerülhet a szövegbe új tény, szám, forrás, idézet, név, esemény, élmény, vélemény vagy érzés. Ahol a szerző saját részlete kellene, `[ide jöhet egy saját példa: …]` jelölés marad, és a kimenet felsorolja.
- A példák eddig kitalált konkrétumokat tanítottak (Gartner-statisztika, „nálunk három hónapig…”, „ahol bevezettük”, „egy héttel korábban”). Ezek törölve vagy „szerzői háttérrel” ellátva: a konkrétum mindig a szerzőtől jön. Az A réteg elején megjegyzés: az „Utána” példák konkrétumai illusztrációk.
- `voice.md` átírva: a hang a szerző anyagából jön, nem kitalált személyiségből; összhangban az S8-cal.

### 2. Új műfaji rétegek

- `references/szepproza.md` — novella, regényrészlet: magyar párbeszéd-tipográfia, a szereplői beszéd/nyelvjárás megőrzése, szépprózai AI-jelek (F1–F8: megnevezett érzelem, klisés kép, érzékszervi hármas, beszélő-igék, tanulságos zárás, túlmagyarázott alszöveg, egyforma szereplők, formulás átmenetek).
- `references/kozossegi-media.md` — Facebook/LinkedIn-poszt: K1–K10 és emojitilalom (horog-nyitány, emojis lista, markdown és Unicode-félkövér, egymondatos bekezdések, kommentvadász zárás, hashtag-halmaz, tanulság, túlzó lelkesedés, regiszterkeveredés, esszészerkezet). A kimenet posztnál sima szöveg.
- A C réteg küszöbei kb. 400 szótól érvényesek; rövid szövegnél minőségi alkalmazás, szépprózában párbeszéd nélkül számolva.

### 3. Javítások a mintafájlokban

- Idézőjel: a skill saját példái is `„…"` alakot tanítottak (egyenes záró idézőjellel). Mindenhol `„…”`; a 14. minta leírja a belső idézetet (`»…«`) és az aposztrófot.
- Gondolatjel: a magyar gondolatjel a szóközös nagykötőjel (`–`), nem az angol `—`; a 15. minta ezt tanítja, és a fájlok szövege is ezt használja.
- M2: a „minden 3–4 mondatból egy legyen 5 szó alatt” kvóta ellentmondott a 25. mintának és az S3-nak — tartalom szerinti ritmusra cserélve.
- M8: a „mondja → mondom” példa hibás volt (az alany a gyár); új példa, és szabály: előbb nézd meg az ige alanyát. T/1-et csak akkor írj E/1-re, ha a szerző valóban egyedül csinálta.
- M9, S2, S4, S5, S6, S10 „Utána” példái nem adnak hozzá új tartalmat.
- Nyelvi hibák: „hangulhoz” (elírás) → „agresszívvá teszi a hangulatot”, „Kétértelmes” → „Kétértelmű”, „A rendszer feldolgoz” → „A rendszer feldolgozza az adatokat”.
- 7. minta: új AI-szavak (kulcsszerepet játszik, zökkenőmentes, betekintést nyújt, egyedülálló, „utazás”, „a … világában”) és a „mikor nem AI-jel” szabály (szakszó, egyszeri előfordulás).
- 18. minta: emoji semmilyen műfajban nem marad, Facebook- és LinkedIn-posztban sem; ha jelentést hordozott, szóval kell kimondani.
- Emojik a rétegfájlok címsoraiból törölve (a skill a saját 18. mintáját sértette).
- Ellenőrzőlista: S4 küszöb összhangba hozva (kettő már vizsgálandó), új szakaszok: tartalmi hűség, széppróza, közösségi média.
- `evolution-notes.md`: a „nemcsak…, hanem…” mintapélda ellentmondott a 9. mintának — átírva.

### 4. SKILL.md

- Frontmatter a Claude skill-szabvány szerint: `version`, `source`, `extends`, `changelog` a `metadata` alá került. A korábbi felső szintű kulcsok miatt a claude.ai / Claude asztali alkalmazás elutasította a feltöltést.
- A leírás visszakapta a magyar triggerkifejezéseket („humanizáld”, „tedd emberibbé”, „AI-szagú”) és a műfajokat.
- A parancsok abszolút úttal futnak (`<skill-mappa>`), nem a munkamappához képest.
- Ha a bootstrap nem sikerül, a humanizálás folytatódik, és a kimenet jelzi, hogy a gépi ellenőrzés nem futott (eddig: „ne humanizálj tovább”).
- A helyesírás-ellenőrzés után kötelező visszaolvasás: a létező, de rossz szót a hunspell nem látja.
- A szerző hangjának megőrzése és a műfaj meghatározása az 1. lépés része.
- Rögzítés: csak általánosítható szócsere, felhasználói mondat nem. Önfejlesztés: csak javaslat, a fájlokat a felhasználó jóváhagyásával.

### 5. Eszközök (`dict/`)

- Új `paths.py`: a szótárak és az adatbázis a `dict/` alá kerülnek, ha írható, különben a felhasználói adatmappába (`MAGYAR_HUMANIZER_HOME` felülírja). Csak olvasható telepítésben is működik.
- `fetch.py`: ha a GitHub API nem érhető el (403, korlátozás, homokozó), a szabványos fájlnevekkel közvetlenül tölt le a raw.githubusercontent.com-ról; a hibaüzenetben emlegetett `GITHUB_TOKEN`-t most ténylegesen használja. `--lang` módban nem tölti le újra a magyart. Hibás letöltésnél nem nulla kilépési kód.
- `ensure.py`: pip-telepítés `--user`, majd `--break-system-packages` visszaeséssel (PEP 668); kiírja az adatmappát és a rendszer-hunspell elérhetőségét.
- `spell.py`: a rendszer `hunspell` programja az elsődleges motor, ha elérhető (a spylls a magyar szótárral hamis hibát ad pl. az „ellenőrzi” alakra); `#hashtag` és `@említés` kihagyva; magyar rövidítések (pl., stb., kb., ún. …) elfogadva; a `--lang` a kivétellistára is érvényes.
- `thesaurus.py`: a címszó nem jelenik meg a saját szinonimái között; a „szófaji címkékkel” állítás javítva (a magyar tezauruszban nincs).
- `db.py`: a „kölcsönös” ellenőrzés valóban kölcsönösséget mér (oda-vissza), ahogy a dokumentáció írta — eddig csak az egyik irányt; `import` nem áll le, ha nincs letöltött szótár; `scan` a toldalékolt alakokat is megtalálja, és jelzi, hogy jelölteket ad, nem kötelező cseréket; `ignore add` nem írja automatikusan a verziókövetett `seed-ignore.tsv`-t (a felhasználói szövegek nevei nem kerülnek a repóba).
- `seed.tsv`: 140 bejegyzés törölve — köznapi szavak, amelyek novellában és posztban hamis találatot adtak („vezet”, „támogat”, „csökkent”, „pirul”, „elmúlás → kaszás”), rossz jelentésű vagy körkörös cserék („megvalósításra kerül → bevezető”, „szinergia → együtthatás”, „hangsúlyoz → aláhúz”), és elrontott idézőjeles sorok.
- `install/build.js`: a verzió a `metadata.version`-ből is kiolvasható; a forrásban lévő NUL bájt `\u0000`-ra cserélve. A `compact.md` az új szabályokkal frissítve és újraszinkronizálva.

---

## v2.1.1 (2026-09-20)

### Bootstrap — szótár és adatbázis automatikus előkészítése

A skill első lépése mostantól kötelezően elindítja a telepítést, ha hiányzik valami:

```bash
python dict/ensure.py
```

- Ellenőrzi a `spylls` csomagot, a `dict/data/hu_HU` helyesírási szótárat + tezauruszt, és a `dict/humanizer.db`-t
- Ami hiányzik, azt telepíti / létrehozza (`fetch.py` + `db.py import`) — nem kérdez rá
- Más nyelv: `python dict/ensure.py --lang hu_HU,en_US`
- Csak ellenőrzés: `python dict/ensure.py --check`

Beírva a SKILL.md folyamatába (0. lépés), a checklistbe és a `dict/README.md`-be.

---

## v2.1.0 (2026-09-20)

### Összefoglalás

Progresszív feltárás: a mintakatalógusok a `references/` alá kerültek. Átemelve a Codex-változat publicisztika- és önfejlesztő rétege. A helyesírási kivételek az adatbázisba költöztek.

### 1. Progresszív feltárás — a monolit felbontása

A SKILL.md most a **kötelező sorrendet, az eszközöket és a kimeneti formátumot** tartja. A minták külön fájlokban vannak:

| Fájl | Tartalom |
|------|----------|
| `references/layer-a-general.md` | A réteg (1–26) |
| `references/layer-b-hungarian.md` | B réteg (M1–M9) |
| `references/layer-c-stylometric.md` | C réteg (S1–S10) |
| `references/voice.md` | személyiség és lélek |
| `references/checklist.md` | teljes ellenőrzőlista |
| `references/examples.md` | végigvezetett példák |

A három alapréteg **mindig mind beolvasandó** — a „szükség szerint" csak a feltételes rétegekre vonatkozik. Ez a Codex-változat „use references selectively" mintáját fordítja meg: ott ez okozta, hogy az agentek csak a magyar réteget futtatták.

A `install/build.js` drift-bélyege a `references/` tartalmát is lefedi, így egy rétegfájl módosulása sem marad észrevétlen a szabályfájl-céloknál.

### 2. Publicisztika réteg (Codex-ből)

Feltételes réteg véleményhez, esszéhez, tárcához:

- `references/publicisztika.md` — állítás, konkrétum, súrlódás, aránytalanság
- `references/publicisztika-audit.md` — záró ellenőrzés átírás után
- `references/publicisztika-sources.md` — 2020 előtti magyar mintaszövegek

Több ponton függetlenül ugyanazt találja meg, mint a C réteg (pl. a túlcsiszolt „X nem ez, hanem az" tételmondat).

### 3. Önfejlesztés

- `references/self-improvement.md` — mikor és hogyan kerülhet új minta a skill memóriájába
- `references/evolution-notes.md` — rövid, tartós jegyzetek

A szócseréket továbbra is az adatbázisba kell írni (`dict/db.py add`), nem a jegyzetekbe.

### 4. Helyesírási kivételek az adatbázisban

A `dict/ignore.txt` megszűnt. A kivételek az `ignore_words` táblában élnek, verziókövetett magjuk a `dict/seed-ignore.tsv`.

```bash
python dict/db.py ignore add LLM --reason szakszo
python dict/db.py ignore list
python dict/db.py dump    # seed.tsv + seed-ignore.tsv
```

---

## v2.0.0 (2026-09-20)

### Összefoglalás

Háromrétegű átszervezés. Új stilometriai réteg (S1–S10), kötelezővé tett rétegsorrend, és `npx skills`-alapú telepítés minden támogatott agentbe.

### 1. Rétegstruktúra — a „csak a magyar réteg fut le" hiba javítása

A v1 leggyakoribb üzemi hibája az volt, hogy az agent meglátta a magyar szöveget, és **csak a magyar-specifikus mintákat** futtatta le. Az általános réteg így kimaradt: bennmaradt a „mérföldkövet jelent", a „szakértők szerint", a bekezdésenkénti három félkövér kiemelés és az emojis fejléc.

**Javítás:**

- A SKILL.md eleje egy **kötelező futtatási sorrend** gate-tel indul, a frontmatter előtti első érdemi szakaszként
- A három réteg explicit nevet kapott: **A — általános** (1–26), **B — magyar** (M1–M9), **C — stilometriai** (S1–S10)
- A B réteg bevezetője kimondja, hogy az A rétegre **ráépül**, nem helyettesíti
- A frontmatter `description` is kimondja, hogy a magyar réteg kiegészítés
- Új 7. lépés a folyamatban: **réteg-audit** — visszaadás előtt ellenőrizni kell, hogy mind a három lefutott
- A kimeneti formátum mostantól **rétegenként bontott** változáslistát kér (A / B / C), így a hiányzó réteg azonnal látszik
- A Gyors ellenőrző lista három szakaszra bomlik, és kimondja: „Ez a lista egyben van. Nem szabad csak a B szakaszát végigfutni."

### 2. Új C réteg — stilometriai minták (S1–S10)

Forrás: Caimelot, *Az MI-használat felismerhető nyomai — mit mutat meg a stilometria?* (2026. szeptember).

Az A és B réteg mondatokat javít, a C réteg **arányokat mér**: egy szöveg minden mondata lehet természetes, miközben a szöveg egésze gépi.

| Minta | Leírás |
|-------|--------|
| S1 | Feltűnően szabályos gondolatvezetés |
| S2 | A „nem az… hanem…" szerkezet túlhasználata, mondatkezdő „Hanem" |
| S3 | Rövid mondatok mint rendszer (megtört szövegritmus) |
| S4 | Retorikai kérdések halmozása |
| S5 | Azonos vázú mondatsorozatok |
| S6 | Két pólusra egyszerűsített érvelés |
| S7 | Az átmenetek túlzott jelölése |
| S8 | A személyesség nyelvi jelölése („szerintem"-szindróma) |
| S9 | Ugyanannak a gondolatnak a többszöri visszatérése |
| S10 | Felsorolások folyó szövegbe rejtve |

**Új: stilometriai mutatótábla** — mérhető küszöbökkel (mondathossz-szórás, 1–3 szavas mondatok aránya, kérdő mondatok aránya, „hanem"-sűrűség, átvezető formulák aránya, véleményjelölő/tapasztalat arány). Alapelv: **egyetlen kilógó érték semmit nem jelent, három vagy több egyszerre már mintázat.**

**Kereszthivatkozások a rétegek között** — a fedések feloldva, hogy ne legyen kétszeres javítás:

- S2 ↔ 9. minta (negatív párhuzamosságok): a 9. egy mondatot néz, az S2 a sűrűséget méri
- S3 ↔ 25. minta + M2: az M2 ritmusváltást kér, az S3 figyelmeztet, hogy ez ne legyen sablonos
- S5 ↔ 10. minta: a 10. a felsorolt elemek számát nézi, az S5 a mondatvázak ismétlődését
- S7 ↔ 26. minta: a 26. egy előfordulást töröl, az S7 az átmenetek változatosságát méri
- S9 ↔ 11. minta: a 11. ugyanannak a *szónak*, az S9 ugyanannak a *gondolatnak* az újrafogalmazása

**S8 korrekciója a „SZEMÉLYISÉG ÉS LÉLEK" szakaszhoz:** a személyességet tapasztalat hordozza, nem jelölő. Ha több a „szerintem", mint a konkrét tapasztalati elem, a személyesség díszlet.

### 3. Új: Felelősség és átláthatóság szakasz

- Az automatikus MI-detektorok korlátai — a százalékos érték nem szerzőségi bizonyíték
- Szerzői felelősség jelentős tartalmi MI-közreműködés esetén
- Az EU MI-rendelet 50. cikk (4) bekezdése: jelzési kötelezettség a nyilvánosság közérdekű tájékoztatására közzétett MI-generált szövegnél (2026. augusztus 2-tól alkalmazandó)

### 4. Új: agent-specifikus telepítő réteg

Korábban csak a Claude Code kézi telepítése volt dokumentálva.

**Elsődleges út — `npx skills`:**

```bash
npx skills add arlinamid/magyar-humanizer
```

A [vercel-labs/skills](https://github.com/vercel-labs/skills) CLI a SKILL.md szabványt használja, és mind a nyolc célt kezeli: Claude Code (CLI és Desktop), OpenAI Codex CLI, Cursor, Windsurf, GitHub Copilot, Gemini CLI / Antigravity, Cline, Zed. Mindegyik a **teljes** SKILL.md-t kapja — a skill nem sérül telepítéskor.

**Visszaesési réteg — `install/build.js`:** transzpiler azokhoz a régebbi beállításokhoz, amelyek csak szabályfájlt olvasnak. Generált formátumok: Cursor `.mdc` rule, Windsurf workspace rule, Copilot scoped instructions, Gemini CLI TOML parancs, `AGENTS.md`.

- A méretkorlátok **karakterben** ellenőrződnek, nem bájtban — a magyar ékezetes szöveg UTF-8-ban 1,1–1,2x annyi bájt, mint karakter, ami a Windsurf 12 000 karakteres korlátjánál téves hibát okozott volna
- A build 95% felett tartalékot jelez, korlát felett hibát ad
- A Windsurf-változatból a forrásjegyzék kimarad, hogy legyen mozgástér

**`install/compact.md` + drift-ellenőrzés:** a szabályfájl-célok kézzel sűrített forrása. Mivel ez önálló forrás, a build egy sha256-bélyeggel a SKILL.md tartalmához köti, és **DRIFT** hibát ad, ha a SKILL.md változott, de a sűrítés nem. Szinkronizálás átvezetés után: `node install/build.js --sync`.

### 5. Szótárrendszer — a `synonyms.json` leváltása

A korábbi `synonyms.json` két dolgot nem tudott: **nem volt benne kereszt-ellenőrzés**, tehát bármilyen elgépelt vagy rossz jelentésű javaslat bekerülhetett, és nehezen lehetett feldolgozni.

**Helyette a teljes LibreOffice szótárcsomag.**

- `dict/fetch.py` — letölti a [LibreOffice/dictionaries](https://github.com/LibreOffice/dictionaries) repóból a kért nyelveket. A magyar mindig települ, a telepítő **rákérdez, kell-e másik nyelv is.** Tezaurusz 29 nyelvhez, helyesírási szótár 66-hoz érhető el.
- A szótárak **nem kerülnek be a repóba.** Nyelvenként ~6 MB, és a licencek eltérnek: a magyar tezaurusz **GPL-2** (© 2009 Németh László), ami nem fér össze ennek a repónak az MIT licencével. Futásidőben használjuk, nem terjesztjük.
- A LibreOffice repó nem tartalmaz `.idx` indexet a tezauruszhoz — a `thesaurus.py` generálja (szó → bájtoffszet), így a 2 MB-os fájlból nem kell mindent memóriába olvasni.

**Nyereség:** 55 szó és 20 kifejezés helyett **21 687 szócikk, 30 500 jelentéscsoport**, szófaji címkékkel.

### 6. Kereszt-ellenőrzés

Minden szinonimajelölt három ellenőrzésen megy át, és az eredmény eltárolódik:

| Ellenőrzés | Mit fog meg |
|------------|-------------|
| helyesírás | elgépelést, rossz egybeírást |
| tezaurusz | koholt vagy túl ritka alakot |
| **kölcsönösség** | rossz jelentésű cserét |

A kölcsönösség a legerősebb jel:

```
kiemelkedő -> kiváló    helyesírás: rendben   tezaurusz: rendben   kölcsönös: rendben
kiemelkedő -> sárcipő   helyesírás: rendben   tezaurusz: rendben   kölcsönös: FIGYELEM
```

**A hiányzó adat nem bukás.** Ha a forrásszó nincs a tezauruszban — és a skill épp ilyen AI-klisékkel dolgozik, mint a „kulcsfontosságú" —, a kölcsönösség „n.a.", nem „FIGYELEM". Az első implementáció ezt elrontotta: 242 bejegyzést jelölt bukottnak, holott csak a forrásszó hiányzott.

**Amit a migráció kihozott:** a régi JSON 348 átemelt bejegyzéséből kettő valódi hiba volt — `bugyborékal` (helyesen *bugyborékol*) és `teljeskörű` (helyesen *teljes körű*). Mindkettő javítva. A javaslatok nagyjából fele pedig olyan tipp, amit a tezaurusz nem erősít meg; ezek benne maradtak, de meg vannak jelölve.

### 7. Helyesírás-ellenőrzés — mostantól kötelező lépés

Korábban opcionális segédeszköz volt. A v2.0-tól a folyamat 7. lépése, és az ellenőrzőlistán is szerepel: **ellenőrizetlen szöveget a skill nem ad vissza.** Az átírás közben keletkezik a legtöbb elgépelés, mert épp akkor cserélsz szavakat és szerkesztesz át mondatokat.

- `dict/spell.py` — teljes hunspell motor (`spylls`), visszaeséssel `pyenchant`-ra, végül nyers szólistára (ilyenkor figyelmeztet)
- **Miért nem elég a szólista:** a „kulcsfontosságú" nem szerepel külön a `.dic`-ben, a hunspell összetételként állítja elő. Szólistával téves hibának látszana, és a ragozott alakok tömegesen buknának.
- A magyar `.dic` néhány `REP` mintája nem érvényes reguláris kifejezés, amitől a spylls betöltés közben elhasalna — ez lekezelve (literálként fordítjuk)
- Kihagyja a kódblokkokat, URL-eket, YAML frontmattert, azonosítókat és fájlneveket
- Kezeli a magyar sajátosságokat: `AI-szag`, `LLM-ek`, `1989-ben`, `Q3-ban`, `40%-ánál`, `„kiemelkedő"-höz`
- Kivételek: `dict/seed-ignore.tsv` → `ignore_words` tábla (`python dict/db.py ignore …`)

**Dogfood:** a saját SKILL.md-n futtatva két valódi hibát talált — `legrövidebbés` (hiányzó szóköz) és `Melléknéveknél` (helyesen *Mellékneveknél*). Mindkettő javítva.

### 8. Saját adatbázis beégetett lista helyett

`dict/db.py` — SQLite adatbázis, amit a skill **munka közben maga épít.**

Az induló készlet csak mag (`origin='seed'`, a SKILL.md M3/M5 tábláiból és a régi JSON-ból). A valódi tartalom onnan jön, hogy a skill rögzíti, mit cserélt, melyik minta alapján, milyen mondatban (`origin='learned'`).

```bash
python dict/db.py add "szerepet játszik" "hat" --pattern M3 --context "…"
python dict/db.py scan szoveg.md
python dict/db.py verify
```

- Táblák: `entries`, `checks` (a kereszt-ellenőrzés eredménye), `contexts` (valódi előfordulások)
- **Verziókövetés:** a `.db` gitignore-olt, a `dict/seed.tsv` commitolva. Bináris SQLite-nak nem olvasható a diffje és nem lehet összefésülni; a TSV-nek igen. `db.py dump` / `db.py import` a két irány között.
- A Poet.hu API és a hozzá tartozó `.env` / `.env.example` megszűnt: a tezaurusz offline, nagyobb, és nem kell hozzá hitelesítés

### 9. Egyéb

- Új háromrétegű végigvezetett példa: a v1 „átírt" mintaszövege átmegy az A és B rétegen, de **elbukik a C-n** — ugyanaz a szöveg C réteg után is átírva
- README.md átírva v2.0-ra, `npx skills` telepítéssel és C réteg táblával
- Verzió: 1.4.1 → 2.0.0

---

## v1.4.1 (2026-03-09)

### Összefoglalás

Credentials kiemelése a kódból: env változók, `.env.example` minta, `.gitignore`. A repó mostantól biztonságosan feltölthető GitHubra.

### Változások

- **Biztonsági javítás:** A Poet.hu API URL-ből eltávolítva a hardcoded felhasználónév és kulcs
- **Új:** `.env` — tényleges credentials (gitignore-olva, nem kerül repóba)
- **Új:** `.env.example` — minta sablon, biztonságosan commitolható
- **Új:** `.gitignore` — `.env` és `dict/hu_HU.*` fájlok kizárva
- **SKILL.md:** API szekció frissítve — `os.environ.get('POET_HU_USER')` / `POET_HU_KEY`
- **CHANGELOG.md:** v1.3.0-ban szereplő hardcoded URL lecserélve env-alapú példára

### Fájlszerkezet feltöltés után (GitHub)

```
magyar-humanizer/
├── SKILL.md          ✓ commitolható
├── synonyms.json     ✓ commitolható
├── CHANGELOG.md      ✓ commitolható
├── .env.example      ✓ commitolható (placeholder adatokkal)
├── .gitignore        ✓ commitolható
├── .env              ✗ gitignore-olva (valódi credentials)
└── dict/
    ├── README.md     ✓ commitolható (forrásjelölés, licenc, telepítési útmutató)
    ├── hu_HU.dic     ✓ commitolható (~1.7 MB, LibreOffice LGPL-2.1/MPL-2.0)
    └── hu_HU.aff     ✓ commitolható (~2.2 MB, LibreOffice LGPL-2.1/MPL-2.0)
```

---

## v1.4.0 (2026-03-09)

### Összefoglalás

CV-humanizálási folyamatból levont tanulságok alapján: új M8 minta (személy-inkonzisztencia), a folyamat 4. lépésének kiegészítése, és 3 új checkbox a Gyors ellenőrző listán.

---

## Új: M8 — Személy-inkonzisztencia (Person drift)

### Miért kellett?

A CV-humanizálás során kiderült, hogy a `pyenchant` helyesírás-ellenőrzője grammatikailag helyes, de logikailag hibás alakokat nem talál meg. Az `én értettük`, `stabilizáltuk`, `csak más nyelven mondja` alakok mind helyesen vannak írva — de E/1 narrációban értelmetlenek vagy félrevezetőek.

### Három alaptípus

| Típus | Példa | Javítás |
|-------|-------|---------|
| E/1 névmás + T/1 ige | `én értettük legjobban` | `én értettem legjobban` |
| T/1 ige eredménymondatban | `csökkentettük a hibaarányt` | `csökkentettem a hibaarányt` |
| E/3 ige E/1 narrációban | `csak más nyelven mondja` | `csak más nyelven mondom` |

### Miért csinálja az AI?

Az AI csapateredményeket T/1-gyel ír le, mert az „szerényebbnek" tűnik. CV-ban ez visszafelé sül el: az olvasó nem tudja, ki cselekedett ténylegesen.

### Kapcsolat M7-tel

Az M7 (Első személyű logikai ellentmondás) az érzések/reakciók logikáját ellenőrzi. Az M8 a grammatikai személy-konzisztenciát — az ige E/1 vagy T/1 alakját. Két különböző hibatípus.

---

## Folyamat 4. lépés kiegészítése

Hozzáadva az ellenőrzési pontok közé:
> **Első személyű szövegben:** minden ige E/1 — nincs T/1 „eredménybújtatás", nincs E/3 perspektívaváltás (M8)

---

## Gyors ellenőrző lista — 3 új checkbox (M8)

```
- [ ] Első személyű narrációban van-e T/1 igealak eredménymondatban?
- [ ] Van E/1 névmás + T/1 ige ellentmondás?
- [ ] Van E/3 ige ott, ahol az alany maga cselekedett?
```

---

## v1.3.0 (2026-03-09)

### Összefoglalás

A v1.2.0-ban csak statikus szabályok és minták voltak. Ez a verzió három önálló eszközzel egészíti ki a skillt: helyi szinonima-adatbázissal, élő API-integrációval és Magyar helyesírás-ellenőrzővel. Az eszközök egymásra épülnek, és a szinonima-adatbázis minden egyes használattal automatikusan bővül.

---

## 1. Helyi szinonima-adatbázis (`synonyms.json`)

### Miért kellett?

A szinonima-keresés eddig teljesen az AI belső tudásán alapult — nem volt referencia, nem volt visszakereshetőség, és ugyanazokat a kérdéses szavakat minden alkalommal újra kellett kiértékelni.

### Mit csináltunk?

Létrehoztuk a `synonyms.json` fájlt két szekkcióval:

**`szavak`** — 38 egyszavas AI-klisé, szócsoportonként rendezve (a Poet.hu API struktúráját tükrözve):

```json
"kulcsfontosságú": [
  ["alapvető", "döntő", "lényeges", "nélkülözhetetlen"],
  ["kritikus", "elsőrendű", "megkerülhetetlen"]
]
```

A szócsoportok különböző jelentésmezőket fednek le — kontextustól függ, melyiket kell választani.

**`kifejezések`** — 22 terpeszkedő fordulat és bevezető klisé javasolt cserékkel:

```json
"szerepet játszik": {
  "helyett": ["hat", "befolyásol", "számít", "közrejátszik"],
  "megjegyzés": "M3 terpeszkedő"
}
```

A bejegyzések forrása: a SKILL.md összes mintája (1., 3., 7., 8., 9., M3, M4, M5).

### Alapalak-egyezmény

A Magyar szavak ragozva jelennek meg a szövegben. Az adatbázis kulcsa és az API paramétere mindig a **toldalék nélküli alapalak**:

| Szövegbeli alak | Alapalak (kulcs) |
|-----------------|-----------------|
| kulcsfontosságúnak | kulcsfontosságú |
| kiemelkedőbb | kiemelkedő |
| hozzájárulnak | hozzájárul |
| elősegítette | elősegít |

Szabály: főneveknél egyes szám alanyeset, melléknéveknél alapfok, igéknél főnévi igenév vagy E/3 jelen idő.

---

## 2. Poet.hu szinonimaszótár API

### Miért kellett?

A helyi adatbázis véges — a szövegben előfordulhatnak olyan szavak, amelyek még nincsenek benne. Ilyenkor élő lekérés szükséges.

### Mit csináltunk?

Integráltuk a [Poet.hu](https://poet.hu) szinonimaszótár API-ját. A lekérés mindig az alapalakkal történik, a hitelesítő adatokat env változókból olvassa:

```python
import os
url = f"https://api.poet.hu/szinonima.php?f={os.environ['POET_HU_USER']}&j={os.environ['POET_HU_KEY']}&s={alapalak}"
```

Válasz (XML):

```xml
<szinonimak>
  <szocsoport>
    <szinonima>alapvető</szinonima>
    <szinonima>döntő</szinonima>
  </szocsoport>
</szinonimak>
```

### Cache-first logika

Az API nem az első, hanem az utolsó eszköz:

```
szövegbeli alak
    → alapalakra vezet vissza
        → synonyms.json-ban van? → igen: onnan veszi
                                 → nem: Poet.hu API-t hívja
                                            → eredményt visszamenti synonyms.json-ba
```

**Az API-hívás után a visszamentés kötelező.** Az adatbázis így folyamatosan bővül — ugyanazt a szót legközelebb már nem kell újra lekérni.

### Mikor NE hívjuk az API-t?

- Ha a szöveg szakmai/jogi regiszterű és a precizitás fontosabb a változatosságnál
- Ha a szinonima megváltoztatná a szöveg pontos jelentését
- Ha a `kifejezések` szekcióban `"[töröld]"` szerepel — ott nem csere, hanem törlés a megoldás

---

## 3. Helyesírás-ellenőrzés (pyenchant + LibreOffice hu_HU)

### Miért kellett?

Ha szinonimát cserélünk, előfordulhat, hogy a kiválasztott alternatíva helyesírása kérdéses — különösen ritkább szavaknál. Eddig nem volt erre eszköz.

### Mit csináltunk?

**Szótárfájlok:** Letöltöttük a LibreOffice GitHub repójából a hivatalos Magyar hunspell szótárat:

- Forrás: [LibreOffice/dictionaries/hu_HU](https://github.com/LibreOffice/dictionaries/tree/master/hu_HU)
- Fájlok: `hu_HU.dic` (1.7 MB) + `hu_HU.aff` (2.2 MB)
- Tartalmazza az összes Magyar ragozási és helyesírási szabályt

**Telepítés:** A `pyenchant` Python könyvtár hunspell-kompatibilis motorjába másoltuk a szótárfájlokat.

**Használat:**

```python
import enchant
d = enchant.Dict('hu_HU')

d.check('kiemelkedő')      # True  — helyes
d.check('kiemelkedo')      # False — hibás
d.suggest('kiemelkedo')    # ['kiemelkedő', ...]
```

**Teszteredmény:** 10/10 — a szótár helyesen azonosítja a hibás alakokat és ad rájuk javítási javaslatot.

| Szó | Eredmény |
|-----|----------|
| `kulcsfontosságú` | ✓ helyes |
| `kulcsfontossagu` | ✗ → `kulcsfontosságú` |
| `fenntartható` | ✓ helyes |
| `fenntartahto` | ✗ → `fenntartott` |
| `innnovatív` | ✗ → `innovatív` |
| `elősegít` | ✓ helyes |

**Mikor használjuk:** nem minden szónál — csak szinonima-cserénél, vagy ha egy átírt alak helyesírása bizonytalan.

---

## Fájlszerkezet

```
skills/magyar-humanizer/
├── SKILL.md          — fő skill (v1.3.0), tartalmazza az összes eszköz leírását
├── synonyms.json     — helyi szinonima-adatbázis (bővül minden API-hívásnál)
├── CHANGELOG.md      — ez a fájl
└── dict/
    ├── hu_HU.dic     — LibreOffice Magyar szótár (1.7 MB)
    └── hu_HU.aff     — LibreOffice Magyar ragozási szabályok (2.2 MB)
```

---

## Ami nem változott

- A 26 általános AI-minta (tartalmi, nyelvi, stílus, kommunikációs)
- A 7 Magyar-specifikus kiterjesztés (M1–M7)
- A személyiség és lélek szekció
- A gyors ellenőrző lista
- A stílusréteg-érzékeny szabályok (köznyelvi / irodalmi / hivatalos)
