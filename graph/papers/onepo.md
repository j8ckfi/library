---
id: paper:onepo
type: paper
title: "HuatuoGPT-3: RL-Only Domain Adaptation from Base Models"
authors:
  - Junying Chen
  - Xinyuan Xie
  - Ziniu Li
  - Wenyuan Gu
  - Jianquan Li
  - Xiang Wan
  - Guangjun Yu
  - Ruoyu Sun
  - Haizhou Li
  - Benyou Wang
year: 2026
month: 10
arxiv_id: "2610.05966"
url: "https://arxiv.org/abs/2610.05966"
methods:
  - method:onepo
cites:
  - paper:olmo-3
  - paper:minimax-m1
tags:
  - post-training
  - rl-alignment
  - domain-adaptation
  - onepo
  - huatuogpt-3
---

# HuatuoGPT-3: RL-Only Domain Adaptation from Base Models

## Abstract Summary
SFT+RL cold-start can shrink exploration. Pure on-policy RL cold-starts badly; mixed-policy RL hits Gradient Starvation and Teacher-Distribution Anchoring. OnePO treats teacher outputs as transient guidance: Adaptive Objective Evolution on informative low-probability teacher tokens, then Teacher Retirement when the policy surpasses them. Medical: HealthBench Total 67.2 with 20K samples, +2.7 vs SFT+RL and +7.4 vs pure RL. Scaled HuatuoGPT-3 27B: 70.1 Total / 71.4 Professional. Code: https://github.com/FreedomIntelligence/HuatuoGPT-3. Plug-in on instruct-sft-alignment; does not retarget OLMo-3 or CISPO.

## Key Contributions
1. **OnePO**: teacher outputs as transient guidance, not a frozen SFT mix.
2. **Adaptive Objective Evolution + Teacher Retirement**.
3. **HuatuoGPT-3**: open medical series; 27B HealthBench 70.1 / 71.4 Professional.

## Empirical Highlights
- HealthBench Total 67.2 with 20K samples; +2.7 vs SFT+RL, +7.4 vs pure RL.
- HuatuoGPT-3 27B: 70.1 Total / 71.4 Professional.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05966`
- Code: `https://github.com/FreedomIntelligence/HuatuoGPT-3` (`code_status: released`; HTTP 200 as of 2026-10-06).
