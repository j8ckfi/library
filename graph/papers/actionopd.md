---
id: paper:actionopd
type: paper
title: 'ActionOPD: Distilling Decisions, Not Tokens'
authors:
- Huining Yuan
- Xiangmin Yi
- Zelai Xu
- Zixu Wang
- Xinlei Chen
- Xiao-Ping Zhang
- Yu Wang
- Chao Yu
year: 2026
month: 10
arxiv_id: '2610.19820'
url: https://arxiv.org/abs/2610.19820
methods:
- method:actionopd
cites:
- paper:opd
- paper:canopy
tags:
- distillation
- opd
- agents
---

# ActionOPD

## Abstract Summary
Token-level OPD needs teacher log-probs and compatible tokenization. ActionOPD treats semantic actions as the unit: sample student and teacher actions at student states and reward agreement.

## Key Contributions
1. Action-level on-policy distill without teacher token probabilities.
2. Cross-family / cross-tokenizer teacher-student pairs.
3. Released trainer at thu-nics/ActionOPD.

## Empirical Highlights
- Qwen3-4B/8B +3.3-6.9pp on four OOD tool-use benches.
- Competitive with offline distillation and token-level OPD on tau2-bench.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19820`
- Code: `https://github.com/thu-nics/ActionOPD` (`code_status: released`).
