#!/usr/bin/env python3
"""Entry point for news-image-20261122: THE WORLD, Sunday 22 November 2026.

Standard library only. Deterministic: the output is a byte-for-byte copy
of the image shipped in this repository, verified by sha256 after writing.
The image itself is drawn by render.py (Pillow + DejaVu fonts) from the
54 dated stories listed in README.md; re-running render.py reproduces
entry.png exactly.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print("entry.png is missing from the repository", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if sha256_of(src) != sha256_of(dst):
        print("copy verification failed: sha256 mismatch", file=sys.stderr)
        sys.exit(1)
    print(f"wrote {dst} sha256={sha256_of(dst)}")


if __name__ == "__main__":
    main()
