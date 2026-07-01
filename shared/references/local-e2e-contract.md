# Local E2E Contract

`local-e2e-verify` is the local black-box verification gate. It must read these project documents:

- `docs/technical/runbooks/local-dev.md`
- `docs/technical/standards/testing.md`
- Approved `docs/features/<feature-slug>/demo/prototype.md` and frontend prototype evidence when the feature is UI-facing
- Relevant `docs/testcases/<product-module>/` cases
- Runtime evidence entries for Log, DB, and Trace
- Risk spike, thin-slice testcase, and capability readiness expectations when `risk-and-readiness-contract.md` marks the feature as high risk

If `local-dev.md` or `testing.md` is missing required commands, block instead of guessing.

Verification must execute or account for relevant black-box E2E, acceptance, smoke, and regression cases. Verification must record:

- Start/stop/status/log commands used.
- Environment and commit.
- Environment capability readiness result: intended checkout/worktree, required services, dependency state, fixture/mock state, provider handling, and report paths.
- Testcase paths executed.
- Demo parity evidence for UI-facing work, such as screenshots, interaction recordings, or Computer Use/browser notes comparing runtime behavior to the approved demo.
- Test report path under `docs/testcases/<product-module>/reports/`.
- Screenshots, logs, DB query summaries, or trace links.
- Evidence authenticity labels for each major claim, such as `mock passed`, `seeded passed`, `local real service passed`, `external provider passed`, `human accepted`, `long-run passed`, `not run`, `pending`, or `blocked`.
- Failures, fixes, reruns, and residual risk.

Do not claim local verification passed unless the documented commands produced fresh successful evidence for the current code revision. If verification fails for a pure implementation defect, route through `debug-failure` instead of guessing a fix.

Do not upgrade a lower-realism result into a higher-realism claim. Seeded or mock verification may pass while external provider, real hardware, human acceptance, or long-run verification remains `pending`.

When runtime UI differs from the approved demo, classify the failure using `demo-implementation-alignment.md`: implementation defect, spec/plan defect, or upstream product/demo change. Do not pass local verification with unexplained demo divergence.
