# Harness Verbs

A project's harness is measured by four verbs, not by documents. The standard: for any behavior
change, the agent can close the loop without a human — run the system, reset it to a known state,
drive it from the outside, and observe what actually happened inside. Capabilities are executable
(scripts, seeds, endpoints); documents only index them.

## L1 — run

- One command starts the full local stack (`make dev` or equivalent); one command stops it.
- Fixed ports; a health endpoint or command that proves "up".
- Dev server output tees to a fixed log file path — stdout alone is invisible to agents.
- Double-start fails loudly (pidfile), never silently forks a second stack.

## L2 — reset (the precondition for determinism)

- One command returns the stack to a clean known state.
- **Named seed scenarios**: a catalog of business-meaningful fixtures invocable by name —
  `seed:empty`, `seed:small-team`, `seed:edge-heavy`, `seed:<feature-specific>` — each documented
  with one line about what world it creates. E2E cases declare which seed they stand on.
- Reset + seed is idempotent: run twice, same world.

## L3 — observe (agent-legible runtime)

- **Structured logs, four elements**: JSON lines; a correlation/request ID on every entry (one user
  action's full causal chain must be reconstructable with one grep); written to a fixed file path;
  AGENTS.md documents the path and the tail/jq recipes.
- **Dev side-channels**: invisible events (emails, SMS, payment callbacks, magic links) are logged
  in dev mode so the agent can complete flows unattended.
- **State dump**: a CLI or dev endpoint answering "what state is entity X in right now"
  (`appctl dump <entity>` beats inferring from log fragments).
- **DB access**: a documented read-only query recipe (psql/sqlite3 command + generated schema doc).
  Prefer recipes over DB MCP servers — the reference MCP servers were archived with unpatched
  SQL injection, and recipes cost zero maintenance and zero context.
- Browser runtime: console/network/trace via the project's browser tooling (e.g. Chrome DevTools
  MCP or Playwright) when the feature has a UI.

## L4 — drive (black-box E2E, two tiers)

- **Tier 1 — scripted (the regression backbone):** committed black-box specs driven at whatever
  interface the feature actually exposes — HTTP/API suites for services, CLI invocations for
  tools, Playwright (or equivalent) for UI. Browser tooling is *one driver*, not the definition;
  an API feature proven only through a UI detour is fragile coverage. Headless, CI-runnable,
  each spec annotated with the AC-IDs it proves and the seed it stands on. Deterministic gates
  run on every change.
- **Tier 2 — agentic (exploration and distillation):** the agent drives the app interactively to
  verify new behavior, check demo parity, and *author* Tier-1 specs. Rule: every agentic
  verification that matters is distilled into a Tier-1 spec — ephemeral intelligence becomes a
  durable asset.
- Computer-use/browser agents are advisory verification, never a blocking gate (stochastic, slow,
  expensive). Blocking gates are Tier-1 only.
- Evidence for E2E claims follows the evidence triangle (`evidence.md`).

## Gap Accounting

Every missing verb capability found during any flow is recorded as a `gap` ledger entry with the
verb it blocks and the label cap it causes. The `harness` skill consumes gap entries as its backlog.
