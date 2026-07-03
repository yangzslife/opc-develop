# opc-develop

[English](README.md)

opc-develop 是一套面向 AI 辅助产品开发的 Claude Code / Codex skill 套件，服务于那些自己对产品、
设计和工程判断负责的 Builder。它把你的品味沉淀在三份产物里（requirement、PRD + demo、技术设计），
把执行交给受机械化 gate 约束的 agent，并且——不同于多数 workflow 套件——**度量自身的流程闭环**，
让流程随着数据的支撑而逐步收缩。

![OPC-Develop skills workflow](assets/opc-develop-skills.png)

## 设计原则（v0.2）

1. **靠反馈对齐，而非前馈。** 三层嵌套闭环：任务级证据（TDD RED/GREEN、证据三角）、
   feature 级 gate（带 rubric 的全新 reviewer、基于 SHA 的新鲜度检查）、
   闭环级度量（`retro` 挖掘 ledger 并提出改进建议）。
2. **约束落在最低层。** 脚本和结构化校验（L0）优先于按需加载的产物（L1），产物优先于散文规则（L2）。
   只有一份始终加载的核心契约（约 1k token）；其余内容按角色按需加载。
3. **Demo 先行：数据是假的，感觉是真的。** 品味要靠体验来验证。prototype 直接放在真实代码库里；
   每一个 mock 都登记在册，并在完成前全部退役。
4. **诚实的证据。** 每一条验证结论都带真实性标签（`mock passed` … `long-run passed`）。
   harness 能力缺失时只封顶标签等级，而不阻塞工作。
5. **默认放行，记录缺口。** 裸仓库也能工作。只有破坏性操作默认拦截。
6. **自我演化。** 已解决的失败会追加到 error ledger；`retro` 检测重复出现的问题，
   并将规则固化到最低的约束层——需人类批准，并有退役复审。

## Skills

Full 流程（一个 feature，四个人类介入点）：

| Skill | 阶段 | 你要做的 |
|---|---|---|
| `brainstorm` | 拷打式追问 → requirement.md | 回答问题，确认一页纸决策摘要 |
| `demo` | 在真实代码库里做 prototype | 反复把玩，直到感觉对了 |
| `design` | PRD（AC-ID）+ 技术设计（决策记录） | 读两份决策清单，批准单向门决策 |
| `contract` | 实现契约（spec+plan 合并） | — |
| `build` | 通过 subagent 做 TDD 实现 | — |
| `verify` | 黑盒 E2E、证据三角、验收清单 | 抽查并给出结论 |
| `ship` | 发布门禁、部署、回滚就绪、分支清理 | 确认部署 |

随时可用：

- `lite` — 80% 场景的路径：小改动、当前分支、零仪式感，兼容裸仓库。
- `retro` — 每周的流程工程报告：token 分布、返工路由、重复错误、规则固化提案。
- `harness` — 评估（靠实际执行而非阅读）并建设项目的 run/reset/observe/drive 能力：
  seed、agent 可读的日志、状态导出、E2E 脚手架。

## 反馈模型

所有人类反馈分为三类：**tune**（原地迭代，零成本）、**revise**（路由到最早出错的层，
通过内容 SHA 检查级联标记过期）、**park**（搁置）。验收驳回会分诊为：实现缺陷 / 产物缺陷 /
品味变化——最后一种是新的增量，永远不算返工。

## Ledger

每一次 gate 结果、返工路由、证据标签和缺口都会追加到
`docs/features/<slug>/ledger.jsonl`；已解决的失败会把根因追加到
`docs/opc/error-ledger.jsonl`。`retro` 把这些数据转化为决策：哪些 gate 该降级、
哪些规则该固化、哪些产物层配得上它的成本。

## 平台说明

- **Claude Code**：完整支持。review 和实现在隔离的 subagent 中运行
  （`opc-reviewer` 通过工具限制强制只读）。
- **Codex / 其他 harness**：skill 可用；在没有隔离 subagent 的环境里，gate 和构建会诚实降级
  （`self-reviewed (no isolation)` 标签会在下一个人类介入点被明确呈现），
  而不是阻塞或默默自我批准。

## 安装

### Claude Code

```bash
claude --plugin-dir ~/plugins/opc-develop
```

skill 通过 plugin namespace 调用，例如 `/opc-develop:brainstorm`、
`/opc-develop:lite`、`/opc-develop:retro`。详见 [docs/claude-code.md](docs/claude-code.md)。

### Codex

```bash
codex plugin marketplace add wallkop/opc-develop --ref main
codex plugin add opc-develop@opc-develop
```

## 目录结构

- `skills/` — 10 个 skill。
- `shared/core-contract.md` — 唯一始终加载的契约。
- `shared/packs/` — 按角色划分的规则包，按需加载。
- `shared/formats/` — 产物格式规范（requirement、PRD、technical、impl-contract、ledger）。
- `shared/rubrics/` — gate rubric；完整交给 reviewer。
- `shared/scripts/` — L0 工具：ledger 追加/汇总、SHA 新鲜度、状态解析、产物校验、
  重复问题扫描、feature slug。仅依赖标准库；由 `test_opc_scripts.py` 覆盖。
- `agents/`、`shared/prompts/` — reviewer 和 implementer subagent 定义。

## 适合人群

Builder——尤其是独立开发者——需要能自己判断一个需求是否成立、一个交互是否顺手、
一个架构是否经得起时间。这套套件保护的是这些判断，而不是代替它们。
如果你希望 agent 替你掌管产品品味，那这不是适合你的工具。

## 安全说明

feature 产物、ledger、凭据和日志应保存在目标项目仓库里——绝不放进这个插件。
部署、force-push、删除和对外发布永远需要人类明确确认。

## License

MIT
