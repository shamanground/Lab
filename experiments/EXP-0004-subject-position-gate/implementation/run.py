#!/usr/bin/env python3
"""EXP-0004: #25 options against a missing #19 subject field."""
import json

SIGNALS = [
    {"id": "A", "subject": "span", "proposition": "length_m", "position": "120", "horizon": "short_term", "goals": ["g1"], "direction": "negative", "confidence": 0.9},
    {"id": "B", "subject": "span", "proposition": "length_m", "position": "140", "horizon": "short_term", "goals": ["g1"], "direction": "positive", "confidence": 0.4},
    {"id": "C", "subject": "route", "proposition": "status", "position": "closed", "horizon": "short_term", "goals": ["g1"], "direction": "negative", "confidence": 0.8},
    {"id": "D", "subject": "span", "proposition": "length_m", "position": "140", "horizon": "long_term", "goals": ["g1"], "direction": "positive", "confidence": 0.7},
    {"id": "E", "subject": None, "proposition": "length_m", "position": "120", "horizon": "short_term", "goals": ["g1"], "direction": "negative", "confidence": 0.5},
]

def keyed(rows):
    rejected = [r["id"] for r in rows if not r["subject"] or not r["proposition"]]
    groups = {}
    for r in rows:
        if r["id"] in rejected:
            continue
        k = (r["subject"], r["proposition"], r["horizon"], tuple(r["goals"]))
        groups.setdefault(k, []).append(r)
    clashes = []
    for members in groups.values():
        positions = {m["position"] for m in members}
        if len(positions) > 1:
            clashes.append(sorted(m["id"] for m in members))
    return rejected, clashes

def main():
    rejected, clashes = keyed(SIGNALS)
    winner = max(SIGNALS, key=lambda r: r["confidence"])["id"]
    report = {
        "weight_winner": winner,
        "average": 130.0,
        "keyed_rejected": rejected,
        "keyed_clashes": clashes,
        "survives": rejected == ["E"] and clashes == [["A", "B"]],
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
