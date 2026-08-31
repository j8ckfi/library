---
id: method:es-reasoning
type: method
title: "ES-Reasoning (Evolution Strategies for LLM Reasoning Coverage)"
category: "rl-alignment"
status: sota
sota_for:
  - task:passk-reasoning-coverage
supersedes: []
papers:
  - paper:es-reasoning
recipes:
  - recipe:es-reasoning
claims:
  - benchmark: "Easy Setting average Pass@K after 2-epoch GSM8K (Qwen2.5-1.5B-Instruct)"
    metric: "Pass@1 / Pass@16 / Pass@32"
    value: "ES 41.5 / 76.0 / 80.9"
    baseline: "GRPO 42.9 / 75.1 / 79.9; Base 41.0 / 75.4 / 80.2"
    date: "2026-08-31"
    verified: true
    notes: "Table 2. GRPO often drops large-K vs base (15 of 18 Easy Pass@16/@32 comparisons). Llama-3.2-3B-Instruct averages: ES 45.9/75.8/80.4 vs GRPO 47.1/72.7/77.0 vs Base 44.1/74.0/78.6. Qwen2.5-7B-Instruct: ES 59.6/80.6/83.1 vs GRPO 61.0/79.0/81.5 vs Base 60.1/80.3/83.0."
  - benchmark: "Hard Setting math average after 1-epoch DeepScaleR (R1-Distill-Qwen-1.5B)"
    metric: "Pass@1 / Pass@16 / Pass@32 on AIME24/AIME25/AMC23/MATH500"
    value: "ES 49.9 / 75.0 / 78.9; ES then GRPO 52.3 / 75.8 / 79.2"
    baseline: "GRPO 52.9 / 74.7 / 78.0; Base 47.7 / 73.5 / 77.4"
    date: "2026-08-31"
    verified: true
    notes: "Table 3. ES then GRPO keeps most of GRPO Pass@1 and the highest Hard Pass@32 under a shared update budget."
tags:
  - post-training
  - rl-alignment
  - evolution-strategies
  - passk
  - es-reasoning
  - sota
---

# ES-Reasoning (Evolution Strategies for LLM Reasoning Coverage)

## Method Overview
Full-parameter one-point Evolution Strategies post-trains an LLM from verifier rewards without backpropagation:
1. **Perturbed forward-only rollouts**: Sample $N$ directions $\epsilon_i\sim\mathcal{N}(0,I)$, evaluate $\theta+\sigma\epsilon_i$ with a task verifier, z-score population rewards $z_i$, then $\theta\leftarrow\theta+(\alpha/N)\sum_i z_i\epsilon_i$. FLOP-matched recipe uses $N=32$ versus GRPO $G=8$, $\sigma=1.5\times 10^{-3}$, $\alpha=2.5\times 10^{-4}$.
2. **Coverage, not entropy collapse**: Population diversity raises Pass@K. GRPO often improves Pass@1 while dropping Pass@16/@32 versus base.
3. **Sequential compositions**: Split a shared update budget as ES then GRPO or GRPO then ES for a Pass@1 versus Pass@K Pareto. ES then GRPO keeps most of GRPO's Pass@1 and the best Hard-setting Pass@32.
4. **Sparse functional updates**: Task gains concentrate in large-magnitude coordinates (LayerNorm and attention), not embeddings / `lm_head` (GRPO's largest coords).
5. **Scaling**: Z-score is required. Two-point / antithetic ZO does not help regenerated reasoning rewards. Larger models need smaller $N$ (0.5B needs $N\approx 32$ to match $N=64$; 1.5B/3B $N=16$ already matches $N=64$).

## When to Use
- When Pass@K / reasoning-path coverage matters more than squeezing Pass@1.
- When backward-pass memory is the bottleneck (forward-only perturbed rollouts).

## Relation to Existing SOTA
- First-hop for `task:passk-reasoning-coverage` only. Listed on `task:math-code-rl-dense` as a coverage alternative. Does **not** replace `method:cispo` (Pass@1 dense RLVR default with MiniMax-M1 / ScaleRL).
- This is **not** a GRPO revival. GRPO stays superseded as the library's math/code RLVR default (`method:cispo` supersedes `method:dapo` supersedes `method:grpo`).

## Gotchas & Failure Modes
- Must z-score population rewards. Raw rewards underperform.
- Do not switch to two-point / antithetic ZO for reasoning; regenerated CoT breaks paired covariance that helps supervised ZO.
- Sequential ES then GRPO is a Pareto mix under a shared budget, not a reason to pick GRPO alone.
- Inner GRPO in `method:j-zero` can be swapped for ES when coverage matters; do not rewrite J-Zero's paper recipe.
