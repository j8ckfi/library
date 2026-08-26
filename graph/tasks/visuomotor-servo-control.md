---
id: task:visuomotor-servo-control
type: task
title: "Visuomotor Servo Control & Robotic Policy Learning"
domain: "control"
summary: "Learning closed-loop visual-feedback motor control trajectories for robot manipulation and servo actuators from multimodal demonstrations."
current_sota:
  - method: method:td-mpc2
    as_of: "2026-08-26"
    benchmark: "Robomimic / DMControl / Continuous Manipulation"
    metric: "success rate across multimodal tasks"
    value: 94.2
    notes: "Default remains TD-MPC2. If planning cost dominates, swap MPPI planner for Dream-MPC. For visual imitation: Diffusion Policy."
methods:
  - method:td-mpc2
  - method:dream-mpc
  - method:diffusion-policy
  - method:act-policy
tags:
  - control
  - robotics
  - imitation-learning
  - diffusion
---

# Visuomotor Servo Control & Robotic Policy Learning

## Problem Definition
Training physical robotic manipulators and high-speed servo actuators directly from camera visual streams requires generating smooth, high-dimensional multi-step motor trajectory vectors. Standard regression or discrete token policies struggle with multimodal demonstration distributions (e.g. going left around an obstacle vs going right).

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**: Robomimic benchmark suite (Can, Square, Tool Hang, Transport), Push-T benchmark, real-world Franka / ALOHA dual-arm manipulation tasks.
- **Metrics**: Task completion success rate, action jitter / trajectory smoothness, closed-loop servo latency.

## SOTA Landscape
**Diffusion Policy** represents the state-of-the-art imitation learning framework, formulating robot visual servo control as conditional denoising diffusion over continuous action sequences. By generating temporal action chunks rather than single-step actions, it avoids compounding prediction errors and naturally handles multimodal operator behavior.
