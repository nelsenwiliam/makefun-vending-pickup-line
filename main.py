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


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
