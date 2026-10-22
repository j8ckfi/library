---
id: paper:data-lr-schedules
type: paper
title: 'Data Schedules and Learning Rate Schedules Should Be Designed Together'
authors:
- 'Haodong Wen'
- 'Kairong Luo'
- 'Tingkai Yan'
- 'Wenguang Chen'
- 'Kaifeng Lyu'
year: 2026
month: 10
arxiv_id: '2610.29348'
url: https://arxiv.org/abs/2610.29348
methods:
- method:muon2
cites:
- paper:olmo-3
tags:
- pretrain
- data-mix
- gotcha
---

# Data Schedules and Learning Rate Schedules Should Be Designed Together

## Abstract Summary
The complete PT-to-MT data cut is only one mix schedule. Which mix is optimal for final mid-training loss depends on the LR schedule; LR decay should start well after MT data enters.

## Key Contributions
1. Joint data-mix and LR-decay scheduling for PT then mid-training.

## Empirical Highlights
- Does not retarget Muon2 or OLMo-3. Not a unique-token epoch law.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29348`
- Code: `none found` (`code_status: none`).
