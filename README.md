# Palworld Settings Option

## example

```python
from convert import load, dump

if __name__ == "__main__":

    # ini(str) -> JSON
    ini_data = ""
    with open("DefaultPalWorldSettings.ini", "r", encoding="utf-8") as f:
        ini_data = f.read()
    json_data = load(ini_data)

    # JSON -> ini(bytes) + sav(bytes)
    ini_bytes, sav_bytes = dump(json_data)
    with open("PalWorldSettings.ini", "wb") as f:
        f.write(ini_bytes)
    with open("WorldOption.sav", "wb") as f:
        f.write(sav_bytes)
```

## Download uesave(.exe)

[https://github.com/trumank/uesave-rs/releases](https://github.com/trumank/uesave-rs/releases)

### ENV

```
UESAVE_PATH=/path/to/downloaded/uesave(.exe)
```
