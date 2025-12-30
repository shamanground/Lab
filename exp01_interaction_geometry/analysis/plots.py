# analysis/plots.py

import csv
from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
DERIVED_DIR = BASE_DIR / "logs" / "derived"
PLOTS_DIR = DERIVED_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

depths = []

with open(DERIVED_DIR / "stiffness.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        depths.append(int(row["depth"]))

# ---------- SCATTER PLOT ----------
plt.figure()
plt.scatter(range(len(depths)), depths)
plt.axhline(sum(depths) / len(depths), linestyle="--")
plt.xlabel("Run index")
plt.ylabel("Failure turn (TPM)")
plt.title("Interaction Depth at TPM Envelope")
plt.savefig(PLOTS_DIR / "depth_scatter.png")
plt.close()

# ---------- HISTOGRAM ----------
plt.figure()
plt.hist(depths, bins=range(min(depths), max(depths) + 2))
plt.xlabel("Failure turn")
plt.ylabel("Count")
plt.title("Depth Distribution at TPM Envelope")
plt.savefig(PLOTS_DIR / "depth_histogram.png")
plt.close()

print("Plots written to logs/derived/plots/")
