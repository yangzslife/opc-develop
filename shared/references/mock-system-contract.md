# Mock System Contract

Mock 系统是 Harness 的一等能力，不是 demo 或测试中的临时技巧。成熟项目必须同时具备 API mock 和 storage mock，用于高保真 demo、prototype worktree、local E2E、黑盒验收、回归测试和故障复现。

## API Mock

API mock must:

- Cover product APIs called by frontend or local clients.
- Match the public API input/output contracts defined in `technical.md`.
- Support scenario switching for success, loading, empty, permission denied, validation error, conflict, external failure, and offline states.
- Avoid real backend calls, real third-party services, real user data, production data, cookies, tokens, and credentials.
- Provide deterministic fixtures that can be reused by high-fidelity demos, local E2E, regression tests, and human acceptance.
- Emit readable diagnostics when a mock route, scenario, or payload is missing.

## Storage Mock

Storage mock must:

- Cover storage state required by frontend, local server, tools, or test harnesses.
- Support deterministic initialization, fixture loading, reset/cleanup, and failure-state simulation.
- Avoid reading or writing production data, real personal data, real tokens, real cloud storage, or real protected user files.
- Be able to simulate relevant storage objects such as file trees, object storage entries, local caches, permissions, conflicts, sessions, messages, task records, and history.
- Reset state between runs or provide an explicit cleanup contract.

## Isolation

Mock mode must be explicit and isolated:

- Use a clear switch such as `MOCK_MODE`, `DEMO_MODE`, mock profile, test flag, or dedicated command.
- Production default paths must not enable mock mode.
- Mock code, fixtures, reports, and generated data must be separated from production data and runtime state.
- Mock fixtures must contain no secrets, credentials, tokens, production personal data, or protected customer data.
- Any fixture derived from real data must be redacted and documented with source and update rules.

## Evidence

The project should provide at least one smoke/check entrypoint that proves both API mock and storage mock are usable.

Evidence should include:

- command or documented manual entrypoint
- mock profile or scenario name
- API mock status
- storage mock status
- reset/cleanup status
- report path such as `.dev/reports/mock-system/` or a project-specific Harness report path
- redaction status for diagnostics and fixtures

## Documentation Targets

Recommended stable project docs:

```text
docs/technical/standards/mock-system.md
docs/technical/runbooks/mock-system.md
docs/testcases/<product-module>/fixtures/
.dev/reports/mock-system/
```

`standards/mock-system.md` defines durable rules. `runbooks/mock-system.md` explains how to run, switch scenarios, reset state, and inspect reports. `fixtures/` stores reusable non-sensitive mock data. `.dev/reports/mock-system/` stores mock smoke, drift audit, and failure diagnostics.

## Relation To create-demo

High-fidelity demo and prototype flows should prefer established project mock conventions when they exist, but `create-demo` must keep new-feature backend simulation strictly frontend-only. Do not modify backend mock servers, API handlers, storage services, database schemas, migrations, or infrastructure during `create-demo`.

If a project lacks a suitable frontend mock mechanism, `create-demo` may add a narrow frontend-only adapter, fixture, store seed, interceptor, or demo-mode guard and must record it in the prototype mock inventory. It must not downgrade to a static concept demo unless the project has no runnable frontend or no documented local runtime; in that case it must report the blocker.
