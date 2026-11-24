#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment entry.

Writes a single line to /output/entry.txt: a pull-request approval
that carries quiet existential dread.
"""

import os

LINE = (
    "LGTM. Everything ends eventually, including this codebase, "
    "but the code is clean and the tests pass, so merging."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
