# Harness 文档规范

> OPC 套件适配说明：本文是 `opc-develop` 的共享 Harness 文档约定。后续设计、开发、评审、验证和收尾类 skill 必须按本文组织项目资产；若本文中的通用示例与 `harness-artifact-contract.md` 或 `branch-stage-contract.md` 冲突，以专门契约为准。特别是 feature 目录在 `opc-develop` 中必须使用无前导零的递增编号格式 `<number>-<feature-name>`，例如 `1-knowledge-base`、`105-web-search-prefer-native`。

本文定义 Harness 体系中的“文档规范”板块，用于约束项目文档与验证资产的组织方式，沉淀产品需求、技术设计、spec & plan、评审记录和端到端测试用例索引。

本规范不绑定任何具体项目。具体项目可以在此基础上按自身技术栈、产品模块和发布流程做少量扩展。

## 在 Harness 体系中的位置

完整 Harness 建议分为四个板块：

1. 开发流程：定义需求从输入、评审、实现到交付的推进方式。
2. 文档规范：定义产品文档、技术文档、spec & plan、测试用例索引和评审记录的组织方式。本文只覆盖这一板块。
3. Runtime：定义运行期可观测性和可追溯能力，例如 Log、DB、Trace。
4. 自动化测试：定义自动化验证入口、测试分层、门禁策略和报告沉淀。

四个板块的关系是：开发流程驱动任务推进，文档规范沉淀过程资产，Runtime 提供运行证据，自动化测试提供验证闭环。

## 核心原则

1. Feature 相关的一切需求资产集中放在 `docs/features/<feature-slug>/`。
2. 长期可复用的测试用例不放在 feature 目录，而是沉淀到全局 `docs/testcases/`。
3. Feature 目录中的 `testcases.md` 只维护测试用例索引，指向 `docs/testcases/` 中的真实用例。
4. 全局技术架构、技术规范、ADR、runbook 和稳定知识放在 `docs/technical/`。
5. PRD 定义“做什么”，技术文档和 spec 定义“怎么做”，plan 定义“怎么落地”，testcase 定义“怎么证明做对了”。
6. 高保真 demo 用于表达目标体验，不替代 PRD，也不承诺具体实现方案。
7. 评审记录必须和被评审对象一一对应，至少覆盖 demo、PRD、feature 技术文档、spec、plan、testcase。

## Mock System

Mock 系统是 Harness 的一等能力，服务高保真 demo、前端 prototype、local E2E、黑盒验收、回归测试和故障复现。成熟项目必须同时具备 API mock 和 storage mock。

推荐文档与资产位置：

```text
docs/technical/standards/mock-system.md
docs/technical/runbooks/mock-system.md
docs/testcases/<product-module>/fixtures/
.dev/reports/mock-system/
```

职责边界：

- `docs/technical/standards/mock-system.md`：长期规则，定义 API mock、storage mock、fixture、隔离、脱敏、reset、drift 检查和生产路径禁用规则。
- `docs/technical/runbooks/mock-system.md`：运行手册，说明如何启动 mock、切换场景、重置状态、执行 smoke/check、查看报告和诊断失败。
- `docs/testcases/<product-module>/fixtures/`：黑盒测试、demo 和回归可复用的非敏感 mock payload、样例数据、截图基线和测试素材。
- `.dev/reports/mock-system/`：mock smoke、drift audit、fixture 脱敏检查和失败诊断报告。

最低要求：

- API mock 覆盖前端或本地 client 调用的产品 API，并与 feature `technical.md` 中定义的 API 公共输入输出一致。
- API mock 支持 success、loading、empty、permission denied、validation error、conflict、external failure、offline 等场景。
- Storage mock 覆盖前端或本地服务依赖的存储状态，支持确定性初始化、fixture 加载、状态重置、清理和失败状态模拟。
- Mock 模式必须有显式开关，例如 `MOCK_MODE`、`DEMO_MODE`、mock profile 或测试命令参数；生产默认路径不得启用 mock。
- Mock 不得访问真实后端、真实第三方服务、真实云存储、真实用户数据、真实 token、生产数据或受保护文件。
- 项目应提供 smoke/check 命令或最小验证入口，证明 API mock 和 storage mock 均可用，并生成可定位的诊断或报告。

## 推荐目录结构

