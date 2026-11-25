"""Entry for make.fun bounty "The 3 AM Excuse".

One line in the voice of a grumpy old hardware wallet refusing to sign
a transaction at 3 AM. The twist lands on the last phrase: the wallet
itself was a 3 AM impulse buy, so it knows exactly how this ends.
"""

from pathlib import Path

LINE = "Denied. It's 3 AM, and your last 'genius trade' was a JPEG of a rock. Funny thing is, you bought me at 3 AM too."
ENTRY_PATH = Path("/output/entry.txt")


def ensure_parent(path):
    path.parent.mkdir(parents=True, exist_ok=True)


def write_entry(path, text):
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def main():
    assert 1 <= len(LINE) <= 199, f"entry must be 1-200 chars, got {len(LINE)}"
    write_entry(ENTRY_PATH, LINE)


if __name__ == "__main__":
    main()
