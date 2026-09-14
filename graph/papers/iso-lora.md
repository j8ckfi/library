---
id: paper:iso-lora
type: paper
title: "Rank-Efficient LoRA via Joint Tangent-Space Optimization under Isotropic Curvature"
authors:
  - "Zihan Zhu"
  - "Zhehang Du"
  - "Xuyang Chen"
  - "Tim Tsz-Kit Lau"
  - "Jiayuan Wu"
  - "X. Y. Han"
  - "Qi Long"
  - "Weijie Su"
year: 2026
month: 9
arxiv_id: "2609.12123"
url: "https://arxiv.org/abs/2609.12123"
methods:
  - method:iso-lora
cites:
  - paper:lr-matters-lora
  - paper:nora
  - paper:anlr-lora
tags:
  - peft
  - lora
  - optimizer
  - iso-lora
---

# Rank-Efficient LoRA via Joint Tangent-Space Optimization under Isotropic Curvature

## Abstract Summary
Nominal LoRA rank sets representational capacity, but the optimizer determines how much of that capacity is used. On GPT-2 LoRA, AdamW concentrates per-step update energy on few singular directions (low effective rank); Muon uses richer directions and benefits more from raising rank. Iso-LoRA couples the LoRA factor updates through spectral descent on the induced tangent perturbation in weight space so energy spreads more evenly across singular directions. A one-step analysis under a spiked-gradient model supports higher effective rank than factor-wise optimizers. Validated on 0.1B-7B language-model adaptation, with the strongest gains at moderate-to-large LoRA ranks.

## Key Contributions
1. **Optimizer-shaped effective rank**: AdamW vs Muon case study at matched nominal rank.
2. **Iso-LoRA**: joint tangent-space spectral descent on \(BA\), LoRA parameterization unchanged.
3. **Rank utilization**, not a new adapter topology.

## Empirical Highlights
- LLaMA-2-7B GSM8K EM: Iso-LoRA rank 128 **61.87** vs Full FT 59.52 vs LoRA-Pro 128 59.20 vs LoRA-Muon 128 59.12 vs LoRA rank 8 45.39.
- Rank 8 / 32 / 128 Iso-LoRA: 54.94 / 58.12 / 61.87. Gains grow with nominal rank.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-14. Paper cites Hugging Face PEFT as the host parameterization.
