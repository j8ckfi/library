---
id: paper:es-reasoning
type: paper
title: "Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO"
authors:
  - "Yunpeng Ba"
  - "Zhi Zheng"
  - "Yue Xie"
  - "Jiaqing Li"
  - "Xialiang Tong"
  - "Tao Zhong"
  - "Mingxuan Yuan"
  - "Zhichao Lu"
  - "Xuyang Wu"
  - "Zhenkun Wang"
year: 2026
month: 8
arxiv_id: "2608.27351"
url: "https://arxiv.org/abs/2608.27351"
methods:
  - method:es-reasoning
cites:
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - evolution-strategies
  - passk
  - es-reasoning
---

# Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO

## Abstract Summary
Evolution Strategies post-train LLMs by perturbing parameters, scoring forward-only rollouts, and aggregating reward-weighted perturbations, so no backward pass is stored. Compared with GRPO, ES keeps broader reasoning coverage: it improves Pass@1 over the base model while beating GRPO on Pass@16 and Pass@32, whereas GRPO often drops large-K versus base via entropy collapse. Sequential ES then GRPO / GRPO then ES traces a Pass@1–Pass@K Pareto under a shared update budget. Task gains come from a sparse subset of large-magnitude updates (LayerNorm and attention), not from whole-model drift implying catastrophic forgetting. Z-score normalization is required; two-point ZO does not help regenerated reasoning rewards; larger models need smaller populations.

## Key Contributions
1. **Coverage advantage versus GRPO**: Verifier-projected Jensen–Shannon diversity across the ES population supports higher Pass@K; empirically ES lifts Pass@1, @16, and @32 over base and wins @16/@32 against GRPO.
2. **Functional sparsity**: Large whole-model drift is not widespread functional change; largest ES coordinates are LayerNorm and attention, while GRPO's largest coordinates sit in embeddings / lm_head.
3. **Estimator and scale rules**: Z-score on; one-point ES; $N\approx 32$ at 0.5B, $N=16$ already matches $N=64$ at 1.5B/3B.

## Empirical Highlights
- Easy GSM8K, Qwen2.5-1.5B-Instruct averages: ES 41.5/76.0/80.9 vs GRPO 42.9/75.1/79.9 vs Base 41.0/75.4/80.2 (Pass@1/@16/@32).
- Hard DeepScaleR math average: ES 49.9/75.0/78.9 vs GRPO 52.9/74.7/78.0 vs Base 47.7/73.5/77.4; ES then GRPO 52.3/75.8/79.2.
- FLOP-match: $N=32$ vs GRPO $G=8$. $\sigma=1.5\times 10^{-3}$, $\alpha=2.5\times 10^{-4}$.

## Open Source Repository
- Code: `https://github.com/yunpengba7/understanding-es`
