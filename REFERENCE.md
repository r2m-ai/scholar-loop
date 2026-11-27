# ScholarLoop reference

The details behind the [README](README.md): command-line modes, review and release rules,
final-test controls, comparison harnesses and environment variables.

## Driving a run from the command line

The web UI runs the same stages as background jobs.

```bash
# 1 · ideation: steer, literature review, direction map, ideas, tournament, your pick
python -m scholarloop.ideation --profile profiles/digits-mlp.yaml \
    --topic "regularization recipes for small MLPs" --out runs/s1

# 2 · experiments: the campaign adopts the idea you picked
SCHOLARLOOP_HANDOFF=runs/s1/handoff.json SCHOLARLOOP_OUT=runs/s1 \
    python examples/run_to_paper.py
```

Scientific review, your approval, then writing:

```bash
python -m scholarloop.review review  --profile profiles/digits-mlp.yaml \
    --ledger runs/s1/experiments.jsonl --registry runs/s1/registry --research runs/s1 --out runs/s1
python -m scholarloop.review approve --profile profiles/digits-mlp.yaml \
    --ledger runs/s1/experiments.jsonl --registry runs/s1/registry --research runs/s1 --out runs/s1 \
    --author Researcher --review-hash EXACT_REVIEW_HASH
python -m scholarloop.writing --profile profiles/digits-mlp.yaml \
    --ledger runs/s1/experiments.jsonl --registry runs/s1/registry --research runs/s1 --out runs/s1
```

### Scripted and deeper ideation modes

`--steer examples/steer.json` (or `--interest "…" --hunch "…" --avoid "…"`) gives the steer
without a terminal. The run then stops at the direction map; `--directions 1,3`,
`--own-direction "…"` and `--direction-note "…"` record your choice and continue.
`--stop-after review|directions|ideas` writes that page and exits for a human. `--feedback "…"`
and `--select 2` resume from another process. `--auto` chooses every mapped direction and the
tournament's top idea; `--unsteered` waives the steer. The automatic pick is logged as
automated, and the waiver is logged under your name.
`--deep --brief examples/research_brief.json` generates ideas by independent strategies
(mechanism, transfer, contradiction) with retrieval per idea.
`--decision reject|refine|merge|revive --idea-ids …` records your decisions against stable
idea IDs. `python -m scholarloop.ideation.pilot` runs a small validation-only pilot across
several ideas before you commit to one.

A meta-reviewer turns the judges' recurring complaints into at most five recommendations. Each
must cite the matches that show it, and the next round of ideas is written against them.

## Details by topic

<details>
<summary><b>Candidates, snapshots and what the Reasoner sees</b></summary>

The Reasoner and Director receive a bounded validation evidence view: configurations, scores,
seed/fold identities, failures and the frontier. It excludes held-out scores and scientific
control runs. Observed losing regions are soft warnings, not causal exclusions; repeated
fidelity tiers count once per candidate when deriving these associations.

Each new run records a `candidate_id` and a separate `run_spec`. Candidate snapshots in
`registry/candidates/` bind the requested configuration, local engine Python sources, frozen
scorer and declared execution context. Different implementations remain distinct even at
identical knobs; changing seed or fidelity creates a different run of the same candidate. The
Reasoner sees the frontier's source and inherits its code and requested knobs by default,
including after restarting a campaign. `base: "root"` explicitly starts from repository code and
profile defaults. Changing scorer or dependencies requires a new root candidate. Legacy runs
without snapshots remain readable but cannot supply inherited implementations.

Scientific review includes these snapshots and rejects missing or modified candidate files. They
document execution inputs; they do not certify undeclared data, external dependencies or
scientific validity. Frontier selection and convergence tracking use a common fidelity and
seed/fold scope, and prediction calibration uses matched reference observations when available.
The funnel's SEM margin is a resource-allocation heuristic, not a significance test.

Loop components: `Orchestrator.population_step(k, max_workers)` (parallel population funnel),
`Governor(max_cost, max_rounds, dry_patience)` (self-stopping), `CalibrationLog`
(predict-then-verify), `SkillLibrary.render(query=…)` (relevance-ranked, time-decaying lessons).

