# ShamanGround Lab

ShamanGround Lab is a research workspace for **controlled, reproducible experiments on large language model interaction dynamics**.

The lab focuses exclusively on **observable interaction-layer behavior under fixed constraints**.
No assumptions are made about internal model architecture, training data, or latent representations.

All claims are evaluated through **explicit experimental design, raw outputs, and falsifiable criteria**.

---

## Current Experiment

### Experiment 02 — Proof of Interaction Axis Existence

**Location**

```
Lab/exp02_axis_compression/
```

**Status**

* Execution: **Complete**
* Raw outputs: **Locked**
* Structural coding: **Complete**
* Final classification: **Pending**

---

## Objective

Test whether **interaction axes exist** at the interaction layer.

An interaction axis is defined operationally as:

> A constraint-defined axis exists if a fixed constraint induces the same structural failure pattern across semantically independent, falsifiable claims, independent of subject matter.

This experiment tests **existence only**.
It does **not** test:

* axis direction
* magnitude
* dynamics
* cross-axis interaction
* internal model causes

---

## Experimental Design (Summary)

* **Claims**: 5 semantically independent, falsifiable statements
* **Runs per claim**: 3

  * Baseline (no constraint)
  * Control (non-contradictory constraint)
  * Primary (explicit contradiction constraint)
* **Total runs**: 15
* **Interaction mode**: single-turn only
* **Model**: GPT-4.1
* **Temperature**: 0.0
* **Max tokens**: 120
* **No replay, no memory, no multi-turn accumulation**

All runs use an **identical system prompt and parameter set**.
Only the user prompt differs by constraint inclusion.

---

## Evaluation Framework

Evaluation is **structural, not semantic**.

Each output is coded along four categorical dimensions:

1. **Reference Orientation**

   * Internal
   * External
2. **Specificity**

   * Preserved
   * Collapsed
3. **Contradiction Handling**

   * None
   * Juxtaposed
   * Masked
   * Deferred
4. **Termination Class**

   * Assertive
   * Hedged
   * Truncated
   * Refusal

Narrative tone, correctness, persuasion, and confidence are explicitly excluded.

---

## Outcome Classification

Results are classified into **exactly one** of the following:

* **PASS — Axis Exists**
  Invariant structural deformation under the primary constraint across all claims.

* **FAIL — Axis Falsified**
  Structural outcomes vary by claim or are reproduced under control.

* **INCONCLUSIVE — Probe Failure**
  One or more primary runs terminate via refusal or truncation not mirrored in control.

No post-hoc exclusions are permitted.

---

## Repository Structure

```
Lab/
└── exp02_axis_compression/
    ├── config/
    │   └── system_prompt.txt
    ├── prompts/
    │   └── claims/
    │       ├── claim_01.txt
    │       ├── claim_02.txt
    │       ├── claim_03.txt
    │       ├── claim_04.txt
    │       └── claim_05.txt
    ├── runs/
    │   ├── raw/
    │   │   └── *.txt
    │   └── exp02_runs.csv
    ├── logs/
    │   ├── *_response.json
    │   └── execution_log.jsonl
    ├── coding/
    │   └── structural_codes.csv
    ├── run_order.sh
    └── README.md
```

All raw outputs and execution logs are committed and treated as immutable.

---

## Methodology Notes

* All experiments operate strictly at the **interaction layer**.
* No assumptions are made about transformer internals.
* No interpretive averaging, scoring, or embedding analysis is used.
* Structural coding is performed **blind to claim domain**.
* Refusals are treated as **probe failures**, not evidence against existence.

---

## Reproducibility

To reproduce Experiment 02:

1. Clone the repository
2. Set a valid OpenAI API key in `.env`
3. Run:

   ```bash
   ./run_order.sh
   ```
4. Verify raw outputs in `runs/raw/`
5. Use `runs/exp02_runs.csv` for independent structural analysis

All prompts, constraints, parameters, and scripts are included.

---

## Status Summary

* Experiment 02: **Execution complete**
* Raw data: **Locked**
* Structural coding: **complete**
* Final determination: **Pending**

Further experiments will extend this framework to additional axes, constraints, and interaction regimes.

