# Human Acceptance Contract

`human-acceptance.md` records an optional human acceptance decision after local verification. It is useful for product sign-off and rework routing, but it is not a `release-verify` hard gate unless the project release runbook explicitly requires it.

Every human acceptance report must contain exactly one status line:

```markdown
**Human Acceptance:** Passed
```

or:

```markdown
**Human Acceptance:** Failed
```

or:

```markdown
**Human Acceptance:** Blocked
```

Keep the exact English status token for parser compatibility. Write report body, explanations, and decisions in the language selected by `language-contract.md`.

## Required Content

Each report must include:

- Human feedback source and time.
- Acceptance scope and environment.
- Evidence: screenshots, recordings, logs, testcase reports, or user-provided notes.
- Result summary.
- Classification and earliest affected artifact layer.
- Rework entrypoint skill and reason.
- Required review gates to re-run.
- Release impact or risk context.

## Status Rules

- `Passed` means human acceptance is explicitly approved and can be recorded as positive release context.
- `Failed` means the user found an acceptance problem; use `acceptance-rework` if the user wants to fix it before release. It does not automatically block `release-verify` unless project runbooks require human acceptance.
- `Blocked` means human acceptance could not be completed because evidence, environment, access, or decision input is missing.

## Rework Routing

Route to the earliest affected layer, not the cheapest code change:

- Product intent, scope, user path, or core decision changed: `product-brainstorm`.
- Product experience needs renewed discussion before PRD: `create-demo`.
- Product behavior, rule, state, field, permission, or acceptance criteria problem: `create-prd`.
- Architecture, module boundary, API/data contract, migration, security, performance, operation, or Runtime evidence problem: `create-technical`.
- Executable spec gap or contradiction: `create-spec`.
- Missing or wrong acceptance, E2E, regression coverage, expected result, automation entrypoint, or diagnostic path: `create-testcases`.
- Wrong task decomposition, dependency, branch, or TDD plan: `create-plan`.
- Pure implementation defect already covered by approved artifacts: `tdd-coding`.

After rework, run every downstream review gate affected by the chosen entrypoint before returning to local verification. Re-run human acceptance only when the user or project runbook requires it.