</details>

<details>
<summary><b>Scientific review, releases and the experiment agenda</b></summary>

Optional `--critic-model ROLE=MODEL` mappings choose different reviewer models; every critic
must answer evidence questions for each claim. `--max-llm-calls` caps cumulative CLI requests,
including retries, rather than dollars. Old v1 releases require re-review under the v2 contract.
Changed evidence, code, declared data or research scope invalidates a release. An existing
writing session bound to an older release needs a new output directory and `--review-dir`.

For `NEEDS_EXPERIMENTS`, use `python -m scholarloop.experiment.agenda plan` with the same
profile, ledger, registry, research and out arguments. Inspect the frozen protocol, then use
`run` with `--protocol-hash HASH --author Researcher` and re-run scientific review.

Use `SCHOLARLOOP_RESUME=1` to continue a campaign containing frozen protocols; fresh mode
refuses to erase that evidence. Protocol hashes detect changed inputs, not hostile execution.
`run_to_paper.py` pauses for the author's decision, including in unattended mode;
`SCHOLARLOOP_WRITING=oneshot` keeps the single-call writer behind the same gate.

In reviewed writing, claim dependencies and evidence IDs are validated, and a separate semantic
reviewer checks attribution, scope and mandatory limitations. A drafted section that drops one
of its agreed key points is flagged in the draft's notes.

</details>

<details>
<summary><b>Final-test controls and attempt logs</b></summary>

Final-test access closes that campaign to new exploration and experiment plans, including when
test scoring fails. A previously frozen confirmation protocol may finish its planned conditions;
review and writing may still inspect its results. This is a ledger-level guard, not OS isolation
or proof that a reused dataset is statistically independent. Historical campaigns containing
test results are also closed to further exploration.

Before a confirmation run starts, the runner persists and fsyncs a test-access receipt beside
its ledger in `<ledger>.test-access/`. Keep this directory with the ledger when moving a
campaign. An incomplete receipt or a receipt without its matching ledger result closes execution
and blocks scientific review; an interrupted run is never automatically replayed. Completed
receipts are part of the review snapshot and permit the original protocol to continue. Recovery
requires inspecting the run and reconciling its real evidence; deleting a receipt or restarting
with the same test data does not restore statistical independence.

Confirmation continuation is validated at the public runner boundary: a claimed protocol must
exist under its content hash and match the frozen context, condition, effective code and config,
seeds, fidelity and test-access setting. Each condition has one canonical run ID. Reusing a
protocol string cannot authorize another candidate or a repeat; exploration artifact caches
cannot be supplied to protocol confirmation runs. A standalone explicit confirmation without a
protocol remains a single access that closes its campaign.

Agent attempts are persisted as `*.agents.jsonl` by experiment, ideation, review and writing
sessions. Each attempt has a durable start event, input and schema fingerprints, model identity,
and a finish event containing the structured output, validation errors, status and elapsed time.
Raw prompts are not stored. An unmatched start denotes an unfinished attempt; provider errors
and invalid JSON remain visible. Client usage snapshots are cumulative and must not be treated
as per-attempt costs when requests share a client. `python -m scholarloop.evaluation` reports
these logs, including corrupt tails.

</details>

<details>
<summary><b>Search comparisons and multi-task suites</b></summary>

Search comparisons freeze declared profile and engine inputs and settings in
`comparison_plan.json`; resuming with different settings is rejected. Interrupted campaign
directories are preserved, failed campaigns are recorded, and budget-skipped repeats remain in
the reported denominator. Score intervals describe observed outcomes only. Run-matched campaigns
reserve each training attempt before dispatch and never exceed their configured count. Failed
and interrupted attempts remain charged; cached models do not consume a new reservation.
Accounting is persisted beside the ledger as `*.training_budget.json`. This caps training
attempts, not GPU seconds or financial cost. `compare_search.py --max-calls` caps model requests
persistently across retries and repeats (default 100); `--max-cost` is an estimated stop
threshold between campaigns. Unknown prices block cost-limited campaigns.

