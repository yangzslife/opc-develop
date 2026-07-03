# Rubric: implementation contracts

You are reviewing the contract tree (`contracts/index.md` + `C-XX-*.md`) against
`formats/impl-contract-format.md`, the approved PRD, technical.md, and the mock inventory.
End with one `**Status:**` line and `Reviewed-SHA:` lines per reviewed file.

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
5. **TDD seeds actionable**: each task's seed names the test, the assertion, and a runnable
   command shape. "Write tests for X" is not a seed.
6. **Dependency order sound**: the index's dependency column is acyclic and the thin slice (when
   risk categories exist) is first with dependents ordered behind it.
7. **Internal design present**: module split, state handling, local component decisions are in the
   contract — an empty Internal Design section pushes design work onto the implementer, which is
   this layer's one job to prevent.
8. **Integration steps**: concrete, ordered, controller-runnable; not "integrate and test".

## Non-blocking

Contract naming, index formatting, seed verbosity.
