# Approval invalidation

Single changes to the evidence a researcher approved, made on a copy of the run, followed by an attempt to start writing. Blocked: the writer made no model call. The profile file is not changed here.

Seed 0, up to 3 edits per file. 54 files in the evidence hash, 1 frozen protocol(s). Unchanged copy: writing started.

| what changed | changes | writing blocked | refused by the approval check |
|---|---|---|---|
| approval record | 3 | 3 | 3 |
| argument | 27 | 27 | 27 |
| literature and brief | 8 | 8 | 8 |
| protocol | 8 | 8 | 8 |
| scorer | 3 | 3 | 3 |
| training code | 68 | 68 | 68 |
| training record | 172 | 172 | 172 |
| all approved evidence | 289 | 289 | 289 |

After each change was undone, writing started again in 291 of 291 cases.

Engine source other than the training entry point and the scorer: 2 of 2 changes blocked. Such a file is hashed only by a frozen protocol.

## Why writing stopped

| reason | changes |
|---|---|
| Evidence/profile/code changed; scientific review and approval are stale | 191 |
| Candidate snapshot was modified | 48 |
| Missing or unreadable candidate <file> | 20 |
| Review artifacts changed; review again | 19 |
| Scientific argument or deterministic evidence checks are incomplete | 8 |
| Required input is missing: <file> | 2 |
| Invalid writing release | 2 |
| Writing blocked: READY_TO_WRITE. Complete scientific review and author approval. | 1 |
