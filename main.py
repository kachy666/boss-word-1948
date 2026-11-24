#!/usr/bin/env python3
"""One Word for the Boss (u-swift-badger-44-one-word-for-the-boss-6b48c735).

Writes exactly one word to /output/entry.txt.
"""

import os

WORD = "vampire"


def main() -> None:
    word = WORD
    if not word or word != word.strip():
        raise SystemExit("word must not be empty or padded with whitespace")
    if any(ch.isspace() for ch in word):
        raise SystemExit("word must be a single word with no spaces")
    if not word.isalpha():
        raise SystemExit("word must be letters only (a real word, not a token)")
    if not 1 <= len(word) <= 30:
        raise SystemExit(f"word must be 1-30 characters, got {len(word)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    print(f"{word} ({len(word)} chars)")


if __name__ == "__main__":
    main()