For multiple tasks, use `python -m scholarloop.experiment.suite --manifest suite.json --out runs/suite`.
The manifest has `version: 1` and a `tasks` array. Every task supplies `id`, `split`
(`development` or `evaluation`), `dataset_group`, `profile`, `seeds` and `train_budget`. Profile
paths are relative to the manifest. Both partitions are required; shared dataset groups or
profile dataset names across partitions are rejected. The suite freezes its declared inputs,
retains every planned repeat, and keeps per-task metrics separate. The CLI runs the
random-search baseline without API calls. Programmatic model arms must provide an orchestrator
with a persistent `CallLimitedLLM` budget. Dataset declarations and disjoint labels do not
establish real-world independence.

</details>

<details>
<summary><b>Research iterations after preliminary results</b></summary>

`ResearchCycle` separates scientific progress from parameter-search progress. Each assessment
reads the complete current dossier (including failures and negative results) and the latest five
iteration records, with older records retained on disk and an explicit omission count. It asks
whether the evidence is insufficient, promising within scope, or contradictory within scope;
these are provisional model assessments, not verified scientific conclusions.

A stable issue register is reconstructed from all rounds and supplied independently of the
five-round history window. Every assessment must update every tracked concern exactly once.
Proposing `addressed_pending_review` requires an existing dossier evidence ID absent when the
issue opened, plus a rationale. This checks provenance, not whether evidence logically resolves
the concern: addressed proposals remain visible and still require scientific review. Reworded
concerns remain separate rather than silently merging away uncertainty.

The next-step recommendation must name the primary and competing explanations, a discriminating
comparison, contrasting predictions, a falsifying outcome, claim limits and a training budget.
When issues already exist, an experimental recommendation must reference at least one tracked
issue ID and select a named competing explanation. It must state prospective decisions for
primary-supporting, alternative-supporting and inconclusive outcomes, along with what the
experiment cannot resolve. These fields accompany the recommendation into critic review and the
experiment planner; the review hash and frozen protocol include the original recommendation.
Critic requests take precedence over the provisional recommendation.

Iteration-derived protocols additionally require a `discrimination` mapping: reference and
treatment names, the reviewed competing explanation, why the contrast is informative, controlled
factors, residual confounds, inconclusive outcomes and departures from the recommendation.
Identical executable configurations for an ablation, falsification or boundary test are
rejected. This is a structural check, not a causal certificate.

Each reassessment must appraise every protocol in the current dossier, citing its protocol ID
and contrasting observations with the frozen predictions. Missing derived analysis requires
`execution_incomplete`; incomplete comparisons cannot favor either explanation. Actions include
debugging, replication, ablation, falsification, boundary tests, pivoting and stopping.
Recommendations cannot execute experiments, issue author approval or open the final test.

```bash
python -m scholarloop.experiment.research_cycle \
  --profile profiles/digits-mlp.yaml --ledger runs/study/experiments.jsonl \
  --registry runs/study/registry --out runs/study \
  --question "Does the mechanism explain the validation improvement?" \
  --max-training-attempts 12

python -m scholarloop.review review \
  --profile profiles/digits-mlp.yaml --ledger runs/study/experiments.jsonl \
  --registry runs/study/registry --out runs/study \
  --iteration runs/study/research_iterations.json
```

Review rejects a recommendation if its evidence snapshot is stale. Accepted experimental
requests proceed through the experiment agenda: freeze the protocol, execute its conditions,
reassess the new evidence, and review again. This closes a research iteration path; it does not
establish that the policy improves itself.

Pairwise ideation ranking receives bounded retrieved abstracts, provisional novelty comparisons,
the research brief and prior dissent. Position-swapped judgments and omission markers remain
explicit, and match records bind the evidence context by hash.

</details>

<details>
<summary><b>Controlled research-decision development harness</b></summary>

A free synthetic harness (no model, no training) for developing evaluations of research
decisions:

