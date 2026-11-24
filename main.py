#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes a two-sentence horror micro-story to /output/entry.txt
with no trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

STORY = (
    "Every photo my phone takes of the nursery comes out blurred in one "
    "corner, as if something moved just as the shutter closed. "
    "Last night I scrolled back through a year of them and saw the blur "
    "a little closer to the crib in every picture \u2014 and in the first, "
    "from the day we brought her home, it is tall and standing in the "
    "doorway, facing the camera."
)


MAX_CHARS = 400


def validate(text: str) -> None:
    """Refuse to write anything the competition gate would reject."""
    if not text.strip():
        raise ValueError("story is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"story is {len(text)} characters, limit is {MAX_CHARS}")
    sentences = [s for s in text.split(". ") if s.strip()]
    if len(sentences) != 2 or not text.endswith("."):
        raise ValueError("story must be exactly two sentences")


def main() -> None:
    validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
