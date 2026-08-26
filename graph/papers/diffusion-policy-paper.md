---
id: paper:diffusion-policy-paper
type: paper
title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
authors:
  - "Cheng Chi"
  - "Siyuan Feng"
  - "Yilun Du"
  - "Zhenjia Xu"
  - "Eric Cousineau"
  - "Benjamin Burchfiel"
  - "Shuran Song"
year: 2023
month: 3
arxiv_id: "2303.04137"
url: "https://arxiv.org/abs/2303.04137"
methods:
  - method:diffusion-policy
cites:
  - paper:act-paper
tags:
  - control
  - robotics
  - imitation-learning
  - diffusion
---

# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

## Abstract Summary
Diffusion Policy represents robot visuomotor behavior as a conditional denoising diffusion process over action spaces. The authors evaluate Diffusion Policy across 12 diverse manipulation benchmarks spanning simulation and physical robot setups, demonstrating a 46.9% average improvement over existing state-of-the-art imitation learning methods by handling multimodal demonstration distributions and expressing high-frequency motor commands.

## Key Contributions
1. **Action-Space Diffusion Formulation**: Applied conditional DDPMs to temporal action chunk generation in continuous robot spaces.
2. **Multimodal Trajectory Expressiveness**: Naturally resolves multimodality in human teleoperation datasets without mode averaging.
3. **Receding Horizon Closed-Loop Control**: Integrated high-speed action trajectory execution with live camera feedback.
