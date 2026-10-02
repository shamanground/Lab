# Review packet — keyed contest for milestone 25

ARCHITECTURE_DECISION_REQUIRED

This is a Lab packet. It does not start #25, reopen #19, or change Prime Atlas.

SOURCE
Roadmap #25 Contradiction Preservation Layer, slices 25-A through 25-E. Frozen #19 Lens Signal Contract. State note: additive #19 subject-position candidate is UNRESOLVED / REPAIR_REQUIRED.

PROBLEM
#25-A must name the subject and the position being contradicted, and must not treat different subjects, goals, or horizons as a clash. #19's frozen fields do not carry subject or proposition. Inspected `atlas_lens_signal.py` standard fields: observation, interpretation, direction, magnitude, confidence, time_horizon, affected_goals.

HYPOTHESIS
An additive subject-position binding, consumed by a fail-closed keyed contest, satisfies the fixture form of 25-A and 25-E. Averaging, weight-winner, and subject-blind pairing do not.

EXPERIMENT
EXP-0004, five signals.

RESULT
Surviving option: keyed contest. Clash only when subject, proposition, horizon, and goal set match and positions differ. Preserve both ids. Winner stays null. Missing subject is rejected, not paired.
Rejected: weight-winner (kept A, dropped B), average (120 and 140 became 130), subject-blind (six false pairs).

EVIDENCE
experiments/EXP-0004-subject-position-gate/results/results.json

LIMITATIONS
Synthetic signals. No replay of #23 interaction output or #24 evidence ids. Does not prove semantic independence. Does not authorize implementation.

REPRODUCTION
`python3 implementation/run.py` in the experiment folder.

RELEVANT PRIME ATLAS FILES
docs/roadmaps/Prime Atlas Roadmap.md (#19, #25-A to #25-E). atlas_lens_signal.py. candidates/lens_signal_contract/. PROJECT_STATE.md repair note.

POSSIBLE INTEGRATION POINT
Additive #19 subject and proposition fields, then #25-A gate. Frozen #19 field set stays frozen unless the architect accepts the additive candidate.

KNOWN CONFLICTS
#23 deferred CONFLICT mathematics. This option does not use Choquet delta, weight, or confidence as a winner rule. #24 dedup must not be reused as a second merger.

OPEN QUESTIONS
Canonical id for subject and proposition. Whether horizon and goal set belong in the key or only in the false-clash filter. Where the additive fields live if #19 stays frozen.

ARCHITECTURE_DECISION_REQUIRED
