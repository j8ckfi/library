---
id: paper:anlr-lora
type: paper
title: "One Rate Is Not Enough: Adaptive Anisotropic Learning Rates for LoRA Fine-Tuning"
authors:
  - "Huiyi Wang"
  - "Daijiao Liu"
  - "Lina Yao"
  - "Dong Gong"
year: 2026
month: 9
arxiv_id: "2609.05885"
url: "https://arxiv.org/abs/2609.05885"
methods:
  - method:anlr-lora
cites: []
tags:
  - peft
  - lora
  - anlr-lora
---

# One Rate Is Not Enough: Adaptive Anisotropic Learning Rates for LoRA Fine-Tuning

## Abstract Summary
Vanilla LoRA applies one global learning rate to every rank-one component. Rank-one directions inside a module update at uneven rates; low-velocity modules collapse to a concentrated singular spectrum and waste the nominal rank. AnLR-LoRA assigns each rank-one component an effective LR from training-time signals (function-space velocity and Adam SNR), mean-normalized per module so the global LR budget is unchanged. No extra trainable parameters. Improves commonsense, NLG, and visual instruction-tuning over LoRA across a wide global-LR range, and transfers to other LoRA variants.

## Key Contributions
1. **Within-module LR heterogeneity** as a rank-underuse mechanism.
2. **Anisotropic per-rank LR** from velocity / Adam SNR, mean-normalized per module.
3. **Drop-in on AdamW LoRA** with no extra parameters.

## Empirical Highlights
- Consistently above LoRA on commonsense reasoning, NLG, and visual instruction-tuning.
- Gains remain under a wide global LR sweep and transfer to other LoRA variants.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
