# Worktree Isolation Contract

Use worktrees only when they reduce real risk: UI/product polishing isolation, parallel plan execution, conflict isolation, test isolation, or project `AGENTS.md` requirements. A worktree is not a lifecycle stage and must not be created by default.

Branch lifecycle timing is owned by `branch-stage-contract.md`: committed Full feature work gets its feature branch when `product-brainstorm` writes `requirement.md`; `create-demo` and all later Full feature skills must already be on that feature branch. Bugfix and Lite work stay on the current branch unless a worktree is deliberately chosen as an isolation tool.

## Detection

Before creating or using a worktree, inspect:

- `git rev-parse --show-toplevel`
- `git branch --show-current`
- `git status --short`
- `git worktree list --porcelain`

Detect linked worktrees, detached HEAD, dirty unrelated changes, and nested worktree attempts. Do not create a worktree inside another worktree or inside a repository path already managed by `git worktree`.

## Branch Rules

Worktree branches must follow project `AGENTS.md` and runbook rules. If project rules require all Full worktrees to branch from `feature/<feature-slug>` and merge back there first, obey that rule.

Do not merge a worktree branch directly into `develop` or `main` unless the project runbook explicitly allows it.

For `lite-develop` and other current-branch workflows, isolated worktrees are short-lived experiment branches from the current branch `HEAD`, not from `develop` by default. Their parent branch is the branch that was current when the worktree was created. Merge or cherry-pick the worktree back only into that recorded parent branch unless the user and project runbook explicitly choose another target.

If the parent checkout has unrelated dirty changes, do not merge a lite worktree back until the dirty state is understood and the user confirms the target state. Do not stash, commit, discard, or copy parent dirty changes automatically.

## Cleanup

After a worktree branch is merged into its required parent branch, remove the worktree with documented or standard `git worktree remove <path>`. Do not remove a worktree with uncommitted work unless the user explicitly chose discard.

## Detached HEAD Handoff

If Codex App or the environment is in detached HEAD, do not invent a branch strategy. Record the state, preserve the diff, and use `finish-branch` to choose local merge, push/PR, keep branch, discard, or handoff.
