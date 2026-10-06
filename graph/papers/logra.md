---
id: paper:logra
type: paper
title: "LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches"
authors:
  - Shaokun Zhang
  - Yifan Zhang
  - Jian Hu
  - Yueying Li
  - Hao Zhang
  - Binfeng Xu
  - Jan Kautz
  - Yi Dong
year: 2026
month: 10
arxiv_id: "2610.06647"
url: "https://arxiv.org/abs/2610.06647"
methods:
  - method:logra
cites:
  - paper:minimax-m1
  - paper:scale
tags:
  - post-training
  - optimizer
  - rl-alignment
  - logra
---

# LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches

## Abstract Summary
LoGRA keeps RL learning signal in low-rank gradient sketches for updates and policy sync, plus predicted-KL step control that estimates the policy change before applying the update. Up to 45.7% average training-memory cut without sacrificing performance. Enables 27B for 1100+ steps on one 8-GPU node where dense Adam OOMs. Abstract cites a Molt library with no URL (`code_status: none`). Beside CISPO / SCALE; does not retarget either.

## Key Contributions
1. **Low-rank gradient sketches** for the RL update and policy sync.
2. **Predicted-KL step control** before applying the update.
3. **45.7%** average RL memory cut; 27B / 1100+ steps on 8 GPUs.

## Empirical Highlights
- Up to 45.7% average training-memory reduction without sacrificing performance.
- 27B-parameter model, 1100+ steps, single eight-GPU node; dense Adam OOM.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06647`
- Code: none found as of 2026-10-06 (`code_status: none`). Abstract names a Molt library without a URL.
