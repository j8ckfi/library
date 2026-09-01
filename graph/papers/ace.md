---
id: paper:ace
type: paper
title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
authors:
  - "Qizheng Zhang"
  - "Changran Hu"
  - "Shubhangi Upasani"
  - "Boyuan Ma"
  - "Fenglu Hong"
  - "Vamsidhar Kamanuru"
  - "Jay Rainton"
  - "Chen Wu"
year: 2025
month: 10
arxiv_id: "2510.04618"
url: "https://arxiv.org/abs/2510.04618"
methods:
  - method:ace
cites: []
tags:
  - agents
  - agent-memory
  - ace
---

# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

## Abstract Summary
ACE evolves an agent playbook as incremental bullets (Generator / Reflector / Curator) instead of rewriting the whole context. It is the memory default for agents that accumulate strategies. It is not a long-context dump strategy (that is RLM) and not a SWE bash loop.

Without execution feedback, ACE and Dynamic Cheatsheet can degrade. Recursive summary as the only long-context strategy fails (RLM paper: compaction OOLONG-Pairs F1 0.1).

## Key Contributions
1. Three-role loop: Generator trajectories, Reflector insights, Curator incremental delta bullets.
2. Counterexample to rewrite-based memory: Dynamic Cheatsheet 18282 tok @66.7 → 122 tok @57.1 (context collapse).
3. Lower adaptation latency versus GEPA.

## Empirical Highlights
- AppWorld, DeepSeek-V3.1: ACE **59.4** vs ReAct 42.4 (+17).
- vs GEPA: latency **−82%** (offline AppWorld −82.3% latency / −75.1% rollouts in the paper's efficiency table).
- Dynamic Cheatsheet collapse: 18282 tokens at 66.7 → 122 tokens at 57.1.

## Open Source
- `https://github.com/ace-agent/ace`
