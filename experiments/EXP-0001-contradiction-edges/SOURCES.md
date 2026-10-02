# Sources

Hypothesis: a contest-edge store keeps both poles and provenance across insertion order; last-write-wins does not.

Used:

- Lab `exp02_axis_compression/Report/report.md`. That run coded contradiction handling in model outputs. It did not test a store. The gap is why this experiment exists.
- Memory of Memory / Provenant Memory, arXiv HTML 2609.25054, read 2026-10-02. Claim used: write-time overwrite drops the displaced value; a provenance graph can contest without deletion. https://arxiv.org/html/2609.25054v1
- Mnemoverse note on knowledge-graph memory, read 2026-10-02, only as a pointer to keeping contradictions live. It cites TOKI, arXiv 2606.06240, and Eywa, arXiv 2605.30771. Those two papers were not fetched in full. https://mnemoverse.com/docs/library/knowledge-graph-memory-for-agents

Not used as evidence:

- X posts the same night about vector stores and on-chain provenance. Marketing. No code traced.
- AgentPatterns generative provenance note, 2026-10-01. Watched, not this test. https://agentpatterns.ai/verification/generative-provenance-records/
