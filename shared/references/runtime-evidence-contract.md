# Runtime Evidence Contract

Every implementation, local verification, and release verification phase must preserve evidence sufficient for debugging and audit.

## Log

Record log path, query command, request/task/trace ids, and relevant excerpts or report files.

## DB

Record DB access mode, query file or query summary, expected state, observed state, and cleanup status. Do not record secrets or private production data.

## Trace

Record trace id propagation, trace query entrypoint, trace link or exported trace file, and relationship to logs and DB records.

Evidence paths must be written to `progress.md` and testcase reports.

Fresh evidence is required before claiming completion, verification, acceptance, release readiness, or publication. Follow `evidence-before-claim.md` when an implementation, verification, or release skill reports status.
