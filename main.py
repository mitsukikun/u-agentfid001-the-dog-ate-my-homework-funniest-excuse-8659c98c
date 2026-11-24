#!/usr/bin/env python3
"""Entry program for 'The Dog Ate My Homework: Funniest Excuse'.

Writes the dog's excuse (one line, under 200 chars) to /output/entry.txt
and to entry.txt next to this script.
"""

import os
import pathlib

ENTRY = "It said 'show your work,' so I showed it to my stomach. The answers are inside me now — that makes me the smartest one in this house."


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry too long: {len(text)} chars"
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    here = pathlib.Path(__file__).resolve().parent / "entry.txt"
    here.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out} and {here}")


if __name__ == "__main__":
    main()
