#!/usr/bin/env python3
"""Print the next numbered opc-develop feature slug."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NUMBERED_FEATURE_RE = re.compile(r"^([1-9][0-9]*)-(.+)$")
USER_PREFIX_RE = re.compile(r"^[0-9]+-(.+)$")


def normalize_feature_name(value: str) -> str:
    value = value.strip().lower()
    match = USER_PREFIX_RE.match(value)
    if match:
        value = match.group(1)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "feature"


def next_number(features_dir: Path) -> int:
    if not features_dir.exists():
        return 1

    maximum = 0
    for child in features_dir.iterdir():
        if not child.is_dir():
            continue
        match = NUMBERED_FEATURE_RE.match(child.name)
        if match:
            maximum = max(maximum, int(match.group(1)))
    return maximum + 1 if maximum else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("feature_name", help="candidate feature name or base slug")
    parser.add_argument(
        "--features-dir",
        default="docs/features",
        help="project features directory (default: docs/features under the cwd)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    feature_name = normalize_feature_name(args.feature_name)
    features_dir = Path(args.features_dir).expanduser()

    legacy_dir = features_dir / feature_name
    if legacy_dir.exists():
        print(
            f"ERROR: an unnumbered legacy feature directory exists: {legacy_dir}. "
            "Decide whether to migrate it or keep using it before creating a numbered feature.",
            file=sys.stderr,
        )
        return 1

    print(f"{next_number(features_dir)}-{feature_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
