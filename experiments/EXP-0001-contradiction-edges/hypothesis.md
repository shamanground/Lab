# EXP-0001 hypothesis

HYPOTHESIS
A contest-edge store that keeps every observation and adds a CONTRADICTS edge only when the same subject and predicate have incompatible objects will return both poles and both provenance ids, in an insertion-order-invariant way. A last-write-wins map on (subject, predicate) will return one pole and drop the displaced provenance, and the survivor will depend on insertion order.

EXPECTED OBSERVATION
On four contradictory pairs, contest reads return 2 ids, 2 objects, 1 edge. On one agreeing pair, contest reads return 2 ids, 1 object, 0 edges. Across 20 shuffles of insertion order (seed 0), contest reads match. LWW reads do not.

FAILURE CONDITION
Contest store drops a pole, emits an edge on the agreeing pair, or changes its read with insertion order.

WHAT WOULD CHANGE MY MIND
A deterministic merge rule that retains displaced provenance outside the node map, or a fixture where object inequality is the wrong contradiction test (units, paraphrases).