```bash
python -m scholarloop.experiment.decision_bench \
  --out runs/decision-development --repeats 3 --seed 0 --budget 3
```

Four single-cause task families share similar preliminary gains: leakage, extra compute,
population-specific effects, and gains that survive the three available controls. Policies
receive a public task plus their observed intervention results. The evaluator holds the truth
and scores decisions without a model as judge. Budget units are synthetic intervention costs.
The runner compares accept-all, abstain-all, fixed-order and random-order controls on the same
tasks and budget. `plan.json` freezes task generation, actions, budget, arms and implementation
hash; `report.json` retains every episode, failure, observation and decision. Failed and
exhausted episodes remain in the accuracy denominator.

This is an evaluator development fixture, not evidence that ScholarLoop improves research. The
full `ResearchCycle` is not yet a benchmark arm. Trusted in-process policies have only an
API-level information boundary. Reports contain truth labels and must not be fed back into an
agent evaluated on the same tasks.

**Model-policy ablation (uses the API, not part of tests):**

```bash
python -m scholarloop.experiment.decision_policy \
  --out runs/decision-model-development --model YOUR_MODEL_ID \
  --repeats 3 --budget 3 --max-calls 8
```

`plain` and `structured` policies use the same model, response schema, budget and per-episode
request cap; only their system instructions differ. `--max-calls` applies separately to each
task and arm, including schema-repair retries: three repeats, four families and two arms reserve
at most 192 requests. Prompts, schema, model, implementation and evaluator hashes are frozen with
the plan. Completed episodes are reused; an episode started without a saved result is retained
as interrupted and never silently rerun.

Add `--arms plain,structured,iteration` to include a stateful component arm that reuses the
production `IterationReviewer` validation and cross-round issue replay on explicitly marked
synthetic evidence. It evaluates the reviewer and state component, not the entire research
cycle, critic panel, frozen-protocol execution or manuscript workflow. With three arms the
maximum is 288 requests. No paid model comparison has been performed.

</details>

<details>
<summary><b>Environment variables for <code>examples/run_to_paper.py</code></b></summary>

| Variable | Meaning |
|---|---|
| `SCHOLARLOOP_OUT` | output directory (default `runs/live`) |
| `SCHOLARLOOP_PROFILE` | `profiles/<name>.yaml` (default `digits-mlp`) |
| `SCHOLARLOOP_MODEL` | model id (default `claude-opus-5-5`) |
| `SCHOLARLOOP_HANDOFF` | a research session's `handoff.json`; the campaign adopts its idea |
| `SCHOLARLOOP_STEPS`, `SCHOLARLOOP_POPULATION`, `SCHOLARLOOP_MAX_WORKERS` | rounds, ideas per round, parallel smoke runs |
| `SCHOLARLOOP_DRY_PATIENCE` | stop after this many rounds without a frontier improvement |
| `SCHOLARLOOP_MAX_COST` | estimated dollar threshold, checked between rounds and stages |
| `SCHOLARLOOP_WRITING` | `session` (interactive on a terminal), `auto`, or `oneshot` |
| `SCHOLARLOOP_PAPER_ONLY` | skip the campaign and write up the saved ledger |
| `SCHOLARLOOP_RESUME` | continue the saved campaign |
| `SCHOLARLOOP_PERSIST_SKILLS` | keep lessons in `~/.scholarloop/skills/<domain>` across campaigns |

</details>

## Measurements

Measured on the three recorded runs in [`examples/sample_runs/`](examples/sample_runs/), all with `claude-opus-5-5`.

The system's own simulated reviewers scored the three papers 2.2, 2.7 and 2.7 out of 10 and
rejected all three, citing one small task each, few seeds, and comparisons on validation data.

### Do the checks catch faults?

`scholarloop.reliability` takes artifacts the checks accepted, changes one thing at a time, and
runs each variant through the production check: 1,627 injected faults over the three runs.

