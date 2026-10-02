#!/usr/bin/env python3
"""EXP-0001 visitor reproduction. Stdlib only."""
import json, random
from pathlib import Path

FIXTURE = json.loads((Path(__file__).resolve().parents[1] / "fixtures" / "claims.json").read_text())
QUERIES = [("bridge.span","length_m"),("alloy.batch7","process"),("route.north","status"),("catalyst.x","yield_pct"),("sensor.q","unit")]
CONTRA = {"bridge.span","alloy.batch7","route.north","sensor.q"}

def key(rec):
    return (rec["subject"], rec["predicate"])

class LWW:
    def __init__(self):
        self.map = {}
    def add(self, rec):
        self.map[key(rec)] = rec
    def read(self, s, p):
        rec = self.map.get((s, p))
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
    def read(self, s, p):
        hits = sorted((r for r in self.nodes.values() if key(r) == (s, p)), key=lambda r: r["id"])
        ids = {h["id"] for h in hits}
        return hits, sorted(e for e in self.edges if set(e[0]) <= ids)

def run(order):
    lww, cg = LWW(), Contest()
    for rec in order:
        lww.add(rec)
        cg.add(rec)
    rows = []
    for s, p in QUERIES:
        lhits = lww.read(s, p)
        chits, edges = cg.read(s, p)
        rows.append({"subject": s, "lww": [h["id"] for h in lhits], "contest": [h["id"] for h in chits], "edges": edges})
    return rows

def main():
    base = run(FIXTURE)
    rng = random.Random(0)
    shuffles = [run((lambda p: (random.Random(0), p))[1]) for _ in []]
    rng_rows = []
    for _ in range(20):
        perm = FIXTURE[:]
        rng.shuffle(perm)
        rng_rows.append(run(perm))
    contest_stable = all([r["contest"] for r in row] == [r["contest"] for r in base] for row in rng_rows)
    lww_variants = {tuple(r["lww"][0] for r in row) for row in [base] + rng_rows}
    print(json.dumps({"contest_stable": contest_stable, "lww_variant_count": len(lww_variants)}, indent=2))

if __name__ == "__main__":
    main()
