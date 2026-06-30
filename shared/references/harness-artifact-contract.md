# Harness Artifact Contract

All opc-develop skills must write project-specific artifacts inside the current project repository. Never write requirement-specific artifacts to ~/.codex, ~/.agents, plugin directories, plugin cache directories, or temporary directories outside the project repository.

`harness-doc.md` is the suite-level documentation convention for Harness layout, feature assets, global testcases, technical docs, reviews, progress, and changelog records. Design, development, review, verification, and branch/commit skills must follow it unless a stricter project `AGENTS.md` rule or this contract says otherwise.

Branch timing must follow `branch-stage-contract.md`: early product brainstorming may remain on the current branch, but `product-brainstorm` must create or enter `feature/<numbered-slug>` before writing `requirement.md`; `create-demo` and all later Full feature skills must run on the corresponding feature branch. Bugfix and Lite workflows remain current-branch workflows unless escalated.

## Resolve Project Root

1. Run `git rev-parse --show-toplevel`.
2. If it fails, use the current working directory only when it is clearly the intended project root.
3. Read the root `AGENTS.md` and any nested `AGENTS.md` that applies to the artifact or source paths.
4. Treat project `AGENTS.md` as binding for development flow, branch strategy, branch creation, acceptance flow, and gates.

## Canonical Layout

```text
docs/
  features/
    <feature-slug>/
      requirement.md
      prd.md
      demo/
        prototype.md
        assets/
      technical.md
      spec.md
      plan/
        plan-01-<workstream>.md
        plan-02-<workstream>.md
        integration-plan.md
      testcases.md
      reviews/
        demo-review.md
        prd-review.md
        technical-review.md
        spec-review.md
        plan-review.md
        testcase-review.md
      human-acceptance.md
      progress.md
      changelog.md
  testcases/
    <product-module>/
      e2e/
      acceptance/
      regression/
      fixtures/
      reports/
  technical/
    architecture/
    standards/
      testing.md
    decisions/
    runbooks/
      local-dev.md
      deploy.md
      rollback.md
      troubleshooting.md
    knowledge/
```

## Feature Slug

`<feature-slug>` is the feature directory name and must include an increasing numeric prefix:

```text
<number>-<feature-name>
```

Examples: `1-knowledge-base`, `105-web-search-prefer-native`.

Rules:

1. Use decimal integers only. Do not left-pad numbers with `0`.
2. Use lowercase hyphen-case for `<feature-name>`.
3. When creating a new feature, scan existing direct children of `docs/features/` whose names match `^[1-9][0-9]*-.+`.
4. Set the new number to the maximum existing numeric prefix plus 1. If there are no numbered feature directories, use `1`.
5. Ignore unnumbered legacy directories when calculating the next number.
6. Strip any user-provided numeric prefix from the proposed feature name before assigning the new number, unless the user explicitly points to an existing numbered feature directory to continue.
7. Record the full numbered slug in `requirement.md` and use the same slug for every downstream artifact path.
8. Do not create a new unnumbered feature directory. If an intended target is a pre-existing unnumbered legacy directory, stop and ask whether to migrate or continue that legacy path.

Use the stable numbered feature slug from `requirement.md` for downstream artifacts. If it is missing, derive it using these numbering rules before writing downstream artifacts.

## Review Files

Review outputs are fixed files, not numbered series. Overwrite the matching review file only when re-running that review gate after revising the upstream artifact.

Review freshness is part of the gate. A review file only approves the artifact revision that existed when the review was written. If `create-demo`, `create-prd`, `create-technical`, `create-spec`, `create-testcases`, or `create-plan` changes its artifact after the matching review file exists, the old review is stale and must not satisfy downstream gates. Re-run the matching `review-*` skill after every creator revision and continue only with a fresh Approved review.

For UI-facing features, `demo/prototype.md` is the canonical demo artifact. It records the running frontend prototype URL, changed frontend files, screenshots or recordings, restart commands, and prototype mock inventory. `demo/index.html` may exist only as an optional auxiliary snapshot; it is not a required gate artifact and must not replace the real frontend prototype.

## Progress

`progress.md` must record gate status, validation commands, evidence paths, blockers, and residual risk. It must not be a low-value activity log.

## Human Acceptance

`human-acceptance.md` records optional manual acceptance after local verification. It is not a `release-verify` hard gate unless the project release runbook explicitly requires it. Failed or blocked human acceptance should use `acceptance-rework` to record feedback and route work back to the earliest affected skill when the user wants to fix the acceptance issue.
