---
id: paper:dpo-paper
type: paper
title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
authors:
  - "Rafael Rafailov"
  - "Archit Sharma"
  - "Eric Mitchell"
  - "Stefano Ermon"
  - "Christopher D. Manning"
  - "Chelsea Finn"
year: 2023
month: 5
arxiv_id: "2305.18290"
url: "https://arxiv.org/abs/2305.18290"
methods:
  - method:dpo
cites:
  - paper:ppo-paper
tags:
  - post-training
  - preference-alignment
---

# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

## Abstract Summary
DPO derives a closed-form substitution that solves the constrained RLHF optimization problem analytically, demonstrating that language models can be aligned to human preferences directly via classification loss on pair data without explicit reward modeling or reinforcement learning loops.

## Key Contributions
1. Analytical derivation proving equivalence between policy optimization and reward modeling under the Bradley-Terry preference framework.
2. Direct binary cross-entropy loss function over paired preference responses.
