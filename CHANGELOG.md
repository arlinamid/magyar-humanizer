# Magyar Humanizer — Fejlesztési napló

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
