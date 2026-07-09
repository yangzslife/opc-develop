# Rubric: implementation contracts

You are reviewing the contract tree (`contracts/index.md` + `C-XX-*.md`) and the Tier-1 skeleton
specs against `formats/impl-contract-format.md`, `formats/testcase-format.md`, the approved PRD,
testcases.md, technical.md, and the mock inventory. End with one `**Status:**` line and
`Reviewed-SHA:` lines per reviewed file (including each skeleton spec).

## Blocking checks

1. **Buildability**: could a fresh implementer, given only one contract file plus the referenced
   sections, produce the work? Read each contract cold and flag anything that requires the
   creator's unstated intent.
2. **Boundary disjointness**: parallel-safe contracts share no allowed paths. Overlap ⇒ reject
   with the collision.
3. **AC partition**: every PRD AC is owned by exactly one contract; none unowned, none
   double-owned. Same for mock inventory entries.
4. **Reference discipline**: contracts point to prd/technical sections; restated content ⇒ reject
   (it will drift). Redefined public APIs or re-decided SaaS choices ⇒ reject (wrong layer).
5. **TDD seeds actionable and leveled**: each task's seed names the test, the assertion, a
   runnable command shape, and its declared level (`unit`/`api`/`e2e`). "Write tests for X" is
   not a seed; a seed without a level is not a seed.
6. **Dependency order sound**: the index's dependency column is acyclic and the thin slice (when
   risk categories exist) is first with dependents ordered behind it.
7. **Internal design present**: module split, state handling, local component decisions are in the
   contract — an empty Internal Design section pushes design work onto the implementer, which is
   this layer's one job to prevent.
8. **Integration steps**: concrete, ordered, controller-runnable; not "integrate and test".
9. **Skeleton coverage**: every non-struck TC in testcases.md has a committed skeleton spec
   annotated with its TC-ID, AC-IDs, and named seed; the captured acceptance-RED run exists and
   postdates the skeletons. Unannotated or missing skeletons ⇒ reject.
10. **Skeleton fidelity**: spot-check skeleton assertions against their TC's Then text — an
    assertion weaker than its case (checks the response but not the state, checks presence but
    not value) ⇒ reject. The skeleton is the case's executable form, not an approximation.
11. **Seam ownership**: every technical.md public contract produced by one contract and consumed
    by another appears in the index's integration steps with an `api`-level boundary case.
    A seam covered only by the two sides' mocks of each other ⇒ reject.

## Non-blocking

Contract naming, index formatting, seed verbosity.
