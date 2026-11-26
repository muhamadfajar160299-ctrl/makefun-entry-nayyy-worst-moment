"""Write the confession entry to the grader output directory.

Reads entry.txt shipped beside this script and copies its single line
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Standard library only; no network, no extra files.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
            text = f.read().strip()
    except OSError as exc:
        print("cannot read entry.txt: %s" % exc, file=sys.stderr)
        return 1
    if not text:
        print("entry.txt is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as exc:
        print("cannot write output: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
