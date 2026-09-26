# Önfejlesztési szabályok

Akkor használd, ha helyben érdemes továbbfejleszteni a `magyar-humanizer` skillt. Egy humanizálási feladat közben ne írd át a skill fájljait: javasold a felhasználónak a bejegyzést, és csak az ő jóváhagyásával vedd fel. A skill mappája sok telepítésben csak olvasható, és egy frissítés felülírja.

## A cél

Megőrizni a visszatérő, újrahasznosítható átírási tudást anélkül, hogy a skill magja felhízna.

## Mikor írj be új jegyzetet

Az [evolution-notes.md](evolution-notes.md) fájlba csak akkor kerüljön bejegyzés, ha **mind** igaz:

- A mintát legalább kétszer láttad (ugyanabban a munkamenetben, vagy a felhasználó megerősíti, hogy visszatérő), vagy nyilvánvalóan túlmutat egyetlen szövegen.
- Még nincs benne a rétegfájlokban (`layer-a-general.md`, `layer-b-hungarian.md`, `layer-c-stylometric.md`, `publicisztika.md`, `szepproza.md`, `kozossegi-media.md`).
- Tömören, 2–6 sorban leírható.
- Tartósan javítja a következő magyar átírásokat.

## Mi való ide

- Új, visszatérő magyar AI-minta.
- Publicisztikai ritmus- vagy hangvétel-heurisztika, ami ismételten javít az eredményen.
- Figyelmeztetés egy félrevezető átírási szokásra.
- Tömör előtte/utána mikroszabály, hosszú felhasználói szöveg másolása nélkül.

## Mi nem való ide

- Hosszú felhasználói szövegrészletek.
- Személyes vagy azonosításra alkalmas anyag.
- Egyszeri, túlságosan kontextusfüggő döntés.
- Olyan átfogalmazás, ami csak szebben hangzik, de nem általánosítható.

## Forma

Tömör bejegyzés, ebben a szerkezetben:

- dátum
- rövid címke
- a szabály egy-két mondatban
- opcionális mikropélda, legfeljebb 1–2 sor

## Mi tartozik máshova

**Szócsere és fordulatcsere nem ide való, hanem az adatbázisba:**

```bash
python3 "<skill-mappa>/dict/db.py" add "<eredeti>" "<csere>" --pattern <minta>
```

Az adatbázis kereshető, számolja a használatot, és minden bejegyzést átereszt a kereszt-ellenőrzésen (helyesírás, tezaurusz, kölcsönösség). Egy prózai jegyzet ezt nem tudja. Ide az olyan megfigyelés kerüljön, ami **nem** fejezhető ki „ezt erre cseréld” formában.

## Tartsd karcsún a skillt

- A stabil munkafolyamat a `SKILL.md`-ben marad.
- A részletes, újrahasznosítható útmutatás a rétegfájlokba való.
- Az `evolution-notes.md` tartós megfigyelések jegyzetfüzete, nem második kézikönyv.
