#!/usr/bin/env python3
import json, random
from collections import defaultdict
from pathlib import Path
EVENTS = json.loads((Path(__file__).resolve().parents[1] / "fixtures" / "events.json").read_text())

def lww(ev):
    m = {}
    for e in ev:
        m[e["key"]] = e["id"]
    return m

def recency(ev):
    m = {}
    for e in sorted(ev, key=lambda x: x["t"]):
        m[e["key"]] = e["id"]
    return m

def contest(ev):
    by = defaultdict(list)
    for e in ev:
        if e["kind"] != "correction":
            by[e["key"]].append(e)
    return {k: {"ids": sorted(r["id"] for r in rows), "clash": len({r["val"] for r in rows}) > 1} for k, rows in by.items()}

def supersede(ev):
    current = {}
    for e in sorted(ev, key=lambda x: (x["t"], x["id"])):
        if e["kind"] == "correction" or e["key"] not in current:
            current[e["key"]] = e["id"]
    return current

def main():
    rng = random.Random(0)
    perms = []
    for _ in range(30):
        p = EVENTS[:]
        rng.shuffle(p)
        perms.append(p)
    rules = {"lww": lww, "recency": recency, "contest": contest, "supersede": supersede}
    out = {name: all(fn(p) == fn(EVENTS) for p in perms) for name, fn in rules.items()}
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