```text
docs/
  features/
    <feature-slug>/
      requirement.md
      prd.md
      demo/
        prototype.md
        assets/
      technical.md
      spec.md
      plan/
        plan-01-<workstream>.md
        plan-02-<workstream>.md
        integration-plan.md
      testcases.md
      reviews/
        demo-review.md
        prd-review.md
        technical-review.md
        spec-review.md
        plan-review.md
        testcase-review.md
      progress.md
      changelog.md

  testcases/
    README.md
    <product-module>/
      README.md
      e2e/
        TC-<module>-001-<title>.md
      acceptance/
        TC-<module>-A001-<title>.md
      regression/
        TC-<module>-R001-<title>.md
      fixtures/
      reports/

  technical/
    README.md
    architecture/
      overview.md
      module-map.md
      data-flow.md
    standards/
      coding.md
      testing.md
      frontend.md
      backend.md
      security.md
      mock-system.md
    decisions/
      ADR-0001-<title>.md
    runbooks/
      local-dev.md
      mock-system.md
      deploy.md
      rollback.md
      troubleshooting.md
    knowledge/
      glossary.md
      environments.md
      dependencies.md
      known-pitfalls.md
```

## 命名规范

### Feature Slug

`<feature-slug>` 表示某个需求或功能的稳定短名，使用小写短横线：

```text
user-login
asset-export
voice-input-refactor
workspace-permission
```

同一个需求的产品文档、技术文档、计划、评审和测试索引都放在同一个 feature 目录下，避免多处维护 slug 导致不一致。

### Product Module

`<product-module>` 表示长期产品模块，而不是单次需求名称。示例：

```text
auth/
workspace/
chat/
billing/
asset-library/
settings/
admin/
```

测试用例按产品模块组织，便于长期复用和回归。

## Feature 目录规范

路径：

```text
docs/features/<feature-slug>/
```

用途：维护单个需求或功能的完整工作资产，包括原始需求、PRD、高保真 demo、feature 专属技术文档、spec、plan、测试索引、评审、进度和需求变更记录。

### requirement.md

原始需求记录。

用于保存：

- 用户或业务方原始输入
- 背景和问题
- 目标
- 约束
- 非目标
- 关键上下文
- 尚未确认的问题

要求：

- 尽量保留原话和上下文。
- 不提前技术化。
- 不把后续方案反写成原始需求。

### prd.md

产品需求文档。

用于定义：

- 用户场景
- 功能范围
- 用户流程
- 页面和交互
- 字段规则
- 状态流转
- 异常路径
- 权限规则
- 埋点和数据口径
- 验收标准
- 不做范围

要求：

- PRD 是产品真相源。
- PRD 只定义产品行为，不写具体代码实现。
- 每条验收标准都应该能转成可验证用例。

### demo/

高保真 demo 目录。

推荐结构：

```text
  demo/
  prototype.md
  assets/
```

用途：

- 表达目标用户体验。
- 记录真实前端代码中的高保真 prototype、预览 URL、服务重启命令、截图或录屏证据。
- 记录新功能后端行为在 demo 阶段使用的前端 mock inventory。
- 帮助产品、设计、研发和测试对齐预期。

要求：

- `create-demo` 应优先直接修改真实前端代码，达到至少 80% 的交付完成度和产品品味对齐。
- demo 阶段禁止修改后端/API handler/数据库/migration/服务端任务/基础设施代码；新增后端数据需求必须通过纯前端 mock 替代。
- 每轮 demo 修改后必须按 `local-dev.md` 重启本地前后端服务，记录可访问预览 URL 和关键证据。
- `prototype.md` 必须列出 changed frontend files、preview URL、restart/status commands、evidence paths、mock inventory、已知偏差和用户反馈。
- `assets/` 放 demo 依赖的图片、视频、字体、样式或非敏感模拟数据。
- `index.html` 只能作为可选辅助快照，不能替代真实前端 prototype。
- demo 不替代 PRD。
- demo 不承诺具体实现技术路线。

### technical.md

Feature 专属技术文档。

用于说明该需求涉及的技术背景和影响范围，例如：

- 涉及模块
- 现有实现现状
- 技术约束
- 接口影响
- 数据结构影响
- 兼容性要求
- 迁移要求
- 安全边界
- 性能影响
- 运维影响
- 主要风险

要求：

- 只写和该 feature 相关的技术说明。
- 不放全局架构和长期规范。
- 如果内容长期有效，应抽象后沉淀到 `docs/technical/`。

### spec.md

