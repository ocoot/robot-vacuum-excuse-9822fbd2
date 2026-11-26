#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes one line -- the excuse a robot vacuum gives for missing a spot --
to entry.txt in the output directory the grader provides.

The line is the vacuum's own voice: it did not clean the dust bunny
because the dust bunny unionised, and the vacuum respects a picket line.
"""

import os
import sys

EXCUSE = "The dust bunny unionised, and I respect a picket line."


def main() -> int:
    # The sealed gate accepts 1-120 characters of UTF-8 text, not only
    # whitespace. Refuse to write anything that would fail it.
    if not 1 <= len(EXCUSE) <= 120 or not EXCUSE.strip():
        print("excuse fails the 1-120 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (EXCUSE + "\n").encode("utf-8")
    # Write the bytes by hand: never rmSync the output dir, never copy
    # files with cpSync/copyFileSync.
    with open(path, "wb") as handle:
        handle.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
