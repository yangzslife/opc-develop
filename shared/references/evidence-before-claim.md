# Evidence Before Claim Contract

Any claim that work is complete, fixed, passed, verified, accepted, merged, or releasable must be backed by fresh evidence from the current artifact revision and current code state.

## Evidence Requirements

Record the command, exit code, timestamp or report path, working directory, branch or commit, and relevant output summary. For browser, UI, DB, log, or trace checks, record the evidence path or stable lookup key.

Do not use stale command output from before the latest code or artifact change.

## Controller Duties

A subagent report is not sufficient evidence by itself. The controller must inspect actual diff, changed files, test output, report files, or Runtime evidence before making a status claim.

`progress.md` must record only evidence-backed status. If evidence is missing, record the state as blocked, unverified, or not run with the reason.

## Prohibited Claims

Do not say Passed, Done, Fixed, Verified, Ready, Releasable, or Published when:

- the relevant command was not run,
- exit code is unknown,
- report paths do not exist,
- output belongs to an older revision,
- the check was skipped without an explicit documented reason,
- the environment was unavailable.
