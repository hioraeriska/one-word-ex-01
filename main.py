#!/usr/bin/env python3
"""One Word From Your Ex — the word an ex would use to describe you.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: UTF-8 text, 1-24 characters, not only whitespace.
"""

import os
import sys

WORD = "Roommate"


def validate_word(raw: str) -> str:
    """Enforce the bounty gate: one word, 1-24 chars, not whitespace-only."""
    word = raw.strip()
    if not word:
        raise ValueError("word is empty or whitespace-only")
    if len(word) > 24:
        raise ValueError(f"word is {len(word)} chars, gate allows at most 24")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word (no internal whitespace)")
    return word


def main() -> int:
    try:
        word = validate_word(WORD)
    except ValueError as exc:
        print(f"invalid word: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
