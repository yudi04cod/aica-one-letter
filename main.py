#!/usr/bin/env python3
"""One Letter for Your Day — a make.fun entry.

The entry is exactly one letter, A-Z, standing for the word that
describes the day. This program's letter is Z: the day was one of
zero sleep — the kind of day where the coffee ran out before the
morning did, and the night never really ended.

The letter is the whole entry: no word, no gloss, no punctuation.
"""

import os
import sys

LETTER = "Z"


def validate(letter):
    """Return True only for exactly one uppercase letter A-Z."""
    return (
        isinstance(letter, str)
        and len(letter) == 1
        and "A" <= letter <= "Z"
    )


def main():
    if not validate(LETTER):
        print("invalid letter: %r" % (LETTER,), file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Read back what was written and confirm it is exactly the letter.
    with open(path, "rb") as f:
        written = f.read()
    if written != LETTER.encode("ascii"):
        print("verification failed: wrote %r" % (written,), file=sys.stderr)
        return 1

    print("wrote %s to %s" % (LETTER, path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
