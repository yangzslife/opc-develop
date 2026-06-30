# TDD Contract

No production code may be written for a task until a failing test has been written and observed to fail for the expected reason.

## TDD Test Scope

`tdd-coding` owns implementation-facing tests:

- Unit tests for pure logic, components, stores, services, adapters, and boundary conditions.
- API tests for changed or new product API endpoints, including success, invalid input, auth/config missing, and external failure scenarios when applicable.
- Focused service or integration tests only when project `AGENTS.md` or the approved plan requires them for implementation confidence.

`tdd-coding` must read approved black-box testcases as acceptance context, but must not execute black-box E2E, acceptance, or regression suites as its completion gate. Black-box execution belongs to `local-e2e-verify` and `release-verify`.

For UI-facing work, `tdd-coding` must also read approved demo context from the assigned plan/spec and use component, DOM, store, or focused integration tests where practical to protect demo-critical layout, state, and interaction behavior. Full runtime screenshot and black-box interaction parity still belongs to `local-e2e-verify`.

When the approved frontend prototype contains mocks, `tdd-coding` must also read the prototype mock inventory and `Prototype Mock Retirement Plan`. TDD seed must include implementation-facing tests that prove real backend/API/storage replacement behavior and prevent production runtime from continuing to use prototype mocks.

Each task must follow:

1. RED: derive the smallest useful failing unit/API/focused implementation-facing test from `spec.md` TDD seed and approved black-box testcase context.
2. Verify RED: run the focused command and confirm expected failure.
3. GREEN: write minimal implementation.
4. Verify GREEN: run the focused command and confirm pass.
5. REFACTOR: clean up only while tests stay green.
6. Record evidence in `progress.md`.

After all implementation and integration steps, run a final mock residual audit whenever prototype mocks existed. Evidence may include focused tests, static scans, changed-file inspection, runtime config checks, or project-specific mock audit commands. Do not claim completion if prototype mock files, flags, fixtures, imports, adapters, interceptors, route guards, store seeds, or component-local fake data still affect production runtime.

If production code was written before the failing test, delete it and restart the task from RED. Generated code and throwaway prototypes require explicit human exception in project artifacts.

Do not require `plan/*.md` to contain RED/GREEN commands. Plans provide boundaries and artifact references; `tdd-coding` derives concrete test commands from spec TDD seed, project testing standards, and local file ownership.

## Failure Debugging

When tests, API checks, E2E, local verification, or human acceptance fail for a pure implementation defect, use `debug-failure` discipline: reproduce first, identify root cause, add a failing test or minimal reproduction before fixing, then verify the fix with fresh evidence.

After three failed repair attempts for the same issue, stop and route back to technical/spec/plan or request human decision.
