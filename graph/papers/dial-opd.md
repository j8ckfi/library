---
id: paper:dial-opd
type: paper
title: "DIAL-OPD: Learning More from Fewer Tokens in On-Policy Distillation"
authors:
  - "Anhao Zhao"
  - "Haoran Xin"
  - "Junlong Tong"
  - "Yingqi Fan"
  - "Xuan Lu"
  - "Ping Nie"
  - "Wenjie Li"
  - "Xiaoyu Shen"
year: 2026
month: 10
arxiv_id: "2610.11659"
url: "https://arxiv.org/abs/2610.11659"
methods:
  - method:dial-opd
cites:
  - paper:opd
  - paper:sparse-opd-supervision
  - paper:ier-opd
tags:
  - post-training
  - distillation
  - opd
  - token-selection
  - dial-opd
---

# DIAL-OPD: Learning More from Fewer Tokens in On-Policy Distillation

## Abstract Summary
Sampled-token OPD can beat full-token OPD with fewer tokens. Disagreement-only keep-masks ignore probability scale: low-low tokens (both models near zero) get large log-ratio rewards and hurt. DIAL-OPD weights reward magnitude by the logarithmic mean of teacher and student probabilities; β sets the mix. 40% tokens beat Vanilla OPD by up to 5.25pp mean; Pass@16 13.33→26.67 in the reported setting. A 4B teacher with DIAL-OPD can beat an 8B teacher with full-token OPD. Code: EIT-NLP/DIAL-OPD.

## Key Contributions
1. Low-low tokens with large log-ratios hinder sampled-token OPD.
2. Keep-score = reward magnitude × log-mean(teacher, student) probabilities; β interpolates.
3. Fewer tokens beat full-token OPD; allocation can outweigh teacher scaling.

## Empirical Highlights
- 40% tokens: up to +5.25pp seven-benchmark mean vs Vanilla OPD.
- Pass@16 13.33% → 26.67% in the reported setting.
- 4B-teacher DIAL-OPD beats 8B-teacher full-token OPD at both student scales.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.11659`
- Code: `https://github.com/EIT-NLP/DIAL-OPD` (`code_status: released`).
