#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to the harness output file
(/output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt when set)
and prints it to stdout. Deterministic, no network, no input.
"""

import os

LINE = "Sorry, I ran garbage collection to go faster, and it collected the deadline."

MAX_CHARS = 160


def validate(line: str) -> None:
    """Gate: the judge only accepts 1-160 non-blank characters."""
    if not line.strip():
        raise SystemExit("entry is blank")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Local copy next to the program, handy for a quick eyeball check.
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
              "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