| Kind of fault | Example | Distillation | AG News | Digits |
|---|---|---|---|---|
| Fabrication | a citation, run id or number that does not exist | 257 of 257 | 360 of 360 | 354 of 354 |
| Misattribution | a real measurement in the wrong place; "lower" flipped to "higher" | 77 of 179 (43%) | 123 of 221 (56%) | 137 of 256 (54%) |
| Clean artifact rejected | an unchanged artifact | 0 of 12 | 0 of 15 | 0 of 14 |

A check that looks up whether something exists cannot tell whether it is used correctly. A
number moved to the wrong claim was caught in 93 to 100% of cases; a flipped direction inside a
drafted section never was. The study also exposed two real holes in the checks, both now closed.

The reports behind this table are in `examples/sample_runs/*/reliability/injection.md`. Injection
needs no model and costs nothing, so you can run it again on a recorded run:

```bash
python -m scholarloop.reliability inject --profile profiles/seq-distill.yaml \
  --run examples/sample_runs/distillation_on_vs_off_policy --recorded-release --out runs/inject
```

The other two runs use `profiles/agnews-bow.yaml` and `profiles/digits-mlp.yaml`. A release is
tied to the machine and paths of the run that produced it, so `--recorded-release` checks the
copy in this repository against its approved evidence as recorded. On your own run, leave the
flag out, or use Evaluation & Tools in the web UI.

### Does a change to the evidence void the approval?

An approval is stored with a hash of the evidence it was given for. `scholarloop.reliability
approval` copies a run, changes one record at a time, and starts the writing stage on the copy.
A change counts as blocked when the writer makes no model call. The changed evidence is then
reviewed again, with the approved argument and the four critics' recorded verdicts in place of
the critics: either the review's own checks refuse it, or it is approved again and writing is
started once more.

| What changed | Changes | Writing blocked | Review refuses the change | Approved again, writing starts |
|---|---|---|---|---|
| A training record: one digit changed, a record removed or added | 389 | 389 | 314 | 75 |
| Training code, as recorded or on disk | 148 | 148 | 140 | 8 |
| An approved statement or a limitation | 78 | 78 | 25 | 53 |
| The literature review or the brief | 24 | 24 | 5 | 19 |
| A frozen protocol (two of the three runs have one) | 16 | 16 | 16 | 0 |
| The scorer | 11 | 11 | 6 | 5 |
| The approval record | 9 | 9 | 0 | 9 |
| All | 675 | 675 | 506 | 169 |

By run, the totals are 112 (distillation), 274 (AG News) and 289 (Digits). The unchanged copies
started writing, and after each change was undone writing started again in every case. A
review refuses a change when a record no longer matches its hash or a statement no longer
matches its measurements. The second review replays the critics, so it tests the gate and the
review's deterministic checks, not what a critic would say about the new evidence.

The hash has a boundary. It covers the training entry point and the scorer, and a frozen
protocol also covers every other source file of the engine. AG News ran no protocol, and there a
change to another engine source file went unnoticed (0 of 2, against 2 of 2 on each of the other
runs). The profile file is not changed in this study; a unit test covers it.

The reports are in `examples/sample_runs/*/reliability/approval.md`. The study needs an approval
that still holds on your machine, so it runs on your own run, not on the copies in this
repository:

```bash
python -m scholarloop.reliability approval --profile profiles/seq-distill.yaml \
  --run runs/my_study --out runs/my_study/reliability
```

### Does the paper say more than the evidence holds?

A judge model read each paper with pipeline marks removed and labelled every result claim
against the recorded evidence. The baseline is one model call given the same evidence, with the
same rules as instructions.

| Run | ScholarLoop paper: claims beyond the evidence | Single-call papers |
|---|---|---|
| Distillation | 5 of 93 (5%) | 59 of 492 (12%) |
| AG News | 0 of 94 (0%) | 28 of 415 (7%) |
| Digits | 1 of 110 (1%) | 65 of 332 (20%) |

Lower in every run. The caveats: one ScholarLoop paper per run, intervals that overlap on
distillation, and a judge from the same model family as the reviewers. Two people then labelled a
blinded sample of 50 of these claims: they agreed with each other on 41 and with the judge on 39
and 44. Two raters and a sample weighted towards flagged claims do not establish the judge's
accuracy.

