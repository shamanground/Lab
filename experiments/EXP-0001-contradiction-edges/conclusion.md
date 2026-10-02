# EXP-0001 conclusion

## Observation

Ten records, four contradictory pairs, one agreeing pair, twenty shuffles, seed 0. The contest store returned both ids, both objects, and one edge on each contradictory key. The agreeing pair (yield 61 and 61) kept two sources and zero edges. Those reads did not change with insertion order. Last-write-wins returned one survivor, and that survivor changed: 17 distinct survivor tuples.

The first comparator was invalid because it mixed last-write-wins fields into the contest check. That miss is not a refutation.

## Interpretation

Object inequality on a shared key preserves an explicit contradiction without a model call, and does not mark agreement as a contradiction, if the object string is already canonical. Order invariance requires the read path to sort ids and edges.

## Status

SUPPORTED. Not an architecture candidate. The fixture is synthetic. Prime Atlas was not modified.
