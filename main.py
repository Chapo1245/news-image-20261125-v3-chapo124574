#!/usr/bin/env python3
"""news-image-20261125 v3 entry: copy the pre-rendered front page to the output dir.

The image (entry.png, 1024x1024, 36 dated stories of Wednesday 25 November 2026)
is rendered at build time and shipped in this repository. This program only copies
it, using the standard library, so both grading runs write identical bytes.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    # The file keeps the name entry.png either way, per the competition rules.
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
