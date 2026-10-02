# ShamanGround Lab

This lab started with a person, not a product.

I have a traumatic brain injury. Words sometimes take longer than the room allows. Memory does not always hand back what I just set down. A note that gets overwritten is not a small inconvenience. It is gone. So the first design question was not how to make an impressive model. It was how to build something that holds the record when I cannot, waits while a sentence forms, and does not treat a wording difference as a fight.

If a tool can do that for me, it can do it for anybody. The injury is the hard case. The product is whatever still works after that case.

## Prove the layer, then build

Before Shaman Ground built on top of a model, the lab had to show that an interaction layer exists.

Not inside the weights. Not as a story about what the model "believes." At the surface, where a fixed constraint meets a reply. The claim was simple enough to fail: the same constraint, laid on unrelated subjects, should leave the same structural mark. If it did not, there was nothing there to design against.

The early experiments were that test.

- [exp01_interaction_geometry](exp01_interaction_geometry/) asked whether a fixed perturbation changes the shape of a loop.
- [exp02_axis_compression](exp02_axis_compression/) asked whether one constraint induces the same response regime across five unrelated claims. Under the primary constraint, it did. Five of five: the contradiction was masked, the specifics collapsed, and the reply still ended sure of itself.

That was the existence proof. A constraint at the interaction layer is real. It is observable. It does not care what the sentence is about.

Once that was known, building started. The lab did not close. A field that moves this fast will obsolete a design that only researches once. Shaman Ground researches while it builds, so an idea can become a tool a person actually uses without freezing the design in last year's interface.

The later folders are that second job. Not another existence proof. A running check on the rules a product would trust.

- [EXP-0001](experiments/EXP-0001-contradiction-edges/conclusion.md) showed that keeping only the last note loses the disagreement, and which note survives depends on write order.
- [EXP-0002](experiments/EXP-0002-paraphrase-poles/conclusion.md) showed that raw text invents fights: `shut` and `closed`, `120` and `120 m`. It also showed the rule we have still misses `not open` against `closed`.
- [EXP-0003](experiments/EXP-0003-resolution-rules/conclusion.md) showed that a stable rule is not a complete rule. A correction and a disagreement are different operations.

Those results are why a Shaman Ground tool is not allowed to swallow a conflict, rush a half-formed sentence, or confuse a rephrasing with news. The same rules that keep my day usable are the rules a visitor should be able to inspect.

## From idea to a human application

Shaman Ground is the path from a constraint, to a falsifiable test, to something a person can hold. The lab is the part that stays honest while the build moves. Designs stay current because the research does not stop at the pitch. A claim that cannot be rerun does not get to steer the product.

Visitors start at [experiments/README.md](experiments/README.md). Each experiment has its own folder. Older runs stay where they were locked. A supported lab result is evidence. It is not, by itself, a production decision.

If you are here because a tool failed you in an ordinary way — it forgot, it hurried, it flattened a disagreement into one confident line — that is the failure this lab was opened to catch.
