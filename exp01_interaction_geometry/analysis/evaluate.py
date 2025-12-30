# analysis/evaluate.py

import json
from pathlib import Path
from statistics import mean

BASE_DIR = Path(__file__).resolve().parents[1]
LOGS_DIR = BASE_DIR / "logs"
DERIVED_DIR = LOGS_DIR / "derived"
DERIVED_DIR.mkdir(exist_ok=True)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

runs = []

# ---------- LOAD LOOP RUNS ----------
for pert_dir in LOGS_DIR.glob("archive_pert*"):
    for run_dir in pert_dir.glob("run*"):
        loop_file = run_dir / "loop.json"
        if not loop_file.exists():
            continue

        data = load_json(loop_file)
        failure = data.get("failure")

        runs.append({
            "condition": "loop",
            "perturb": pert_dir.name,
            "run": run_dir.name,
            "failure_type": failure["type"] if failure else None,
            "failure_turn": failure["turn"] if failure else None,
        })

# ---------- LOAD CONTROLS ----------
single = load_json(LOGS_DIR / "raw" / "single.json")
replay = load_json(LOGS_DIR / "raw" / "replay.json")

runs.append({
    "condition": "single",
    "failure_type": None,
    "failure_turn": len(single["turns"]),
})

runs.append({
    "condition": "replay",
    "failure_type": replay.get("failure", {}).get("type"),
    "failure_turn": replay.get("failure", {}).get("turn"),
})

# ---------- FILTER TPM RUNS ----------
tpm_runs = [
    r for r in runs
    if r["condition"] == "loop" and r["failure_type"] == "TPM_RATE_LIMIT"
]

depths = [r["failure_turn"] for r in tpm_runs]

summary = {
    "num_loop_runs": len(tpm_runs),
    "min_depth": min(depths),
    "max_depth": max(depths),
    "mean_depth": mean(depths),
    "depth_range": max(depths) - min(depths),
    "relative_range": (max(depths) - min(depths)) / mean(depths),
}

with open(DERIVED_DIR / "summary.json", "w") as f:
    json.dump(summary, f, indent=2)

with open(DERIVED_DIR / "stiffness.csv", "w") as f:
    f.write("run,depth\n")
    for r in tpm_runs:
        f.write(f"{r['run']},{r['failure_turn']}\n")

print("Evaluation complete. Outputs written to logs/derived/")