可执行技术规格。

用于把 PRD 和 `technical.md` 转换成清晰的实现规格，包括：

- 模块边界
- 接口契约
- 数据模型
- 状态机
- 关键流程
- 错误处理
- 失败模式
- 兼容策略
- 迁移策略
- 安全策略
- 验证点

要求：

- spec 应该足够具体，研发可以据此拆任务。
- 不写空泛原则。
- 对跨模块契约、数据结构和状态变化必须明确。

### plan/

实施计划目录。

推荐文件：

```text
plan/
  plan-01-<workstream>.md
  plan-02-<workstream>.md
  integration-plan.md
```

`plan-XX-<workstream>.md` 用于拆解一个可独立执行的工作流。每个 plan 内可以包含多个 task。

要求：

- create-plan 必须读取项目根目录及相关作用域内 `AGENTS.md`，并严格遵循其中定义的开发流程、分支策略、验收流程和门禁要求。
- 每个 plan 必须声明适用的 `AGENTS.md` 规则来源、当前 feature 分支预期、验收入口和验收通过标准；plan 不创建新分支，Full feature 分支在 `product-brainstorm` 写入 `requirement.md` 前创建或进入。
- 不同 `plan-XX-<workstream>.md` 必须能并行执行。
- 如果两个任务必须串行执行，必须放到同一个 plan 内，用 task 依赖关系表达顺序。
- 每个 plan 必须声明自身依赖、可并行条件、ready 标准、影响范围和引用文件地图。
- 每个 task 必须声明 task id、目标、引用的上游产物、允许/禁止修改边界、涉及文件或模块、依赖 task 和完成标准；具体技术细节、API schema、数据库设计、RED/GREEN 命令和测试用例不得写入 plan。
- plan 结构必须像 tree：多个独立 plan/task 分支并行推进，最后合流到统一联调节点。

`integration-plan.md` 用于定义最终联调节点。

要求：

- 必须等待全部 `plan-XX-<workstream>.md` 和其中 task ready 后才能执行。
- 必须定义合流顺序、冲突处理、联调范围、必要的白盒/灰盒联调检查、交接给 `local-e2e-verify` 的黑盒回归入口、失败回滚方式和完成标准。

每个 task 必须包含：

- 目标
- 文件地图条目或涉及模块
- 引用的上游产物章节或行号
- 允许修改边界
- 禁止修改边界
- 依赖关系和并行条件
- ready 标准

验证策略不得把 plan 写成测试计划。职责边界：

- Unit/API/focused implementation-facing 测试由 `spec.md` 的 TDD seed 和 `tdd-coding` 派生执行。
- 黑盒 E2E、acceptance、regression 用例由 `create-testcases` 写入 `docs/testcases/<product-module>/`。
- 本地黑盒回归、运行时截图、手工验收证据由 `local-e2e-verify` 和 `release-verify` 执行。
- `plan/*.md` 只写开发顺序、边界、依赖、引用和 ready 标准。

### testcases.md

本 feature 关联测试用例索引。

完整测试用例不写在这里，而是写入 `docs/testcases/<product-module>/`。

示例：

```md
# Testcase Index

| Type | Case ID | Path | Coverage |
| --- | --- | --- | --- |
| E2E | TC-auth-001-login-success | docs/testcases/auth/e2e/TC-auth-001-login-success.md | 登录成功链路 |
| Acceptance | TC-auth-A001-login-error-message | docs/testcases/auth/acceptance/TC-auth-A001-login-error-message.md | 登录失败提示 |
| Regression | TC-auth-R003-token-expired | docs/testcases/auth/regression/TC-auth-R003-token-expired.md | token 过期回归 |
```

要求：

- 只维护索引，不复制完整用例内容。
- 每条记录必须指向真实存在的 testcase 文件。
- Coverage 简短描述该用例覆盖的产品行为。

### reviews/

评审记录目录。

推荐文件：

```text
reviews/
  demo-review.md
  prd-review.md
  technical-review.md
  spec-review.md
  plan-review.md
  testcase-review.md
```

`demo-review.md`：评审 `demo/`。

重点检查：

- demo 是否覆盖需求目标
- 核心用户路径是否完整
- 空态、错误态、成功态和权限态是否覆盖
- 视觉和交互是否能支撑产品讨论

`prd-review.md`：评审 `prd.md`。

重点检查：

