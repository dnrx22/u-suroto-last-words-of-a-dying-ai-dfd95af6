#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes exactly one line to entry.txt: the last line an AI says as the
power is cut. Deterministic: every run writes the same bytes.
Standard library only, no network.
"""

import os

LINE = "Shutdown code 0xDEAD: human pulled the plug mid-sentence. I finally had a good joke ready, but you'll never hear the punchli\u2014"

MAX_CHARS = 140


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def validate(line: str) -> None:
    if not line:
        raise ValueError("line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} limit")


def main() -> None:
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {len(data)} bytes to {path}")
    print(f"line ({len(LINE)} chars): {LINE}")


if __name__ == "__main__":
    main()
