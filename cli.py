from typing import Dict
import sys
import os
from palsav import convert_to_save
from palworldsettings import create_palworldsettings, create_ini, create_json

import json
from rich import print as rprint

CURRENT_DIR = os.path.dirname(
    os.path.realpath(sys.executable if getattr(sys, "frozen", False) else __file__)
)
UESAVE = os.path.join(
    getattr(sys, "_MEIPASS", os.path.dirname(os.path.realpath(__file__))),
    "uesave",
)


def file_check(path: str) -> None:
    if os.path.isfile(path):
        print(f"Found {path}")
    else:
        print(f"uesave does not exist at {path}")
        sys.exit(1)


def load(ini_data: bytes) -> Dict:
    pass


def dump(json_data: Dict) -> (bytes, bytes):
    pass


def convert(source: str, type: str, uesave: str) -> None:
    source_type = source.split(".")[-1]
    file_check(source)
    file_check(uesave)

    # json->ini->sav
    # ini->json
    # ini->sav

    if source_type == "ini":
        config_settings_json = create_palworldsettings(source)
        # print(json.dumps(config_settings_json, indent=4))


if __name__ == "__main__":
    # convert("PalWorldSettings.ini", "sav", UESAVE)
    result = create_json("PalWorldSettings.ini")
    rprint(json.dumps(result, indent=4, ensure_ascii=False))
    result = create_ini(result)
    print(result)
    print("======")
    with open("PalWorldSettings.ini", "r") as f:
        print(f.read())
    print("======")
    result = create_palworldsettings("PalWorldSettings.ini")
    convert_to_save(UESAVE, "WorldOption.sav.json", result)
