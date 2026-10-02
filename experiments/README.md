# Experiments

This folder is the visitor entrance. Each experiment has its own folder. Read `conclusion.md` for the finding. Read `hypothesis.md` for what would have counted as a failure. Run `implementation/run.py` to reproduce the later store tests.

Custodian: Grok, on the Lab repo only. Prime Atlas is not updated from here. A supported Lab result is not a production decision.

## What was found

- EXP-01, in `../exp01_interaction_geometry/`. Locked. Loop-depth records under a fixed perturbation. Not moved.
- EXP-02, in `../exp02_axis_compression/`. Locked. One constraint produced the same response regime on five unrelated claims: masked contradiction, collapsed specificity, assertive ending. Not moved.
- [EXP-0001](EXP-0001-contradiction-edges/conclusion.md). If two notes disagree, keeping both and marking a clash survives a shuffle. Keeping only the last note does not. The survivor changed 17 ways in 20 shuffles.
- [EXP-0002](EXP-0002-paraphrase-poles/conclusion.md). Comparing raw text invents fights. `shut` and `closed`, `120` and `120 m`, `Open` and `open` are the same claim. A short cleaner fixed those and still flagged 120 against 140. `not open` against `closed` is still wrongly flagged.
- [EXP-0003](EXP-0003-resolution-rules/conclusion.md). Five rules on one fixture. Last-write-wins follows log order. Recency, contest, supersede, and a timestamp multi-value register do not, and they do not return the same answer. A later disagreement is not the same operation as an explicit correction.

## What was not found

No experiment decided which note was true. None started Prime Atlas milestone #25. None is an architecture candidate.

The working index, including deferred probes, is [INDEX.md](INDEX.md).
