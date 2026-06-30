# PRD Format

`prd.md` must define product truth, not implementation details.

Use this structure:

```markdown
# PRD: <feature title>

> Source: requirement.md
> Demo: demo/prototype.md
> Status: Draft

## 1. Background
## 2. Users and Scenarios
## 3. Goals
## 4. Non-goals
## 5. Functional Requirements
## 6. User Flow and States
## 7. Demo Alignment Contract
## 8. Field, Permission, and Business Rules
## 9. Error and Empty Paths
## 10. Analytics or Data Definitions
## 11. Acceptance Criteria
## 12. Risks and Open Questions
```

Every acceptance criterion must be testable and later mapped to at least one testcase.

For UI-facing features, `## 7. Demo Alignment Contract` must summarize the approved demo's binding layout hierarchy, interaction model, key states, and any intentional deviations. If a demo decision is not represented in the PRD, state why it is non-binding or out of scope. Silent demo-to-PRD loss is not allowed.
