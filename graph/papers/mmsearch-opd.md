---
id: paper:mmsearch-opd
type: paper
title: 'MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents'
authors:
- Huanyao Zhang
- Jiepeng Zhou
- Jiaye Lin
- Ontai Tang
- Jingtian Hao
- Mugeng Liu
- Ru Peng
- Lang Mei
- Xiaohan Yu
- Liyan Liu
- Chong Chen
- Wentao Zhang
year: 2026
month: 10
arxiv_id: '2610.22240'
url: https://arxiv.org/abs/2610.22240
methods:
- method:mmsearch-opd
cites:
- paper:iris
- paper:opd
tags:
- distillation
- opd
- multimodal
- search
---

# MMSearch-OPD

## Abstract Summary
Long-horizon multimodal search is starved of hard training questions and process feedback. MMSearch-OPD refines simple image-question seeds (Expand / Blur / Visualize) then jointly trains RL outcome rewards with reward-gap-modulated token-level OPD on imperfect student trajectories, decaying the teacher coefficient.

## Key Contributions
1. Controllable Refine operators over existing multimodal seeds.
2. Joint RL + OPD with reward-gap token weights and exponential teacher decay.
3. Seven-bench multimodal search eval at 9B / 27B.

## Empirical Highlights
- MMSearch-OPD-9B avg 60.2 vs Qwen3.5-9B agentic workflow 44.9 (+15.3); vs DeepVoyager-VL-8B +9.6.
- SFT 44.9→57.9 then joint RL-OPD 60.2.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22240`
- Code: `none found` (`code_status: none`).

