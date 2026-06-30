# Spec Format

`spec.md` translates approved PRD and approved technical design into executable micro technical contracts for AI implementers.

It must cover:

- Internal implementation boundaries: modules, services, adapters, stores, controllers, tools, and local components.
- API internal implementation contracts that implement the public API input/output already approved in `technical.md`.
- Function contracts, event contracts, tool contracts, or UI component contracts.
- UI/demo parity contracts for UI-facing work: layout regions, component responsibilities, interaction events, state rendering, responsive constraints, and accepted deviations from the approved demo.
- Prototype mock retirement for UI-facing work that used frontend-only mocks during `create-demo`.
- Local data models, field semantics, persistence rules, and compatibility constraints, including sqlite, local file storage, local caches, and in-memory state when relevant.
- State machines, state transitions, and key flows.
- Internal error handling, failure modes, empty states, permission failures, and external dependency failure mapping.
- Security and permissions.
- Rollout, rollback, and migration verification points.
- Observability and Runtime evidence points mapped to Log, DB, and Trace when relevant.
- Verification points mapped to PRD acceptance criteria and testcase coverage.
- TDD seed list: focused unit/API/implementation-facing test targets that `tdd-coding` can execute without inventing test strategy.

## Prototype Mock Retirement Plan

When `docs/features/<feature-slug>/demo/prototype.md` lists frontend mocks, `spec.md` must include a `Prototype Mock Retirement Plan` section.

For every mock, specify:

- mock inventory entry and file path;
- simulated backend/API/storage behavior;
- real implementation replacement;
- frontend integration change from mock to real data;
- exact file, import, flag, fixture, adapter, interceptor, route guard, or store seed to delete, replace, or restrict to test-only scope;
- unit/API/focused test seed proving the real behavior;
- residual audit command or scan pattern that `tdd-coding` must run;
- allowed exceptions, only for existing test-only or Harness-only mocks outside production runtime.

Do not leave "remove mock later" or "wire real API" as a plan placeholder. If replacement requires public API input/output, SaaS, or storage decisions missing from `technical.md`, stop and route back to `create-technical`.

## Boundary With Technical Design

`spec.md` defines what must be true for implementation, not why an architecture was selected.

Avoid repeating `technical.md` prose. A spec that mostly restates architecture, risks, and rationale without precise executable contracts is not implementation-ready and must not pass review.

Do not redefine public API input/output, SaaS components, or architecture choices already owned by `technical.md`. If they are missing upstream, stop and route back to `create-technical`.

## Implementation-Ready Standard

`create-plan` must be able to produce a boundary-only task tree from `spec.md` without inventing module placement, internal interfaces, states, errors, permissions, verification points, or TDD seed targets.

The spec must contain no TODO/TBD placeholders. Missing decisions must be listed as blocking questions.

For UI-facing features, a spec that omits the approved frontend prototype's layout, interaction requirements, or required mock retirement details is not implementation-ready, even if the API/data contracts are complete.

See `artifact-boundary-contract.md` for the full technical/spec/plan boundary.
