# Grilling Domain Contract

This contract adapts `grill-with-docs` into the opc-develop Harness flow. Use it inside `product-brainstorm`; do not invoke an external skill as a black box.

## Product Grilling Gate

Before writing or updating `requirement.md`, stress-test the raw requirement until the feature can be explained without hidden product decisions.

- Walk the product decision tree branch by branch: scope, users and roles, key paths, states and errors, domain semantics, constraints, alternatives, acceptance signals, and follow-up boundaries.
- Resolve dependencies between decisions one at a time. Do not ask about a downstream choice until its upstream scope or semantic dependency is clear.
- Ask one question at a time when human input is required. Every question must include the recommended answer and the reason for that recommendation.
- If repository code, existing docs, previous feature artifacts, or attachments can answer a question, inspect them instead of asking the user.
- Use concrete scenarios to test fuzzy requirements, edge cases, role boundaries, permissions, empty states, conflicts, and failure paths.
- For meaningful product choices, compare 2-3 viable approaches with concise tradeoffs and one recommendation. Do not collapse ambiguous scope, UX, or product semantics into a single path without explaining why.

## Domain Modeling In Opc

Capture domain language while grilling, but respect opc branch and artifact rules.

- Challenge terms that conflict with existing project language. Prefer existing canonical terms from `docs/technical/knowledge/glossary.md`, `CONTEXT.md`, `CONTEXT-MAP.md`, feature docs, and source identifiers unless the user confirms a rename or semantic split.
- Sharpen vague or overloaded words into one canonical term. Record avoided aliases when they are likely to reappear.
- Only record terms specific to the product domain. Do not put general implementation concepts, libraries, utility patterns, or temporary UI labels into the domain glossary.
- During early brainstorming before the feature branch exists, keep domain updates as pending notes. Write project artifacts only after branch rules allow it.
- Prefer the opc Harness glossary path `docs/technical/knowledge/glossary.md` for project-wide terms. If the repository already uses `CONTEXT.md` or `CONTEXT-MAP.md`, follow the existing project convention and mention the chosen target in `requirement.md`.
- Use the feature `requirement.md` for feature-local semantics, unresolved terminology, and candidate glossary updates that are not yet stable project-wide language.

## Decision Records In Opc

Do not turn every brainstorm decision into an ADR. Create or propose an ADR only when all three are true:

1. The decision is hard to reverse.
2. The choice would surprise a future reader without context.
3. There was a real tradeoff between credible alternatives.

Use `docs/technical/decisions/ADR-000N-<slug>.md` unless the project already has a stricter ADR convention. Feature-local product choices that do not meet the ADR bar belong in `requirement.md` under alternatives, tradeoffs, and recommendation.

## Ready To Persist

The requirement is ready to persist only when all of the following are true:

- The problem, target user, and current scope can be summarized in one or two sentences.
- Independently shippable subsystems have been split, or the core slice and follow-up candidates are explicit.
- Goals and non-goals are paired tightly enough to prevent obvious scope creep.
- The key user paths cover the main path plus important empty, failure, permission, and conflict states for this stage.
- Core domain terms are stable or explicitly listed as blocking terminology questions.
- Constraints and assumptions are visible, including data source, compatibility, release, compliance, and existing-system constraints when relevant.
- Meaningful alternatives have tradeoffs and one recommendation, or the requirement explains why there is no meaningful choice.
- Acceptance signals are clear enough for PRD creation, even if detailed testcases will be written later.
- Code or documentation contradictions have been resolved, or are listed as blockers.
- Remaining open questions are non-blocking. If an answer could change scope, core behavior, or acceptance, stop and report a blocker instead of writing a completed requirement.

## Documentation Timing

- Preserve the original user or business wording in `requirement.md`.
- Append clarified facts as dated additions rather than rewriting history.
- Write stable feature facts, non-goals, paths, constraints, alternatives, tradeoffs, recommendation, and non-blocking open questions into `requirement.md`.
- Write stable project-wide terms to the chosen glossary target only after branch rules allow project artifact changes.
- Write ADRs sparingly and only after the ADR criteria above are met.
