# Sources

Hypothesis: last-write-wins follows log order; recency, contest, supersede, and a timestamp multi-value register are order-stable and still return different reads.

Used:

- EXP-0001, which had already falsified last-write-wins on shuffle.
- The strategy split stated in the Lab session before the run: overwrite, recency, contest, supersede.
- Multi-value register: the usual concurrent-write rule where a later timestamp clears the slot and an equal timestamp keeps both. Applied here as a fixture rule, not copied from a paper fetched for this run.

No new external paper.
