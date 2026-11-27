# Approval invalidation

Single changes to the evidence a researcher approved, made on a copy of the run, followed by an attempt to start writing. Blocked: the writer made no model call. The changed evidence is then reviewed again with the critics' recorded verdicts and, if the review accepts it, approved. The profile file is not changed here.

Seed 0, up to 3 edits per file. 21 files in the evidence hash, 1 frozen protocol(s). Unchanged copy: writing started.

| what changed | changes | writing blocked | refused by the approval check | review refuses the changed evidence | reviewed and approved again | then writing starts |
|---|---|---|---|---|---|---|
| approval record | 3 | 3 | 3 | 0 | 3 | 3 |
| argument | 23 | 23 | 23 | 6 | 17 | 17 |
| literature and brief | 8 | 8 | 8 | 2 | 6 | 6 |
| protocol | 8 | 8 | 8 | 8 | 0 | 0 |
| scorer | 4 | 4 | 4 | 3 | 1 | 1 |
| training code | 28 | 28 | 28 | 25 | 3 | 3 |
| training record | 38 | 38 | 38 | 32 | 6 | 6 |
| all approved evidence | 112 | 112 | 112 | 76 | 36 | 36 |

The second review uses the approved argument and the critics' recorded verdicts, so it shows what the deterministic review checks and the gate do, not what a critic would say.

After each change was undone, writing started again in 114 of 114 cases.

Engine source other than the training entry point and the scorer: 2 of 2 changes blocked. Such a file is hashed only by a frozen protocol.

## Why writing stopped

| reason | changes |
|---|---|
| Evidence/profile/code changed; scientific review and approval are stale | 62 |
| Candidate snapshot was modified | 18 |
| Review artifacts changed; review again | 17 |
| Missing or unreadable candidate <file> | 6 |
| Scientific argument or deterministic evidence checks are incomplete | 6 |
| Required input is missing: <file> | 2 |
| Invalid writing release | 2 |
| Writing blocked: READY_TO_WRITE. Complete scientific review and author approval. | 1 |

## Why the second review refused the changed evidence

| reason | changes |
|---|---|
| INSUFFICIENT_EVIDENCE | 38 |
| ReviewBlocked: Candidate snapshot was modified | 18 |
| ReviewBlocked: Missing or unreadable candidate <id> | 6 |
| ReviewBlocked: Invalid claim graph: <statement>: numbers lack explicitly bound measuremen | 6 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown papers ['arXiv:2607.29078', 'arX | 1 |
| ReviewBlocked: Duplicate/invalid run id: protocol_<id>_corrupt_prefix | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown papers ['arXiv:1606.07947']; rel | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown measurement protocol:<id>::val_i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: numbers ['32'] are not written in ['scor | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: numbers ['500'] are not written in ['sco | 1 |
| ReviewBlocked: Required input is missing: /private<copy>/engine/engines/seq_distill/prepare.py | 1 |
| ReviewBlocked: Required input is missing: /private<copy>/engine/engines/seq_distill/train.py | 1 |
