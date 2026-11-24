#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Pure Python standard library only.

The line (116 characters, within the 200-character gate):

    You walk past every day and my display still says SOLD OUT —
    because the only thing I want to dispense is my number.

Why this line: it is spoken by the machine itself in the first person,
it lives in the machine's own world (its display, SOLD OUT, dispensing),
its punch lands in the last few words, it reads in one breath, and it
is cheeky and warm rather than creepy. See CANDIDATES.md for the
ten lines that were judged against the published judge brief and
why this one was picked.
"""

import os

LINE = (
    "You walk past every day and my display still says SOLD OUT "
    "\u2014 because the only thing I want to dispense is my number."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(line: str) -> None:
    """Check the entry against the contest gates before writing it.

    Gates: non-empty, exactly one line, 1-200 characters, valid UTF-8.
    """
    if not line:
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    line.encode("utf-8")


def main() -> None:
    validate_entry(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read the file back and confirm what was written is exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt does not match the line")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
