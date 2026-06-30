# Language Adaptation Contract

All opc-develop skills must adapt user-visible language to the user's language context instead of enforcing a fixed default language.

## Default Language

- Use the language of the user's latest explicit request for user-visible dialogue, clarification questions, blockers, review reports, requirements, PRDs, technical designs, specs, testcases, plans, progress records, verification reports, release reports, and frontend prototype demo copy.
- If the user explicitly asks for a language, use that language.
- If project rules specify a language for artifacts, follow the project rules.
- If the user's language context is mixed or unclear, use the dominant language in the current request and keep technical identifiers unchanged.
- Do not produce bilingual output unless the user asks for it or the artifact itself is explicitly meant to be bilingual.

## Content That Must Preserve Source Form

- Preserve file paths, commands, code, config keys, variable names, API/DB fields, schema names, log excerpts, raw error text, third-party status values, brand names, and proper nouns.
- Do not translate fixed protocol values, including review status lines `**Status:** Approved` and `**Status:** Issues Found`, human acceptance status lines `**Human Acceptance:** Passed`, `**Human Acceptance:** Failed`, `**Human Acceptance:** Blocked`, and subagent status tokens `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, and `BLOCKED`.
- When quoting upstream raw requirements, preserve the original wording. Add explanations in the selected output language when needed.

## Templates And Headings

- English headings and examples in shared format files are structural hints, not a forced output language.
- Machine-parseable fields, status tokens, file names, and directory names remain as written; surrounding explanations follow the selected output language.
- Code comments, test names, and commit messages should follow the target project's existing language style.

## Blockers And Clarifications

- When blocking, asking questions, or explaining risks, use the selected output language to state missing inputs, violated gates, decisions that cannot be inferred, and the next human decision needed.
- Raw command output and logs may remain in their original language, but conclusions and judgments must follow the selected output language.
