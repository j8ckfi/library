---
id: paper:lr-matters-lora
type: paper
title: "LR Matters in LoRA: Re-evaluating Low-Rank Fine-Tuning and DoRA"
authors:
  - "Yuang Lee et al."
year: 2026
month: 2
arxiv_id: "2602.04998"
url: "https://arxiv.org/abs/2602.04998"
methods:
  - method:lr-matters-lora
cites:
  - paper:dora
  - paper:lora-paper
tags:
  - peft
  - lora
  - rslora
  - lr-matters-lora
---

# LR Matters in LoRA: Re-evaluating Low-Rank Fine-Tuning and DoRA

## Abstract Summary
This comprehensive 2026 study demonstrates that with rank-stabilized scaling (rsLoRA) and proper learning rate sweeping, standard vanilla LoRA matches or exceeds Weight-Decomposed LoRA (DoRA) across language understanding, math, and coding benchmarks without additional magnitude parameter overhead or memory penalty.

## Key Contributions
1. **LR Scaling Analysis**: Proves that previously observed DoRA advantages stemmed primarily from suboptimal learning rate calibration for standard LoRA.
2. **Quality Default**: Recommends vanilla LoRA + rsLoRA + LR sweep as the primary PEFT quality baseline.

## Open Source Repository
- Implementation: `https://github.com/yuang-lee/lr-matters-lora`
