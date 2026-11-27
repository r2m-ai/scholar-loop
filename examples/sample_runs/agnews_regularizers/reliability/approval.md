# Approval invalidation

Single changes to the evidence a researcher approved, made on a copy of the run, followed by an attempt to start writing. Blocked: the writer made no model call. The changed evidence is then reviewed again with the critics' recorded verdicts and, if the review accepts it, approved. The profile file is not changed here.

Seed 0, up to 3 edits per file. 49 files in the evidence hash, 0 frozen protocol(s). Unchanged copy: writing started.

| what changed | changes | writing blocked | refused by the approval check | review refuses the changed evidence | reviewed and approved again | then writing starts |
|---|---|---|---|---|---|---|
| approval record | 3 | 3 | 3 | 0 | 3 | 3 |
| argument | 28 | 28 | 28 | 11 | 17 | 17 |
| literature and brief | 8 | 8 | 8 | 1 | 7 | 7 |
| scorer | 4 | 4 | 4 | 1 | 3 | 3 |
| training code | 52 | 52 | 52 | 50 | 2 | 2 |
| training record | 179 | 179 | 179 | 146 | 33 | 33 |
| all approved evidence | 274 | 274 | 274 | 209 | 65 | 65 |

The second review uses the approved argument and the critics' recorded verdicts, so it shows what the deterministic review checks and the gate do, not what a critic would say.

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

## Why the second review refused the changed evidence

| reason | changes |
|---|---|
| INSUFFICIENT_EVIDENCE | 112 |
| ReviewBlocked: Candidate snapshot was modified | 36 |
| ReviewBlocked: Missing or unreadable candidate <id> | 15 |
| ReviewBlocked: Invalid claim graph: <statement>: numbers lack explicitly bound measuremen | 11 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0001' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0002' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0003' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0004' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0005' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0006' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0007' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0008' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0010' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0009' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0011' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0012' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0013' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0014' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0015' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0016' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0017' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence ['exp_0018'] | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0019' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0020' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0021' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0022' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0023' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0024' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0025' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0027' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0026' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0028' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0029' is not an i | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown evidence: 'exp_0030' is not an i | 1 |
| ReviewBlocked: Duplicate/invalid run id: exp_0030 | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: unknown papers ['arXiv:1603.02754']; rel | 1 |
| ReviewBlocked: Required input is missing: /private<copy>/engine/engines/text_cls/prepare.py | 1 |
| ReviewBlocked: Invalid claim graph: <statement>: numbers ['128'] are not written in ['tra | 1 |
| ReviewBlocked: Required input is missing: /private<copy>/engine/engines/text_cls/train.py | 1 |
