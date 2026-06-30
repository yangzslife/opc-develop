#!/usr/bin/env python3
"""Parse an opc_develop review Markdown file and print its status."""

from __future__ import annotations

import re
import sys
from pathlib import Path


STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(Approved|Issues Found)\s*$", re.I | re.M)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: parse_review_status.py <review.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1]).expanduser()
    text = path.read_text(encoding="utf-8")
    matches = STATUS_RE.findall(text)
    if len(matches) != 1:
        print("expected exactly one status", file=sys.stderr)
        return 1

    status = matches[0]
    print("Approved" if status.lower() == "approved" else "Issues Found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
