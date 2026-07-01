# Development Input Contract

Full 开发不得只看 plan 开发。进入 `tdd-coding` 前，必须同时具备并读取完整开发输入。

## Required Inputs

- Approved frontend prototype evidence, mock inventory, and `reviews/demo-review.md` for UI-facing work.
- Approved `prd.md`.
- Approved `technical.md`.
- `risk-spike.md` when `risk-and-readiness-contract.md` marks any risk category as present.
- Approved `spec.md`.
- Approved `plan/*.md` and `plan/integration-plan.md`.
- Approved black-box `testcases.md` and real testcase files as acceptance context.

缺少任一输入或对应 fresh Approved review 时，Full `tdd-coding` 必须阻塞。

## Input Roles

- demo: 约束 UI 布局、交互、状态、体验对齐，并提供需要被真实实现替换/清退的前端 prototype mock inventory。
- PRD: 约束产品行为、用户场景、验收标准和非目标。
- technical: 约束架构方向、SaaS 组件、API 公共输入输出、跨系统边界和 gate 分层。
- risk-spike: 约束高风险运行时假设、最小探针、capability readiness、真实性标签和未验证 blocker。
- spec: 约束 AI 实现者的内部模块、代码结构、本地组件、状态机、内部错误、TDD seed。
- plan: 约束 workstream 拆分、顺序、依赖、修改边界和引用来源。
- testcases: 提供黑盒验收语义参考；`tdd-coding` 只用来设计 unit/API/focused 测试，不执行黑盒回归。

## Controller Duties

Before dispatching implementer subagents, `tdd-coding` must verify:

- All required artifacts exist.
- Matching reviews are fresh Approved.
- `technical.md` owns API public I/O and SaaS decisions.
- High-risk features have `risk-spike.md`, thin-slice testcase references, capability readiness evidence, and no unresolved readiness blockers before broad implementation dispatch.
- `spec.md` owns internal implementation contracts and TDD seed.
- When frontend prototype mocks exist, `spec.md` owns the `Prototype Mock Retirement Plan`.
- `plan/*.md` does not contain technical detail that belongs in technical/spec.
- UI-facing work includes approved frontend prototype context sufficient for implementers.
- If prototype mocks exist, spec and plan include enough mock retirement detail for implementers to replace/remove mocks and prove no production mock residual remains.

If an implementer needs to invent product behavior, architecture, API public contract, SaaS component choice, module structure, or test strategy, stop and route back to the earliest missing artifact.
