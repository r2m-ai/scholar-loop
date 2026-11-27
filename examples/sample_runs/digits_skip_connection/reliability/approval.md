# Approval invalidation

Single changes to the evidence a researcher approved, made on a copy of the run, followed by an attempt to start writing. Blocked: the writer made no model call. The changed evidence is then reviewed again with the critics' recorded verdicts and, if the review accepts it, approved. The profile file is not changed here.

Seed 0, up to 3 edits per file. 54 files in the evidence hash, 1 frozen protocol(s). Unchanged copy: writing started.

| what changed | changes | writing blocked | refused by the approval check | review refuses the changed evidence | reviewed and approved again | then writing starts |
|---|---|---|---|---|---|---|
| approval record | 3 | 3 | 3 | 0 | 3 | 3 |
| argument | 27 | 27 | 27 | 8 | 19 | 19 |
| literature and brief | 8 | 8 | 8 | 2 | 6 | 6 |
| protocol | 8 | 8 | 8 | 8 | 0 | 0 |
| scorer | 3 | 3 | 3 | 2 | 1 | 1 |
| training code | 68 | 68 | 68 | 65 | 3 | 3 |
| training record | 172 | 172 | 172 | 136 | 36 | 36 |
| all approved evidence | 289 | 289 | 289 | 221 | 68 | 68 |

The second review uses the approved argument and the critics' recorded verdicts, so it shows what the deterministic review checks and the gate do, not what a critic would say.

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

## Why the second review refused the changed evidence

| reason | changes |
|---|---|
| INSUFFICIENT_EVIDENCE | 120 |
| ReviewBlocked: Candidate snapshot was modified | 48 |
| ReviewBlocked: Missing or unreadable candidate <id> | 20 |
| ReviewBlocked: Invalid claim graph: <statement>: numbers lack explicitly bound measuremen | 8 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown papers ['arXiv:2510.01796'] | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0001' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0003' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0002' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence ['exp_0004']; setup_exp | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0005' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0006' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0007' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0008' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0012' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0013' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0014' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0015' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0016' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0017' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0021' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0022' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0023' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0024' is not an i | 1 |
| ReviewBlocked: Duplicate/invalid run id: protocol_<id>_resid_lr002 | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown papers ['arXiv:2104.07393'] | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown measurement protocol:<id>::val_t | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: numbers ['80'] are not written in ['scor | 1 |
| ReviewBlocked: Required input is missing: /private<copy>/engine/engines/torch_vision/prepare.py | 1 |
| ReviewBlocked: Required input is missing: /private<copy>/engine/engines/torch_vision/train.py | 1 |
