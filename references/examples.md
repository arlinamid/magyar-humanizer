# Végigvezetett példák

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

### C réteg — a harmadik passz ugyanazon a szövegen

A fenti átírás az A és a B rétegen átmegy. A C rétegen **nem.** Nézd meg újra:

- „Az AI nélkül ma már nehéz versenyezni — **ez nem kérdés. A valódi kérdés az, hogy…**" → egyszerre S7 (átmenetjelölés: a szöveg bejelenti, hogy most jön a lényeg) és S2 (szembeállító keret)
- „**nem** a technológia a szűk keresztmetszet, **hanem** a képzés" → második S2 ugyanabban a rövid bekezdésben
- „Aki erre nem költ, az pár éven belül megérzi." → S3: rövid, összegző nyomatékosító záró, közvetlenül a hosszú magyarázat után

Négy mondatban két szembeállítás, egy átmenetbejelentés és egy záró ütés. Mondatszinten mindegyik hibátlan — a **sűrűségük** az AI-jel.

### Átírva, mind a három réteg után:

> A Gartner 2023-as felmérésében a bevezetés szűk keresztmetszete sehol nem a technológia volt: a munkavállalók 60%-a soha nem kapott rendszeres AI-oktatást. Ez nálunk is pontosan így nézett ki — a licencek három hónapig álltak kihasználatlanul, mire valaki megkérdezte, tudja-e egyáltalán bárki, mire való. Azóta sem a szoftverre megy el a pénz nagyobbik fele.

**Mit változott a C rétegben:**
- Törölt: „ez nem kérdés / a valódi kérdés az" (S7 — az átmenet most magából a tartalomból derül ki)
- Törölt: az egyik „nem X, hanem Y" keret; a másik átírva állító mondattá (S2)
- Törölt: a záró nyomatékosító ütés; helyette egy konkrét következmény (S3)
- Hozzáadva: konkrét tapasztalati elem — három hónap, kihasználatlan licencek (S8, a „szerintem" helyett)
- A mondathosszak szórása nőtt: 24 / 32 / 13 szó (S3 + M2)

---
