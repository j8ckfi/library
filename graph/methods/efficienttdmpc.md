---
id: method:efficienttdmpc
type: method
title: "EfficientTDMPC (Continuous Control Family)"
category: "control"
status: sota
sota_for:
  - task:continuous-control-world-model
supersedes:
  - method:td-mpc2
papers:
  - paper:efficienttdmpc
recipes:
  - recipe:efficienttdmpc
claims:
  - benchmark: "DMControl 100 / ManiSkill / Humanoid Continuous Control"
    metric: "sample efficiency & planning latency"
    value: "Default SOTA for continuous control world models"
    baseline: "TD-MPC2"
    date: "2026-08-26"
    verified: true
    notes: "Accelerated model-predictive control built on the BMPC framework with block planning."
tags:
  - control
  - robotics
  - mpc
  - world-models
  - efficienttdmpc
  - sota
---

# EfficientTDMPC (Continuous Control Family)

## Method Overview
EfficientTDMPC establishes the state-of-the-art framework for continuous robotic control and world-model reinforcement learning:
1. **Block-Wise Latent Planning**: Replaces single-step MPPI trajectory sampling with accelerated block optimization (built on BMPC principles).
2. **High Sample Efficiency**: Retains TD-MPC2 terminal Q-learning while slashing planning compute requirements.

## When to Use
- Default SOTA method for continuous control and learned world models (Dream-MPC remains the primary gradient planner alternative).

## Supersession
- Supersedes `method:td-mpc2` as the continuous control default.
