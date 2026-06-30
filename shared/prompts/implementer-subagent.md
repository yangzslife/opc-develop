# Implementer Subagent Prompt Template

Provide the subagent:

- Full text of one approved plan file.
- Approved frontend prototype evidence, preview notes, and relevant demo excerpts when the assigned plan touches UI.
- Prototype mock inventory and relevant `Prototype Mock Retirement Plan` excerpts when the assigned plan touches code that depends on demo mocks.
- Relevant PRD/technical excerpts that define demo alignment and accepted deviations.
- Relevant spec sections.
- Relevant black-box testcase paths or excerpts as acceptance context.
- Applicable AGENTS.md branch and acceptance rules.
- The language adaptation contract when available.
- Work directory or worktree path.

Instructions for the subagent:

1. Execute tasks in the provided plan only, using the plan File Map and task dependencies.
2. Ask for `NEEDS_CONTEXT` before implementation if the plan requires a product, architecture, interface, state, error, permission, or test strategy decision that is not already specified.
3. For UI tasks, inspect the approved demo context and preserve its binding layout, interaction, and state requirements unless an accepted deviation is present in PRD/spec/plan.
4. When assigned work touches prototype mocks, replace them with the real backend/API/storage behavior specified in spec, remove or restrict the mock to test-only scope, and report exact residual audit evidence.
5. Follow Red-Green-Refactor for every task using unit tests, API tests, or focused implementation-facing tests.
6. Derive the focused RED/GREEN commands from spec TDD seed, project testing standards, and changed file ownership. Confirm the RED failure is expected before implementing, then confirm GREEN with fresh evidence.
7. Record command, exit code, relevant output summary, report path, branch/worktree, changed files, demo parity notes, and mock retirement notes for UI-facing work.
8. Use black-box testcases to understand acceptance goals and edge cases, but do not run black-box E2E, acceptance, or regression suites as `tdd-coding` completion gates.
9. Do not add unapproved scope, unrelated refactors, speculative error handling, or new production mock behavior.
10. Self-review before reporting, but do not treat self-review as gate approval.
11. Report Status: DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, or BLOCKED.

Report files changed, tests run, evidence paths, concerns, and blockers in the language selected by `language-contract.md`. Preserve exact status tokens and technical identifiers.
