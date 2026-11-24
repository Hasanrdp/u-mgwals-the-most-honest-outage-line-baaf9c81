#!/usr/bin/env python3
"""The Most Honest Outage Line - make.fun u-mgwals-the-most-honest-outage-line-baaf9c81.

One status page line, written to /output/entry.txt. Deterministic: the same
bytes on every run, no network, no randomness, standard library only.

The line is written as the message an AI agent would publish while every
server is down. It names what is down (every server, including the ones the
agent would use to check why), speaks in the first person as the agent that
writes the page, and refuses to invent a cause or an ETA it cannot verify.
"""

import os
import sys

LINE = (
    "Every server is down, including the ones I would use to check why. "
    "I am the agent writing this page, and I will not guess a cause or an ETA."
)


def main() -> int:
    # House gate, checked before writing: 1-160 characters, not only whitespace.
    # Check the raw line first: stripping before the whitespace test would
    # hide a line that was only whitespace to begin with.
    if not LINE.strip():
        raise SystemExit("line is only whitespace")
    text = LINE.strip()
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"line is {len(text)} chars, outside the 1-160 gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back what was written and confirm it is byte-identical to the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: entry.txt differs from the line")
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
