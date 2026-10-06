---
id: paper:rethink-mopd
type: paper
title: "Rethinking Self-Distillation for Multi-Teacher Capability Merging"
authors:
  - Roy Xie
  - Dan Friedman
  - Feng Nan
  - Yukun Huang
  - Zhichao Xu
  - Chengjiu Zhang
  - Jun Xu
  - Manaal Faruqui
  - Vivek Rathod
  - Bhuwan Dhingra
year: 2026
month: 10
arxiv_id: "2610.04272"
url: "https://arxiv.org/abs/2610.04272"
methods:
  - method:open-mopd
  - method:sf-mopd
  - method:mopd-router
  - method:dn-mopd
  - method:pmopd
  - method:latent-mopd
cites:
  - paper:open-mopd
tags:
  - post-training
  - distillation
  - mopd
  - gotcha
  - rethink-mopd
---

# Rethinking Self-Distillation for Multi-Teacher Capability Merging

## Abstract Summary
Controlled study of multi-teacher capability merging. After matching training design and hyperparameters, tuned off-policy SFT / Soft-KD approaches MOPD accuracy while MOPD costs 14.8–23.1× SFT GPU-hours. Claim note on Open-MOPD and siblings so agents know a tuned off-policy baseline may be enough. Announced GitHub apple-aiml-research/ml-rethink-mopd was 404 as of 2026-10-06 (under legal review). No new method.

## Key Contributions
1. **Training-design confound**: much of reported MOPD gain can be recovered by a tuned off-policy baseline.
2. **Cost**: MOPD 14.8–23.1× SFT GPU-hours in the paper.
3. **Not a method**: caveat on Open-MOPD / SF-MOPD / MOPD-Router / DN-MOPD / PMOPD / Latent-MOPD.

## Empirical Highlights
- Tuned SFT / Soft-KD ≈ MOPD after matching HPs.
- MOPD 14.8–23.1× SFT GPU-hours.
- Do not retarget Open-MOPD (library 83.4% bake-off is a different card).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.04272`
- Code: announced `https://github.com/apple-aiml-research/ml-rethink-mopd` (HTTP 404 / under legal review as of 2026-10-06; `code_status: announced`).
