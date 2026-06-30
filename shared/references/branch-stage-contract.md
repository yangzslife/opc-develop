# Branch Stage Contract

Branching is a lifecycle boundary, not a default convenience. A worktree is only a tool for isolation.

## Current-Branch Workflows

These workflows must work on the current branch and must not silently create, switch, merge, or delete branches:

- early product brainstorming before committing a requirement artifact
- bug fixes and small iterations, including `lite-develop`
- acceptance feedback recording and routing

For early brainstorming, bugfix, and Lite work, the default expected branch is `develop`. If the current branch is not `develop`, stop before writing current-branch artifacts or code and ask the user to confirm that the current branch is the intended target. Do not auto-checkout `develop`.

If the project `AGENTS.md` or git-flow runbook defines a stricter current-branch rule, follow the project rule. If the project rule contradicts this contract, stop and report the contradiction instead of guessing.

## Requirement Branch Boundary

`product-brainstorm` may discuss, ask clarifying questions, explore options, and stop without creating a branch. Once it is ready to write or update the committed feature requirement artifact, it must create or enter the corresponding feature branch first.

Before writing `docs/features/<numbered-slug>/requirement.md`, `product-brainstorm` must:

1. inspect `git branch --show-current`, `git status --short`, and applicable project branch rules;
2. derive the numbered feature slug using `next_feature_slug.py` or the existing feature directory named in the user request;
3. if already on `feature/<numbered-slug>`, continue there;
4. if not on `feature/<numbered-slug>`, confirm the base when the current branch is not `develop`;
5. create or switch to `feature/<numbered-slug>` from the confirmed current `HEAD`, following the project git-flow runbook;
6. avoid carrying unrelated dirty changes into the feature branch; if dirty state is unclear, stop for user confirmation.

Use the existing branch naming convention `feature/<numbered-slug>`, for example `feature/12-knowledge-base`. If a project `AGENTS.md` requires another exact feature branch naming scheme, follow the project rule and record the mapping in `progress.md`.

## Feature-Branch-Only Workflow

Starting with `create-demo`, every Full feature skill must operate on the corresponding feature branch. This includes demo, PRD, technical design, reviews, spec, testcases, plan, TDD implementation, local verification, acceptance rework, release verification, and branch finishing.

These skills must stop when the current branch is `develop`, `main`, `master`, detached HEAD, or any branch that is not the corresponding feature branch or a project-approved feature branch equivalent. They must not silently create the feature branch, switch branches, or continue on the wrong branch. Route back to `product-brainstorm` or ask the user to switch when the requirement branch has not been created.

## Worktree Is A Tool

Do not use a worktree as a lifecycle default. Create one only when it reduces real risk:

- UI/product polishing needs an isolated throwaway attempt;
- parallel implementation plans would conflict or block each other;
- tests or services require isolated working directories;
- the project `AGENTS.md` explicitly requires worktree isolation.

When a worktree is needed, follow `worktree-isolation-contract.md`. The parent branch is the branch that is current at the time the worktree is created.

## Forbidden Defaults

- Do not create a `feature/*` branch at the start of product brainstorming before the requirement is ready to be written.
- Do not write `requirement.md` on `develop`, `main`, or `master`.
- Do not run `create-demo` or any later Full feature skill on `develop`, `main`, or `master`.
- Do not create a worktree just because a skill is running.
- Do not merge back to `develop`, `main`, or another parent without explicit user instruction or project-rule authority.
- Do not stash, commit, discard, copy, or move dirty work to satisfy this contract without explicit authority.
