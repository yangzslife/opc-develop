# Demo Implementation Alignment

Approved demo is the binding product-experience reference for UI-facing features until an upstream artifact explicitly revises it and the matching review gate is rerun. In opc-develop, the approved demo is the running frontend prototype plus its preview evidence and mock inventory, not a standalone static HTML file.

## What Is Binding

For UI-facing work, downstream artifacts and implementation must preserve the approved demo's:

- Primary runtime surface: the product shell, route, page, header, sidebar, input area, workspace, or other existing UI surface where the feature was demonstrated.
- Page or panel layout hierarchy.
- Primary information architecture and visual grouping.
- User flow order and navigation shape.
- Key interaction model, including click, selection, edit, submit, cancel, confirm, empty, loading, error, permission, and success states.
- Important copy intent, control affordances, and state transitions.
- Responsive behavior that is visible or implied by the demo.

## What Is Not Binding

The demo does not bind production architecture:

- Framework, component library, routing, API, auth, persistence, state management, storage, or deployment choices.
- Frontend prototype mock data internals.
- Exact pixel values when the project design system requires adaptation.

Prototype frontend code should be reused where it is compatible with production architecture. Prototype mocks are explicitly temporary and must be retired through `prototype-mock-retirement-contract.md`.

## Allowed Deviations

Any intentional deviation from the approved demo's product experience must be explicit:

1. `prd.md` records the product-level deviation and why it is acceptable.
2. `technical.md` records any technical constraint that forces the deviation.
3. `spec.md` turns the final approved behavior into executable UI/component contracts.
4. The matching review gate is rerun after the artifact changes.

Do not silently replace the demo's layout or interaction model during implementation. If the implementer discovers that the demo cannot be implemented safely, stop and route to the earliest affected artifact:

- `create-demo` when the target experience itself needs to change.
- `create-prd` when product behavior or acceptance criteria need to change.
- `create-technical` when a technical constraint changes the feasible product experience.
- `create-spec` when executable UI/component contracts are incomplete.
- `create-plan` when implementation tasks do not include the required UI parity work.

## Shell Integration Drift

If a demo feature belongs in an existing product shell, downstream artifacts must preserve that shell placement. Do not convert a shell-integrated demo into a standalone page, and do not treat a query-param-only demo root as sufficient evidence when the approved product experience depends on normal app navigation.

For UI features that touch existing navigation/header/sidebar/input/workspace surfaces:

- `create-prd` must name the real entry and exit surfaces.
- `create-technical` must map those surfaces to production modules.
- `create-spec` must define component contracts for those surfaces.
- `create-testcases` must include black-box cases through the normal product shell.
- `tdd-coding` must remove or gate any demo-only route after the real shell path works.

## Downstream Responsibilities

- `create-prd`: extract a Demo Alignment section from the approved frontend prototype and preview evidence.
- `create-technical`: map the prototype experience to production modules and identify technical constraints.
- `create-spec`: define executable UI/component contracts, accepted deviations, and prototype mock retirement details.
- `create-testcases`: create black-box visual and interaction cases for demo-critical flows.
- `create-plan`: include demo-derived implementation tasks, mock retirement work boundaries, and verification signals.
- `tdd-coding`: provide approved demo context and mock retirement plan to implementer subagents, require component/UI parity checks where practical, and verify no prototype mock remains in production runtime.
- Implementation review: compare actual code and tests against approved demo context and mock retirement plan during spec compliance.
- `local-e2e-verify`: capture runtime screenshots or interaction evidence and compare against the approved demo and black-box testcases.

## Failure Classification

If the shipped UI diverges from the approved demo:

- Treat it as an implementation defect when PRD/spec/plan already preserve the demo behavior.
- Treat it as a spec or plan defect when the demo behavior was lost before implementation.
- Treat it as a product/design defect only when the approved demo is no longer the desired experience.
