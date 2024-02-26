import json
import os
import subprocess
from typing import Any, Dict
import zlib


def convert_to_save(uesave_path: str, json_path: str, json_blob: Dict[str, Any]):
    sav_file = json_path[:-5]
    # Convert the file back to binary
    uesave_run = subprocess.run(
        uesave_from_json_params(uesave_path),
        capture_output=True,
        input=json.dumps(json_blob).encode("utf-8"),
    )
    print(uesave_run.stderr.decode("utf-8"))
    if uesave_run.returncode != 0:
        print(uesave_run.stdout.decode("utf-8"))
        raise Exception(
            f"uesave failed to convert {json_path} (return {uesave_run.returncode})"
        )
    if os.environ.get("DEBUG", "0") == "1":
        with open(json_path + ".sav", "wb") as f:
            f.write(uesave_run.stdout)
    # Open the old sav file to get type
    if os.path.exists(sav_file):
        with open(sav_file, "rb") as f:
            data = f.read()
            save_type = data[11]
    # If the sav file doesn't exist, use known heuristics
    else:
        # Largest files use double compression
        if "LocalData" in sav_file or "Level" in sav_file:
            save_type = 0x32
        else:
            save_type = 0x31

    data = uesave_run.stdout
    uncompressed_len = len(data)
    compressed_data = zlib.compress(data)
    compressed_len = len(compressed_data)
    if save_type == 0x32:
        compressed_data = zlib.compress(compressed_data)
    with open(sav_file, "wb") as f:
        f.write(uncompressed_len.to_bytes(4, byteorder="little"))
        f.write(compressed_len.to_bytes(4, byteorder="little"))
        f.write(b"PlZ")
        f.write(bytes([save_type]))
        f.write(bytes(compressed_data))
    print(f"Converted {json_path} to {sav_file}")


def uesave_from_json_params(uesave_path: str) -> list[str]:
    args = [
        uesave_path,
        "from-json",
        "--input",
        "-",
        "--output",
        "-",
    ]
    return args
