# EXP-0003 hypothesis

On one fixture of observations plus one explicit correction, last-write-wins changes its read with log order. Recency, contest, supersede, and a timestamp multi-value register do not. Their stable reads are not the same read.

Failure: any non-last-write-wins rule changes its read across shuffles, or contest and supersede return the same current set.
