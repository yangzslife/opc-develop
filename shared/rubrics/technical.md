# Rubric: technical.md

You are reviewing a technical design against `formats/technical-format.md`, the approved PRD, and
the project's existing architecture (inspect the codebase — do not take the document's word for
what exists). End with one `**Status:**` line and `Reviewed-SHA:` lines per reviewed file.

## Blocking checks

1. **One committed route**: exactly one design. Parallel "we could also" paths outside decision
   records' Options ⇒ reject.
2. **Decision records complete**: every contested choice (datastore, provider, queue, API shape,
   layering) is a numbered TD record with context/options/decision/consequences and a reversibility
   tag. Untagged irreversible choices are the highest-severity finding.
3. **Baseline compliance**: datastore/infrastructure choices match the project's existing baseline,
   or a TD record explicitly justifies divergence as [ONE-WAY]. Verify the baseline by inspecting
   the project, not the document.
4. **Public contracts fully specified**: every endpoint has request/response shapes and an error
   envelope; every schema change has a forward migration and a rollback note.
5. **AC coverage**: every PRD AC is implementable under this design; name any AC the design cannot
   satisfy.
6. **Runtime Evidence Plan present and concrete**: per AC-cluster, named log events with
   correlation IDs, DB assertions, or dump commands — written against the project's actual
   observability (check `packs/harness-verbs.md` L3). "We will add logging" is not a plan.
7. **Boundary discipline**: no internal module design, no TDD detail — that belongs to
   impl-contracts. Leakage downward is a defect, not thoroughness.
8. **Risk integration**: spike results referenced, thin slice designated when risk categories exist.
9. **Demo alignment**: the design supports the contractual demo interactions (data shapes, latency
   class, state visibility).

## Non-blocking

Capacity estimates, sequencing detail, appendix depth.
