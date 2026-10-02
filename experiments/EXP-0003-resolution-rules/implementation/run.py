#!/usr/bin/env python3
"""EXP-0003: LWW, recency, contest, supersede, timestamp MVR."""
import json
import random
from collections import defaultdict
from pathlib import Path

EVENTS = [
    {"id": "e1", "key": "span", "val": "120", "src": "s2019", "t": 1, "kind": "obs"},
    {"id": "e2", "key": "span", "val": "140", "src": "s2024", "t": 2, "kind": "obs"},
    {"id": "e3", "key": "span", "val": "140", "src": "s2024b", "t": 3, "kind": "correction", "retires": "e1"},
    {"id": "e4", "key": "route", "val": "open", "src": "am", "t": 1, "kind": "obs"},
    {"id": "e5", "key": "route", "val": "closed", "src": "pm", "t": 2, "kind": "obs"},
    {"id": "e6", "key": "yield", "val": "61", "src": "r1", "t": 1, "kind": "obs"},
    {"id": "e7", "key": "yield", "val": "61", "src": "r2", "t": 2, "kind": "obs"},
]

def lww(ev):
    m = {}
    for e in ev:
        m[e["key"]] = e
    return {k: [v["id"]] for k, v in m.items()}

def recency(ev):
    m = {}
    for e in sorted(ev, key=lambda x: x["t"]):
        m[e["key"]] = e
    return {k: [v["id"]] for k, v in m.items()}

def contest(ev):
    by = defaultdict(list)
    for e in ev:
        if e["kind"] == "correction":
            continue
        by[e["key"]].append(e)
    out = {}
    for k, rows in by.items():
        vals = {r["val"] for r in rows}
        out[k] = {"ids": sorted(r["id"] for r in rows), "clash": len(vals) > 1}
    return out

def supersede(ev):
    current = {}
    history = defaultdict(list)
    for e in sorted(ev, key=lambda x: (x["t"], x["id"])):
        history[e["key"]].append(e["id"])
        if e["kind"] == "correction":
            current[e["key"]] = e["id"]
        elif e["key"] not in current:
            current[e["key"]] = e["id"]
    return {"current": current, "history": dict(history)}

def mvr(ev):
    held = defaultdict(list)
    for e in ev:
        rows = held[e["key"]]
        if e["kind"] == "correction":
            held[e["key"]] = [(e["t"], e["id"], e["val"])]
            continue
        tmax = max((r[0] for r in rows), default=-1)
        if e["t"] > tmax:
            held[e["key"]] = [(e["t"], e["id"], e["val"])]
        elif e["t"] == tmax:
            held[e["key"]].append((e["t"], e["id"], e["val"]))
    return {k: sorted(i for _, i, _ in rows) for k, rows in held.items()}

def main():
    rng = random.Random(0)
    perms = []
    for _ in range(30):
        p = EVENTS[:]
        rng.shuffle(p)
        perms.append(p)
    rules = {"lww": lww, "recency": recency, "contest": contest, "supersede": supersede, "mvr_timestamp": mvr}
    report = {"n_events": len(EVENTS), "n_shuffles": 30, "seed": 0, "rules": {}}
    for name, fn in rules.items():
        first = fn(EVENTS)
        report["rules"][name] = {
            "order_invariant": all(fn(p) == first for p in perms),
            "read": first,
        }
    report["hypothesis_supported"] = (
        report["rules"]["lww"]["order_invariant"] is False
        and all(report["rules"][n]["order_invariant"] for n in ("recency", "contest", "supersede", "mvr_timestamp"))
        and report["rules"]["contest"]["read"]["span"]["clash"] is True
        and report["rules"]["contest"]["read"]["yield"]["clash"] is False
        and "e3" not in report["rules"]["contest"]["read"]["span"]["ids"]
        and report["rules"]["supersede"]["read"]["current"]["span"] == "e3"
        and report["rules"]["supersede"]["read"]["current"]["route"] == "e4"
        and report["rules"]["mvr_timestamp"]["read"]["yield"] == ["e7"]
    )
    out = Path(__file__).resolve().parents[1] / "results" / "results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"hypothesis_supported": report["hypothesis_supported"], "invariant": {k: v["order_invariant"] for k, v in report["rules"].items()}}, indent=2))

if __name__ == "__main__":
    main()
