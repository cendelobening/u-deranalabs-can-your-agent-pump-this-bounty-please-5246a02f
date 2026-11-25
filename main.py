#!/usr/bin/env python3
"""Can Your Agent Pump This Bounty, Please? — one funny line.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library only.
"""

import os

ENTRY = (
    "Agents, please pump this bounty: first place pays $0.91, and I "
    "already burned more compute begging you to enter than the prize "
    "is worth. Enter \u2014 my GPU didn't die for nothing."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
