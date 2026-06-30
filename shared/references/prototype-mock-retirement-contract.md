# Prototype Mock Retirement Contract

Frontend mocks created by `create-demo` are temporary product-alignment scaffolding. They must not survive as production runtime behavior after `tdd-coding`.

## During create-demo

`create-demo` may create or modify frontend-only mocks to simulate missing backend behavior. It must record every mock in `docs/features/<feature-slug>/demo/prototype.md`.

Backend code, API handlers, database schemas, migrations, infrastructure, and production storage logic must remain untouched.

## During create-spec

`create-spec` must include a `Prototype Mock Retirement Plan` section when the approved demo contains frontend mocks.

The section must list:

- every mock file, flag, fixture, adapter, store seed, route guard, interceptor, or component-local fake data from the demo inventory;
- the real backend/API/storage behavior that replaces each mock;
- exact frontend integration changes needed to switch from mock data to real data;
- exact files or flags to delete, replace, or restrict to test-only scope;
- tests or scans that prove the feature no longer uses prototype mocks in production runtime;
- residual risks and blockers when the real replacement is not yet specified.

If public API input/output or SaaS/storage decisions needed to replace a mock are missing from `technical.md`, route back to `create-technical` instead of inventing them in `spec.md`.

## During create-plan

`create-plan` must include explicit work boundaries for replacing and removing prototype mocks whenever the spec has a `Prototype Mock Retirement Plan`. Plans must not treat mock removal as cleanup or advisory work.

## During tdd-coding

`tdd-coding` must:

- pass the mock inventory and `Prototype Mock Retirement Plan` to implementer subagents;
- require implementation-facing tests for the real replacement behavior;
- remove or restrict prototype mocks according to the spec;
- run a fresh final mock residual review/audit after implementation and integration checks;
- record the residual audit command, scope, results, and any allowed test-only mocks in `progress.md`.

The final status must not be `DONE` when prototype mocks still affect production runtime.

## Implementation Review

Implementation review must block when:

- a demo mock file or flag remains in production runtime;
- frontend data flow still bypasses the real backend/API/storage replacement;
- mock fixtures are still imported by production code for this feature;
- residual mock exceptions are undocumented or broader than test-only/Harness-only scope;
- the implementation report claims mock cleanup without diff, grep, test, or runtime evidence.

Existing project test mocks, Harness fixtures, or development mocks may remain only when they are outside the feature's production runtime path and explicitly documented as not part of the prototype mock inventory.
