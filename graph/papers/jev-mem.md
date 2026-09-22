---
id: paper:jev-mem
type: paper
title: "Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents"
authors:
  - "Dongming Jiang"
  - "Yi Li"
  - "Bingzhe Li"
year: 2026
month: 9
arxiv_id: "2609.23986"
url: "https://arxiv.org/abs/2609.23986"
methods:
  - method:jev-mem
cites:
  - paper:ace
  - paper:code2skill
  - paper:memgpt
tags:
  - agents
  - agent-memory
  - jev-mem
---

# Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents

## Abstract Summary
Many agentic memory systems put an autoregressive LLM on the critical path of typing, routing, budget, traversal, scoring, and stop. Jev-Mem splits System-One control from System-Two reasoning. A dedicated System-One plane governs memory typing and multi-relational organization on the write path, and query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping on the read path. Canonical observations sit in a shared memory with semantic, temporal, causal, and entity views. System Two is invoked only for hard reasoning and answer synthesis. On LoCoMo with GPT-4o-mini as the answer model, Jev-Mem reaches LLM-as-a-Judge 0.777 (+11.0% relative vs MAGMA 0.700), builds memory in 158 s (6.6× vs fastest competitor Nemori 1,044 s), and queries at 0.93 s (−36.7% vs MAGMA 1.47 s).

## Key Contributions
1. **System-One control plane**: typed probabilistic decisions (Noul / Choice) for high-frequency memory ops, not free-form generation.
2. **Multi-relational memory**: one node set, four graph views, plus vector and lexical indexes.
3. **Adaptive retrieval loop**: route, budget, expand, score, stop; escalate to System Two only for synthesis.

## Empirical Highlights
- LoCoMo overall judge 0.777 vs MAGMA 0.700 / Nemori 0.590 / A-MEM 0.580 / MemoryOS 0.553 / full context 0.481.
- Category: Multi-Hop 0.623, Open-Domain 0.618, Single-Hop 0.802, Adversarial 0.962; Temporal 0.637 (MAGMA 0.650).
- Construction 158 s vs Nemori 1,044 s (6.6×). Query latency 0.93 s vs MAGMA 1.47 s.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.23986`
- Code: `https://github.com/libingzheren/Jev-Mem` (`code_status: released`).
- Space: Hugging Face `libingzheren/Jev-Mem`.
