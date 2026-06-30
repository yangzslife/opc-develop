# Requirement Format

`docs/features/<feature-slug>/requirement.md` is the raw requirement and brainstorm record.

It must include:

- Original user or business input, preserving source wording.
- Feature slug in numbered `<number>-<feature-name>` format, such as `1-knowledge-base` or `105-web-search-prefer-native`.
- Background and problem.
- Goals and non-goals.
- Key user paths.
- Constraints and assumptions.
- Open questions and human decisions.
- Brainstorm summary with alternatives and tradeoffs.
- Grilling summary showing the major decision branches explored, resolved answers, recommendation, and any remaining non-blocking questions.
- Domain language notes: confirmed product terms, avoided aliases when useful, terminology conflicts, and glossary follow-ups.
- Acceptance signals clear enough for PRD creation.

## Product Brainstorm Discipline

Before writing or updating `requirement.md`, perform a scope decomposition gate:

- If the request spans multiple independently shippable subsystems, split it into separate feature candidates before continuing.
- If the request contains a small core plus speculative future work, keep the core in scope and record future work as non-goals or follow-up candidates.
- Ask one critical product question at a time only when the answer blocks scope, behavior, or acceptance.

Then run the grilling gate from `grilling-domain-contract.md`:

- Walk the product decision tree branch by branch instead of only filling a template.
- Inspect code, existing docs, prior feature artifacts, and attachments before asking the user when they can answer the question.
- Ask one question at a time, and include a recommended answer plus rationale for every question.
- Use concrete scenarios to test fuzzy product language, edge cases, permissions, empty states, conflicts, and failure paths.
- Keep grilling until shared understanding is reached, or stop when a blocking question could change scope, core behavior, or acceptance.

For non-trivial product decisions, include 2-3 viable approaches, concise tradeoffs, and one recommended approach. Do not present a single path when scope, UX, or product semantics are genuinely ambiguous.

## Domain And Decision Capture

During brainstorming, capture domain language and durable decisions using the opc-adapted rules in `grilling-domain-contract.md`:

- Put feature-local semantics, unresolved terms, and candidate glossary updates in `requirement.md`.
- Promote stable project-wide terms to the project glossary target only when branch and project rules allow it.
- Promote an ADR only when the decision is hard to reverse, surprising without context, and the result of a real tradeoff.
- If an ADR is not justified, keep the decision in the brainstorm summary, alternatives, tradeoffs, or recommendation.

## Requirement Self-Review

Before finishing, confirm:

- No TODO/TBD/FIXME placeholders remain.
- The grilling gate reached shared understanding, or unresolved blocking questions are explicitly reported instead of being buried in the requirement.
- Goals and non-goals are explicit.
- Key user paths and acceptance signals are clear enough for PRD creation.
- Hidden product decisions are either resolved or listed as blocking questions.
- Core terminology is stable, or terminology questions are listed as blockers when they affect scope, behavior, or acceptance.
- Alternatives, tradeoffs, recommendation, glossary follow-ups, and ADR follow-ups are present when applicable.
- The requirement does not prematurely dictate implementation details.

Never rewrite original requirements into implementation language. Add clarifications under dated append-only sections.
