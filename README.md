# opc-develop

[简体中文](README.zh-CN.md)

opc-develop is a Claude Code / Codex skill suite for AI-assisted product development by builders
who own the product, design, and engineering judgment themselves. It captures your taste in three
artifacts (requirement, PRD + demo, technical design), hands execution to agents under mechanical
gates, and — unlike most workflow suites — **measures its own loop** so the process can shrink as
the data justifies it.

![OPC-Develop skills workflow](assets/opc-develop-skills.png)

## Design Principles (v0.2)

1. **Alignment by feedback, not feedforward.** Three nested loops: task-level evidence (TDD
   RED/GREEN, evidence triangles), feature-level gates (fresh reviewers with rubrics, SHA-based
   freshness), and loop-level measurement (`retro` mines ledgers and proposes improvements).
2. **Enforcement lives at the lowest layer.** Scripts and structural validation (L0) over
   pulled-on-demand artifacts (L1) over prose (L2). One always-loaded core contract (~1k tokens);
   everything else loads per role.
3. **Demo first: data fake, feeling real.** Taste is verified by experience. The prototype lives
   in the real codebase; every mock is inventoried and retired before done.
4. **Honest evidence.** Every verification claim carries an authenticity label (`mock passed` …
   `long-run passed`). Missing harness capability caps the label instead of blocking the work.
5. **Fail open with recorded gaps.** Bare repositories work. Only destructive actions fail closed.
6. **Self-evolution.** Resolved failures append to an error ledger; `retro` detects recurrences
   and crystallizes rules at the lowest enforcement layer — with human approval and retirement
   review.

## The Skills

Full flow (one feature, four human touchpoints):

| Skill | Phase | You do |
|---|---|---|
| `brainstorm` | grilling → requirement.md | answer questions, confirm a 1-page decision summary |
| `demo` | prototype in the real codebase | play with it until the feel is right |
| `design` | PRD (AC-IDs) + technical (decision records) | read two decision sheets, approve one-way doors |
| `contract` | implementation contracts (spec+plan merged) | — |
| `build` | TDD implementation via subagents | — |
| `verify` | black-box E2E, evidence triangles, acceptance sheet | spot-check and give a verdict |
| `ship` | release gates, deploy, rollback readiness, branch cleanup | confirm the deploy |

Always available:

- `lite` — the 80% path: small changes, current branch, zero ceremony, bare-repo compatible.
- `retro` — weekly loop-engineering report: token distribution, rework routing, recurring errors,
  rule crystallization proposals.
- `harness` — assess (by executing, not reading) and build the project's run/reset/observe/drive
  capabilities: seeds, agent-legible logs, state dumps, E2E scaffolding.

## Feedback Model

All human feedback classifies as **tune** (iterate in place, free), **revise** (route to the
earliest broken layer, cascade staleness via content-SHA checks), or **park**. Acceptance
rejections triage into implementation defect / artifact defect / taste change — the last is a new
increment, never rework.

## Ledgers

Every gate outcome, rework routing, evidence label, and gap appends to
`docs/features/<slug>/ledger.jsonl`; resolved failures append root causes to
`docs/opc/error-ledger.jsonl`. `retro` turns these into decisions: which gates to downgrade,
which rules to crystallize, which artifact layers earn their cost.

## Platform Notes

- **Claude Code**: full support. Reviews and implementation run in isolated subagents
  (`opc-reviewer` is read-only by tool restriction).
- **Codex / other harnesses**: skills work; where isolated subagents are unavailable, gates and
  builds degrade honestly (`self-reviewed (no isolation)` labels surfaced at the next human
  touchpoint) instead of blocking or silently self-approving.

## Install

### Claude Code

```bash
claude --plugin-dir ~/plugins/opc-develop
```

Skills are invoked with the plugin namespace, e.g. `/opc-develop:brainstorm`,
`/opc-develop:lite`, `/opc-develop:retro`. See [docs/claude-code.md](docs/claude-code.md).

### Codex

```bash
codex plugin marketplace add wallkop/opc-develop --ref main
codex plugin add opc-develop@opc-develop
```

## Layout

- `skills/` — the 10 skills.
- `shared/core-contract.md` — the one always-loaded contract.
- `shared/packs/` — role-specific rule packs, loaded on demand.
- `shared/formats/` — artifact format specs (requirement, PRD, technical, impl-contract, ledger).
- `shared/rubrics/` — gate rubrics; given to reviewers in full.
- `shared/scripts/` — L0 tooling: ledger append/summary, SHA freshness, status parsing, artifact
  validation, recurrence scan, feature slugs. Stdlib-only; `test_opc_scripts.py` covers them.
- `agents/`, `shared/prompts/` — reviewer and implementer subagent definitions.

## Migrating from v0.1

| v0.2 | absorbs (v0.1) |
|---|---|
| `brainstorm` | product-brainstorm |
| `demo` | create-demo, review-demo, build-demo |
| `design` | create/review/build-prd, create/review/build-technical, loop-design |
| `contract` | create/review-spec, create/review-testcases, create/review-plan |
| `build` | tdd-coding, debug-failure, loop-develop |
| `verify` | local-e2e-verify, acceptance-rework |
| `ship` | release-verify, finish-branch |
| `lite` | lite-develop |
| `retro` | — (new) |
| `harness` | harness-init, harness-eval |

v0.1 feature artifacts remain readable; new features use the v0.2 artifact formats
(`shared/formats/`).

## Who It Is For

Builders — especially solo operators — who can judge whether a requirement is sound, an
interaction feels right, and an architecture will age well. The suite protects those judgments;
it does not replace them. If you want an agent to own product taste for you, this is the wrong tool.

## Safety Notes

Keep feature artifacts, ledgers, credentials, and logs in the target project repository — never
in this plugin. Deploys, force-pushes, deletions, and external publication always require explicit
human confirmation.

## License

MIT
