---
id: paper:diffusion-opsd
type: paper
title: "On-Policy Self-Distillation in Diffusion Models"
authors:
  - "DiffusionOPSD Team"
  - "Wei Liu"
year: 2026
month: 8
arxiv_id: "2608.24646"
url: "https://arxiv.org/abs/2608.24646"
methods:
  - method:diffusion-opsd
cites:
  - paper:opd
tags:
  - diffusion
  - post-training
  - distillation
  - alignment
  - diffusion-opsd
---

# On-Policy Self-Distillation in Diffusion Models

## Abstract Summary
DiffusionOPSD introduces an on-policy self-distillation framework for diffusion and flow post-training. Instead of optimizing endpoint rewards directly with high-variance RL gradients, DiffusionOPSD converts image-level reward guidance into bounded positive and negative targets around the behavior policy's own clean-output predictions at visited query states. The trainable model fits these targets through finite fitting before an exponential moving average (EMA) update refreshes the behavior policy. Across SD 3.5-M and Z-Image-Turbo, DiffusionOPSD achieves the best held-out score in 19 of 20 reward-matched settings while reducing GPU-hours by 40% to 63% compared to DiffusionNFT.

## Key Contributions
1. **On-Policy Self-Distillation for Continuous Processes**: Converts image-level reward gradients into explicit, continually refreshed intermediate supervision for diffusion trajectories.
2. **Decoupled Target Construction and Realization**: Constructs bounded positive/negative clean-output targets around behavior anchors, enabling separate diagnosis of reward guidance quality and finite parameter fitting.
3. **Efficiency and Benchmark Wins**: Outperforms RL-based diffusion fine-tuning baselines (ReFL, FlowGRPO, DiffusionNFT) across 10 evaluators on both standard and step-distilled backbones.

## Open Source Repository
- Implementation: `https://github.com/worldbench/DiffusionOPSD`
