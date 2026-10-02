#!/usr/bin/env python3
"""EXP-0001: contest-edge store vs last-write-wins. Stdlib only."""
import json
import random
from pathlib import Path

FIXTURE = [
    {"id": "e1", "subject": "bridge.span", "predicate": "length_m", "object": "120", "source": "survey-2019"},
    {"id": "e2", "subject": "bridge.span", "predicate": "length_m", "object": "140", "source": "survey-2024"},
    {"id": "e3", "subject": "alloy.batch7", "predicate": "process", "object": "annealed", "source": "lab-a"},
    {"id": "e4", "subject": "alloy.batch7", "predicate": "process", "object": "quenched", "source": "lab-b"},
    {"id": "e5", "subject": "route.north", "predicate": "status", "object": "open", "source": "ops-am"},
    {"id": "e6", "subject": "route.north", "predicate": "status", "object": "closed", "source": "ops-pm"},
    {"id": "e7", "subject": "catalyst.x", "predicate": "yield_pct", "object": "61", "source": "run-1"},
    {"id": "e8", "subject": "catalyst.x", "predicate": "yield_pct", "object": "61", "source": "run-2"},
    {"id": "e9", "subject": "sensor.q", "predicate": "unit", "object": "celsius", "source": "manual"},
    {"id": "e10", "subject": "sensor.q", "predicate": "unit", "object": "kelvin", "source": "firmware"},
]
QUERIES = [
    ("bridge.span", "length_m"),
    ("alloy.batch7", "process"),
    ("route.north", "status"),
    ("catalyst.x", "yield_pct"),
    ("sensor.q", "unit"),
]
CONTRA = {"bridge.span", "alloy.batch7", "route.north", "sensor.q"}

def key(rec):
    return (rec["subject"], rec["predicate"])

class LWW:
    def __init__(self):
        self.map = {}
    def add(self, rec):
        self.map[key(rec)] = rec
    def read(self, subject, predicate):
        rec = self.map.get((subject, predicate))
        return [] if rec is None else [rec]

class Contest:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    def add(self, rec):
        self.nodes[rec["id"]] = rec
        for other in list(self.nodes.values()):
            if other["id"] == rec["id"]:
                continue
            if key(other) == key(rec) and other["object"] != rec["object"]:
                edge = (tuple(sorted([other["id"], rec["id"]])), "CONTRADICTS")
                if edge not in self.edges:
                    self.edges.append(edge)
        self.edges.sort()
    def read(self, subject, predicate):
        hits = sorted((r for r in self.nodes.values() if key(r) == (subject, predicate)), key=lambda r: r["id"])
        ids = {h["id"] for h in hits}
        edges = sorted(e for e in self.edges if set(e[0]) <= ids)
        return hits, edges

def run(order):
    lww, cg = LWW(), Contest()
    for rec in order:
        lww.add(rec)
        cg.add(rec)
    rows = []
    for s, p in QUERIES:
        lhits = lww.read(s, p)
        chits, edges = cg.read(s, p)
        rows.append({
            "subject": s,
            "predicate": p,
            "lww_ids": [h["id"] for h in lhits],
            "lww_objects": [h["object"] for h in lhits],
            "lww_sources": [h["source"] for h in lhits],
            "contest_ids": [h["id"] for h in chits],
            "contest_objects": [h["object"] for h in chits],
            "contest_sources": [h["source"] for h in chits],
            "contest_edges": edges,
        })
    return rows

def main():
    base = run(FIXTURE)
    rng = random.Random(0)
    shuffles = []
    for _ in range(20):
        perm = FIXTURE[:]
        rng.shuffle(perm)
        shuffles.append(run(perm))
    contest_fields = ["subject", "predicate", "contest_ids", "contest_objects", "contest_sources", "contest_edges"]
    lww_fields = ["subject", "predicate", "lww_ids", "lww_objects", "lww_sources"]
    def proj(rows, fields):
        return [{k: row[k] for k in fields} for row in rows]
    contra = [q for q in base if q["subject"] in CONTRA]
    agree = next(q for q in base if q["subject"] == "catalyst.x")
    result = {
        "n_records": len(FIXTURE),
        "n_shuffles": 20,
        "seed": 0,
        "lww_one_pole_on_contradictions": all(len(q["lww_objects"]) == 1 for q in contra),
        "lww_drops_displaced_provenance": all(len(q["lww_sources"]) == 1 for q in contra),
        "contest_both_poles": all(len(set(q["contest_objects"])) == 2 and len(q["contest_ids"]) == 2 for q in contra),
        "contest_edges_on_contradictions": all(len(q["contest_edges"]) == 1 for q in contra),
        "agreement_two_sources_zero_edges": agree["contest_ids"] == ["e7", "e8"] and agree["contest_edges"] == [] and agree["lww_objects"] == ["61"],
        "contest_order_invariant": all(proj(r, contest_fields) == proj(base, contest_fields) for r in shuffles),
        "lww_order_invariant": all(proj(r, lww_fields) == proj(base, lww_fields) for r in shuffles),
        "base_read": base,
    }
    result["hypothesis_supported"] = all([
        result["lww_one_pole_on_contradictions"],
        result["lww_drops_displaced_provenance"],
        result["contest_both_poles"],
        result["contest_edges_on_contradictions"],
        result["agreement_two_sources_zero_edges"],
        result["contest_order_invariant"],
        result["lww_order_invariant"] is False,
    ])
    out = Path(__file__).resolve().parents[1] / "results" / "results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in result if k != "base_read"}, indent=2))

if __name__ == "__main__":
    main()
