# Contracting (build phase A)

Partition the approved PRD + technical design into implementation contracts, then turn the
approved test cases into failing acceptance skeletons. Internal to `build` — not a user-facing
phase. Formats: `formats/impl-contract-format.md`, `formats/testcase-format.md`; gate rubric:
`rubrics/impl-contract.md`.

## Partition Rules

- Every PRD AC owned by exactly one contract; every mock inventory entry owned by exactly one.
- Parallel-safe contracts share no allowed paths — overlap is a gate-blocking defect; merge or
  serialize instead of shipping a known collision.
- Thin slice first when risk categories exist; everything risky depends on it.
- Prefer fewer, fuller contracts over many thin ones — dispatch overhead is real.

## Content Rules

- Each `C-XX-<name>.md`: boundary globs, AC references (never restated text), internal design
  (module split, state handling, local component decisions — the detail technical.md deliberately
  excludes), TDD seeds concrete enough to start RED, mock retirement assignments, done-means
  checklist.
- Every TDD seed declares its level — `unit`, `api`, or `e2e`. An undeclared level defaults to
  unit in the implementer's hands, which is exactly how interfaces go untested.
- **Cross-contract seams are owned**: when a public contract from technical.md is produced by one
  contract and consumed by another, the index names ≥1 `api`-level boundary case (a TC or an
  added skeleton) that exercises the real interface. The seam between two contracts is never left
  to their private mocks of each other.
- `index.md`: dependency table (acyclic), parallel-safety column, thin slice, ordered integration
  steps the controller will run — each boundary case listed in the step that runs it.
- Contracts point to prd/technical sections; restated content drifts and is rejected. No public
  API redefinition, no SaaS re-decisions — wrong layer.

## Tier-1 Skeletons (acceptance first)

Before any implementer is dispatched, translate every non-struck TC in testcases.md into a
committed **failing** Tier-1 spec skeleton in the project's spec location (harness L4):

- One skeleton per TC, annotated with its TC-ID, the AC-IDs it proves, and its named seed.
  Assertions come from the TC's Then text — the case is the source of truth, the skeleton its
  executable form.
- Run the suite once and capture the failing output as **acceptance RED** evidence — the
  black-box counterpart of the task-level RED the implementers will capture.
- Skeletons are fixed once gated: implementation makes them pass; nobody weakens an assertion to
  make one pass. A skeleton that appears wrong means the TC is wrong — route `revise` to `prd`,
  stale cascade applies.
- Missing harness capability (no runner, no seed) ⇒ record the `gap`, write the skeleton as far
  as it can execute, and note the label cap it forces.

## Gate

L0 precheck every file (`validate_artifacts.py <contract-file> --prd <prd-path>`), then one fresh
reviewer on `rubrics/impl-contract.md` reading the contracts **and the skeletons** cold —
buildability by a stranger is the bar, and skeleton↔TC fidelity is part of it. Fix and re-gate
until Approved; ledger rounds. Questions the artifacts can't answer route `revise` upstream;
never paper over gaps with invented design that contradicts technical.md.

## Staleness

Contracts are stale when the PRD or technical.md revisions moved past the contract gate's
`Reviewed-SHA`; skeletons are additionally stale when testcases.md moved. `build` re-runs this
phase automatically on staleness; unaffected contracts are confirmed by targeted re-review, not
rewritten.
