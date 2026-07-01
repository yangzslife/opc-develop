# Plan Reviewer Prompt

Inputs: approved frontend prototype evidence and mock inventory when UI-facing, prd.md, technical.md, risk-spike.md when high-risk categories are present, spec.md, testcases.md, plan/*.md, project AGENTS.md, project commands.

Check:

- Plan tree implements the complete spec without unrelated work.
- UI-facing plans preserve approved demo parity by pointing implementer subagents to concrete approved demo/spec/PRD references.
- When spec includes a `Prototype Mock Retirement Plan`, plans include explicit work boundaries for replacing/removing prototype mocks and final residual audit handoff.
- High-risk features reference `risk-spike.md`, thin-slice testcase coverage, capability readiness evidence, and expected evidence authenticity labels before broad implementation begins; unresolved readiness blockers are not bypassed.
- Parallel work is split into separate plan files.
- Serial work is kept inside the same plan with task dependencies.
- Every plan declares AGENTS.md rule source, current feature branch expectation, acceptance entrypoint, gate requirements, File Map, allowed change boundary, forbidden change boundary, dependencies, and referenced upstream artifacts.
- integration-plan.md waits for all ready states and defines integration/conflict handling and verification.
- Plan does not contain API schemas, error matrices, database design, component selection, algorithms, RED/GREEN commands, or concrete test cases.
- TDD seed and test strategy live in `spec.md`; plan only references relevant spec sections.
- Plans use approved black-box testcases as acceptance context, but do not put black-box E2E, acceptance, or regression suites inside `tdd-coding` task gates.
- Plans hand off runtime screenshot or interaction parity checks to `local-e2e-verify`.
- Tasks avoid placeholders such as TODO, similar to, add proper error handling, handle edge cases, write tests later, or implement appropriately.
- Buildability: an implementer subagent can execute each task by reading the referenced approved artifacts without making extra product, architecture, interface, state, error, permission, or test strategy decisions.

Return `Issues Found` when a plan carries technical detail that belongs in technical/spec, introduces new technical decisions, lacks boundaries/references, omits required mock retirement work, omits high-risk readiness or thin-slice handoff, is not executable from referenced artifacts, or when frontend tasks would require the implementer to infer the demo layout/interaction model.
