#!/usr/bin/env python3
"""Validate a project-local opc-develop feature artifact directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REVIEW_STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(Approved|Issues Found)\s*$", re.I | re.M)
HUMAN_ACCEPTANCE_RE = re.compile(r"^\*\*Human Acceptance:\*\*\s*(Passed|Failed|Blocked)\s*$", re.I | re.M)
PLACEHOLDER_RE = re.compile(
    r"\b(TBD|TODO|FIXME|fill in|implement later|write tests later)\b"
    r"|similar to|add proper error handling|handle edge cases|implement appropriately",
    re.I,
)
FORBIDDEN_PATH_RE = re.compile(r"(/Users/[^/\s]+/\.codex|/Users/[^/\s]+/\.agents|/Users/[^/\s]+/plugins|~/.codex|~/.agents|~/plugins)")
FEATURE_DIR_RE = re.compile(r"^[1-9][0-9]*-[a-z0-9][a-z0-9-]*$")

STAGE_REQUIREMENTS = {
    "requirement": ["requirement.md"],
    "demo": ["requirement.md", "demo/prototype.md", "reviews/demo-review.md"],
    "prd": ["requirement.md", "demo/prototype.md", "prd.md", "reviews/demo-review.md", "reviews/prd-review.md"],
    "technical": ["requirement.md", "demo/prototype.md", "prd.md", "technical.md", "reviews/demo-review.md", "reviews/prd-review.md", "reviews/technical-review.md"],
    "spec": ["requirement.md", "demo/prototype.md", "prd.md", "technical.md", "spec.md", "reviews/demo-review.md", "reviews/prd-review.md", "reviews/technical-review.md", "reviews/spec-review.md"],
    "testcases": ["demo/prototype.md", "prd.md", "technical.md", "spec.md", "testcases.md", "reviews/demo-review.md", "reviews/prd-review.md", "reviews/technical-review.md", "reviews/spec-review.md", "reviews/testcase-review.md"],
    "plan": ["demo/prototype.md", "prd.md", "technical.md", "spec.md", "testcases.md", "plan/integration-plan.md", "reviews/demo-review.md", "reviews/prd-review.md", "reviews/technical-review.md", "reviews/spec-review.md", "reviews/testcase-review.md", "reviews/plan-review.md"],
    "complete": ["requirement.md", "demo/prototype.md", "prd.md", "technical.md", "spec.md", "testcases.md", "progress.md", "plan/integration-plan.md", "reviews/demo-review.md", "reviews/prd-review.md", "reviews/technical-review.md", "reviews/spec-review.md", "reviews/testcase-review.md", "reviews/plan-review.md"],
    "acceptance": ["requirement.md", "demo/prototype.md", "prd.md", "technical.md", "spec.md", "testcases.md", "progress.md", "plan/integration-plan.md", "reviews/demo-review.md", "reviews/prd-review.md", "reviews/technical-review.md", "reviews/spec-review.md", "reviews/testcase-review.md", "reviews/plan-review.md", "human-acceptance.md"],
    "release": ["requirement.md", "demo/prototype.md", "prd.md", "technical.md", "spec.md", "testcases.md", "progress.md", "plan/integration-plan.md", "reviews/demo-review.md", "reviews/prd-review.md", "reviews/technical-review.md", "reviews/spec-review.md", "reviews/testcase-review.md", "reviews/plan-review.md"],
}

REVIEW_FRESHNESS = {
    "reviews/demo-review.md": ["demo"],
    "reviews/prd-review.md": ["prd.md"],
    "reviews/technical-review.md": ["technical.md"],
    "reviews/spec-review.md": ["spec.md"],
    "reviews/testcase-review.md": ["testcases.md"],
    "reviews/plan-review.md": ["plan"],
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def check_no_placeholders(path: Path) -> list[str]:
    errors: list[str] = []
    for md in sorted(path.rglob("*.md")):
        if md.name == "requirement.md":
            continue
        text = md.read_text(encoding="utf-8")
        if PLACEHOLDER_RE.search(text):
            errors.append(f"{md}: contains placeholder text")
        if FORBIDDEN_PATH_RE.search(text):
            errors.append(f"{md}: references a forbidden global artifact path")
    return errors


def check_reviews(path: Path) -> list[str]:
    errors: list[str] = []
    reviews = path / "reviews"
    if not reviews.exists():
        return errors
    for md in sorted(reviews.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        matches = REVIEW_STATUS_RE.findall(text)
        if len(matches) != 1:
            errors.append(f"{md}: expected exactly one '**Status:** Approved|Issues Found'")
    return errors


def artifact_files(path: Path, artifact_rels: list[str]) -> list[Path]:
    files: list[Path] = []
    for rel in artifact_rels:
        artifact = path / rel
        if artifact.is_file():
            files.append(artifact)
        elif artifact.is_dir():
            files.extend(sorted(child for child in artifact.rglob("*") if child.is_file()))
    return files


def check_review_freshness(path: Path) -> list[str]:
    errors: list[str] = []
    for review_rel, artifact_rels in REVIEW_FRESHNESS.items():
        review = path / review_rel
        if not review.exists():
            continue

        reviewed_files = artifact_files(path, artifact_rels)
        if not reviewed_files:
            continue

        newest_artifact = max(reviewed_files, key=lambda file: file.stat().st_mtime)
        if review.stat().st_mtime < newest_artifact.stat().st_mtime:
            errors.append(
                f"{review}: review is older than {newest_artifact.relative_to(path)}; "
                "rerun the matching review after the latest create/revision"
            )
    return errors


def check_human_acceptance(path: Path) -> list[str]:
    errors: list[str] = []
    report = path / "human-acceptance.md"
    if not report.exists():
        return errors
    text = report.read_text(encoding="utf-8")
    matches = HUMAN_ACCEPTANCE_RE.findall(text)
    if len(matches) != 1:
        errors.append(f"{report}: missing exactly one '**Human Acceptance:** Passed|Failed|Blocked'")
    return errors


def check_plan_tree(path: Path) -> list[str]:
    errors: list[str] = []
    plan_dir = path / "plan"
    if not plan_dir.exists():
        return errors
    plan_files = sorted(plan_dir.glob("plan-[0-9][0-9]-*.md"))
    if not plan_files:
        errors.append("missing plan/plan-XX-<workstream>.md")
    if not (plan_dir / "integration-plan.md").exists():
        errors.append("missing plan/integration-plan.md")
    for plan in plan_files:
        text = plan.read_text(encoding="utf-8")
        required_patterns = {
            "File Map": r"file map|文件地图",
            "Allowed change boundary": r"allowed change boundary|允许修改|允许变更|修改边界",
            "Forbidden change boundary": r"forbidden change boundary|禁止修改|禁止变更|禁止边界",
            "Referenced artifacts": r"referenced upstream artifacts|artifact references|引用.*(spec|demo|prd|technical|文档|工件)",
            "Ready standard": r"ready standard|完成标准|ready",
        }
        for label, pattern in required_patterns.items():
            if not re.search(pattern, text, re.I):
                errors.append(f"{plan}: missing {label}")
        forbidden_detail_patterns = {
            "API schema": r"request schema|response schema|请求 schema|响应 schema",
            "RED/GREEN commands": r"\bRED command\b|\bGREEN implementation\b|expected RED|expected pass signal",
        }
        for label, pattern in forbidden_detail_patterns.items():
            if re.search(pattern, text, re.I):
                errors.append(f"{plan}: contains {label} that belongs in technical/spec, not plan")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("feature_dir")
    parser.add_argument("--stage", choices=sorted(STAGE_REQUIREMENTS), default="complete")
    args = parser.parse_args()

    feature_dir = Path(args.feature_dir).expanduser().resolve()
    if not feature_dir.exists() or not feature_dir.is_dir():
        fail(f"{feature_dir} is not a directory")
        return 1

    errors: list[str] = []
    if not FEATURE_DIR_RE.match(feature_dir.name):
        errors.append(
            f"feature 目录名必须使用无前导零的 '<number>-<feature-name>' 格式：{feature_dir.name}"
        )

    for rel in STAGE_REQUIREMENTS[args.stage]:
        if not (feature_dir / rel).exists():
            errors.append(f"missing {rel}")

    if args.stage in {"plan", "complete"}:
        errors.extend(check_plan_tree(feature_dir))

    errors.extend(check_no_placeholders(feature_dir))
    errors.extend(check_reviews(feature_dir))
    errors.extend(check_review_freshness(feature_dir))
    errors.extend(check_human_acceptance(feature_dir))

    if errors:
        for error in errors:
            fail(error)
        return 1

    print(f"OK: {feature_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
