# Harness Initialization Planning Framework

## Purpose

Use this reference to produce a guided Harness initialization plan for any software project. It is abstract and must not depend on one specific product, company, repository, CI platform, browser tool, or deployment system.

The Harness model has four pillars:

1. Development process: how work moves from idea to release.
2. Documentation standards: where product, technical, plan, review, and testcase assets live.
3. Runtime evidence: how Log, DB, and Trace support debugging and verification.
4. Automated verification: how tests, gates, reports, and release checks prove correctness.

Mock system is a required cross-cutting capability inside automated verification and local runtime: every target Harness plan must address API mock, storage mock, fixture isolation, scenario switching, and reset evidence.

## Planning Only Rule

This skill produces a plan. It must not directly modify the project. The plan may name files that should be created or updated later, but it must clearly mark them as planned deliverables.

## Current-State Inventory

Inspect what exists, then classify each item as `Present`, `Partial`, `Missing`, or `Unknown`.

Check:

- Root AI rules: `AGENTS.md`, scoped agent rules, or equivalent.
- Docs structure: `docs/features`, `docs/testcases`, `docs/technical`, or project-specific alternatives.
- Product assets: requirements, PRD, demos, reviews, changelogs, progress records.
- Technical assets: architecture, standards, ADRs, runbooks, knowledge base.
- Local lifecycle: install, start, stop, status, logs, health checks, ports, env vars.
- Testing: unit, integration/API, E2E, smoke, regression, coverage, reports.
- Mock system: API mock, storage mock, scenario switching, fixture directories, reset/cleanup, smoke/check commands, and isolation from real backend/storage.
- Release: build, release gate, deploy, rollback, post-release verification.
- Runtime evidence: log location, DB connection or local file, trace/correlation IDs, report paths.
- Secrets policy: env files, credential sources, redaction rules, protected data boundaries.

## Guided Question Flow

Ask questions in batches. Do not ask the full bank at once.

### Batch 1: Scope and Target

Ask when not inferable:

1. Which project path is in scope?
2. Is the target a single app, monorepo, multi-service system, library, or platform?
3. Should the plan cover development only, release only, or the full idea-to-release lifecycle?
4. Which environments matter: local, test, staging, production?
5. Should the Harness be strict immediately or staged through governance baselines?

### Batch 2: Development Flow

Ask:

1. What is the standard current branch for design, bugfix, and Lite work, normally `develop`?
2. What branch naming rules are mandatory for Full feature branches created by `product-brainstorm` before writing `requirement.md`?
3. When the current branch is not the standard branch, what confirmation is required before writing?
4. Are local merges and pushes to protected branches allowed?
5. Which risk triggers justify optional worktrees for UI polish, parallel development, service isolation, or test isolation?
6. What must happen before a feature branch merges back?
7. What requires human approval?
8. What evidence must be recorded in progress or reports?

### Batch 3: Documentation

Ask:

1. Which product modules should organize long-lived testcases?
2. Which docs already exist and must be migrated?
3. Are historical docs mixed with knowledge/analysis docs?
4. Should feature docs follow `requirement -> demo -> prd -> technical -> spec -> testcases -> plan -> reviews`?
5. Which review records are mandatory?
6. Which global technical standards/runbooks are required before development can proceed?

### Batch 4: Local Runtime

Ask:

1. What commands install dependencies, start services, stop services, check status, and view logs?
2. Which services and ports must be healthy before tests run?
3. Which env files are required, and which values are secrets?
4. How should local test data be prepared and cleaned?
5. What is the expected failure evidence package when startup or E2E fails?

### Batch 5: Testing and Gates

Ask:

1. What test layers exist now: unit, integration/API, E2E, smoke, regression?
2. Which coverage thresholds are current hard gates?
3. Which targets are governance goals but not yet hard gates?
4. How are API endpoints inventoried and mapped to test scenarios?
5. How are new-feature E2E cases executed and reviewed?
6. How are long-lived regression cases automated?
7. Where do test reports, screenshots, videos, traces, and failure logs go?
8. Does login or protected data access require a standard credential source?

