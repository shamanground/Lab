#!/usr/bin/env python3
import json

def gate(rows):
    rejected, usable = [], []
    for r in rows:
        if not r["lineage_ok"] or not r["subject"] or not r["evidence"]:
            rejected.append(r["id"])
        else:
            usable.append(r)
    groups = {}
    for r in usable:
        k = (r["subject"], r["proposition"], r["horizon"], tuple(r["goals"]))
        groups.setdefault(k, []).append(r)
    out = []
    for members in groups.values():
        positions = {m["position"] for m in members}
        if len(positions) == 1:
            out.append({"state": "not_a_contradiction", "ids": sorted(m["id"] for m in members)})
            continue
        evidence = [tuple(m["evidence"]) for m in members]
        out.append({
            "state": "unresolved",
            "ids": sorted(m["id"] for m in members),
            "winner": None,
            "evidence_basis": "shared" if len(set(evidence)) < len(evidence) else "distinct_ids",
            "independence_claimed": False,
        })
    return {"rejected": rejected, "results": out}

def main():
    A = {"id":"A","subject":"span","proposition":"length_m","position":"120","horizon":"short_term","goals":["g1"],"evidence":["ev1"],"lineage_ok":True}
    B = {"id":"B","subject":"span","proposition":"length_m","position":"140","horizon":"short_term","goals":["g1"],"evidence":["ev2"],"lineage_ok":True}
    S = {"id":"S","subject":"span","proposition":"length_m","position":"140","horizon":"short_term","goals":["g1"],"evidence":["ev1"],"lineage_ok":True}
    F = {"id":"F","subject":"span","proposition":"length_m","position":"90","horizon":"short_term","goals":["g1"],"evidence":["ev9"],"lineage_ok":False}
    D = {"id":"D","subject":"span","proposition":"length_m","position":"140","horizon":"long_term","goals":["g1"],"evidence":["ev2"],"lineage_ok":True}
    first = gate([A,B,S,F,D])
    second = gate([F,D,B,A,S])
    clash = [r for r in first["results"] if r["state"]=="unresolved"][0]
    report = {
        "deterministic": first==second,
        "forged_rejected": first["rejected"]==["F"],
        "ids": clash["ids"],
        "winner": clash["winner"],
        "survives": first==second and first["rejected"]==["F"] and clash["ids"]==["A","B","S"] and clash["winner"] is None and clash["independence_claimed"] is False,
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
