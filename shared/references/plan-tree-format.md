# Plan Tree Format

`create-plan` must produce a plan tree under `docs/features/<feature-slug>/plan/`.

Plans are orchestration artifacts. They define how to split, order, and bound implementation work. They must not restate or invent technical details.

## Required Files

```text
plan-01-<workstream>.md
plan-02-<workstream>.md
integration-plan.md
```

Use as many `plan-XX-<workstream>.md` files as needed. Different plan files must be able to run in parallel. Work that must be serial must live in the same plan file as ordered tasks.

## Required Plan Header

Each plan file must declare:

- Applicable `AGENTS.md` path and rules summary.
- Branch expectation from project `AGENTS.md` and `branch-stage-contract.md`. Plans may reference the feature branch created by `product-brainstorm` before writing `requirement.md`, but must not introduce a new branch creation step.
- Acceptance entrypoint and acceptance pass criteria from project `AGENTS.md` or project docs.
- File Map: exact files or directories expected to change, with purpose and ownership notes. References may point to artifact sections or line ranges.
- Demo parity references for UI-facing work: approved demo path and referenced demo/PRD/spec sections; do not restate UI technical detail.
- Goal.
- Scope.
- Dependencies.
- Parallel-safe conditions.
- Ready standard.
- Risk and rollback notes.

## Task Format

Each task must include:

- Task ID.
- Goal.
- File Map entries used by this task.
- Referenced upstream artifacts: exact spec/demo/PRD/technical sections or line ranges needed by the implementer.
- Allowed change boundary.
- Forbidden change boundary.
- Development order notes.
- Dependencies on other tasks.
- Ready standard.

Plans must be intentionally indirect: they orchestrate work but do not contain technical implementation details. Do not put API schemas, error matrices, database design, component selection, algorithms, RED/GREEN commands, or concrete test cases in plan files. Those details belong in `technical.md` or `spec.md`.

Tasks must be executable by an implementer subagent by following the referenced approved artifacts, not by inventing extra design decisions. Use approved black-box testcases as acceptance context only; do not place black-box E2E, acceptance, or regression execution inside `tdd-coding` task gates. Avoid placeholder language such as TODO, similar to, add proper error handling, handle edge cases, write tests later, or implement appropriately.

For frontend tasks, plans must point to the approved demo and spec sections that define layout and interaction. Leave full runtime screenshot and black-box interaction parity to `local-e2e-verify`.

## Integration Plan

`integration-plan.md` must wait for every plan/task ready state. It must define integration or conflict handling, integration order, focused white/gray-box integration checks when needed, handoff to `local-e2e-verify`, failure rollback, and completion evidence. Do not make `tdd-coding` run black-box regression; local E2E and release black-box checks are later gates.

See `artifact-boundary-contract.md` for the full technical/spec/plan boundary.
