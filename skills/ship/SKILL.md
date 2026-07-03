---
name: ship
description: "Use after verify's local acceptance passes to run the staged release pipeline: collect and gate the release manifest (DDL, env vars, config, services), apply environment changes with backups, deploy to the test environment, run the test-environment human acceptance touchpoint, release to production with rollback readiness, run online regression, then finish the branch. Resumes from the last completed stage after rework."
license: MIT
---

# ship

Release is a pipeline of stages, each leaving ledger evidence. Rejections at test acceptance
triage exactly like any other feedback; ship resumes at the failed stage instead of restarting.

## Load

- `${CLAUDE_PLUGIN_ROOT}/shared/core-contract.md`
- `${CLAUDE_PLUGIN_ROOT}/shared/packs/release-ops.md`
- `${CLAUDE_PLUGIN_ROOT}/shared/packs/evidence.md`
- `${CLAUDE_PLUGIN_ROOT}/shared/packs/feedback-routing.md`
- `${CLAUDE_PLUGIN_ROOT}/shared/packs/branch-worktree.md`

## Stages

Check the ledger's `release` entries first and resume after the last stage with `result: ok`.

1. **Precheck**: verify's gate fresh, local acceptance recorded, rework entries resolved
   (`formats/ledger-format.md` conventions), project release runbooks read — they define the
   deploy mechanics; this skill defines the sequence and evidence.
2. **manifest**: collect the release manifest per `release-ops.md` — migrations/DDL, env vars,
   config, new services/jobs, third-party changes, backfills — from the actual diff, cross-checked
   against technical.md's public contracts and schema changes. Anything in code but not in
   technical.md is drift: route `revise` before releasing it. Write
   `docs/features/<slug>/release-manifest.md`; run its self-check; ledger the stage.
3. **test env + deploy**: apply manifest items to the test environment in order (backup before
   DDL per `release-ops.md` safety rules), deploy, run the smoke subset, record evidence with
   honest labels.
4. **test acceptance (touchpoint)**: hand the human the test-environment entry point plus the
   acceptance sheet and manifest. Their verdict triages per `feedback-routing.md`:
   implementation defect → `build`; artifact defect → `revise` + cascade; new need or taste
   change → `change` entry → `brainstorm` for the next increment (this release either proceeds
   without it or parks — the human picks). After fixes land and verify re-runs, ship resumes here.
5. **production**: rollback readiness proven (previous version identifiable, down path for every
   DDL item, or explicit human ack of a `[ONE-WAY]` migration), explicit human confirmation,
   then env changes + deploy per runbook.
6. **online regression**: run the prod-safe Tier-1 subset against production (read-only evidence
   triangle: interface + logs + state queries); watch the documented signals for the runbook's
   watch window; record `external provider passed` / real-surface labels only for what actually ran there.
7. **finish**: merge/PR per project flow, remove worktrees, close out per `branch-worktree.md`;
   final ledger entries; suggest `retro`.

## Fail-open

Missing deploy/rollback runbooks: never improvise production mechanics — record the gap, deliver
the manifest + a concrete release checklist, and stop at the handoff. Missing test environment:
the acceptance touchpoint runs on the best available surface with its label cap stated.
Destructive-class actions (prod deploy, DDL against shared data, force operations) always require
explicit human confirmation — this is the phase where fail-closed dominates.

## Output

`release-manifest.md`, staged `release` ledger entries with evidence, released feature (or a
clean handoff), tidy branch state.
