# EXP-0003 conclusion

## Observation

Seven events, thirty shuffles, seed 0. Last-write-wins was not order-invariant. Recency, contest, supersede, and the timestamp multi-value register were.

Contest kept e1 and e2 on span and marked a clash, kept e4 and e5 on route and marked a clash, kept e6 and e7 on yield and did not mark a clash. The correction e3 was absent from contest reads.

Supersede history held every id. Current moved to e3 only because that event was marked correction. Route current stayed e4. A later observation did not retire an earlier one.

Recency and the multi-value register both kept e3, e5, and e7. The later identical yield displaced e6 from the current read.

## Interpretation

Stable is not the same as complete. Recency is overwrite with a clock. Contest answers what was claimed and has no correction type. Supersede answers what was explicitly corrected and will not treat a later clash as a retirement. The multi-value register keeps concurrent timestamps and drops older current sources, including an older source with the same value.

## Speculation

A production store would need at least contest and supersede as separate operations. Not tested here.

## Prime Atlas comparison

atlas_graph.py already has conflicts_with and supersedes on plan nodes. This fixture does not show those edges being selected by an event kind. No Prime Atlas file was modified. #25 was not started.

## Status

SUPPORTED on this fixture. Not ARCHITECTURE_CANDIDATE.

No production decision.
