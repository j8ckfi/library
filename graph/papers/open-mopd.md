---
id: paper:open-mopd
type: paper
title: "Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation"
authors:
  - "Huan-ang Gao"
  - "Haohan Chi"
  - "Yong Yan"
  - "Shiyuan Feng"
  - "Hanlin Wu"
  - "Zheng Jiang"
  - "Bingxiang He"
  - "Wei-Ying Ma"
  - "Ya-Qin Zhang"
  - "Hao Zhou"
year: 2026
month: 8
arxiv_id: "2608.19098"
url: "https://arxiv.org/abs/2608.19098"
methods:
  - method:open-mopd
cites:
  - paper:opd
  - paper:nemotron-cascade-2
  - paper:kimi-k3
tags:
  - post-training
  - distillation
  - multi-teacher
  - open-mopd
---

# Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation

## Abstract Summary
Multi-teacher on-policy distillation (M-OPD) consolidates domain-specialized expert models into a single generalist student via dense token-level supervision. However, standard M-OPD suffers from a severe capability integration gap—capturing only 35.6% of available headroom relative to domain-routed oracle ensembles, with concise tasks like instruction following undergoing severe degradation. This failure stems not from gradient conflict, but from a severe misallocation of token-level optimization budgets driven by sequence-length disparities, dynamic convergence drift, and multi-step reward staleness. Open-MOPD resolves these pathologies through token-share balancing, gap-aware dynamic budget allocation, and student reward refresh, elevating headroom recovery from 35.6% to 83.4% in a single deployable student.

## Key Contributions
1. **Capability Imbalance Diagnosis**: Identifies that M-OPD performance collapse is caused by token budget misallocation (long chain-of-thought vs concise instructions), dynamic convergence rate disparities, and reward staleness rather than gradient direction interference.
2. **Token-Share Balancing**: Equalizes domain gradient contributions regardless of raw token length differences across domains.
3. **Gap-Aware Dynamic Budget Allocation**: Dynamically scales domain optimization weights based on student-to-teacher headroom gaps.
4. **Student Reward Refresh**: Mitigates reward staleness from asynchronous policy updates.
5. **Empirical Headroom Recovery**: Boosts oracle headroom recovery from 35.6% to 83.4% on SmolLM3-3B with fully open-sourced recipes and evaluation suites.

## Open Source Repository
- Project Page: `https://bytedtsinghua-sia.github.io/Open-MOPD/`
- Code Repository: `https://github.com/BytedTsinghua-SIA/Open-MOPD`
