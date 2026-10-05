---
id: paper:latent-mopd
type: paper
title: "Latent-MOPD: Latent Multi-Teacher On-Policy Distillation"
authors:
  - "Zhengyu Fang"
  - "Seoyeon Hong"
  - "Jie Yang"
  - "Muyang Li"
  - "Koyoshi Shindo"
  - "Brandon Joseph Lwowski"
  - "Jing Li"
year: 2026
month: 10
arxiv_id: "2610.02381"
url: "https://arxiv.org/abs/2610.02381"
methods:
  - method:latent-mopd
cites:
  - paper:open-mopd
  - paper:lastopd
  - paper:ride
tags:
  - post-training
  - distillation
  - multi-teacher
  - latent
---

# Latent-MOPD: Latent Multi-Teacher On-Policy Distillation

## Abstract Summary
Token-only multi-teacher OPD transfers what specialists predict. Latent-MOPD also matches the hidden states used to compute those predictions, without extra teacher training. Late-layer targets are chosen from the teacher–student relationship, unequal widths are bridged with a shared projection, and updates are grouped by domain. Supervision shifts from hidden states to token predictions, both from the same routed specialist. Active plug-in beside Open-MOPD. Code: `https://github.com/fangzy96/Latent-MOPD`.

## Key Contributions
1. **Representation-level multi-teacher OPD**: hidden states plus tokens from the same routed specialist.
2. **Late-layer selection + shared projection** for unequal widths; domain-grouped updates.
3. **Same-family 1.5B last-3 Norm 1.05** vs token-only MOPD 0.90 vs uniform 0.79.

## Empirical Highlights
- Same-family last-3: GYM 52.4 / BBH 66.3 / AIME24 50.8 vs token-only 51.8 / 65.4 / 46.0.
- Cross-family last-1 Linear Norm 0.26 vs token-only 0.16.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02381`
- Code: `https://github.com/fangzy96/Latent-MOPD` (`code_status: released`; HTTP 200 as of 2026-10-05).
