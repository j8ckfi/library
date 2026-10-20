---
id: paper:arctic-swe
type: paper
title: 'Arctic-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design'
authors:
- 'Boyi Liu'
- 'Yite Wang'
- 'Xinyu Lian'
- 'Fan Shu'
- 'Sida Li'
- 'Feng Yan'
- 'Mingjia Zhang'
- 'Yuxiong He'
- 'Zhewei Yao'
year: 2026
month: 10
arxiv_id: '2610.24914'
url: https://arxiv.org/abs/2610.24914
methods:
- method:arctic-swe
cites:
- paper:sao
- paper:miles
tags:
- rl-alignment
- swe
- async-rl
- active
---

# Arctic-SWE

## Abstract Summary
An async SWE RL baseline on Prime-RL. Overfit-on-small-pool is the stress test. On raw R2E-Gym, Qwen3.5-4B reaches 62.0% SWE-bench Verified pass@1 without new algorithms. Curated data then reaches 65.0/38.3/59.7 on Verified/Pro-v1/Pro-v2.

## Key Contributions
1. Gated reward, IS control, aligned engines, execution-grounded test repair.

## Empirical Highlights
- Unsealed eval environments inflate scores; the paper audits that channel.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24914`
- Code: `none found` (`code_status: none`).
