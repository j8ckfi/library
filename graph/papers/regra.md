---
id: paper:regra
type: paper
title: 'ReGRA: Residual-Gradient Adaptation for Complementary Low-Rank Fine-Tuning'
authors:
- Fanyao Li
- Yuxi Liu
- Xiaohao Liu
- He Chang
- Zhaoxin Wang
- Zhulin Tao
year: 2026
month: 10
arxiv_id: '2610.19700'
url: https://arxiv.org/abs/2610.19700
methods:
- method:regra
cites:
- paper:dt-lora
- paper:lr-matters-lora
tags:
- peft
- lora
- residual-gradient
---

# ReGRA

## Abstract Summary
Raising LoRA rank does not guarantee useful extra directions. ReGRA spends a fixed rank in two stages: residual gradients after stage 1 initialize a complementary adapter that merges at deploy.

## Key Contributions
1. Top-component diagnostic on rank-16 LoRA.
2. Residual-gradient second-stage init plus orthogonality regularizer.
3. GLUE and Llama-3-8B math vs matched-rank and 2x-rank LoRA.

## Empirical Highlights
- RoBERTa-base GLUE 84.74 vs LoRA r=8 83.21 / r=16 83.97.
- RoBERTa-large 88.42 vs 87.73/87.75; Llama-3-8B math 72.14 vs 70.83.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19700`
- Code: `https://github.com/Fanyao-Li/ReGRA` (`code_status: released`).
