---
id: paper:cppo
type: paper
title: "Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning"
authors:
  - "Renjie Mao"
  - "Xiangxin Zhou"
  - "Lvfang Tao"
  - "Yixin Ding"
  - "Yu Shi"
  - "Yongguang Lin"
  - "Yuheng Wu"
  - "Honglin Zhu"
  - "Qian Qiu"
  - "Wenxi Zhu"
year: 2026
month: 6
arxiv_id: "2606.10968"
url: "https://arxiv.org/abs/2606.10968"
methods:
  - method:cppo
cites: []
tags:
  - post-training
  - rl-alignment
  - reasoning
  - trust-region
  - cppo
---

# Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning

## Abstract Summary
Standard PPO-style token-level trust regions treat all token positions uniformly, which conflicts with finite-horizon policy-improvement bounds where early token drift has a cascading effect on downstream trajectory distributions. Cumulative Prefix-divergence Policy Optimization (CPPO) introduces a token-level masking rule combining position-weighted thresholds (stricter early, looser late) and a cumulative prefix budget that bounds cumulative drift along the sequence.

## Key Contributions
1. **Non-Uniform Trust Region**: Analyzes theoretical limitations of uniform token-level clipping under sequential generation.
2. **Cumulative Prefix-Divergence Masking**: Implements dynamic token masking governed by position-weighted thresholds and sequence-level prefix divergence accumulation.
3. **Finite-Horizon Alignment**: Guarantees monotonic policy improvement by bounding cascading trajectory distribution shifts.

## Open Source Repository
- Project Page: `https://hunyuan-cppo.github.io/`
