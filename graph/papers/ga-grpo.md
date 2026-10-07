---
id: paper:ga-grpo
type: paper
title: "When Does External Guidance Help LLM Reasoning? A Bias-Variance Theory of Guidance-Augmented GRPO"
authors:
  - Sofia Torres
  - Gabriel Almeida
  - Carter Adams
  - Camila Rocha
year: 2026
month: 10
arxiv_id: "2610.06861"
url: "https://arxiv.org/abs/2610.06861"
methods:
  - method:rgpo
  - method:mintrl
  - method:cispo
cites:
  - paper:rgpo
  - paper:mintrl
tags:
  - post-training
  - rl-alignment
  - guidance
  - theory
  - ga-grpo
---

# When Does External Guidance Help LLM Reasoning? A Bias-Variance Theory of Guidance-Augmented GRPO

## Abstract Summary
Theory/evidence paper for LUFFY / ExPO / RGPO-style guidance-augmented GRPO. Optimal guidance weight λ*(T,δ,σ²)=σ0²/(σ0²+Rmax²δ²T). 31% fewer GPU-h; Qwen2.5-Math-7B-Base. No new method. Linked from `method:rgpo` and the guidance family. Does not retarget CISPO.

## Key Contributions
1. **Bias-variance theory** of guidance-augmented GRPO.
2. **Closed-form λ*** as a function of horizon, bias, and reward noise.
3. **31% fewer GPU-h** in the measured setting.

## Empirical Highlights
- Qwen2.5-Math-7B-Base. Not a CISPO bake-off.
- No dedicated trainer node.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06861`
- Code: none found as of 2026-10-07 (`code_status: none`).
