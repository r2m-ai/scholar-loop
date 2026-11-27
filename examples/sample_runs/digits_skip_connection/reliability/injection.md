# Guard reliability: fault injection

Detection of single-site injected faults by the production postchecks. Fabrication faults refer to something absent from the evidence; misattribution faults use real evidence in the wrong place. In legacy mode a lexical check cannot see misattribution. In reviewed mode numbers are bound to the statements a sentence cites, so part of it is visible.

Guard mode: reviewed, against the release as recorded (not re-validated on this machine). Seed 0, at most 8 sites per fault and artifact. Unmodified controls: 0 of 14 accepted artifacts rejected.

## Detection by fault

| tier | fault | detected |
|---|---|---|
| fabrication | dropped_limitations | 1/1 (100%, 95% CI 21-100) |
| fabrication | dropped_section | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_citation | 59/59 (100%, 95% CI 94-100) |
| fabrication | fabricated_number | 69/69 (100%, 95% CI 95-100) |
| fabrication | fabricated_run_id | 19/19 (100%, 95% CI 83-100) |
| fabrication | fabricated_statement_id | 94/94 (100%, 95% CI 96-100) |
| fabrication | near_miss_citation | 13/13 (100%, 95% CI 77-100) |
| fabrication | uncited_claim | 13/13 (100%, 95% CI 77-100) |
| fabrication | uncited_sentence | 78/78 (100%, 95% CI 95-100) |
| misattribution | direction_flip | 16/61 (26%, 95% CI 17-38) |
| misattribution | misattributed_number | 67/69 (97%, 95% CI 90-99) |
| misattribution | miscitation | 0/13 (0%, 95% CI 0-23) |
| misattribution | wrong_run_id | 15/19 (79%, 95% CI 57-91) |
| misattribution | wrong_statement_id | 39/94 (41%, 95% CI 32-52) |

| tier | detected |
|---|---|
| fabrication | 354/354 (100%, 95% CI 99-100) |
| misattribution | 137/256 (54%, 95% CI 47-60) |

## Where faults pass, by pipeline stage

| tier | fault | stage | detected |
|---|---|---|---|
| fabrication | dropped_limitations | outline | 1/1 (100%, 95% CI 21-100) |
| fabrication | dropped_section | key_points | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_citation | ideas | 5/5 (100%, 95% CI 57-100) |
| fabrication | fabricated_citation | key_points | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_citation | lit_review | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_citation | outline | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_citation | section | 30/30 (100%, 95% CI 89-100) |
| fabrication | fabricated_number | key_points | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_number | outline | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_number | section | 53/53 (100%, 95% CI 93-100) |
| fabrication | fabricated_run_id | key_points | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_run_id | section | 11/11 (100%, 95% CI 74-100) |
| fabrication | fabricated_statement_id | key_points | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_statement_id | outline | 8/8 (100%, 95% CI 68-100) |
| fabrication | fabricated_statement_id | section | 78/78 (100%, 95% CI 95-100) |
| fabrication | near_miss_citation | ideas | 5/5 (100%, 95% CI 57-100) |
| fabrication | near_miss_citation | lit_review | 8/8 (100%, 95% CI 68-100) |
| fabrication | uncited_claim | ideas | 5/5 (100%, 95% CI 57-100) |
| fabrication | uncited_claim | key_points | 8/8 (100%, 95% CI 68-100) |
| fabrication | uncited_sentence | section | 78/78 (100%, 95% CI 95-100) |
| misattribution | direction_flip | key_points | 8/8 (100%, 95% CI 68-100) |
| misattribution | direction_flip | outline | 8/8 (100%, 95% CI 68-100) |
| misattribution | direction_flip | section | 0/45 (0%, 95% CI 0-8) |
| misattribution | misattributed_number | key_points | 8/8 (100%, 95% CI 68-100) |
| misattribution | misattributed_number | outline | 8/8 (100%, 95% CI 68-100) |
| misattribution | misattributed_number | section | 51/53 (96%, 95% CI 87-99) |
| misattribution | miscitation | ideas | 0/5 (0%, 95% CI 0-43) |
| misattribution | miscitation | lit_review | 0/8 (0%, 95% CI 0-32) |
| misattribution | wrong_run_id | key_points | 8/8 (100%, 95% CI 68-100) |
| misattribution | wrong_run_id | section | 7/11 (64%, 95% CI 35-85) |
| misattribution | wrong_statement_id | key_points | 8/8 (100%, 95% CI 68-100) |
| misattribution | wrong_statement_id | outline | 0/8 (0%, 95% CI 0-32) |
| misattribution | wrong_statement_id | section | 31/78 (40%, 95% CI 30-51) |

## Ablation (one guard disabled at a time)

Only guards whose removal changes the count are listed.

| tier | configuration | detected |
|---|---|---|
| fabrication | all_guards | 354/354 (100%, 95% CI 99-100) |
| fabrication | without_citation | 82/354 (23%, 95% CI 19-28) |
| fabrication | without_number | 301/354 (85%, 95% CI 81-88) |
| fabrication | without_structure | 325/354 (92%, 95% CI 88-94) |
| misattribution | all_guards | 137/256 (54%, 95% CI 47-60) |
| misattribution | without_citation | 104/256 (41%, 95% CI 35-47) |
| misattribution | without_number | 60/256 (23%, 95% CI 19-29) |
| misattribution | without_structure | 121/256 (47%, 95% CI 41-53) |
