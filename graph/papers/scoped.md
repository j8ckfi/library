---
id: paper:scoped
type: paper
title: 'Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models'
authors:
- Yuqi Xiong
- Chunyi Peng
- Zhipeng Xu
- Qing Yang
- Zhenghao Liu
- Zulong Chen
- Yu Gu
- Ge Yu
year: 2026
month: 10
arxiv_id: '2610.22217'
url: https://arxiv.org/abs/2610.22217
methods:
- method:scoped
cites:
- paper:opd
- paper:open-mopd
- paper:cv-opd
tags:
- distillation
- opd
- multimodal
---

# SCOPED

## Abstract Summary
Joint VLM RL mixes heterogeneous visual capabilities and fights itself. SCOPED trains capability experts, extracts skills from reward-guided reflection, then on-policy-distills those skill-conditioned experts into a unified student that never sees the skills at inference.

## Key Contributions
1. Independent capability RL then skill-decoupled OPD.
2. Skills as privileged expert context, not student context.
3. Qwen3-VL-8B/4B on eight multimodal benches.

## Empirical Highlights
- SCOPED-8B +5.83 vs backbone on all eight benches; +3.82 vs Mix-RL.
- SCOPED-4B +3.90 vs backbone.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22217`
- Code: `https://github.com/NEUIR/SCOPED` (`code_status: released`).

