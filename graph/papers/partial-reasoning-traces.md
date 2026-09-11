---
id: paper:partial-reasoning-traces
type: paper
title: "Revisiting Complete Reasoning Traces for Post-Training"
authors:
  - "Jaehui Hwang"
  - "Sangdoo Yun"
  - "Byeongho Heo"
  - "Dongyoon Han"
year: 2026
month: 9
arxiv_id: "2609.07103"
url: "https://arxiv.org/abs/2609.07103"
methods:
  - method:partial-reasoning-traces
cites:
  - paper:olmo-3
  - paper:opd
  - paper:minimax-m1
tags:
  - post-training
  - sft
  - reasoning
  - data-recipe
  - emnlp-2026
---

# Revisiting Complete Reasoning Traces for Post-Training

## Abstract Summary
Long complete reasoning trajectories are the usual SFT target for reasoners. Pilot study: full traces give limited benefit; partial / truncated traces remain effective even under heavy truncation. Attention analyses and controlled token-removal show intermediate tokens contribute little to final quality. Training on endpoints changes reasoning behavior and also helps RL and on-policy distillation hosts. Prefer curated or partial traces over dumping complete CoT. EMNLP 2026 Findings. Code: naver-ai/revisiting-trace.

## Key Contributions
1. **Full traces are overfed**: partial/truncated trajectories match or beat complete-CoT SFT.
2. **Intermediate tokens are weak**: attention + token-removal studies.
3. **Endpoints transfer**: the same truncation principle helps RL and on-policy distillation, not only SFT.

## Empirical Highlights
- Pilot: full trajectories provide only limited SFT benefit; partial traces remain effective under heavy truncation.
- Intermediate-token removal does not collapse final reasoning quality in the paper's controlled studies.

## Open Source Repository & Resources
- Code: `https://github.com/naver-ai/revisiting-trace`
