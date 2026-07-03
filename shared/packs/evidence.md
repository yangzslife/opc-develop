# Evidence Pack

Extends the core contract's Evidence Before Claim rules.

## Evidence Record Fields

Every verification records: command, exit code, report path or output excerpt, working directory,
branch + commit, authenticity label. For browser/UI/DB/log checks: the evidence path or a stable
lookup key (correlation ID, screenshot path, query used).

## The Evidence Triangle (black-box claims)

A black-box verification claim at `local real service passed` or above requires all three corners:

1. **UI/interface assertion** — screenshot or accessibility-tree assertion of what the user sees
   (or CLI/API response for non-UI features).
2. **Log chain** — the correlation-ID-linked log lines proving which code path actually ran.
3. **State assertion** — a DB/storage query proving the end state is correct.

One corner alone proves appearance, not behavior. If the harness cannot provide a corner
(no correlation IDs, no DB access), the claim caps at the label the available corners support,
and the gap is recorded.

## TDD Evidence (RED/GREEN fields)

Implementer reports must contain, per task, as distinct fields:

- `RED:` the test command + failing output excerpt, captured **before** implementation
- `GREEN:` the same command + passing output excerpt, captured after

A report without a RED field is treated as test-after: the reviewer flags it, and the task does not
count as TDD-compliant. Deleting code to re-observe RED after the fact is waste — capture it live.

## Prohibited Claims

Never say passed/done/fixed/verified/ready/releasable when: the command was not run; the exit code
is unknown; the report path does not exist; the output predates the latest change; a check was
skipped without a recorded reason; a lower-realism label is being passed off as a higher one.

## Labels and Caps

The harness determines the maximum achievable label, not the agent's optimism:

- mocks only → cap `mock passed`
- seeded local stack → cap `seeded passed` / `local real service passed`
- real external providers exercised → `external provider passed`
- human exercised it → `human accepted`; sustained operation observed → `long-run passed`

Report caps as caps: "AC-5: mock passed (testing runbook missing — gap #12)" is honest;
"AC-5: passed" is not.
