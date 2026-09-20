# dict/ — szótárak és nyelvi eszközök

Négy eszköz, mind offline, egyik sem igényel API-kulcsot.

| Fájl | Mire való |
|------|-----------|
| `fetch.py` | szótárak letöltése a LibreOffice repóból (interaktív nyelvválasztás) |
| `spell.py` | helyesírás-ellenőrzés teljes hunspell motorral — **kötelező lépés** |
| `thesaurus.py` | szinonimakeresés kereszt-ellenőrzéssel |
| `db.py` | a skill saját adatbázisa, amit munka közben ő maga épít |
| `seed.tsv` | az adatbázis verziókövetett szöveges magja (szócserék) |
| `seed-ignore.tsv` | helyesírási kivételek magja (angol szakszó, név, márka) |

---

## Telepítés

```bash
python dict/fetch.py                 # interaktív: rákérdez, mely nyelvek kellenek
python dict/fetch.py --lang hu_HU    # csak magyar
python dict/fetch.py --list          # mi érhető el
pip install spylls                   # a teljes hunspell motorhoz
```

A magyar mindig települ. A telepítő rákérdez, kell-e másik nyelv is — a skill más nyelvű szövegekhez is használható, és a helyesírás-ellenőrzés csak a letöltött nyelvekre tud futni. Tezaurusz 29 nyelvhez érhető el, helyesírási szótár 66-hoz.

A letöltött fájlok a `dict/data/<nyelv>/` alá kerülnek, és **nem kerülnek be a repóba**. Ennek két oka van: nyelvenként ~6 MB, és a licencek nem egységesek (lásd lent).

---

## Miért teljes hunspell és nem szólista?

A magyar toldalékol és összetételt képez. A „kulcsfontosságú" nem szerepel külön a `hu_HU.dic` fájlban — a hunspell összetételként állítja elő. Puszta szólista-tagsággal ez téves hibának látszana, és a ragozott alakok tömegesen buknának.

Ezért a `spylls` (tiszta Python hunspell) a mérce. Ha nincs telepítve, a `spell.py` előbb a `pyenchant`-ot próbálja, végül a nyers szólistára esik vissza — de ilyenkor jelzi, hogy az eredmény csak szótári alakokra megbízható.

A magyar `.dic` néhány `REP` mintája nem érvényes reguláris kifejezés, amitől a spylls betöltés közben elhasalna. A `spell.py` ezt lekezeli: az ilyen mintát literálként fordítja.

```bash
python dict/spell.py check szoveg.md --suggest
python dict/spell.py word kiemelkedo --suggest
python dict/spell.py engine              # melyik motor aktív
```

A `-` jeles alakokat (`AI-szag`, `LLM-ek`, `1989-ben`), a rövidítéseket, a kódblokkokat, az URL-eket és a YAML frontmattert az eszköz magától kihagyja.

---

## A kereszt-ellenőrzés

Ez hiányzott a korábbi JSON-alapú megoldásból. Minden szinonimajelölt három ellenőrzésen megy át:

| Ellenőrzés | Kérdés | Mit fog meg |
|------------|--------|-------------|
| helyesírás | valódi szó-e | elgépelést (`bugyborékal`), rossz egybeírást (`teljeskörű`) |
| tezaurusz | szótári szócikk-e | koholt vagy túl ritka alakot |
| **kölcsönösség** | a jelölt szócikkében visszajön-e az eredeti szó | rossz jelentésű cserét |

A kölcsönösség a legerősebb jel:

```
kiemelkedő -> kiváló    helyesírás: rendben   tezaurusz: rendben   kölcsönös: rendben
kiemelkedő -> sárcipő   helyesírás: rendben   tezaurusz: rendben   kölcsönös: FIGYELEM
```

A „sárcipő" valódi szó, és szerepel is a tezauruszban — csak éppen semmi köze a „kiemelkedő"-höz. Egyedül a kölcsönösség fogja meg.

**A hiányzó adat nem bukás.** Ha a forrásszó nincs a tezauruszban — és a skill épp ilyen AI-klisékkel dolgozik, mint a „kulcsfontosságú" vagy a „mélységes" —, a kölcsönösség „n.a.", nem „FIGYELEM".

---

## Az adatbázis

A `humanizer.db` (SQLite) tárolja, mit mire cseréltünk, melyik minta alapján, milyen mondatban. Nem beégetett lista: az induló készlet csak mag (`origin='seed'`), a tartalom a munkából jön (`origin='learned'`).

```bash
python dict/db.py add "szerepet játszik" "hat" --pattern M3 --context "…"
python dict/db.py scan szoveg.md
python dict/db.py lookup "kiemelkedő"
python dict/db.py verify
python dict/db.py stats
python dict/db.py export --out dump.tsv
```

**Verziókövetés:** a `.db` gitignore-olt, a `seed.tsv` viszont commitolva van. Bináris SQLite-nak nem olvasható a diffje és nem lehet összefésülni; a TSV-nek igen.

```bash
python dict/db.py dump      # .db  -> seed.tsv   (commit előtt)
python dict/db.py import    # seed.tsv -> .db    (klónozás után)
```

---

## Licencek

A letöltött szótárak **nem ennek a repónak a részei**, és nem is azonos licencűek. Ezért tölti le őket a `fetch.py` ahelyett, hogy be lennének másolva.

| Komponens | Licenc |
|-----------|--------|
| magyar helyesírási szótár (`hu_HU.dic` / `.aff`) | LGPL-2.1 / MPL-2.0 |
| **magyar tezaurusz** (`th_hu_HU_v2.dat`) | **GPL-2** — Copyright © 2009 Németh László |
| elválasztási minták (`hyph_hu_HU.dic`) | LGPL-2.1 / MPL-2.0 |
| ez a skill (kód és SKILL.md) | MIT |

A magyar tezaurusz GPL-2 licencű, ami nem fér össze az MIT-tel egy terjesztett csomagban. A skill futásidőben használja, nem terjeszti — a felhasználó tölti le a LibreOffice repójából. Ha a skillt becsomagolva terjeszted, a tezauruszt ne tedd bele.

Az egyes nyelvek pontos licencfeltételeit a `fetch.py` a `README_*.txt` fájlokkal együtt letölti a `dict/data/<nyelv>/` mappába.

Forrás: [LibreOffice/dictionaries](https://github.com/LibreOffice/dictionaries)
