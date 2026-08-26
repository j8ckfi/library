---
id: paper:act-paper
type: paper
title: "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware"
authors:
  - "Tony Z. Zhao"
  - "Vikash Kumar"
  - "Sergey Levine"
  - "Chelsea Finn"
year: 2023
month: 4
arxiv_id: "2304.13705"
url: "https://arxiv.org/abs/2304.13705"
methods:
  - method:act-policy
cites: []
tags:
  - control
  - robotics
  - imitation-learning
  - baseline
---

# Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

## Abstract Summary
This paper presents the ALOHA low-cost bimanual teleoperation system and Action Chunking with Transformers (ACT). ACT predicts sequences of future joint angles using a Conditional Variational Autoencoder, demonstrating fine-grained manipulation capabilities such as threading zip ties and opening ziploc bags.

## Key Contributions
1. **Action Chunking with CVAE**: Formulated chunked multi-step action prediction with latent style variables.
2. **Temporal Ensembling**: Smoothed consecutive overlapping action trajectories via exponential weighting.
3. **Open-Source Bimanual Teleoperation**: Released the low-cost ALOHA hardware and software stack.
