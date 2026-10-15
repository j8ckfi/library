---
id: paper:forkgrpo
type: paper
title: 'ForkGRPO: Efficient Exploration and Fine-Grained Credit Assignment for Diffusion Language Models'
authors:
- Zhaoyan Jia
- Chengwei Zhou
- Gourav Datta
- Massoud Pedram
year: 2026
month: 10
arxiv_id: '2610.19408'
url: https://arxiv.org/abs/2610.19408
methods:
- method:forkgrpo
cites:
- paper:a2d
- paper:justopd
- paper:canvasanneal
tags:
- diffusion
- dllm
- rlvr
---

# ForkGRPO

## Abstract Summary
dLLM RL still fights entropy collapse. Left-to-right GRPO helps but under-explores forks and assigns uniform trajectory credit. ForkGRPO branches from high-entropy intermediate states and splits within-state group advantages from Monte Carlo segment values.

## Key Contributions
1. Prefix-reused forks at high-entropy / boundary states.
2. Two-level credit: continuation choice vs segment value.
3. ForkGRPO-fast wall-clock variant.

## Empirical Highlights
- GSM8K/MATH-500/HumanEval/MBPP 90.4/46.6/51.8/49.0 vs JustGRPO +0.8/+0.6/+1.2/+0.4.
- 18.75-27.83% fewer generated tokens; ForkGRPO-fast 2.49x at 90.3 GSM8K.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19408`
- Code: `none found` (`code_status: none`).
