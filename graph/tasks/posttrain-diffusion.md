---
id: task:posttrain-diffusion
type: task
title: "Diffusion Post-Training and Reward Alignment"
domain: "diffusion"
summary: "Aligning text-to-image diffusion and flow models with human preferences and task-specific reward functions using on-policy trajectory guidance."
current_sota:
  - method: method:diffusion-opsd
    as_of: "2026-08-27"
    benchmark: "SD 3.5-M / Z-Image-Turbo (10 Evaluators)"
    metric: "held-out reward score & GPU-hours"
    value: "Best in 19/20 reward-matched settings; 40-63% GPU-hr reduction"
    notes: "DiffusionOPSD (2608.24646) converts image-level rewards into bounded intermediate clean-output targets."
methods:
  - method:diffusion-opsd
tags:
  - diffusion
  - post-training
  - alignment
  - generative-models
---

# Diffusion Post-Training and Reward Alignment

## Problem Definition
Aligning generative diffusion and flow models with downstream reward functions (aesthetic quality, text-image alignment, human preference ratings). Endpoint rewards create a structural mismatch because feedback is only observed on decoded final images, while the model operates across multi-step denoising trajectories.

## SOTA Recommendation (as of 2026-08-27)
- **Primary Method**: **DiffusionOPSD** (`method:diffusion-opsd`, `paper:diffusion-opsd` `arXiv:2608.24646`) for on-policy self-distillation with bounded intermediate clean-output targets.
