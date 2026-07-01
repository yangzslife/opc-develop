# Black-Box Testcase Format

Real testcases live in `docs/testcases/<product-module>/`. Feature-local `testcases.md` is only an index to real testcase files.

`create-testcases` produces black-box product testcases only. These testcases describe externally observable behavior for local E2E, acceptance, regression, release smoke, or manual verification.

Do not use `create-testcases` to design unit tests, API tests, service integration tests, implementation test plans, mocks, fixtures for white-box tests, or TDD task commands. Those belong to `tdd-coding`, `create-plan`, and project test code.

## Product Module Layout

```text
docs/testcases/<product-module>/
  README.md
  e2e/
    TC-<module>-001-<title>.md
  acceptance/
    TC-<module>-A001-<title>.md
  regression/
    TC-<module>-R001-<title>.md
  fixtures/
  reports/
```

Each testcase must include:

- Case ID.
- Title.
- Product module.
- Type: E2E, Acceptance, or Regression.
- Related PRD acceptance criteria.
- Related approved demo state or interaction when the case covers UI behavior.
- Preconditions.
- Test data or fixtures.
- Steps.
- Expected result.
- Automation entrypoint or manual verification path.
- Failure diagnostics: screenshot/log/DB/trace hints.
- Evidence authenticity expectation when the case can run at different realism levels, such as mock, seeded, local real service, external provider, human, or long-run.

Each testcase must be executable from the user or system boundary. It may reference API calls only when the API is the product boundary under test; it must not become an internal handler/unit-test recipe.

`tdd-coding` must read these black-box testcases as acceptance context for designing unit tests and API tests, but must not execute black-box regression as its own completion gate.

For UI-facing features, black-box E2E and acceptance cases must cover demo-critical layout, state, and interaction paths. They should verify visible behavior from the user boundary, not internal component structure.

## Thin Slice Testcases

When `risk-and-readiness-contract.md` marks a feature as high risk, create at least one thin vertical slice testcase before `create-plan` proceeds.

The thin slice testcase must cover:

- normal product entrypoint when one exists;
- real route, state, API, storage, or shell boundary involved in the feature;
- provider, hardware, or external dependency handled through a project-approved mock/fixture or explicitly marked as real-environment pending;
- start action through visible or persisted user value;
- diagnostics that identify which boundary failed.

Do not turn the thin slice into a unit, API implementation, or white-box test recipe. It remains a black-box product testcase with explicit automation or manual execution path.

Do not store secrets, passwords, tokens, production private data, or customer data in fixtures.
