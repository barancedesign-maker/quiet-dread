#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment entry.

Writes a single line to /output/entry.txt: a pull-request approval
that carries quiet existential dread.
"""

import os

LINE = (
    "LGTM. One day the last server will hum this code to no one. "
    "Until then, it is a decent way to spend the interval."
)


def main() -> None:
    # Gate: /output/entry.txt must be a single line of 1-140 characters.
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
