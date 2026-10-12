---
id: paper:rpd-opd
type: paper
title: Rethinking Relative Policy Differences Transfer of On-Policy Distillation
authors:
- Rong Wu
- Daocheng Fu
- Yu Yang
- Xuemeng Yang
- Siqi Li
- Shu Zou
- Yao Zhu
- Botian Shi
- Bo Zhang
- Cong Zhang
- Pinlong Cai
- Jianbiao Mei
year: 2026
month: 10
arxiv_id: '2610.13205'
url: https://arxiv.org/abs/2610.13205
methods:
- method:rpd-opd
cites:
- paper:opd
- paper:semi-opd
tags:
- post-training
- distillation
- opd
- rpd-opd
---

# Rethinking Relative Policy Differences Transfer of On-Policy Distillation

## Abstract Summary
Standard OPD needs a much stronger teacher. Relative policy-difference transfer uses log(π_expert/π_ref) as an implicit KL-regularized reward and recovers ordinary OPD as a special case. Task-specific training residuals transfer; scale-only residuals do not. The reference filters shared behavior. Success also requires the induced update to move the target toward the expert off the sampled rollouts.

## Key Contributions
1. Unified log-ratio implicit-reward view; any-to-any OPD as a special case.
2. Task-specific FT/RL residuals transfer; scale-only residuals do not.
3. Reference choice, not raw policy distance, predicts transfer.

## Empirical Highlights
- See `method:rpd-opd` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13205`
- Code: `none found` (`code_status: none`).
