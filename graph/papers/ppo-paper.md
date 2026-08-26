---
id: paper:ppo-paper
type: paper
title: "Proximal Policy Optimization Algorithms"
authors:
  - "John Schulman"
  - "Filip Wolski"
  - "Prafulla Dhariwal"
  - "Alec Radford"
  - "Oleg Klimov"
year: 2017
month: 7
arxiv_id: "1707.06347"
url: "https://arxiv.org/abs/1707.06347"
methods:
  - method:ppo-rlhf
cites: []
tags:
  - reinforcement-learning
  - classic
---

# Proximal Policy Optimization Algorithms

## Abstract Summary
This seminal reinforcement learning paper introduces Proximal Policy Optimization (PPO), which alternates between sampling data through interaction with the environment and optimizing a clipped surrogate objective function using stochastic gradient ascent.

## Key Contributions
1. Introduced clipped probability ratio objectives to constrain policy update steps within a trust region.
2. Formed the standard baseline for continuous control and early LLM RLHF alignment systems.
