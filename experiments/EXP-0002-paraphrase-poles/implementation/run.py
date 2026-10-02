#!/usr/bin/env python3
import json, re, unicodedata
from pathlib import Path
SYNONYMS = {"shut": "closed", "opened": "open"}
UNITS = (" m", " meters")

def norm_key(obj):
    s = unicodedata.normalize("NFKC", obj).strip().casefold()
    s = re.sub(r"\s+", " ", s)
    for unit in UNITS:
        if s.endswith(unit):
            s = s[: -len(unit)].strip()
            break
    return SYNONYMS.get(s, s)

def main():
    cases = json.loads((Path(__file__).resolve().parents[1] / "fixtures" / "pairs.json").read_text())
    rows = []
    for c in cases:
        exact = "contradict" if c["a"] != c["b"] else "agree"
        norm = "contradict" if norm_key(c["a"]) != norm_key(c["b"]) else "agree"
        rows.append({"id": c["id"], "exact": exact, "norm": norm, "expected": c["expected"]})
    print(json.dumps({"exact_correct": sum(r["exact"]==r["expected"] for r in rows), "norm_correct": sum(r["norm"]==r["expected"] for r in rows), "n": len(rows)}, indent=2))

if __name__ == "__main__":
    main()