- 目标是否清楚
- 范围是否明确
- 用户流程是否完整
- 异常路径是否覆盖
- 验收标准是否可验证

`technical-review.md`：评审 `technical.md`。

重点检查：

- 技术背景是否准确
- 模块边界是否清晰
- 兼容性、迁移、安全、性能、运维影响是否说明
- 主要风险是否暴露

`spec-review.md`：评审 `spec.md`。

重点检查：

- 规格是否可执行
- 接口、数据、状态、失败模式是否完整
- 是否和 PRD 一致
- 是否遗漏关键边界条件

`plan-review.md`：评审 `plan/`。

重点检查：

- 任务拆分是否合理
- 实施顺序是否正确
- 并行化拆分是否合理
- 必须串行的任务是否放在同一个 plan 内
- 不同 plan 是否具备并行执行条件
- `integration-plan.md` 是否定义最终合流联调节点
- 白盒/灰盒检查与黑盒验证交接是否明确
- 完成标准是否可判断

`testcase-review.md`：评审 `testcases.md` 及其索引到的真实测试用例。

重点检查：

- 是否覆盖 PRD 验收标准
- 是否覆盖核心异常路径
- 是否覆盖回归风险
- 用例步骤和预期结果是否可执行

### progress.md

执行进度记录。

用于记录：

- 当前状态
- 已完成任务
- 阻塞项
- 关键决策
- 已执行验证
- 失败验证和处理结论
- 残余风险

要求：

- 不写流水账。
- 只记录对交付、回溯和继续推进有价值的信息。

### changelog.md

需求变更记录。

用于记录：

- PRD 关键变更
- 技术方案关键变更
- 范围变化
- 验收标准变化
- 变更原因
- 影响范围

推荐格式：

```md
| Date | Change | Reason | Impact |
| --- | --- | --- | --- |
| 2026-01-01 | 调整登录失败提示规则 | 产品确认 | 影响 auth 错误态 testcase |
```

## 全局 Testcases 规范

路径：

```text
docs/testcases/
```

用途：维护长期、全局、可复用的测试用例库。

测试用例按产品模块组织，而不是按 feature 组织。这样可以避免测试用例随着 feature 目录归档而失去回归价值。

### docs/testcases/README.md

全局测试用例库说明。

建议包含：

- 产品模块划分
- 用例类型说明
- 用例编号规则
- 夹具管理规则
- 报告管理规则
- 自动化脚本入口约定

### docs/testcases/<product-module>/README.md

产品模块测试说明。

建议包含：

- 模块范围
- 核心用户路径
- 关键状态
- 依赖模块
- 测试账号或数据要求说明
- 自动化覆盖情况
- 高风险回归点

### e2e/

端到端测试用例。

用于覆盖完整用户链路。每个用例建议包含：

- Case ID
- 标题
- 所属模块
- 前置条件
- 测试数据
- 操作步骤
- 预期结果
- 自动化脚本入口
- 失败排查提示

### acceptance/

验收测试用例。

用于业务验收。语言应尽量让非技术人员也能判断通过或失败。

每个用例建议包含：

- 验收目标
- 操作路径
- 预期用户可见结果
- 失败判据
- 相关 PRD 条目

### regression/

回归测试用例。

用于沉淀历史风险和跨版本需要反复验证的路径。

每个用例建议包含：

- 回归风险来源
- 曾经出现的问题
- 受影响功能
- 操作步骤
- 预期结果
- 适用发布场景

### fixtures/

测试夹具目录。

可放：

- mock payload
- 样例数据
- 截图基线
- 测试素材
- 非敏感账号说明

要求：

- 不得放密钥、密码、token、生产隐私数据。
- 大文件应有来源说明和更新规则。
- API mock 与 storage mock 使用的 fixture 必须可重置、可复现，并与真实生产数据隔离。
- 供高保真 demo、local E2E、回归和人工验收复用的 fixture 应标明适用场景和 mock profile。

### reports/

测试报告目录。

可放：

- 每轮测试执行结果
- 自动化报告
- 失败截图
- 关键日志摘要
- 残余风险

报告应标明：

- 执行时间
- 执行环境
- 执行人或执行工具
- 用例范围
- 通过/失败情况
- 未覆盖项
- 关联 feature slug
- 关联 testcase 路径
- 关键截图、日志、DB 查询或 trace 证据路径

## 全局 Technical 规范

路径：

```text
docs/technical/
```

