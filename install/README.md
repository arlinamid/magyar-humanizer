# Telepítés

## 1. Elsődleges út — `npx skills`

A skill SKILL.md-szabvány szerint épül, ezért a [skills CLI](https://github.com/vercel-labs/skills)-jel közvetlenül telepíthető. **Ez kezeli az összes agentet**, a linkelést és a frissítést is.

```bash
npx skills add arlinamid/magyar-humanizer
```

Ez felismeri a gépen lévő agenteket és felajánlja a telepítést. Konkrét célok megadása:

```bash
npx skills add arlinamid/magyar-humanizer --agent claude-code codex cursor
npx skills add arlinamid/magyar-humanizer -g                # globálisan (user-szintű)
npx skills add arlinamid/magyar-humanizer --all             # minden agent, kérdés nélkül
npx skills add arlinamid/magyar-humanizer --copy            # másolás symlink helyett
```

Frissítés és eltávolítás:

```bash
npx skills update magyar-humanizer
npx skills remove magyar-humanizer
```

### Hova kerül agentenként

| Agent | `--agent` név | Cél |
|-------|---------------|-----|
| Claude Code (CLI és Desktop) | `claude-code` | `~/.claude/skills/` · `.claude/skills/` |
| OpenAI Codex CLI | `codex` | `~/.codex/skills/` · `.codex/skills/` |
| Cursor | `cursor` | `.cursor/skills/` |
| Windsurf | `windsurf` | `.windsurf/skills/` |
| GitHub Copilot | `github-copilot` | `.github/skills/` |
| Gemini CLI / Antigravity | `gemini`, `gemini-cli` | `.gemini/skills/` |
| Cline | `cline` | `.agents/skills/` |
| Zed | `zed` | `.agents/skills/` |

Mindegyik a **teljes SKILL.md-t** kapja, mind a három réteggel. Ez a lényeg: a skill nem sérül a telepítés során.

---

## 2. Kézi telepítés CLI nélkül

A SKILL.md-t értő agenteknél elég a mappát bemásolni:

```bash
git clone https://github.com/arlinamid/magyar-humanizer.git
cp -r magyar-humanizer ~/.claude/skills/     # Claude Code / Desktop
cp -r magyar-humanizer ~/.codex/skills/      # Codex CLI
cp -r magyar-humanizer ~/.cursor/skills/     # Cursor
```

Windows (PowerShell):

```powershell
git clone https://github.com/arlinamid/magyar-humanizer.git
Copy-Item -Recurse magyar-humanizer $env:USERPROFILE\.claude\skills\
```

---

## 2b. Szótárak — telepítés után

A skill eszközei külön szótárakat igényelnek. Ezek licencokok miatt nem részei a repónak (a magyar tezaurusz GPL-2, a repó MIT), ezért külön kell letölteni őket:

```bash
python dict/fetch.py      # rákérdez, mely nyelvek kellenek a magyaron kívül
pip install spylls        # a teljes hunspell motorhoz
```

Enélkül a helyesírás-ellenőrzés nyers szólistára esik vissza, és a tezaurusz nem érhető el. Részletek: [../dict/README.md](../dict/README.md)

---

## 3. Visszaesési réteg — régi, szabályfájl-alapú beállítások

**Ez csak akkor kell**, ha az agented még nem ismeri a skill-mappát, és kizárólag szabályfájlt olvas (régebbi Windsurf `.windsurf/rules/`, Copilot `copilot-instructions.md`, Gemini CLI slash-parancs). Ezeknek a fájloknak méret- vagy kontextuskorlátjuk van, ezért nem a teljes skillcsomag megy beléjük, hanem a kézzel sűrített [`compact.md`](compact.md).

```bash
node install/build.js --list            # elérhető formátumok
node install/build.js --all             # minden formátum az install/dist/ mappába
node install/build.js --target windsurf,copilot
```

A generált fájlok:

| Formátum | Kimenet | Cél |
|----------|---------|-----|
| Cursor project rule | `dist/magyar-humanizer.mdc` | `.cursor/rules/` |
| Windsurf workspace rule | `dist/magyar-humanizer.windsurf.md` | `.devin/rules/` (fallback: `.windsurf/rules/`) |
| Copilot scoped instructions | `dist/magyar-humanizer.instructions.md` | `.github/instructions/` |
| Gemini CLI parancs | `dist/magyar-humanizer.toml` | `~/.gemini/commands/` |
| Általános | `dist/AGENTS.magyar-humanizer.md` | `AGENTS.md` (beillesztendő) |

### Méretkorlátok

A korlátok **karakterben** értendők, nem bájtban — a magyar ékezetes szöveg UTF-8-ban 1,1–1,2-szer annyi bájt, mint karakter. A Windsurf 12 000 karakteres korlátjánál a build prioritási sorrendben hagy el szakaszokat, amíg befér — először a forrásjegyzéket, aztán a jogi-etikai részt, végül az eszközleírást —, és kiírja, mit hagyott el. Az operatív szabályok mindig bennmaradnak. Egyéb céloknál 95% felett figyelmeztet, korlát felett hibát ad.

---

## A compact.md és a drift

A `compact.md` **kézzel írt** sűrítés, tehát önálló forrás — és minden önálló forrás el tud csúszni az eredetitől. Ezért a build a SKILL.md tartalmához köti egy bélyeggel:

```
<!-- synced-with: SKILL.md@2.1.0 sha256:eeb317506525 -->
```

Ha a SKILL.md változik, de a `compact.md` nem, a build **DRIFT** hibát ad. A teendő ilyenkor:

1. Nézd át, hogy a SKILL.md változása érinti-e a sűrített változatot
2. Ha igen, vezesd át kézzel a `compact.md`-be
3. Frissítsd a bélyeget: `node install/build.js --sync`

A `--sync` **csak a bélyeget írja át**, a tartalmat nem nézi meg helyetted. Ha átvezetés nélkül szinkronizálsz, a drift-ellenőrzés elveszti az értelmét.

### Miért van egyáltalán két forrás?

Mert a két cél mérete különbözik. A skill-mappába telepített csomag igény szerint tölti be a `references/` fájlokat, ezért lehet benne teljes mintakatalógus, példák és ellenőrzőlista. A szabályfájlok viszont minden promptba bekerülnek, és a Windsurfnál kemény karakterkorlát is van. Egy automatikusan csonkolt változat pont a példákat veszítené el, amitől a szabályok használhatók — ezért a sűrítés kézi, és ezért kell hozzá a drift-ellenőrzés.

**Ha csak SKILL.md-t értő agentet használsz (Claude Code, Codex, Cursor), a `compact.md` és a `build.js` nem érint.**
