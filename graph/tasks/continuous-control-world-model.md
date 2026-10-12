---
id: task:continuous-control-world-model
type: task
title: "Continuous Control & Learned World-Model RL"
domain: "control"
summary: "Sample-efficient model-based reinforcement learning and continuous servo control via learned latent world models and trajectory optimization."
current_sota:
  - method: method:efficienttdmpc
    as_of: "2026-08-26"
    benchmark: "DMControl 100 / ManiSkill / Humanoid"
    metric: "sample efficiency & planning latency"
    value: "Default SOTA Continuous Control"
    notes: "EfficientTDMPC (2605.16692) family; Dream-MPC (2605.04568) gradient planner."
  - method: method:dream-mpc
    as_of: "2026-08-26"
    benchmark: "High-Speed Robot Control Benchmarks"
    metric: "planning latency"
    value: "SOTA Gradient Planner"
    notes: "Dream-MPC (2605.04568) ICML 2026 gradient planner."
methods:
  - method:ppo-fp16
  - method:efficienttdmpc
  - method:dream-mpc
  - method:td-mpc2
  - method:grasp
  - method:td-jepa
  - method:latent-geometry
  - method:diffusion-policy
redirects:
  - when: "structure-aware numerical stabilization for half-precision PPO (control, not LLM)"
    to: "method:ppo-fp16"
last_reviewed: "2026-10-12"
tags:
  - control
  - robotics
  - world-models
  - efficienttdmpc
---

# Continuous Control & Learned World-Model RL

## Problem Definition
Controlling continuous robotic and servo systems with high sample efficiency directly from proprioceptive and visual state observations.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **EfficientTDMPC** (`method:efficienttdmpc`, 2605.16692) family.
- **Gradient Planner**: **Dream-MPC** (`method:dream-mpc`, 2605.04568) gradient planner.
- **Optional half-precision on-policy PPO (not this world-model default)**: `method:ppo-fp16` (`arXiv:2610.13306`) residual-protected FP16 PPO on continuous-control tasks. Lowest mean return-AUC rank 1.90; optimizer state −71.7–74.9%. Control PPO, not LLM RL. No public code. Does not replace EfficientTDMPC or CISPO.