### Batch 5b: Mock System

Ask:

1. Which product APIs must support API mock for demo, E2E, regression, and human acceptance?
2. Which storage objects must storage mock simulate: files, object storage, permissions, cache, sessions, users, messages, tasks, history, or other state?
3. How should mock scenarios switch: environment variable, UI scenario switcher, test parameter, mock profile, or dedicated command?
4. Where should mock fixtures live, and what prevents secrets, tokens, production data, or protected personal data from entering them?
5. Must mock support streaming, tool calls, external provider failure, offline state, conflict state, or permission failures?
6. Which command or documented entrypoint can prove API mock and storage mock are both usable?

### Batch 6: Runtime Evidence

Ask:

1. Where are local and deployed logs?
2. What fields correlate a request, task, user action, job, or agent step?
3. How can an agent query or inspect DB state safely?
4. Which DB operations are read-only, mocked, or forbidden in tests?
5. What trace data exists for tool calls, agent calls, jobs, requests, or UI actions?
6. How should evidence be redacted before sharing?

### Batch 7: Release and Rollback

Ask:

1. What commands build and package release artifacts?
2. What release gates must pass before deployment?
3. Is deployment local, CI/CD driven, platform-driven, or manual?
4. What evidence proves release success?
5. What rollback path exists?
6. Are rollback scripts available, or is rollback manual?
7. Who must approve final release or production publication?

## Target Documentation Structure

Use this structure as the default target unless the project needs an explicit adaptation:

```text
docs/
  features/
    <feature-slug>/
      requirement.md
      prd.md
      demo/
        prototype.md
        assets/
      technical.md
      spec.md
      plan/
        plan-01-<workstream>.md
        plan-02-<workstream>.md
        integration-plan.md
      testcases.md
      reviews/
        demo-review.md
        prd-review.md
        technical-review.md
        spec-review.md
        plan-review.md
        testcase-review.md
      progress.md
      changelog.md

  testcases/
    README.md
    <product-module>/
      README.md
      e2e/
      acceptance/
      regression/
      fixtures/
      reports/

  technical/
    README.md
    architecture/
      overview.md
      module-map.md
      data-flow.md
    standards/
      coding.md
      testing.md
      frontend.md
      backend.md
      security.md
      mock-system.md
    decisions/
      ADR-0001-<title>.md
    runbooks/
      local-dev.md
      mock-system.md
      deploy.md
      rollback.md
      troubleshooting.md
    knowledge/
      glossary.md
      environments.md
      dependencies.md
      known-pitfalls.md
```

Rules:

- Feature-specific assets live under `docs/features/<feature-slug>/`.
- Long-lived testcases live under `docs/testcases/<product-module>/`.
- Feature `testcases.md` only indexes real testcase files.
- Global architecture, standards, decisions, runbooks, and stable knowledge live under `docs/technical/`.
- Review records must correspond to reviewed artifacts.
- Historical requirements should migrate to `docs/features/`.
- Pure knowledge or analysis should migrate to `docs/technical/knowledge/`.
- Mock system standards live under `docs/technical/standards/mock-system.md`.
- Mock system run commands, scenario switching, reset, and report inspection live under `docs/technical/runbooks/mock-system.md`.
- Reusable non-sensitive mock fixtures live under `docs/testcases/<product-module>/fixtures/`.

## Development Flow Model

Default lifecycle:

```text
product brainstorm
-> high-fidelity demo
-> demo review
-> PRD
-> PRD review
-> technical design
-> technical review
-> spec
-> spec review
-> testcases
-> testcase review
-> plan tree
-> plan review
-> TDD coding
-> local E2E verification
-> human acceptance
-> release verification
```

The plan should decide whether the project will adopt this full lifecycle immediately or in phases.

## Plan Tree Model

When planning implementation workflow, require:

- Each `plan-XX-<workstream>.md` represents an independent parallel workstream.
- Tasks that must be serial stay inside one plan.
- Each plan declares dependencies, ready criteria, current feature branch expectation, file map, affected files/modules, and allowed/forbidden change boundaries.
- `integration-plan.md` is the final join node and waits for all plan/task workstreams to be ready.
- Plan review must explicitly assess parallelization, serial constraints, and integration readiness.

