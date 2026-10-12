---
id: paper:state-opd
type: paper
title: 'State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents'
authors:
- Zhentao Zhang
- Yanzhao Zheng
- Yanlin Liu
- Yuanqiang Yu
- Tianze Xu
- Chao Ma
- Jihuai Zhu
- Lelun Wu
- Baohua Dong
- Hangcheng Zhu
- Ruohui Huang
- Gang Yu
year: 2026
month: 10
arxiv_id: '2610.13238'
url: https://arxiv.org/abs/2610.13238
methods:
- method:state-opd
cites:
- paper:opd
- paper:pivotopd
- paper:actfirst-opd
tags:
- post-training
- distillation
- opd
- agentic
- state-opd
---

# State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents

## Abstract Summary
Student reasoning in multi-turn OPD has two roles: prior reasoning distorts teacher supervision; current reasoning shapes action alternatives at the same state. State-OPD grounds the teacher in the interaction state (not the student's semantic trajectory), reallocates sampling to multiple complete reasoning-action responses at high-entropy states, and keeps full-history student generation.

## Key Contributions
1. Interaction-state vs semantic-trajectory split for agentic OPD.
2. Budget reallocation to high-entropy states with complete reasoning-action resamples.
3. Qwen3-4B macro-average 26.07→31.74; beats a 32B teacher on ALFWorld Seen.

## Empirical Highlights
- See `method:state-opd` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13238`
- Code: `none found` (`code_status: none`).
