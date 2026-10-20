---
id: paper:agentic-rl-data-scaling
type: paper
title: 'How Data Scales in Agentic Reinforcement Learning: Laws and Synthesis Strategies'
authors:
- 'Bowei He'
- 'Yankai Chen'
- 'Xiaokun Zhang'
- 'Changjiang Han'
- 'Ye Yuan'
- 'Chong Li'
- 'Xue Liu'
year: 2026
month: 10
arxiv_id: '2610.23946'
url: https://arxiv.org/abs/2610.23946
methods:
- method:agentic-rl-data-scaling
cites:
- paper:codemidas
- paper:canopy
tags:
- rl-alignment
- scaling-laws
- active
---

# Agentic RL Data Scaling

## Abstract Summary
Agentic RL data is not a token count. The paper fits environment, task, and trajectory exponents and a compute-optimal recipe D_E* ∝ C^0.34, D_T* ∝ C^0.27, D_τ* ∝ C^0.13, N* ∝ C^0.26. NeurIPS 2026.

## Key Contributions
1. Per-axis discount factors and isoFLOP validation of the allocation.

## Empirical Highlights
- Matched-token Qwen3-8B GRPO runs diverge when only the axis split changes.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23946`
- Code: `none found` (`code_status: none`).
