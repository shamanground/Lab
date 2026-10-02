# Signal — provenance retention vs overwrite

- date: 2026-10-02
- source: arXiv HTML 2609.25054 (Memory of Memory / P-Mem), Mnemoverse note citing TOKI arXiv 2606.06240 and Eywa arXiv 2605.30771, AgentPatterns generative provenance note 2026-10-01
- links: https://arxiv.org/html/2609.25054v1 ; https://mnemoverse.com/docs/library/knowledge-graph-memory-for-agents ; https://agentpatterns.ai/verification/generative-provenance-records/
- claim: write-time CRUD memory overwrites, so a displaced value and its provenance are unrecoverable; a typed provenance graph can contest or supersede without deletion. Separate claim: agents emit trajectories but not claim-level evidence spans.
- why it matters: Prime Atlas #25 is contradiction preservation and is not started. Lab has no store-level test of pole retention.
- confidence: medium on the mechanism claim (paper states it; not re-benchmarked here). Low on X posts the same night about vector stores and on-chain provenance; those are marketing, not evidence.
- related Lab concept: EXP-02 coded contradiction handling in model outputs, not in a store.
- related Prime Atlas concept: #25 Contradiction Preservation Layer. #24 dedup is closed and is a different operation.
- experimentation justified: yes, synthetic, no API.
- triage: EXPERIMENT for store mechanic. WATCH for generative provenance records. IGNORE for X vector-database and chain-provenance posts.