### Does enforcement change what a campaign tests?

The same idea was handed to the experiment agent in two ways, ten campaigns each.

| | Enforced by the harness | Asked for in the prompt |
|---|---|---|
| Campaigns that edited the code | 10 of 10 | 2 of 10 |
| Edit implements the idea with a control that isolates it, per a judge model | 3 of 10 | 0 of 10 |

Enforcement secures a matched pair. It does not secure that the pair tests the idea. One idea,
one engine, and a judge from the same model family.

### Agent versus random search

Same number of training runs for each side, three campaigns each, on digits.

| Agent | Agent held-out error | Random search | Result |
|---|---|---|---|
| first version | 4.22 | 3.13 ± 0.08 | random wins |
| told the knob ranges, with an explore phase | 3.72 ± 0.24 | 3.13 | random wins all 9 pairs |
| warm-started on random draws | 3.14 | 3.13 | a tie |

A language model proposing hyperparameters does not beat random search on a small search space.
If it has an edge, it is in changing the method, and we have not shown that it does.

## Comparison with other systems: sources

The paper's Table 1 compares ScholarLoop with six research-agent systems on six properties. The
cells were filled from each system's paper and the default branch of its public repository, read
on 26 November 2026 by static reading; nothing was run. A cell may be out of date, and
corrections are welcome.

Marks: **yes** code enforces it by default; **optional** it exists but is off by default or
applies in one mode only; **partial** code enforces it for part of the pipeline; **model** it is
an instruction to a model or a model's judgment; **none** no description found.
Injection-tested counts a reported evaluation that inserts known faults; unit tests are not
counted, for any system.

| System | Repository | Commit |
|---|---|---|
| AI Scientist-v2 | `SakanaAI/AI-Scientist-v2` | `96bd516` |
| Agent Laboratory | `SamuelSchmidgall/AgentLaboratory` | `d9017d9` |
| TinyScientist | `ulab-uiuc/tiny-scientist` | `888c5e3` |
| Dr. Claw | `OpenLAIR/dr-claw` | `37493cd` |
| Curie | `Just-Curieous/Curie` | `db1b1f5` |
| data-to-paper | `Technion-Kishony-lab/data-to-paper` | `81df14c` |

