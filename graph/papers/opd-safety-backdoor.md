---
id: paper:opd-safety-backdoor
type: paper
title: "Does On-Policy Distillation for Safety Pose Backdoor Risks?"
authors:
  - Jian Luo
  - Kehan Qi
  - Qingqiao Hu
  - Meilong Xu
  - Jiacheng Qiu
  - Weimin Lyu
  - Jiawei Zhou
  - Chao Chen
year: 2026
month: 10
arxiv_id: "2610.07654"
url: "https://arxiv.org/abs/2610.07654"
methods:
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - safety
  - backdoor
  - gotcha
  - opd-safety-backdoor
---

# Does On-Policy Distillation for Safety Pose Backdoor Risks?

## Abstract Summary
Caution/evidence paper. A backdoored safety teacher transfers hidden behavior under OPD: 3% poison → up to 70% ASR; 10 samples / 16 epochs → 67% ASR; more epochs amplify; top-k KL transfers faster. Warning on OPD used for safety alignment. No new method. Does not retarget OPD as the matching default.

## Key Contributions
1. **Backdoored safety teacher transfers** via OPD.
2. **3% poison → up to 70% ASR**; 10 samples / 16 epochs → 67% ASR.
3. **Top-k KL is a faster transfer channel**.

## Empirical Highlights
- More epochs amplify ASR. Do not use OPD as an un-audited safety-alignment trainer.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07654`
- Code: none found as of 2026-10-07 (`code_status: none`).
