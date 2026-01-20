### Experiment 01 — Interaction Geometry Under Turn-Based Constraints

**Location**
Lab/exp01_interaction_geometry/

**Objective**  
Measure interaction depth and failure behavior of an LLM under repeated turn-based interaction, using fixed prompts and controlled perturbation timing.

Failure is defined operationally as reaching the **tokens-per-minute (TPM) envelope**, treated as an external constraint boundary.

**Conditions Tested**
- Single-shot (control)
- Replay (control)
- Loop with perturbation (experimental)

**Key Outputs**
- Raw interaction logs (`data/raw/`)
- Derived metrics (`data/derived/`)
- Failure depth statistics
- Distribution and scatter plots
- Reproducible analysis scripts
- Written report (`report.md`)

---

## Repository Structure

Lab/
└── exp01_interaction_geometry/
├── analysis/
│ ├── evaluate.py
│ └── plots.py
├── config/
│ └── experiment.yaml
├── execution/
│ ├── run_single.py
│ ├── run_loop.py
│ └── run_replay.py
├── prompts/
│ ├── system.txt
│ ├── turn1.txt
│ ├── loop.txt
│ └── perturb.txt
├── data/
│ ├── raw/
│ └── derived/
├── figures/
│ ├── depth_histogram.png
│ └── depth_scatter.png
└── report.md

---

## Methodology Notes

- All experiments operate strictly at the interaction layer.
- No assumptions are made about transformer internals.
- All conclusions are derived from observable inputs, outputs, and failure depth.
- Stochastic variability is handled via repeated independent runs.
- Controls are evaluated using the same evaluator and plotting pipeline.

---

## Reproducibility

To reproduce Experiment 01:
1. Install dependencies in a virtual environment
2. Configure `experiment.yaml`
3. Run execution scripts in order:
   - `run_single.py`
   - `run_loop.py`
   - `run_replay.py`
4. Run analysis scripts:
   - `analysis/evaluate.py`
   - `analysis/plots.py`

All required prompts and parameters are included in the repository.

---

## Status

- Experiment 01: **Complete**
- Analysis: **Complete**
- Report: **Complete**
- Further experiments will extend this framework to additional interaction regimes and constraint envelopes.
