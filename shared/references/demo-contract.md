# Demo Contract

`create-demo` builds a high-fidelity frontend prototype in the real frontend codebase. It no longer creates a standalone static HTML demo as the primary artifact.

## Primary Output

The primary demo deliverable is working frontend code on the feature branch:

- Real frontend routes, components, stores, styles, and interactions.
- Real product shell integration when the product already has a usable shell, route, page, header, sidebar, input area, or workspace surface for the requested user flow.
- Frontend-only mock data flow for any backend capability that does not exist yet.
- Runtime preview evidence: local URL, commands, screenshots or recordings, and changed-file summary.
- Feature-local demo notes under `docs/features/<feature-slug>/demo/`, such as `prototype.md`, screenshots, and mock inventory.

`docs/features/<feature-slug>/demo/index.html` is optional and must not be used as a substitute for the real frontend prototype.

## Real Shell Primary Path

When the product has an existing frontend shell, the demo's primary user path must run inside that shell. A query-param-only alternate root app, standalone demo route, isolated mock page, or detached playground is not sufficient as the primary demo surface.

Required behavior:

- The intended production entry point is visible in the running UI at its intended location.
- The main feature state renders inside the existing product page, route, shell, layout, or component hierarchy.
- Existing navigation/header/sidebar/input/workspace surfaces are used when the requirement depends on them.
- The normal product URL or route exposes either the feature entry or a reviewer-visible mock state.
- Query params such as `?demo=<feature>` may seed mock data, select scenarios, or unlock reviewer states, but must not be the only way to see the feature when a real shell exists.
- Any secondary isolated preview must be labeled as secondary and cannot replace the shell-integrated primary demo.

If shell integration would require backend, database, Electron, or infrastructure changes, keep those capabilities mocked in frontend code. Do not bypass the real shell to avoid the integration work; stop and report a blocker only when the frontend/backend boundary is genuinely unclear.

## Fidelity Standard

The prototype must be at least 80% of the expected frontend experience:

- Main layout, navigation, information architecture, and visual hierarchy are implemented in the actual frontend.
- Existing product shell placement is implemented for user-facing entries, status surfaces, and exits.
- Core interactions and state transitions are clickable or otherwise visible in runtime.
- Happy path plus requirement-relevant empty, loading, error, permission, confirmation, and success states are represented.
- Mock data drives the same frontend data flow shape expected from the real backend.
- Remaining gaps are limited to backend integration, persistence, production auth, edge cases, or explicitly documented constraints.

If the agent cannot reach this fidelity without backend changes, stop and report the blocker instead of downgrading to a static concept demo.

## Frontend-Only Mock Rule

`create-demo` must not modify backend code, API handlers, database schemas, migrations, server jobs, infrastructure, or production storage logic.

Strictly do not modify backend code during `create-demo`.

When new backend data or behavior is needed for the demo, use frontend-only mocks:

- frontend fixtures
- frontend store seeds
- frontend adapter/interceptor/mock provider
- demo-mode route guard or query flag
- component-local fake data only when a narrower mock is enough

Mock mode must be explicit and reversible. Production default paths must not silently enable demo mocks.

## Runtime Preview

After every `create-demo` edit batch, restart local services using documented project commands:

1. stop or reset existing local services when the runbook requires it;
2. start backend and frontend services, or the documented combined local stack;
3. run status/health checks;
4. provide the user with the preview URL;
5. record commands, exit codes, URL, branch, and evidence paths in `progress.md` or `demo/prototype.md`.

Do not guess service commands. If the local-dev runbook cannot identify how to restart both frontend and backend, stop and report the missing Harness rule.

## Mock Inventory

Every frontend mock introduced or changed by `create-demo` must be recorded in `docs/features/<feature-slug>/demo/prototype.md`:

- file path
- mock type: fixture, adapter, store seed, route guard, interceptor, component-local data
- scenario names and visible states
- backend/API/storage behavior being simulated
- how the mock is enabled
- expected real replacement owner for `create-spec`

This inventory is mandatory input for `create-spec` and `tdd-coding`.

## Review Standard

`review-demo` must review the running frontend prototype, not just files. It must reject demos that:

- are only static HTML or screenshots when a real frontend exists;
- do not reach the 80% frontend fidelity standard;
- modify backend code;
- use real backend data for unavailable behavior instead of frontend-only mocks;
- lack runtime preview URL/evidence;
- lack a mock inventory for newly introduced demo mocks.

After `review-demo` is Approved, the frontend prototype is the binding product-experience reference for UI-facing work. Downstream skills must follow `demo-implementation-alignment.md` and `prototype-mock-retirement-contract.md`.
