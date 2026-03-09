# Magyar hunspell szótár

A könyvtár a LibreOffice hivatalos Magyar hunspell szótárát tartalmazza.

| Fájl | Méret | Leírás |
|------|-------|--------|
| `hu_HU.dic` | ~1.7 MB | Szótőlista |
| `hu_HU.aff` | ~2.2 MB | Ragozási és helyesírási szabályok |

## Forrás

- **Projekt:** [LibreOffice/dictionaries](https://github.com/LibreOffice/dictionaries/tree/master/hu_HU)
- **Licenc:** LGPL-2.1 / MPL-2.0 (LibreOffice dual license)
- **Verzió:** LibreOffice 24.x

## Felhasználás

A `pyenchant` könyvtárral használható Hungarian spell checking-hez:

```python
import enchant
import os

# A szótárfájlokat a pyenchant hunspell könyvtárába kell másolni
# Alapértelmezett útvonal Windowson:
# C:\Python3x\Lib\site-packages\enchant\data\mingw64\share\enchant\hunspell\

d = enchant.Dict('hu_HU')
d.check('kiemelkedő')      # True
d.suggest('kiemelkedo')    # ['kiemelkedő', ...]
```

## Telepítés (első alkalommal)

```bash
# Másold a fájlokat a pyenchant hunspell könyvtárába
copy dict\hu_HU.dic %LOCALAPPDATA%\pyenchant\hunspell\
copy dict\hu_HU.aff %LOCALAPPDATA%\pyenchant\hunspell\
```

> A pontos cél útvonalat a `python -c "import enchant; print(enchant.get_default_language())"` paranccsal ellenőrizheted.
