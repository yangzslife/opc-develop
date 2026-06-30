# Demo Reviewer Prompt

Inputs: requirement.md, frontend prototype diff or changed-file summary, demo/prototype.md, preview URL, service restart evidence, screenshots or recordings when available, mock inventory, visual references when available.

Check:

- Prototype covers the requirement intent and key user paths in the real frontend codebase.
- Runtime preview URL and service restart evidence are present; frontend and backend services were restarted through documented commands.
- Prototype reaches at least 80% frontend fidelity: layout, navigation, visual hierarchy, core interactions, data flow, and important states are usable or visible.
- Prototype covers important empty, loading, error, success, confirmation, and permission states.
- Frontend-only mocks simulate missing backend behavior; mock enablement is explicit and reversible.
- Mock inventory lists every fixture, adapter, interceptor, store seed, route guard, or component-local fake data introduced for the demo.
- No backend code, API handlers, database schemas, migrations, server jobs, infrastructure, or production storage logic were modified.
- Visual language is aligned with the target project or explicitly marked as neutral when no project style exists.

Return `Issues Found` when the demo is static-only despite an existing frontend, lacks preview evidence, changes backend code, lacks mock inventory, or falls short of the 80% frontend fidelity standard.
