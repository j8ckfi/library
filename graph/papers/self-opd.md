---
id: paper:self-opd
type: paper
title: "Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher"
authors:
  - "Shiyi Zhang"
  - "Mushui Liu"
  - "Yunze Tong"
  - "Wanggui He"
  - "Siyu Zou"
  - "Jinlong Liu"
  - "Yunlong Yu"
  - "Jian Song"
  - "Hao Jiang"
  - "Pipei Huang"
  - "Bo Zheng"
year: 2026
month: 8
arxiv_id: "2608.26872"
url: "https://arxiv.org/abs/2608.26872"
methods:
  - method:self-opd
cites:
  - paper:diffusion-opsd
  - paper:opd
tags:
  - generative-models
  - flow-matching
  - diffusion
  - distillation
  - alignment
  - self-opd
---

# Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher

## Abstract Summary
Self-OPD provides a teacher-free on-policy distillation framework for flow matching models, resolving both the high computational cost of training specialized domain teachers and the distribution mismatch that leads to compounding trajectory errors. By branching deterministic next-state predictions into $K$ stochastic SDE candidates at each timestep, rolling each candidate out with an ODE sampler, and comparing their rewards against a deterministic self-reference baseline, Self-OPD obtains normalized step-wise advantages. Optimization is conducted via an all-branch pull-push velocity objective equipped with direction-aware attenuation and SDE-variance normalization. For multi-objective alignment, Self-OPD fuses normalized scalar scores at the reward level, avoiding direct gradient competition and teacher-routing conflicts.

## Key Contributions
1. **Teacher-Free Per-Step Supervision**: Converts reward-guided stochastic SDE branch exploration and a deterministic self-reference ODE baseline into dense per-step velocity supervisory signals.
2. **All-Branch Pull-Push Objective**: Leverages both high-advantage (pull) and low-advantage (push) branches with SDE-variance normalization and direction-aware attenuation to prevent gradient degradation.
3. **Reward-Level Fusion for Multi-Objective Alignment**: Fuses multi-objective scalar rewards prior to branch ranking, achieving simultaneous multi-property alignment (text rendering, composition, aesthetics) in a single image without field-level teacher routing.
4. **Empirical Results**: Outperforms prior RL (Flow-GRPO, DiffusionNFT) and teacher-based OPD methods across single-reward and mixed-reward benchmarks.

## Open Source Repository
- Code Repository: `https://github.com/Shiy-Zhang/Self-OPD`
