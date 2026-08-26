---
id: method:td-mpc2
type: method
title: "TD-MPC2 (Temporal Difference Model Predictive Control 2)"
category: "servo-control"
status: sota
sota_for:
  - task:continuous-control-world-model
supersedes: []
papers:
  - paper:td-mpc2
recipes:
  - recipe:tdmpc2-control
claims:
  - benchmark: "DMControl 100 & ManiSkill Continuous Benchmarks"
    metric: "sample efficiency & multi-task success"
    value: "State of the art in model-based RL"
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
TD-MPC2 trains a task-oriented latent world model without pixel-level decoding. It combines short-horizon trajectory rollouts generated via Model Predictive Path Integral (MPPI) sampling with terminal Value/Q-function estimates trained by Temporal Difference learning.

## When to Use
- Default framework for continuous servo control and multi-task model-based RL.
