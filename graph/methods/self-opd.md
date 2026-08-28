---
id: method:self-opd
type: method
title: "Self-OPD (Teacher-Free On-Policy Distillation for Flow Matching)"
category: "diffusion-alignment"
status: sota
sota_for:
  - task:posttrain-diffusion
supersedes: []
papers:
  - paper:self-opd
recipes:
  - recipe:self-opd
claims:
  - benchmark: "Flow Matching Visual Alignment (Single & Mixed Reward Benchmarks)"
    metric: "reward score and multi-objective Pareto front"
    value: "Outperforms Flow-GRPO, Flow-OPD, and DiffusionNFT without external task-specific teachers"
    baseline: "Flow-GRPO / Teacher-based Flow-OPD / DiffusionNFT"
    date: "2026-08-28"
    verified: true
    notes: "Stochastic SDE branching vs deterministic self-reference baseline; all-branch pull-push velocity loss with reward-level multi-objective fusion."
tags:
  - diffusion
  - flow-matching
  - distillation
  - alignment
  - self-opd
  - sota
---

# Self-OPD (Teacher-Free On-Policy Distillation for Flow Matching)

## Method Overview
Self-OPD converts student self-exploration into dense per-step velocity guidance for flow matching models without requiring pre-trained teacher models:
1. **Stochastic SDE Branching**: At timestep $t_j$, branches deterministic state $x_{t_{j+1}, \theta}$ into $K$ stochastic SDE candidates via isotropic perturbations $z_j \sim \mathcal{N}(0, \mathbf{I})$.
2. **Self-Reference Baseline**: Computes a parallel deterministic ODE rollout from the parent state, providing a baseline reward $r^{\text{ref}}$ to convert candidate endpoint rewards into normalized branch advantages $A_k$.
3. **All-Branch Pull-Push Velocity Field Optimization**: High-advantage branches pull the velocity field toward favorable directions ($v_+$), while low-advantage branches push away ($v_-$), regulated by direction-aware attenuation $d_k$ and SDE-variance normalization.
4. **Reward-Level Multi-Objective Fusion**: Fuses normalized scalar reward scores before ranking sampled branches, bypassing field-level teacher conflicts and optimizing a single model for joint high-reward criteria.

## When to Use
- When post-training flow matching or continuous diffusion backbones without task-specific teacher models.
- When aligning models against multiple downstream reward signals (e.g., text rendering, spatial composition, and aesthetic quality) simultaneously.

## Relation to Existing SOTA
- Co-exists with `method:diffusion-opsd` under `task:posttrain-diffusion`: use `method:diffusion-opsd` as the general reward/self-distillation default; use `method:self-opd` when working with flow matching models and avoiding task-specific teachers.
