# Local Verification (build phase C)

Prove the feature black-box on the local stack before anything leaves the machine. Internal to
`build`. Gate rubric: `rubrics/e2e.md`.

## Local Deploy

- Bring the stack up per harness L1 (`run`); reset + seed per L2.
- Apply this feature's migrations/DDL and config changes to the local or shared dev database
  **per the safety rules in `release-ops.md`** (backup before DDL on shared data, expand →
  migrate → contract, destructive changes need human confirmation when data is shared). Record
  what was applied in the ledger — these entries seed the release manifest later.
- **Shared dev infra is a serialized resource across features**: before applying DDL/config to a
  shared database or environment, check other active features' ledgers for un-reverted env
  entries; two features mutating shared schema concurrently coordinate through the humans, not
  by racing. (Feature-internal parallelism is already isolated by worktrees; this rule is about
  two *features* building at once — the PM/architect duo case.)
- Missing verbs ⇒ record `gap` entries and note the label caps they force.

## Tier-1 First (skeletons → green)

- Run the full Tier-1 suite: the Phase A skeletons plus all pre-existing regression specs.
  Capture output and exit codes. The skeletons turning green is the feature's primary acceptance
  signal — they were written from the approved test cases before implementation existed.
- A skeleton that cannot go green without weakening its assertion is a triage, not an edit:
  implementation defect (fix the code) vs testcase artifact defect (`revise` to `prd`, stale
  cascade). Nobody edits a skeleton to make it pass.
- Per AC, assemble the evidence triangle: interface assertion, correlation-ID log chain, state
  assertion. Record per-AC `evidence` ledger entries with honest labels.

## Agentic Gap Hunt → Distillation

- With the cases green, drive the running app *beyond* them — browser tooling for UI, real
  requests for APIs: unlisted paths, hostile inputs, state left by one case entering another.
- Demo parity: exercise the contractual interactions from PRD Demo alignment; divergence is a
  finding — triage implementation defect vs artifact defect, don't assume.
- Distill every discovery that matters into an additional committed Tier-1 spec annotated with
  its AC-IDs, named seed, and an `explored` marker (it proves behavior the cases missed —
  candidate TCs for testcases.md next revision).

## Acceptance Sheet

Write `docs/features/<slug>/acceptance.md` — one line per AC: verdict, label, evidence pointer,
reproduction entry point; plus recorded gaps and their caps. Immutable after the gate; human
verdicts go to the ledger. The sheet travels with the feature: the human normally exercises it
on the test environment at `ship`'s acceptance touchpoint, not locally (a local spot-check is
welcome but not a gate).

## Gate

Fresh reviewer on `rubrics/e2e.md`: AC coverage, seed declarations, triangles, label honesty,
distillation, regression freshness. Computer-use style verification stays advisory; blocking
evidence is Tier-1 output.
