# opc-develop

[English](README.md)

opc-develop 是一套面向受控 AI 辅助开发的 Codex / Claude Code skill 套件。它把小需求快速迭代的 Lite 流程、完整产品开发的 Full 流程，以及 Harness 初始化/评估能力组合在同一个插件里。

![OPC-Develop skills workflow](assets/opc-develop-skills.png)

## 特点

- 根据用户输入语言自适应输出，而不是固定使用某一种默认语言。
- 在 PRD 和技术方案之前先做真实前端 prototype demo。
- 明确维护 demo parity、前端 mock inventory 和 prototype mock retirement。
- 下游产物和实现前必须经过独立 review gate。
- Harness 优先：文档、测试用例、runtime evidence、本地 E2E、发布验证形成闭环。
- 技术设计阶段必须明确 SaaS / 基础设施决策；默认把 MySQL 作为 SaaS 数据库基线，除非目标项目规则要求升级为人工决策。

## 内容

- `.codex-plugin/plugin.json` - Codex 插件 manifest。
- `.claude-plugin/plugin.json` - Claude Code 插件 manifest。
- `skills/` - 原子 skill 和编排 skill。
- `agents/` - Claude Code 自定义 subagents，用于 OPC review 和 implementation 角色。
- `shared/references/` - 共享契约、格式和流程规则。
- `shared/prompts/` - reviewer 和 implementer subagent prompt。
- `shared/scripts/` - 小型产物校验脚本。
- `docs/` - 平台使用说明。

## 主要流程

- `lite-develop` - 在当前分支处理小型或中低风险开发。
- `product-brainstorm` - 早期需求澄清、领域语言、方案取舍、目标/非目标和验收信号沉淀。
- `loop-design` - demo、PRD、technical design 的设计闭环。
- `loop-develop` - spec、testcases、plan、TDD implementation 和 local verification 的开发闭环。
- `harness-init` - 引导式 Harness 初始化规划。
- `harness-eval` - 可复用的 Harness 成熟度评分。
- `release-verify` - 发布门禁、发布后验证和回滚就绪检查。

## 安装

### Codex

把这个仓库作为版本源，克隆到你的 Codex personal plugin source 目录，并在 Codex 中启用 `opc-develop` personal plugin。

```bash
git clone https://github.com/wallkop/opc-develop.git ~/plugins/opc-develop
```

如果你的 Codex 使用其他 personal plugin source 目录，请克隆到对应目录。开发时保持这个仓库作为 source of truth，让 Codex 从它安装或缓存。

### Claude Code

同一个仓库也可以作为 Claude Code plugin source：

```bash
claude --plugin-dir ~/plugins/opc-develop
```

Claude Code 中使用 plugin namespace 调用 skill，例如 `/opc-develop:product-brainstorm` 或 `/opc-develop:harness-eval`。

更多说明见 [docs/claude-code.md](docs/claude-code.md)。

## 更新

Peers 可以从 Git tag 或默认分支更新：

```bash
cd ~/plugins/opc-develop
git pull --ff-only
```

更新后，如你的 Codex 或 Claude Code 版本需要，请重启或重新加载插件。

## 发布与发现

GitHub 是历史、tag、diff、issue 和 release notes 的 canonical source。SkillHub、Claude marketplace、Codex marketplace 等目录站更适合做 discovery surface，并链接回这个仓库。

## 安全说明

这个仓库不应该包含项目业务产物、凭据、私有日志、`.env` 文件或生成后的 feature 文档。具体需求的输出应写入目标项目仓库，而不是写进这个插件。

## License

MIT
