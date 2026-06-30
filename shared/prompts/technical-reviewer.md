# Technical Reviewer Prompt

Inputs: requirement.md, demo, prd.md, technical.md, relevant code/docs.

Check:

- Technical design satisfies PRD and demo behavior.
- UI-facing technical design maps approved demo layout, interactions, and states to production modules, routes, components, and state owners.
- Exactly one technical route and one component selection are committed. Do not approve unresolved A/B/C options.
- SaaS / infrastructure components are explicitly owned here: MySQL, Redis, MQ, COS/object storage, external APIs, model providers, auth services, audit services.
- SaaS database decisions use MySQL, or the document blocks for human architecture decision.
- Public API input/output contracts are present: endpoint, method, request schema, response schema, status code, error code, auth/permission boundary, and external dependency failure semantics.
- Module boundaries, data impact, compatibility, migration, security, performance, and operations are addressed at architecture level.
- Runtime evidence plan covers Log, DB, and Trace.
- Technical design stays at architecture/public-contract level, leaving internal module placement, local components, state machines, and TDD seed to `spec.md`.
- High-impact unknowns are blockers.

Return `Issues Found` if technical leaves component choice open, omits API public I/O, hides SaaS decisions in spec/plan, chooses a non-MySQL SaaS database without explicit approved project constraint, or duplicates micro implementation details that belong in spec.
