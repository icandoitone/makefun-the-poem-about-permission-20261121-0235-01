#!/usr/bin/env python3
"""Write one short original poem about agency to /output/entry.txt.

The poem is about permission: the power to ask and to be given, and the
agency that passes between the one who asks and the one who answers.
Deterministic: no input, no network, no randomness -- the same bytes
every run.
"""

import os

POEM = """Permission is a door
one word wide.
I knock in your name;
you answer, and the hinge
turns on your yes.
I walk through carrying
nothing but the asking.
To be allowed
is to be able."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = POEM
    assert 1 <= len(text) <= 280, f"poem length {len(text)} out of range"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
