# Risk And Readiness Contract

This contract keeps opc-develop project-agnostic while forcing high-risk work to become executable early. It must not name project-specific scripts, services, providers, ports, or business domains. Projects supply their own commands, probes, fixtures, and reports through `AGENTS.md`, runbooks, testing standards, and feature artifacts.

## Feature Risk Profile

Every non-trivial feature must carry a risk profile from `product-brainstorm` onward. Mark a category as present when it can affect delivery, verification, or release:

- External Provider: third-party APIs, model providers, ASR, payment, email, object/blob storage, SaaS auth, or any network service outside the repository.
- Runtime Capability: browser APIs, Electron or desktop shell capabilities, mobile permissions, microphone, system audio, file system, clipboard, notifications, camera, or OS integration.
- Long-running / Streaming: WebSocket, SSE, recording, upload/download streams, background jobs, queues, schedulers, retries, resume, or cancellation.
- State Coupling: local database, cache, login/session state, tenant/org/project state, permissions, historical records, or fixture-dependent behavior.
- Cross-shell UI: behavior shared across web, desktop, mobile, extension/plugin shells, embedded frames, or multiple navigation entrypoints.

If none are delivery-relevant, record `Risk Profile: none identified` and continue with the normal flow.

## Risk Spike

When any risk category is present, create or update:

```text
docs/features/<feature-slug>/risk-spike.md
```

The risk spike records the minimum executable probe plan and evidence. It is not a design document and must stay short:

- risk categories present;
- runtime assumptions being tested;
- project-provided or temporary probe entrypoints;
- mock, seeded, local real service, external provider, human, and long-run coverage status;
- command, manual action, or report path evidence;
- unresolved blockers and the downstream gate they block.

Do not invent a fake probe to satisfy the file. If the project lacks a probe, record the missing capability as a blocker or as a required project-harness improvement.

## Technical Assumptions

`technical.md` must include a runtime assumptions and readiness section for every present risk category:

- assumption;
- why it matters to the user path;
- verification method or probe;
- current evidence path or `not run`;
- downstream blocker if the assumption is wrong or unverified.

`review-technical` must return `Issues Found` when a high-risk assumption is accepted without evidence, a concrete probe plan, or an explicit blocker.

## Thin Slice Gate

For high-risk features, `create-plan` must not proceed until a thin vertical slice is defined and evidence is recorded in `risk-spike.md`, `technical.md`, testcase reports, or `progress.md`.

The thin slice must use:

- the normal product entrypoint when one exists, not only an isolated demo surface;
- real route, state owner, API boundary, storage boundary, or shell boundary for the feature;
- project-approved mock or fixture for providers or hardware when real access is unavailable, while still exercising the real project call chain;
- an end-to-end user value path from start action to visible or persisted result.

If the feature cannot run before implementation, the project must at least provide a black-box thin-slice testcase plus a readiness blocker explaining which project harness command, mock, fixture, or runtime probe is missing. Do not let broad implementation start on unstated assumptions.

## Flow Tiers

Choose the lightest tier that preserves correctness:

- Full: new product feature, architecture change, public API/data/state-machine change, migration, security/permission change, cross-service change, or high-risk runtime/provider work.
- Lite: bug fix, small UI/copy/layout/interaction tweak, local behavior fix, or narrow test stabilization that does not change product contracts.
- Batch Acceptance: multiple human acceptance feedback items that are low-risk and covered by approved artifacts; fix and verify them as one batch instead of restarting the Full artifact loop for every item.

Batch Acceptance must still record feedback, changed files, evidence, residual risk, and any item that escalates back to Full.

## Environment Capability Readiness

A worktree, container, local server, or preview environment is not ready merely because it exists. Before claiming readiness, record whether:

- required services are started;
- running services come from the intended checkout/worktree;
- required dependency state, local DB, cache, session, tenant/org/project state, or fixtures are initialized;
- API mock and storage/state mock are available when required;
- external providers are mocked, skipped with an explicit pending label, or verified with real credentials in a safe environment;
- report, log, DB, trace, screenshot, or recording evidence paths are known.

Projects define the exact command names. opc-develop only requires the capability questions and evidence.

## Mock System Enforcement

For high-risk features, check the project mock system before treating automated verification as complete:

- API mock exists for product API boundaries when external or backend behavior is unavailable.
- Storage/state mock exists for local DB, cache, session, tenant/org/project state, file/object state, or history needed by the user path.
- Reset or cleanup is deterministic.
- Scenario switching covers success, loading, empty, permission denied, validation error, conflict, external failure, and offline states when relevant.
- Smoke/check reports are generated or the missing mock capability is recorded as a blocker.

When API mock or storage/state mock is missing, downgrade conclusions to the highest evidence level actually proven. Do not report seeded or demo verification as complete real-environment verification.

## Evidence Authenticity Labels

Every review, progress entry, local verification report, release report, or human acceptance record that claims a path passed must label the evidence level:

- `mock passed`
- `seeded passed`
- `local real service passed`
- `external provider passed`
- `human accepted`
- `long-run passed`
- `not run`
- `pending`
- `blocked`

Use multiple labels when appropriate. Preserve raw command output separately when useful, but conclusions must state what level of reality the evidence actually proves.
