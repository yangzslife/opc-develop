# opc-develop

[简体中文](README.zh-CN.md)

opc-develop is a Codex / Claude Code skill suite for controlled AI-assisted product development. It combines a Lite flow for small iterations, a Full flow for end-to-end product development, and Harness initialization/evaluation capabilities.

![OPC-Develop skills workflow](assets/opc-develop-skills.png)

## Highlights

- Adapts output language to the user's input instead of enforcing a fixed default language.
- Builds real frontend prototype demos before PRD and technical design.
- Maintains explicit demo parity, frontend mock inventory, and prototype mock retirement.
- Uses independent review gates before downstream artifacts and implementation.
- Treats Harness as a first-class concern: documentation, testcases, runtime evidence, local E2E, and release verification are part of the workflow.
- Requires SaaS/infrastructure decisions in technical design; MySQL is the default SaaS database baseline unless target project rules require human escalation.

## Contents

- `.codex-plugin/plugin.json` - Codex plugin manifest.
- `.claude-plugin/plugin.json` - Claude Code plugin manifest.
- `skills/` - atomic and orchestration skills.
- `agents/` - Claude Code custom subagents for OPC review and implementation roles.
- `shared/references/` - shared contracts, formats, and process rules.
- `shared/prompts/` - reviewer and implementer subagent prompts.
- `shared/scripts/` - small artifact validation helpers.
- `docs/` - platform-specific usage notes.

## Main Flows

- `lite-develop` - controlled small or medium-low-risk current-branch development.
- `product-brainstorm` - early feature clarification, domain language, alternatives, tradeoffs, and requirement capture.
- `loop-design` - demo, PRD, and technical design review loop.
- `loop-develop` - spec, testcases, plan, TDD implementation, and local verification loop.
- `harness-init` - guided Harness initialization planning.
- `harness-eval` - reusable Harness maturity scoring.
- `release-verify` - release gates, post-release checks, and rollback readiness.

## Install

### Codex

Use this repository as the canonical version source. Clone it into your Codex personal plugin source directory and enable the `opc-develop` personal plugin in Codex.

```bash
git clone https://github.com/wallkop/opc-develop.git ~/plugins/opc-develop
```

If your Codex setup uses a different personal plugin source directory, clone the repository there instead. For local development, keep this repository as the source of truth and let Codex install/cache from it.

### Claude Code

Use the same repository as a Claude Code plugin source:

```bash
claude --plugin-dir ~/plugins/opc-develop
```

Claude Code skills are invoked with the plugin namespace, for example `/opc-develop:product-brainstorm` or `/opc-develop:harness-eval`.

See [docs/claude-code.md](docs/claude-code.md) for details.

## Update

Peers should update from Git tags or the default branch:

```bash
cd ~/plugins/opc-develop
git pull --ff-only
```

After updating, restart Codex or Claude Code, or reload plugins if your client requires it.

## Publishing And Discovery

GitHub is the canonical source for history, tags, diffs, issues, and release notes. SkillHub, Claude marketplace, Codex marketplace, and similar directories are better used as discovery surfaces that link back to this repository.

## Safety Notes

This repository should not contain project-specific business artifacts, credentials, private logs, `.env` files, or generated feature documents. Keep requirement-specific outputs inside the target project repository, not inside this plugin.

## License

MIT
