# EXP-0001 conclusion

## Observation

On the 10-record fixture, last-write-wins returned one object and one source for each contradictory key. The contest store returned both ids, both objects, and one CONTRADICTS edge. The agreeing pair (e7, e8, both yield 61) kept two provenance records and zero CONTRADICTS edges. Across 20 insertion shuffles, seed 0, contest reads were identical. LWW survivor ids were not: 17 distinct survivor tuples.

First comparator run was invalid and is recorded in results/results.json. It does not count as a refutation.

## Interpretation

Object-inequality on a shared (subject, predicate) is enough to preserve an explicit contradiction without a model call, and to avoid marking agreement as contradiction. Order invariance requires the read path to sort ids and edges. LWW cannot be made order-invariant without keeping the displaced record, which is the thing under test.

## Speculation

This is the store shape Prime Atlas #25 would have to beat or absorb if the architect reopens that milestone. Not tested against atlas_graph.py, lens memory, or inbox dedup. #24 signal deduplication is a different operation and is closed; this experiment does not reopen it.

## Prime Atlas comparison

- Does Prime Atlas already solve this? PROJECT_STATE says #25 is not started. Not demonstrated here.
- Is the Lab result different? Yes relative to a flat last-write map. Unknown relative to existing atlas_graph.py.
- Conflict with a frozen authority? Unknown. #25 research artifact was not located. No authority was edited.
- Architectural change required? Not decided. This is a mechanism probe.
- Irrelevant to current 88-roadmap work? Not irrelevant to #25, and not a reason to start #25. Sidequest gate still stands.

## Status

SUPPORTED. Not ARCHITECTURE_CANDIDATE. External validity is the fixture, not a Prime Atlas replay.

LAB commit: experiment/exp-0001-contradiction-edges
No production decision.
