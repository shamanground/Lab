# EXP-0003 conclusion

## Observation

Seven events, thirty shuffles, seed 0. Last-write-wins was not order-invariant. Recency, contest, supersede, and the timestamp multi-value register were.

Contest kept both span notes and marked a clash, kept both route notes and marked a clash, kept both yield notes and did not mark a clash. The correction was absent from contest reads.

Supersede history held every id. Current moved to the correction only because that event was marked as a correction. The later route disagreement did not retire the earlier note.

Recency and the multi-value register kept the newest span, route, and yield. The later identical yield displaced the earlier source from the current read.

## Interpretation

Stable is not the same as complete. Recency is overwrite with a clock. Contest answers what was claimed and has no correction type. Supersede answers what was explicitly corrected. The multi-value register keeps concurrent timestamps and drops older current sources.

## Status

SUPPORTED on this fixture. Not an architecture candidate. Prime Atlas was not modified.
