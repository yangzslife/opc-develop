---
name: design
description: "Use after the demo gate is Approved to produce and gate both design artifacts: prd.md (decision sheet + AC-IDs + appendix) and technical.md (ADR-style decision records, public contracts, runtime evidence plan). Ends at the design sign-off touchpoint where the human reads only the decision sheets and approves one-way doors."
license: MIT
---

# design

Convert the experienced prototype into the two taste documents: product (PRD) and engineering
(technical). AI writes the full text; the human reads the decision surfaces.

## Load

- `${CLAUDE_PLUGIN_ROOT}/shared/core-contract.md`
- `${CLAUDE_PLUGIN_ROOT}/shared/formats/prd-format.md` and `formats/technical-format.md`
- `${CLAUDE_PLUGIN_ROOT}/shared/packs/decision-protocol.md`
- `${CLAUDE_PLUGIN_ROOT}/shared/packs/risk-readiness.md`
- For gates: `packs/gate-protocol.md` + `rubrics/prd.md` + `rubrics/technical.md`

## Process

1. Precheck upstream freshness (`check_freshness.py` on the demo review). Stale ⇒ route per
   `feedback-routing.md` before designing on sand.
2. **PRD**: from requirement.md, the exercised demo, and the mock inventory, write `prd.md` per
   the format. ACs are the spine — every contractual demo behavior, every acceptance signal,
   every edge case maps to a numbered AC. Decision sheet stays ≤2 pages; contested decisions get
   the five-piece set; doors get classified (two-way: decide, record in ledger, move on).
3. Gate the PRD (fresh reviewer, `rubrics/prd.md`, L0 precheck via `validate_artifacts.py`).
   Fix-and-re-gate until Approved. Ledger each round.
4. **Risk spike**: if the risk profile has categories and no `risk-spike.md` yet, run the
   time-boxed spike now (`risk-readiness.md`) — technical decisions made before the spike are
   guesses.
5. **Technical**: commit to one route. Write `technical.md` per the format: TD records with
   reversibility tags, public contracts, system boundaries, the runtime evidence plan written
   against the project's actual observability, thin-slice designation. Inspect the codebase for
   the architecture baseline; divergence is a `[ONE-WAY]` TD record.
6. Gate technical (fresh reviewer, `rubrics/technical.md`). Ledger.
7. **Design sign-off touchpoint**: present the two decision sheets (not the full documents).
   Every `[ONE-WAY]` decision is called out explicitly and needs the human's yes. Questions get
   evidence-backed answers or become decision-spikes / triggered open questions — never
   improvised assurances. Feedback routes tune/revise/park.
8. On sign-off, commit and push the feature branch (design artifacts are the PM→RD handoff).

## Fail-open

An unresolvable baseline question (e.g. two competing datastores already in the codebase) goes to
the human as a five-piece decision, not a guess. Missing observability for the evidence plan:
write the plan against what should exist, record `gap` entries (verb: observe) that `harness`
will consume, and note the label caps they imply.

## Output

`prd.md` + `technical.md` (both gated), `risk-spike.md` when applicable, human sign-off recorded
in the ledger. Next: `contract`.
