"""The Robot Pickup Line Championship — entry program.

Writes a single pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt. Deterministic: the same line every run.
Standard library only.
"""

import os

LINE = "I passed my Turing test today \u2014 the examiner said no machine could blush that hard around you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate checks, applied before anything is written.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    # Create the output directory only; never delete anything under /output.
    os.makedirs("/output", exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Verify the round-trip: exactly the line, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written output differs from the line"


if __name__ == "__main__":
    main()
