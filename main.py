#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt. The word is chosen once,
deterministically, and validated against the competition gate before it
is written: UTF-8 text of 1 to 111 characters, not only white space,
exactly one word.

The word: "Recalled".

Why this word: it is a one-word verdict on a former partner that lands
as a joke at a glance. "Recalled" reads two ways at once — an ex
remembered, and a faulty product pulled back by the manufacturer.
That double meaning is the twist: the ex was not a tragedy, just a
defective unit the factory took back. It is spelled correctly, needs
no punctuation trick and no caption, and anyone who has had an ex
recognises both readings instantly.
"""

import os
import sys

# The entry: one word describing an ex.
WORD = "Recalled"

# Where the harness expects the entry text.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(word: str) -> str:
    """Check the word against the competition gate."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not (1 <= len(word) <= 111):
        raise ValueError("entry must be 1 to 111 characters")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must contain no white space")
    return word


def main() -> int:
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
