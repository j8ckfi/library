---
id: method:td-mpc2
type: method
title: "TD-MPC2 (Temporal Difference Model Predictive Control 2)"
category: "servo-control"
status: active
superseded_by: method:efficienttdmpc
sota_for: []
supersedes: []
papers:
  - paper:td-mpc2
recipes:
  - recipe:tdmpc2-control
claims:
  - benchmark: "DMControl 100 & ManiSkill Continuous Benchmarks"
    metric: "sample efficiency & multi-task success"
    value: "Historical Model-Based RL Baseline"
    baseline: "DreamerV3 / SAC"
    date: "2023-10"
    verified: true
    notes: "Learns latent dynamics model with terminal Q-value estimation, planned with Model Predictive Path Integral (MPPI)."
tags:
  - control
  - robotics
  - world-model
  - mpc
---

# TD-MPC2 (Temporal Difference Model Predictive Control 2)

## Method Overview
TD-MPC2 trains a task-oriented latent world model without pixel-level decoding.

## Supersession
- Superseded by `method:efficienttdmpc` (2605.16692) as the continuous control default.
