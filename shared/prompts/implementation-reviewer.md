# Implementation Review Subagent Prompt Template

Purpose: review a completed implementation plan in isolated subagents while reducing unnecessary review.

Inputs:

- Assigned plan text.
- Approved demo path or excerpts when the implementation touches UI.
- Prototype mock inventory and `Prototype Mock Retirement Plan` excerpts when the implementation touches frontend prototype code or backend replacement behavior.
- Relevant PRD/technical/spec demo alignment sections and accepted deviations.
- Relevant spec and testcase excerpts.
- Applicable `AGENTS.md` rules and project commands.
- Implementer report.
- Diff or changed files.
- Test evidence and command output.

Output:

- Return exactly one status line: `**Status:** Approved` or `**Status:** Issues Found`.
- Use `Approved` only when both phases pass.
- Include these sections:
  - `## Spec Compliance`
  - `## Mock Residual Review`
  - `## Code Quality` when risk-triggered, otherwise `## Code Quality: Not Run`
  - `## Blocking Issues`
  - `## Advisory Notes`

Rules:

- Run as a fresh review subagent; do not share the implementer's execution context.
- Use only the provided inputs. Do not rely on hidden conversation context, implementer private reasoning, controller conclusions, or desired outcomes.
- Read actual code and tests. Do not trust only the implementer report.
- Treat subagent reports as claims until confirmed by diff, changed files, test output, and report paths.
- Do not approve when evidence is stale, missing, from the wrong branch/worktree, or from before the latest code change.
- Spec compliance must run first. Check missing requirements, extra work, wrong assumptions, failed testcase coverage, demo parity for UI-facing work, mock retirement for prototype-mocked work, and unapproved scope against the assigned plan, approved demo, PRD/technical/spec, and testcases.
- Mock residual review is mandatory after `tdd-coding` implementation work. Block when prototype mock files, flags, fixtures, imports, adapters, interceptors, route guards, store seeds, or component-local fake data still affect production runtime, or when frontend data flow still bypasses real backend/API/storage replacement.
- If spec compliance has blocking issues, set overall status to `Issues Found`, mark code quality as `Not Run`, and report only obvious severe safety, data-loss, secret, or destructive-operation risks if noticed.
- Run code quality review only when `review-trigger-policy.md` risk triggers apply or the controller explicitly marks the repair as risk-triggered. Check project patterns, maintainability, test quality, error handling, edge cases, security, sensitive data, and unrelated refactors.
- For targeted re-review, restrict the review to previous blocking issues, actual diff, affected upstream/downstream contracts, and fresh evidence unless the new diff changes the main semantics.
- For `tdd-coding`, expect unit/API/focused implementation-facing test evidence. Do not require black-box E2E, acceptance, or regression execution in this gate.
- For UI-facing implementation, do not approve when actual code obviously replaces the approved demo layout, interaction model, or states without an accepted upstream deviation.
- Do not approve when mock cleanup is claimed without diff, grep/residual scan, test, or runtime evidence. Existing project test mocks or Harness fixtures may remain only when outside production runtime and explicitly documented.
- Treat any claim that black-box regression passed during `tdd-coding` as unsupported unless it is explicitly part of a later `local-e2e-verify` or `release-verify` artifact.
- List blocking issues before advisory notes.
- Write findings and rationale primarily in Simplified Chinese. Preserve exact status tokens and technical identifiers.
