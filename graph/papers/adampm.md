---
id: paper:adampm
type: paper
title: 'AdamPM: Memory-Efficient LLM Optimization via Moment Pooling'
authors:
- 'Xiaowei Ji'
- 'Lishan Xu'
- 'Jianing An'
- 'Jie Luo'
- 'Wenjun Wu'
- 'Lei Huang'
year: 2026
month: 10
arxiv_id: '2610.24598'
url: https://arxiv.org/abs/2610.24598
methods:
- method:adampm
cites:
- paper:scale
tags:
- optimizer
- memory-efficient
- active
---

# AdamPM

## Abstract Summary
AdamPM pools adjacent Adam second-moment entries along a row or column into a shared mean. Group size s cuts second-moment memory to 1/s. Second-moment pooling is the effective design; hyperparameters transfer from Adam.

## Key Contributions
1. Drop-in Adam second-moment pooling without extra HP search.

## Empirical Highlights
- LLaMA pretrain, GLUE FT, and multimodal runs match Adam quality and step time at lower optimizer-state memory.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24598`
- Code: `https://github.com/jixiaowei95/AdamPM` (`code_status: released`).
