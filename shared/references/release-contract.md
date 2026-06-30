# Release Contract

`release-verify` must read:

- `docs/technical/runbooks/deploy.md`
- `docs/technical/runbooks/rollback.md`
- `docs/technical/standards/testing.md`
- Final `progress.md`
- Latest testcase reports
- Optional `docs/features/<feature-slug>/human-acceptance.md` when it exists or when the project release runbook requires it

If deploy, rollback, or release gate instructions are missing, block instead of guessing.

Human acceptance is optional release context, not an opc-develop hard gate. Missing, Failed, or Blocked `human-acceptance.md` must be reported as risk context, but must not block release unless the project release runbook or explicit user instruction makes human acceptance mandatory. If human acceptance is Failed or Blocked and the user wants to fix it before release, run `acceptance-rework`.

Release verification owns post-release black-box smoke, automated acceptance, or regression checks required by deploy/testing runbooks.

Release evidence must include:

- Optional human acceptance status, report path, and risk summary when present.
- Release gate command and result.
- Version number.
- Commit SHA.
- Build or artifact path.
- Checksum.
- CI/CD link or release command output.
- Upload or registration result.
- Post-release automated acceptance result.
- Rollback entrypoint.

Do not claim release readiness, release success, or rollback readiness from intention, old logs, or subagent summaries. Every release claim must cite fresh evidence from the current release revision.
