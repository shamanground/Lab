# EXP-0003 hypothesis

HYPOTHESIS
On one fixture of observations plus one explicit correction, last-write-wins changes its read with log order. Recency, contest, supersede, and a timestamp multi-value register do not. Their stable reads are not the same read: contest keeps both poles and ignores the correction; supersede moves current only on the correction; recency and the multi-value register keep the newest timestamp and drop older current sources.

EXPECTED OBSERVATION
Thirty shuffles, seed 0. LWW order_invariant false. The other four true. Contest clash on span and route, no clash on yield, correction absent. Supersede current on span is the correction; route current stays the first observation. MVR current yield is only the later 61.

FAILURE CONDITION
Any non-LWW rule changes its read across shuffles, or contest and supersede return the same current set.

WHAT WOULD CHANGE MY MIND
A supersede rule defined as "later observation retires earlier," which would collapse supersede into recency. This experiment does not use that definition.
