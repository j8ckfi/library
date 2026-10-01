---
id: paper:ride
type: paper
title: "The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation Residuals in On-Policy Distillation"
authors:
  - "Hao Li"
  - "MeiJia Chen"
  - "Weijie Ren"
  - "Donghan Li"
  - "Zijun Tian"
  - "Jingchun Huang"
  - "Naibo Wang"
year: 2026
month: 9
arxiv_id: "2609.36484"
url: "https://arxiv.org/abs/2609.36484"
methods:
  - method:ride
cites:
  - paper:opd
  - paper:oprd
tags:
  - post-training
  - distillation
  - on-policy
  - ride
---

# The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation Residuals in On-Policy Distillation

## Abstract Summary
Output-space OPD extrapolation uses sampled-token log-probability ratios after the LM head, which attenuates RL-induced hidden-state change anisotropically and injects noise that a global coefficient amplifies. RIDE (RL-Induced Direction Extrapolation) measures the layerwise residual between an RL teacher and its pre-RL checkpoint on the student's prefixes and regresses student hidden states toward targets displaced beyond the teacher along that residual. \(\lambda=1\) recovers OPRD. Across four base/RL-teacher pairs (R1-Distill-1.5B, Qwen3-4B, Llama-3.2-3B, Phi-4-mini), RIDE is the only method whose mean Avg@16 on AIME24 / AIME25 / AIMO approaches or exceeds the RL teacher, and it beats output-space extrapolation on every pair (output-space falls below the teacher whenever the teacher is close to its base). Code: `https://github.com/xixixixixxxx/RIDE`.

## Key Contributions
1. **RL-induced residual**: teacher minus pre-RL hidden states at every layer on identical on-policy prefixes.
2. **Representation-space extrapolation**: quadratic penalty around the teacher plus a linear directional reward; \(\lambda=1\) is OPRD.
3. **Head-attenuation diagnosis**: weakest head directions carry most of the residual energy in hidden space but little of it in centered logits.

## Empirical Highlights
- Four pairs spanning scale / family / vocabulary. RIDE mean exceeds or matches the RL teacher; output-space extrapolation is below the teacher on every pair.
- Same-initialization setting is load-bearing: student starts at the pre-RL checkpoint so the residual lives in a shared representation space.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36484`
- Code: `https://github.com/xixixixixxxx/RIDE` (`code_status: released`).
