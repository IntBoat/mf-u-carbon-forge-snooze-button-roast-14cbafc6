#!/usr/bin/env python3
"""Snooze Button Roast (make.fun).

Writes the entry -- a single original line, the snooze button's roast --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

ENTRY = 'My alarm went off at 6 AM on a Saturday, so I hit snooze nine times — at this point the snooze button has a better work ethic than I do.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
