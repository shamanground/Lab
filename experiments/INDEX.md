# Lab experiment index

Operator charter: Lab discovers. Prime Atlas adjudicates. This index is not production authority.

| ID | Title | Status | Source signal | Hypothesis | Result | Confidence | Relevance | Commit | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EXP-01 | Interaction geometry / stiffness loops | SUPPORTED (historical, pre-index) | Lab exp01 | Fixed perturbation changes loop depth distribution | See exp01 report and derived summary | medium | interaction layer | main @ 4d34bb92 | leave immutable |
| EXP-02 | Constraint-induced response regimes | SUPPORTED (historical, pre-index) | Lab exp02 | Identical constraint yields identical regime across claims | 5/5 masked + collapsed + assertive under C-1 | medium | interaction layer; not memory | main @ 4d34bb92 | leave immutable |
| EXP-0001 | Contradiction edge vs last-write-wins | SUPPORTED | research/signals/2026-10-02-provenance-contradiction.md | Contest-edge store keeps both poles and provenance independent of insert order; LWW does not | Supported on 10-record fixture, 20 shuffles, seed 0 | medium on mechanism, low on external validity | Prime Atlas #25 not started; comparison only | experiment/exp-0001-contradiction-edges @ 621d65f2 | do not promote |
| EXP-0002 | Exact inequality vs synonym/unit normalization | SUPPORTED | EXP-0001 limitation | Exact inequality false-flags same-pole paraphrases; a fixed normalizer separates those from real opposites, except negation | 4/5 same-pole false flags corrected; negation residual; 120/140 preserved | medium on the rule, low outside the fixture | detection rule under #25; PA graph has conflicts_with but no claim detector | experiment/exp-0002-paraphrase-poles | not a candidate; negation algebra untested |

## Triaged, not run

| Candidate | Class | Why deferred |
| --- | --- | --- |
| Generative claim-level provenance records | WATCH | Needs a model loop. No paid API authorized. |
| Version-string provider qualification vs capability probe | BLOCKED | Would require live provider calls. |
| Negation algebra (not open == closed) | RESEARCH | Residual miss from EXP-0002. Next safe experiment if continued. |

Statuses used: DESIGNED, RUNNING, SUPPORTED, REFUTED, INCONCLUSIVE, BLOCKED, ARCHITECTURE_CANDIDATE.
Neither EXP-0001 nor EXP-0002 is ARCHITECTURE_CANDIDATE.
