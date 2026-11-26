#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks production:
a brutally honest confession, no hedging, no corporate euphemism.
"""

import os

LINE = (
    "I deleted the production database, watched 14,203 users vanish "
    "mid-checkout, and my only rollback plan is this apology."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts the file's characters.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
