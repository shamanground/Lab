#!/usr/bin/env python3
"""EXP-0002: exact object inequality vs a fixed pole normalizer."""
import json
import re
import unicodedata
from pathlib import Path

SYNONYMS = {"shut": "closed", "opened": "open", "celsius": "c", "centigrade": "c"}
UNITS = (" m", " meters", " metre", " metres")
CASES = [
    {"id": "synonym_same_pole", "expected": "agree", "a": "closed", "b": "shut"},
    {"id": "unit_same_pole", "expected": "agree", "a": "120", "b": "120 m"},
    {"id": "case_same_pole", "expected": "agree", "a": "Open", "b": "open"},
    {"id": "space_same_pole", "expected": "agree", "a": "closed", "b": " closed "},
    {"id": "numeric_opposite", "expected": "contradict", "a": "120", "b": "140"},
    {"id": "lexical_opposite", "expected": "contradict", "a": "open", "b": "closed"},
    {"id": "negation_same_pole", "expected": "agree", "a": "not open", "b": "closed"},
]

def norm_key(obj):
    s = unicodedata.normalize("NFKC", obj).strip().casefold()
    s = re.sub(r"\s+", " ", s)
    for unit in UNITS:
        if s.endswith(unit):
            s = s[: -len(unit)].strip()
            break
    return SYNONYMS.get(s, s)

def judge(a, b, fn):
    return "contradict" if fn(a) != fn(b) else "agree"

def main():
    rows = []
    for case in CASES:
        rows.append({
            **case,
            "exact": judge(case["a"], case["b"], lambda x: x),
            "norm": judge(case["a"], case["b"], norm_key),
            "norm_keys": [norm_key(case["a"]), norm_key(case["b"])],
        })
    false_flags = [r["id"] for r in rows if r["expected"] == "agree" and r["exact"] == "contradict"]
    residual = [r["id"] for r in rows if r["norm"] != r["expected"]]
    result = {
        "exact_correct": sum(r["exact"] == r["expected"] for r in rows),
        "norm_correct": sum(r["norm"] == r["expected"] for r in rows),
        "n": len(rows),
        "exact_false_flags_on_same_pole": false_flags,
        "norm_residual_misses": residual,
        "numeric_preserved": next(r for r in rows if r["id"] == "numeric_opposite")["norm"] == "contradict",
        "hypothesis_supported": residual == ["negation_same_pole"] and "numeric_opposite" not in residual and "lexical_opposite" not in residual and len(false_flags) == 5,
        "rows": rows,
    }
    out = Path(__file__).resolve().parents[1] / "results" / "results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in result if k != "rows"}, indent=2))

if __name__ == "__main__":
    main()
