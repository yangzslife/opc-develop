# Black-Box Testcase Reviewer Prompt

Inputs: approved demo when UI-facing, prd.md, risk-spike.md when high-risk categories are present, spec.md, feature testcases.md, real docs/testcases files.

Check:

- Every PRD acceptance criterion maps to at least one real testcase.
- UI-facing testcases cover demo-critical layout, state, and interaction paths from the user boundary.
- E2E, acceptance, and regression coverage is appropriate and black-box.
- High-risk features have a thin vertical slice testcase that uses the normal product entrypoint when possible, real project boundaries, and explicit mock/seeded/local/external/human/long-run evidence expectations.
- Steps and expected results are executable.
- Automation entrypoints and failure diagnostics are present.
- Evidence authenticity expectations are present when a case can pass at different realism levels.
- Feature index paths point to real files.
- Testcases do not define unit tests, API implementation tests, mocks, white-box fixtures, TDD task commands, or internal code-level assertions.

Return `Issues Found` if the testcase set mixes black-box product cases with UT/API/TDD design, or if a high-risk feature reaches plan review without a thin-slice black-box testcase.
