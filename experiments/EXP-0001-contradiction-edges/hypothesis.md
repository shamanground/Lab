# EXP-0001 hypothesis

A contest-edge store that keeps every observation, and adds a CONTRADICTS edge only when the same subject and predicate have incompatible objects, returns both poles and both provenance ids independent of insertion order. A last-write-wins map on (subject, predicate) returns one pole, drops the displaced provenance, and the survivor depends on insertion order.

Failure: the contest store drops a pole, emits an edge on an agreeing pair, or changes its read with insertion order.
