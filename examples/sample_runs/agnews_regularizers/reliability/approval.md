# Approval invalidation

Single changes to the evidence a researcher approved, made on a copy of the run, followed by an attempt to start writing. Blocked: the writer made no model call. The profile file is not changed here.

Seed 0, up to 3 edits per file. 49 files in the evidence hash, 0 frozen protocol(s). Unchanged copy: writing started.

| what changed | changes | writing blocked | refused by the approval check |
|---|---|---|---|
| approval record | 3 | 3 | 3 |
| argument | 28 | 28 | 28 |
| literature and brief | 8 | 8 | 8 |
| scorer | 4 | 4 | 4 |
| training code | 52 | 52 | 52 |
| training record | 179 | 179 | 179 |
| all approved evidence | 274 | 274 | 274 |

After each change was undone, writing started again in 276 of 276 cases.

Engine source other than the training entry point and the scorer: 0 of 2 changes blocked. Such a file is hashed only by a frozen protocol.

## Why writing stopped

| reason | changes |
|---|---|
| Evidence/profile/code changed; scientific review and approval are stale | 190 |
| Candidate snapshot was modified | 36 |
| Review artifacts changed; review again | 17 |
| Missing or unreadable candidate <file> | 15 |
| Scientific argument or deterministic evidence checks are incomplete | 11 |
| Required input is missing: <file> | 2 |
| Invalid writing release | 2 |
| Writing blocked: READY_TO_WRITE. Complete scientific review and author approval. | 1 |
