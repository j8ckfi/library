---
id: paper:iris
type: paper
title: "Iris: Climbing to the Search Frontier"
authors:
  - "Ziyuan Liu"
  - "Hengqi Liu"
  - "Zichuan Wang"
  - "Yang Qin"
  - "Jiachen Liang"
  - "Xu Chu"
  - "Shaowei Chen"
  - "Yuantao Gu"
  - "Mu Chuan"
year: 2026
month: 9
arxiv_id: "2609.04304"
url: "https://arxiv.org/abs/2609.04304"
methods:
  - method:iris
cites: []
tags:
  - post-training
  - agentic
  - web-search
  - sft-rl-climbing
  - iris
---

# Iris: Climbing to the Search Frontier

## Abstract Summary
Iris-mini (Qwen3.6-35B-A3B) and Iris-pro (Qwen3.5-397B-A17B) are live-web search agents plus the data and train recipe behind them. Multi-hop questions are reverse-constructed from a web hyperlink graph: entity chains from a seed page and its out-links, non-answer entities rewritten so clues are not string-matchable, kept only when a reference model fails closed-book and succeeds given the supporting evidence. Teacher ReAct trajectories are filtered at trajectory level (correct, non-degenerate, minimum tool depth) then turn level (data-induced KEEP/MASK rubric, at most 10% of assistant turns masked). RL is against live search with an in-cluster judge and observation summarizer (Qwen3.5-397B-A17B FP8), and over-long rollouts are interrupted at the request level and resumed from the committed prefix. SFT and RL alternate as **SFT-RL climbing**: hardest solved, most efficient RL rollouts are recycled into the next SFT. Evaluation is a single ReAct agent, no sub-agents and no test-time verification, with and without context management under a fixed tool set, context limit, and judge. With discard-all CM: BrowseComp / BrowseComp-ZH / DeepSearchQA / HLE-text Iris-mini 82.2 / 84.8 / 86.9 / 52.3 and Iris-pro 88.6 / 85.1 / 92.9 / 56.4.

## Key Contributions
1. **Reverse-constructed multi-hop web tasks** from a hyperlink entity graph with dual-criteria (hard and solvable) admission.
2. **Trajectory then turn filtering** before SFT, including a data-induced turn rubric and ≤10% MASK.
3. **Live-search RL** with in-cluster GenRM + summarizer and request-level partial rollout (truncated IS on spliced prefixes).
4. **SFT-RL climbing**: recycle 0 < pass-rate ≤ 1/2, ≥K_rft tool turns, shortest successful trajectory back into SFT.

## Empirical Highlights
- Table 1 (CM enabled, discard-all for Iris): 30-35B Iris-mini BrowseComp 82.2 vs Aquila-mini 78.8; BrowseComp-ZH 84.8 vs 82.9; HLE 52.3 vs 51.1; DeepSearchQA 86.9 vs Aquila-mini 89.5 (Iris not best on this column).
- ~400B Iris-pro 88.6 / 85.1 / 92.9 / 56.4 vs Aquila-pro 84.8 / 85.1 / 92.5 / 53.3.
- Table 2 no-CM: Iris-mini BrowseComp 64.7 vs FORT-Searcher 55.9; discard-all +17.5 to 82.2. Iris-pro no-CM 72.6 → 88.6.
- Frontier still ahead (Kimi-K3 BrowseComp 91.2). discard-all+retry Iris-pro 90.3 is an upper bound, not the default table.

## Open Source Repository & Resources
- Code / harness: `https://github.com/AllSpark-Research/Iris` (`Iris-Harness`). Weights: Hugging Face `AllSpark-Research/Iris-mini`, `AllSpark-Research/Iris-pro`. RL engine cited: Relax (`redai-infra/Relax`).
