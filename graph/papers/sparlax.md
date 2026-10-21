---
id: paper:sparlax
type: paper
title: 'Sparse RL Relaxation for LLM Reasoning'
authors:
- 'Jiabin Fan'
- 'Matthias Lindemann'
- 'Zita Marinho'
- 'André FT Martins'
- 'Lili Mou'
year: 2026
month: 10
arxiv_id: '2610.27220'
url: https://arxiv.org/abs/2610.27220
methods:
- method:sparlax
cites:
- paper:minimax-m1
tags:
- rlvr
- soft-cot
- active
---

# Sparse RL Relaxation for LLM Reasoning

## Abstract Summary
SpaRLax trains soft-CoT by backpropagating through differentiable mixture tokens and using entmax sparsity so confident steps collapse while uncertain steps keep several candidates.

## Key Contributions
1. Sparse-relaxed soft-CoT RL with cross-step gradients.

## Empirical Highlights
- Highest average among compared soft-CoT RL methods on nine reasoning benches.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27220`
- Code: `none found` (`code_status: none`).
