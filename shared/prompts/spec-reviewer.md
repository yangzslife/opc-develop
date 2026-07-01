# Spec Reviewer Prompt

Inputs: requirement.md, approved frontend prototype evidence and mock inventory when UI-facing, approved prd.md, approved technical.md, risk-spike.md when high-risk categories are present, spec.md.

Check:

- Spec maps to PRD and technical design.
- For UI-facing work, spec preserves approved demo layout, interaction, state, responsive, and accepted-deviation requirements as executable UI/component contracts.
- Spec uses the public API input/output contracts from `technical.md` without redefining or changing them.
- Spec defines internal implementation contracts: module placement, code structure, local components such as sqlite/local storage/local cache, state, errors, failure modes, security, migration, rollout, rollback, and verification points.
- For high-risk features, spec converts approved runtime assumptions and capability readiness needs into executable internal contracts, focused test seeds, reset/cleanup expectations, and diagnostics without changing `technical.md` decisions.
- Spec includes acceptance mapping and TDD seed list sufficient for executable TDD planning.
- When the approved prototype contains frontend mocks, spec includes a complete `Prototype Mock Retirement Plan` that maps each mock to real replacement behavior, exact removal/restriction steps, and residual audit evidence.
- Spec does not repeat `technical.md` prose instead of defining executable contracts.
- Spec preserves the boundary: SaaS components and API public I/O stay in `technical.md`; micro implementation contracts live in `spec.md`.
- Spec contains no TODO/TBD and no hidden decisions.

Return `Issues Found` if the spec is mostly a rewritten technical design, changes API public I/O from technical, introduces SaaS components, lacks internal implementation contracts, drops demo-critical UI behavior, omits high-risk readiness contracts, omits prototype mock retirement details, allows production mock residuals, or requires `create-plan`/`tdd-coding` to invent missing design decisions.
