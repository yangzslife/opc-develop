# Implementation Contract Format

Path: `docs/features/<slug>/contracts/` — one `C-XX-<name>.md` per independently implementable
workstream plus one `index.md`. This layer merges the old spec + plan: each contract is a complete,
self-sufficient work order for one implementer subagent.

## index.md

```
# Contracts: <feature>

| id | name | depends on | parallel-safe | ACs owned | mocks owned |
|----|------|-----------|---------------|-----------|-------------|
| C-01 | export-api | — | yes | AC-1..3 | M-1 |
...

Thin slice: C-01                      (mandatory when risk categories exist)
Integration steps:                    ordered controller-run steps after all contracts complete
```

## C-XX-<name>.md

```
# C-XX: <name>

## Boundary
Allowed paths:                        globs the implementer may change
Forbidden paths:                      globs it must not touch
ACs owned:                            AC-IDs this contract proves (reference, don't restate)
References:                           prd.md#section, technical.md#TD-n — pointers, not copies

## Internal Design
                                      module split, state handling, local storage/cache decisions,
                                      internal error handling — the executable micro-detail that
                                      technical.md deliberately leaves out

## TDD Seed
                                      per task: test name, what it asserts, suggested command —
                                      enough for the implementer to start RED without inventing
                                      the test strategy

## Mock Retirement
                                      inventory entries (M-x) this contract retires, and how

## Done Means
                                      per-task completion checklist: RED/GREEN evidence, tests
                                      green, boundary respected, mocks retired, report filed
```

## Rules

- Different contracts must be independently implementable; shared-file overlap between
  parallel-safe contracts is a gate-blocking defect.
- Contracts reference upstream artifacts by section pointer; a contract that restates PRD or
  technical content will drift and is rejected at the gate.
- No public API redefinition, no SaaS re-decisions — that is technical.md's territory.
- Every mock in the inventory appears in exactly one contract's Mock Retirement section.
