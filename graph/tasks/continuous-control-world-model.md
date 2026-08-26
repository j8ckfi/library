---
id: task:continuous-control-world-model
type: task
title: "Continuous Control & Learned World-Model RL"
domain: "control"
summary: "Sample-efficient model-based reinforcement learning and continuous servo control via learned latent world models and trajectory optimization."
current_sota:
  - method: method:td-mpc2
    as_of: "2026-08-26"
    benchmark: "DMControl 100 / ManiSkill / Humanoid"
    metric: "sample efficiency & asymptotic score"
    value: "SOTA Model-Based RL Default"
    notes: "Default is TD-MPC2. If planning latency dominates, swap MPPI planner for Dream-MPC."
methods:
  - method:td-mpc2
  - method:dream-mpc
  - method:diffusion-policy
tags:
  - control
  - robotics
  - world-models
  - model-based-rl
---

# Continuous Control & Learned World-Model RL

## Problem Definition
Controlling continuous robotic and servo systems with high sample efficiency directly from proprioceptive and visual state observations.

## SOTA Recommendation (as of 2026-08-26)
- **Default Baseline**: **TD-MPC2** (`method:td-mpc2`).
- **High-Speed Planning**: If online planning compute dominates runtime, swap the MPPI sampling planner for **Dream-MPC** (`method:dream-mpc`).
