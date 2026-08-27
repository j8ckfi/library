---
id: method:diffusion-opsd
type: method
title: "DiffusionOPSD (On-Policy Self-Distillation for Diffusion Models)"
category: "diffusion-alignment"
status: sota
sota_for:
  - task:posttrain-diffusion
supersedes: []
papers:
  - paper:diffusion-opsd
recipes:
  - recipe:diffusion-opsd
claims:
  - benchmark: "SD 3.5-M & Z-Image-Turbo (10 Evaluators: ImageReward, HPSv3, DeQA, etc.)"
    metric: "held-out reward score & GPU-hours"
    value: "Best in 19/20 reward-matched settings; up to +44.0% over strongest baseline; 40-63% GPU-hr reduction vs DiffusionNFT"
    baseline: "DiffusionNFT / ReFL / FlowGRPO"
    date: "2026-08-27"
    verified: true
    notes: "Translates image-level reward gradients into bounded positive/negative clean-output targets for intermediate denoising queries."
tags:
  - diffusion
  - post-training
  - distillation
  - alignment
  - diffusion-opsd
  - sota
---

# DiffusionOPSD (On-Policy Self-Distillation for Diffusion Models)

## Method Overview
DiffusionOPSD adapts on-policy distillation principles to diffusion model alignment:
1. **Behavior Rollout & Anchor Collection**: A frozen behavior policy generates on-policy trajectories and provides query states and clean-output anchors.
2. **Bounded Target Construction**: Converts endpoint reward gradients into bounded positive and negative clean-output targets around the anchor predictions.
3. **Finite Target Fitting**: The trainable model updates against the constructed clean-output targets under a finite optimization budget.
4. **Behavior EMA Refresh**: Updates the behavior policy via exponential moving average (EMA) to continually supply refreshed on-policy rollouts.

## When to Use
- When post-training text-to-image diffusion or rectified flow models to maximize aesthetic, human preference, or task-specific reward functions.
- When RL-style policy gradient methods (such as DiffusionNFT or FlowGRPO) suffer from training instability, slow convergence, or high GPU compute cost.

## Relation to Existing SOTA
- Extends the on-policy distillation concept from language models (`method:opd`) to generative diffusion models without affecting language distillation defaults.
