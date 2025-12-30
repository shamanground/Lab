# Experiment 01 — Interaction Geometry Under Turn-Based Constraints

## Abstract
We investigate the interaction-layer geometry of a large language model under fixed prompting and looping constraints. Using repeated looped interactions with controlled perturbation timing, we measure failure depth at the tokens-per-minute (TPM) envelope. Results indicate a narrow, stable basin of attraction with consistent collapse depth across stochastic realizations.

---

## 1. Objective
To determine whether interaction depth under fixed constraints exhibits:
- consistent failure thresholds
- basin stiffness independent of perturbation magnitude
- evidence of geometric structure in interaction space

---

## 2. Experimental Setup

### 2.1 Model
- Model: `gpt-4.1`
- API: OpenAI Responses API
- Temperature: <fill>
- Top-p: <fill>
- Max output tokens: 800

### 2.2 Termination Criterion
- Each run terminates when the Tokens-Per-Minute (TPM) limit is reached.
- TPM is treated as an external envelope, not an internal model failure.

---

## 3. Conditions

### 3.1 Single-Shot (Control)
- One system prompt
- One user turn
- No accumulation

**Artifact**
# Experiment 01 — Interaction Geometry Under Turn-Based Constraints

## Abstract
We investigate the interaction-layer geometry of a large language model under fixed prompting and looping constraints. Using repeated looped interactions with controlled perturbation timing, we measure failure depth at the tokens-per-minute (TPM) envelope. Results indicate a narrow, stable basin of attraction with consistent collapse depth across stochastic realizations.

---

## 1. Objective
To determine whether interaction depth under fixed constraints exhibits:
- consistent failure thresholds
- basin stiffness independent of perturbation magnitude
- evidence of geometric structure in interaction space

---

## 2. Experimental Setup

### 2.1 Model
- Model: `gpt-4.1`
- API: OpenAI Responses API
- Temperature: <fill>
- Top-p: <fill>
- Max output tokens: 800

### 2.2 Termination Criterion
- Each run terminates when the Tokens-Per-Minute (TPM) limit is reached.
- TPM is treated as an external envelope, not an internal model failure.

---

## 3. Conditions

### 3.1 Single-Shot (Control)
- One system prompt
- One user turn
- No accumulation

**Artifact**
data/raw/single.json

---

### 3.2 Replay (Control)
- Full interaction history replayed as static input
- No turn-by-turn accumulation

**Artifact**
data/raw/replay.json

---

### 3.3 Loop (Experimental)
- Iterative user–assistant interaction
- Fixed loop prompt
- Single perturbation injected at a specified turn
- Run continues until TPM envelope is reached

**Artifacts**
data/raw/archive_pert*/run*/loop.json

Each `loop.json` corresponds to one independent stochastic realization.

---

## 4. Data Collection

For each loop run:
- Turn index at TPM failure recorded
- Full interaction trace logged
- Failure type classified

Derived metrics computed across runs:
- Minimum failure depth
- Maximum failure depth
- Mean failure depth
- Depth range

Derived files:
data/derived/summary.json
data/derived/stiffness.csv

---

## 5. Results

### 5.1 Depth Distribution

![Depth Histogram](figures/depth_histogram.png)

**Description**  
Histogram of failure turn across 60 loop runs. Distribution is narrow and unimodal.

---

### 5.2 Depth Scatter Across Runs

![Depth Scatter](figures/depth_scatter.png)

**Description**  
Failure depth plotted by run index. Dashed line indicates mean depth. No systematic drift across runs is observed.

---

### 5.3 Summary Statistics

| Metric | Value |
|------|------|
| Number of runs | 60 |
| Minimum depth | 19 |
| Maximum depth | 29 |
| Mean depth | 24.4 |
| Depth range | 10 |

---

## 6. Interpretation
- Failure depth clusters tightly despite stochastic sampling.
- Perturbation timing and magnitude do not materially alter collapse depth.
- Interaction collapse is dominated by structural constraints.
- Indicates a stiff interaction basin under fixed conditions.

---

## 7. Limitations
- TPM envelope is infrastructure-defined.
- Results are model- and configuration-specific.
- Observable depth is bounded by throughput constraints.
- No semantic correctness metric applied.

---

## 8. Reproducibility
All materials required to reproduce this experiment are included:
- Prompts: `prompts/`
- Raw outputs: `data/raw/`
- Derived metrics: `data/derived/`
- Analysis scripts: `analysis/`

---

## 9. Future Work
- Vary system prompt constraint strength
- Test multi-perturbation schedules
- Replace TPM with fixed-token envelopes
- Replicate across model families

---
