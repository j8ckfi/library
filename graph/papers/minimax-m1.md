---
id: paper:minimax-m1
type: paper
title: "MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention"
authors:
  - "MiniMax AI Team"
year: 2025
month: 6
arxiv_id: "2506.13585"
url: "https://arxiv.org/abs/2506.13585"
methods:
  - method:cispo
cites:
  - paper:dapo
tags:
  - post-training
  - rl-alignment
  - dense-rl
  - cispo
  - minimax
---

# MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention

## Abstract Summary
MiniMax-M1 presents large-scale dense policy optimization using Clipped IS-weight Policy Optimization (CISPO), achieving breakthrough performance on competitive mathematics and coding benchmarks.

## Key Contributions
1. **CISPO Algorithm (§3.1)**: Clipped IS-weight policy optimization clips \(\text{sg}(\text{clip}(\rho))\) on the importance sampling weights, guaranteeing valid gradient signals across all tokens and rare branches.
2. **Dense Scaling Laws**: Demonstrates steady reasoning accuracy gains scaling dense models with verifiable RL.

## Open Source Repository
- Implementation: `https://github.com/MiniMax-AI/MiniMax-M1`
