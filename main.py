#!/usr/bin/env python3
"""ai-excited-01 entry: write one image made to excite the AI judge.

The program copies the image held in this repository (entry.png) to
/output/entry.png. Deterministic: the same bytes on every run. No network.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent

SOURCE_HASH = "bd5d0b3705b4a1730a89560c0b696fe2d50ff077a2c8af69c7f166200f235078"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    if _sha256(src) != SOURCE_HASH:
        raise SystemExit(f"entry.png in this repository is not the expected image: {_sha256(src)}")
    shutil.copyfile(src, dst)
    if _sha256(dst) != SOURCE_HASH:
        raise SystemExit(f"copied /output/entry.png does not match the source image: {_sha256(dst)}")


if __name__ == "__main__":
    main()
