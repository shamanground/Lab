# Sources

Hypothesis: milestone 25 cannot pair lenses safely unless a signal carries subject and proposition; frozen milestone 19 does not; keyed contest survives and average, weight-winner, and subject-blind pairing do not.

Used, read-only, Prime Atlas commit inspected 2026-10-02 (`aa0e4ed7` at read time):

- `docs/roadmaps/Prime Atlas Roadmap.md` — #19 Lens Signal Contract field list; #25-A through #25-E, especially 25-A subject and position, and 25-E no average, no weight winner, no dropped minority.
- `atlas_lens_signal.py` — `LENS_SIGNAL_STANDARD_FIELDS`: observation, interpretation, direction, magnitude, confidence, time_horizon, affected_goals. No subject. No proposition.
- `docs/migration/github-baseline-20261001/STATE_AND_DISPOSITIONS.md` and `PROJECT_STATE.md` — additive #19 subject-position candidate is UNRESOLVED / REPAIR_REQUIRED, and that note does not reopen frozen #19.
- EXP-0001 through EXP-0003, for the store rules the options were compared against.

No external paper. Prime Atlas was not modified.
