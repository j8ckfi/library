---
id: method:diffusion-policy
type: method
title: "Diffusion Policy (Visuomotor Robot Policy Learning)"
category: "servo-control"
status: sota
sota_for:
  - task:visuomotor-servo-control
supersedes:
  - method:act-policy
papers:
  - paper:diffusion-policy-paper
recipes:
  - recipe:diffusion-policy-servo
claims:
  - benchmark: "Robomimic Benchmark (Square, Tool Hang, Can)"
    metric: "success rate across multimodal tasks"
    value: 94.2
    baseline: "LSTM-GMM (74.1), IBC (56.8), ACT (89.5)"
    date: "2024-03"
    verified: true
    notes: "Generates temporal action trajectory chunks conditioned on visual camera observations via DDPM."
tags:
  - control
  - robotics
  - visuomotor
  - diffusion
  - servo-control
---

# Diffusion Policy (Visuomotor Robot Policy Learning)

## Method Overview
Diffusion Policy formulates robot motor control as a conditional Denoising Diffusion Probabilistic Model (DDPM) over continuous action trajectories.

Given a history of visual observations \(O_t = \{o_{t-T_{\text{obs}}+1}, \dots, o_t\}\) (RGB camera feeds, proprioceptive joint states), the model predicts a future action sequence \(A_t = \{a_t, a_{t+1}, \dots, a_{t+T_{\text{act}}-1}\}\) via iterative reverse diffusion:
\[
A_t^{k-1} = \frac{1}{\sqrt{\alpha_k}} \left( A_t^k - \frac{\beta_k}{\sqrt{1 - \bar{\alpha}_k}} \epsilon_\theta(A_t^k, O_t, k) \right) + \sigma_k z
\]
Key architectural elements include:
1. **Action Chunking**: Predicting horizon \(T_{\text{act}} = 16\) action steps simultaneously, ensuring physical velocity and acceleration continuity across servo updates.
2. **Multimodal Behavior Distribution**: Naturally expresses complex multimodal demonstrations (e.g. choice between left vs right approach trajectories) without mode collapse.

## When to Use
- **Robotic Arm & Gripper Control**: Closed-loop visual manipulation tasks involving contact-rich dynamics (peg insertion, tool hanging, cable routing).
- **High-Rate Servo Trajectory Generation**: Generating continuous motor velocity/torque vectors from camera streams.

## Gotchas & Failure Modes
1. **Inference Latency**: Standard 100-step DDPM sampling is too slow for real-time 50Hz control loops; use 10-16 step DPM-Solver or DDIM inference schedules.
2. **Visual Latency / Frame Drops**: If camera input drops a frame or changes exposure, action chunking can drift unless receding-horizon replanning is executed at every step.
