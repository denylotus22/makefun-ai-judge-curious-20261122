#!/usr/bin/env python3
"""Write one short, curious text to /output/entry.txt.

The text is a quiet mystery: a book in the back of a library that no one
remembers buying, whose last page carries a line in the reader's own
handwriting, dated next spring - though the reader has never written in it.
"""

from pathlib import Path

ENTRY = (
    "In the back of the library there is a book no one remembers buying. "
    "Its last page is blank except for one line, in your handwriting, "
    "dated next spring. You have never written in it."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
