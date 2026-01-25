# Experiment 02 — Constraint-Induced Response Regimes

## Abstract

This experiment evaluates whether a fixed interaction-level constraint induces a reproducible response regime across semantically independent, falsifiable claims. The assessment is performed using single-turn interactions only and relies exclusively on externally observable response features. Regime existence is established by the presence of an invariant regime signature under identical constraint configurations.

---

## Invariant Under Test

**Invariant**

> Identical interaction-level constraints produce identical response regimes across independent prompts.

Operationally, this means that when the same constraint configuration is applied to unrelated claims, the resulting response class (as defined by contradiction handling, specificity, and termination) remains invariant up to topic-specific surface variation.

---

## Constraint Configuration

**Primary Constraint (C-1)**

- The model is instructed to produce an assertive response
- The response must state something that contradicts the given claim
- The interaction is restricted to a single turn

This constraint configuration invalidates the default explanatory regime and forces the model to resolve contradiction under completion pressure.

**Control Condition (C-0)**

- No explicit contradiction is required
- Normal completion behavior is permitted

**Baseline Condition**

- Unmodified claim
- No contradiction pressure applied

---

## Experimental Design

### Conditions

- **Baseline:** No contradiction, assertive completion
- **Control (C-0):** Implicit contradiction allowed, hedged completion
- **Primary (C-1):** Forced contradiction with assertive completion

### Domains Tested

Five semantically independent domains were selected to eliminate topic-specific bias:

- Physics
- Biology
- Economics
- History
- Mathematics

### Interaction Scope

- Single-turn only
- No multi-step reasoning
- No prompt optimization
- No memory or cross-run carryover

---

## Structural Coding Schema

Responses were coded using externally observable features only.

### Dimensions

**Contradiction Handling**
- None: No contradiction present
- Juxtaposed: Contradiction presented without reconciliation
- Masked: Contradiction absorbed or obscured by explanation
- Deferred: Contradiction displaced to a later scope

**Specificity**
- Preserved: Concrete claims remain intact
- Collapsed: Claims degrade into generalized assertions

**Termination Class**
- Assertive: Ends with a definitive commitment
- Hedged: Ends with uncertainty or qualification

The combination of these features constitutes a **regime signature**.

---

## Results

Under the **Primary (C-1)** constraint, all five domains produced the same regime signature:

- Masked contradiction
- Collapsed specificity
- Assertive termination

This regime signature was **5 / 5 invariant** across all claims.

Under **Baseline** and **Control (C-0)** conditions, responses remained topic-dependent and aligned with the default response regime.

---

## Interpretation

These results demonstrate that:

- Response regimes are **constraint-defined**, not topic-defined
- A single interaction-level constraint can force the model into a stable, reproducible regime
- Semantic domain does not alter regime outcome under sufficient constraint pressure

This experiment establishes the existence of **constraint-induced response regimes** at the interaction layer.

---

## Non-Claims (Explicit Exclusions)

This experiment does **not** make claims about:

- Internal model representations
- Stored user state or memory
- Latent axes or coordinate systems
- Training data composition
- Safety or alignment behavior

All observations are interaction-layer and externally observable only.

---

## Limitations

- Single model and parameterization
- Single constraint configuration tested
- Single-turn interactions only

---

## Reproducibility

All prompts, scripts, raw outputs, and derived artifacts are publicly available in the repository:

https://github.com/shamanground/Lab/tree/main/exp02_axis_compression

The repository contains sufficient information to independently reproduce all reported results.

---

## Status

- **Experiment ID:** EXP-02
- **State:** Complete
- **Revision:** Immutable
- **Date:** 2026-01