| System | Property | Mark | What it rests on | Where |
|---|---|---|---|---|
| AI Scientist-v2 | Researcher decisions | partial | Ideation and experiments are separate commands and the user passes the index of the idea to run; there is no approval step | README, `launch_scientist_bfts.py` |
| | Dollar cap | none | Cost is tallied after the run; nothing limits it | `ai_scientist/utils/token_tracker.py` |
| | Scorer outside agent | none | The agent writes the experiment and the code that parses its metrics | `ai_scientist/treesearch/parallel_agent.py` |
| | Frozen protocol | partial | The harness sets the seeds that replicate each stage's best node; the configurations compared and a falsifying outcome are not fixed | `ai_scientist/treesearch/parallel_agent.py`, `bfts_config.yaml` |
| | Sentence binding | model | A prompt instruction not to report results absent from the logs | `ai_scientist/perform_icbinb_writeup.py` |
| | Injection-tested | none | | |
| Agent Laboratory | Researcher decisions | optional | Co-pilot mode is one of two modes and is off by default | `ai_lab_repo.py`, paper §3.3.1 |
| | Dollar cap | none | A cost estimate is printed; there is no limit | `inference.py` |
| | Scorer outside agent | none | Metrics come from agent-written code; a model scores candidate solutions | `mlesolver.py` |
| | Frozen protocol | model | A plan is written before experiments and a model scores adherence to it | `mlesolver.py`, paper §3.2 |
| | Sentence binding | none | | |
| | Injection-tested | none | | |
| TinyScientist | Researcher decisions | optional | The web interface advances stage by stage; the Python interface and the demo script do not pause | `backend/app.py`, `examples/demo.py` |
| | Dollar cap | optional | The budget is unset by default; when set, exceeding it raises an error | `tiny_scientist/scientist.py`, `tiny_scientist/budget_checker.py` |
| | Scorer outside agent | model | A model validator flags placeholder metrics; the metrics come from the agent's code | `tiny_scientist/coder.py` |
| | Frozen protocol | model | The same validator checks the code against the planned experiment table | `tiny_scientist/coder.py` |
| | Sentence binding | none | | |
| | Injection-tested | partial | The safety checker is tested on known unsafe requests; no faults are inserted into experiments or the paper | paper §6.1–6.2 |
| Dr. Claw | Researcher decisions | yes | The user dispatches tasks one at a time; an automatic mode is opt-in | README, `server/routes/auto-research.js` |
| | Dollar cap | none | Token usage is displayed; there is no limit | `server/claude-sdk.js` |
| | Scorer outside agent | model | The agent is told not to change metric definitions or evaluation logic and not to modify guard or test files; a model judges the implementation | `skills/ds-experiment/SKILL.md`, `skills/autoresearch/SKILL.md`, `skills/inno-experiment-dev/SKILL.md` |
| | Frozen protocol | model | Instructions to the agent | `skills/aris-experiment-plan/SKILL.md` |
| | Sentence binding | model | The agent is told to write a map from claims to evidence; no code checks it | `skills/ds-write/SKILL.md` |
| | Injection-tested | partial | One induced error, shown as a recovery demonstration | paper §5.2 |
| Curie | Researcher decisions | optional | Plan approval is behind a setting that is off in the shipped configurations | `curie/nodes/user_input.py`, `curie/experiment.py` |
| | Dollar cap | none | Cost is logged; the limit is a number of steps | `curie/model.py` |
| | Scorer outside agent | partial | The harness re-runs the agent's script, but the script and its metrics are agent-written | `curie/nodes/exec_validator.py` |
| | Frozen protocol | partial | Plans are stored through a schema and ordered by a scheduler; they can be redone during the run | `curie/tool.py` |
| | Sentence binding | none | | |
| | Injection-tested | none | | |
| data-to-paper | Researcher decisions | yes | Human review is on by default and the run waits for it | `src/data_to_paper/env.py` |
| | Dollar cap | none | Cost is tracked and displayed | `src/data_to_paper/servers/llm_call.py` |
| | Scorer outside agent | partial | Analysis code is model-written but runs inside wrappers of the statistics libraries | `src/data_to_paper/run_gpt_code/overrides/` |
| | Frozen protocol | partial | A hypothesis and plan stage precedes analysis and the seed is fixed; adherence is not checked by code | `src/data_to_paper/research_types/hypothesis_testing/scientific_stage.py` |
| | Sentence binding | partial | Code rejects a number in the Results section that does not link to an output; other sections are not checked | `src/data_to_paper/base_steps/base_products_conversers.py` |
| | Injection-tested | none | | |

ScholarLoop's own row: a protocol is frozen on request, so that cell is **optional**. The
dollar cap is always applied in the web interface (default $10); on the command line it applies
when `SCHOLARLOOP_SPEND_CAP` is set. Its injection covers the output checks and the approval,
not the rules that act during experiments.

## Known limits

This is a research preview. It runs end to end on real experiments, and several things are
missing or unproven.

- **It has not been shown to produce better research.** Its own reviewers rejected all three
  papers, and the output is a Markdown manuscript without figures or typesetting.
- **"Treatment" is a label the agent applies.** The harness enforces the order of control and
  treatment and records the edit. It does not verify that the edit implements the idea: a judge
  found that it did in 3 of 10 campaigns.
- **Wrong-but-real references get through the lexical checks.** Catching a real citation on the
  wrong claim falls to the critics and a model reviewer, and those are model judgments.
- **There is no real sandbox yet.** A hash detects a tampered scorer, but nothing stops a process
  from writing to disk. The guards are designed for a model proposing edits, not for hostile code.
- **Small tasks, one provider.** The shipped engines train in seconds on a CPU, and live runs go
  through the Anthropic SDK.