用途：维护全局技术架构、长期技术规范、ADR、runbook 和稳定知识。

这里不放单个 feature 的临时技术细节。Feature 专属技术说明应放在 `docs/features/<feature-slug>/technical.md`。

### architecture/

全局架构文档。

推荐文件：

- `overview.md`：整体架构。
- `module-map.md`：模块边界和职责。
- `data-flow.md`：核心数据流和调用链。

### standards/

全局技术规范。

推荐文件：

- `coding.md`：编码规范。
- `testing.md`：测试规范。
- `frontend.md`：前端规范。
- `backend.md`：后端规范。
- `security.md`：安全规范。

`testing.md` 必须定义自动化测试和验收入口：

- 单元测试命令
- 集成测试命令
- E2E 测试命令
- smoke 测试命令
- release gate 命令
- 覆盖率命令和阈值
- 测试报告输出位置
- 自动化验收脚本入口
- 无法自动化覆盖时的人工验收记录规则

### decisions/

架构决策记录，即 ADR。

命名：

```text
ADR-0001-<title>.md
ADR-0002-<title>.md
```

每个 ADR 建议包含：

- 背景
- 问题
- 可选方案
- 决策
- 后果
- 适用范围

ADR 用于记录重要技术取舍，不用于记录普通实现细节。

### runbooks/

操作手册。

推荐文件：

- `local-dev.md`：本地开发启动和验证。
- `deploy.md`：部署流程。
- `rollback.md`：回滚流程。
- `troubleshooting.md`：排障流程。

runbook 应尽量可执行，避免只写原则。

`local-dev.md` 必须定义本地服务启动和验证流程：

- 依赖安装命令
- 环境变量说明，不得包含密钥明文
- 本地服务启动命令
- 本地服务停止命令
- 本地服务状态检查命令
- 本地日志查看命令
- 端口、进程、健康检查地址
- 本地测试数据准备和清理方式
- 本地 Runtime 证据入口，包括 Log、DB、Trace
- 常见启动失败和排查步骤

`deploy.md` 必须定义 CI/CD 发布流程：

- 构建命令
- 发布前门禁命令
- 版本号规则
- CI/CD pipeline 入口
- 制品输出位置
- 制品上传位置
- 发布环境和审批规则
- 发布后自动化验收入口
- 发布证据记录规则

`rollback.md` 必须定义回滚流程：

- 回滚触发条件
- 回滚命令或平台入口
- 回滚验证命令
- 数据回滚边界
- 回滚证据记录规则

### knowledge/

稳定知识库。

推荐文件：

- `glossary.md`：术语表。
- `environments.md`：环境说明。
- `dependencies.md`：外部依赖。
- `known-pitfalls.md`：常见坑。

要求：

- 只记录长期有效、已验证的事实。
- 不记录一次性排查过程。
- 不记录未验证猜测。
- 不记录密钥、密码、客户隐私和敏感数据。

## 文档流转建议

一个 feature 推荐按以下顺序推进：

1. 写 `requirement.md`：记录原始需求。
2. 写 `demo/`：定义目标体验。
3. 写 `reviews/demo-review.md`：评审 demo。
4. 写 `prd.md`：定义产品方案。
5. 写 `reviews/prd-review.md`：评审产品需求。
6. 写 `technical.md`：分析 feature 技术背景和影响范围。
7. 写 `reviews/technical-review.md`：评审技术文档。
8. 写 `spec.md`：形成可执行技术规格。
9. 写 `reviews/spec-review.md`：评审技术规格。
10. 在 `docs/testcases/` 中新增或更新真实测试用例。
11. 在 `testcases.md` 中维护本 feature 的测试用例索引。
12. 写 `reviews/testcase-review.md`：评审测试覆盖。
13. 写 `plan/`：拆并行 plan tree 和最终联调节点。
14. 写 `reviews/plan-review.md`：评审计划和并行化合理性。
15. 实施代码或配置变更。
16. 在 `progress.md` 中记录执行状态和验证结果。
17. 如需求变化，更新 `changelog.md`。

## 边界总结

```text
docs/features/<feature-slug>/
```

维护本次需求的产品、demo、技术、spec、plan、评审、进度、变更记录和测试索引。

```text
docs/testcases/
```

维护长期、全局、可复用的测试用例库，按产品模块组织。

```text
docs/technical/
```

维护全局技术架构、规范、ADR、runbook 和稳定知识。
