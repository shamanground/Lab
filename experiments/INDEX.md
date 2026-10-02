# Lab experiment index

Operator charter: Lab discovers. Prime Atlas adjudicates. This index is not production authority.

| ID | Title | Status | Source signal | Hypothesis | Result | Confidence | Relevance | Commit | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EXP-01 | Interaction geometry / stiffness loops | SUPPORTED (historical, pre-index) | Lab exp01 | Fixed perturbation changes loop depth distribution | See exp01 report and derived summary | medium | interaction layer | main @ 4d34bb92 | leave immutable |
| EXP-02 | Constraint-induced response regimes | SUPPORTED (historical, pre-index) | Lab exp02 | Identical constraint yields identical regime across claims | 5/5 masked + collapsed + assertive under C-1 | medium | interaction layer; not memory | main @ 4d34bb92 | leave immutable |
| EXP-0001 | Contradiction edge vs last-write-wins | SUPPORTED | research/signals/2026-10-02-provenance-contradiction.md | Contest-edge store keeps both poles and provenance independent of insert order; LWW does not | Supported on 10-record fixture, 20 shuffles, seed 0 | medium on mechanism, low on external validity | Prime Atlas #25 not started; comparison only | experiment/exp-0001-contradiction-edges | do not promote; needs real PA fixture before candidate |

## Triaged, not run

| Candidate | Class | Why deferred |
| --- | --- | --- |
| Generative claim-level provenance records (tool_turn_id, evidence_span, support_relation) | WATCH | Needs a model loop. No paid API authorized. |
| Version-string provider qualification vs capability probe | BLOCKED | Would require live provider calls. Recorded so it is not silently substituted. |

Statuses used: DESIGNED, RUNNING, SUPPORTED, REFUTED, INCONCLUSIVE, BLOCKED, ARCHITECTURE_CANDIDATE.
EXP-0001 is SUPPORTED, not ARCHITECTURE_CANDIDATE.
