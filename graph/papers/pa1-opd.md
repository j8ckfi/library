---
id: paper:pa1-opd
type: paper
title: 'PA1-OPD: One-Step Prefix-Augmented On-Policy Distillation for Language Model Pretraining'
authors:
- Zhenhe Wu
- Jian Yang
- Yaping Jin
- Xinlai Kang
- Jie Hu
- Hanting Chen
year: 2026
month: 10
arxiv_id: '2610.19601'
url: https://arxiv.org/abs/2610.19601
methods:
- method:pa1-opd
cites:
- paper:opd
tags:
- distillation
- pretraining
- opd
---

# PA1-OPD

## Abstract Summary
Pretrain KD matches the teacher at corpus prefixes and never sees student-induced states. PA1-OPD samples one student token from selected prefixes and adds teacher supervision at the successor, keeping NTP and corpus-path KD.

## Key Contributions
1. One-step on-policy branch from data-anchored roots with tree attention.
2. Surprisal root selection (Top10) vs full coverage.
3. Two OLMo2 continued-pretrain settings on C4 / PG-19 / Pile.

## Empirical Highlights
- Stage2 Top10 surprisal adds 48.85% to KD's Macro CE gain over NTP.
- Full coverage beats KD at every evaluated checkpoint on all three corpora.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19601`
- Code: `none found` (`code_status: none`).