## Automated Verification Model

Separate hard gates from governance targets.

Recommended layers:

- Unit: function/module behavior and coverage threshold.
- Integration/API: service and API behavior, DB or external boundary behavior.
- E2E: user-visible workflow validation.
- Mock smoke/check: proves API mock and storage mock can start, switch scenario, reset state, and produce diagnostics without real backend/storage.
- Smoke: fast environment health check.
- Regression: long-lived product-module regression suite.
- Release gate: required pre-release combination of tests, build, and evidence.

For each layer, define:

- command
- scope
- owner
- report path
- hard gate or governance target
- failure evidence requirement
- known gaps and migration plan

## Mock System Model

Require project facts for:

- API mock: covered API groups, response schema source, scenario switch, diagnostics, and drift detection.
- Storage mock: simulated storage objects, fixture source, reset/cleanup command, failure-state simulation, and isolation from real data.
- Fixture isolation: directory, redaction rule, source/update rule, sensitive-data scan, and large-file policy.
- Demo/prototype integration: how high-fidelity demo or prototype worktree consumes API mock and storage mock.
- E2E/regression integration: which tests use mock profiles and which must hit real services.
- Evidence: smoke/check command, report path, API mock status, storage mock status, reset status, and redaction status.

## Runtime Evidence Model

Require project facts for:

- Log: location, format, correlation fields, local view command, deployed query method, redaction.
- DB: local path or connection, schema source, read/write boundary, test data setup/cleanup, safe queries.
- Trace: ID generation, propagation, collection point, query path, link to logs and DB.

Runtime evidence must be usable during:

- local service startup failure
- automated test failure
- agent/tool or job failure
- release verification failure
- rollback analysis

## Release Verification Model

Require runbooks before declaring release readiness:

- `docs/technical/runbooks/deploy.md`
- `docs/technical/runbooks/rollback.md`
- `docs/technical/standards/testing.md`

The plan must state that release verification blocks if any are missing or unclear.

Release evidence should include:

- version
- commit
- build command and result
- artifact paths
- checksums when applicable
- upload or deployment result
- post-release verification result
- rollback entry point
- human approval status

## Status Model

Use one of:

- `Not Started`: no reliable artifact exists.
- `Partial`: artifact exists but lacks mandatory facts, gates, or evidence.
- `Planned`: decision made and work planned, not implemented.
- `Blocked`: cannot proceed without a user decision or external access.
- `Ready for Implementation`: plan is approved and inputs are sufficient.
- `Done`: only use if an artifact already exists and satisfies acceptance criteria.

## Phase Plan Template

Use this table shape:

| Phase | Status | Goal | Key Actions | Deliverables | Dependencies | Owner/Decision Needed | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- | --- | --- |

Recommended phases:

1. Baseline inventory and decision capture.
2. Development process and AI rules.
3. Documentation standards and migration plan.
4. Local service lifecycle runbook.
5. Mock System Baseline.
6. Automated verification and coverage gates.
7. Runtime evidence: Log, DB, Trace.
8. Release and rollback verification.
9. Governance backlog and rollout schedule.

`Mock System Baseline` deliverables must include API mock plan, storage mock plan, mock fixture standard, mock runbook, mock smoke/check command, mock report path, and demo/local-e2e/regression integration plan.

`Mock System Baseline` acceptance criteria:

- At least one API mock scenario can run.
- At least one storage mock scenario can reset.
- Mock does not access real backend, real cloud storage, real credentials, or production data.
- Mock fixtures contain no sensitive data.
- A command or documented step proves API mock and storage mock are both usable.

## Output Quality Bar

The final plan must:

- Distinguish known facts from assumptions.
- Mark unresolved decisions explicitly.
- Avoid claiming gates are enforced unless commands exist and are documented.
- Avoid turning governance targets into hard gates before they are executable.
- Include exact planned file paths, but not create them.
- Include acceptance criteria for every phase.
- Include a short immediate next step list.
