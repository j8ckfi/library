---
id: paper:respo
type: paper
title: "ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy Learning"
authors:
  - "Yihang Chen"
  - "Yuanhao Ban"
  - "Cho-Jui Hsieh"
year: 2026
month: 9
arxiv_id: "2609.35433"
url: "https://arxiv.org/abs/2609.35433"
methods:
  - method:respo
cites:
  - paper:carm
  - paper:grpo
tags:
  - post-training
  - rlvr
  - off-policy
  - respo
---

# ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy Learning

## Abstract Summary
RLVR that reuses rollouts across updates hits sign-dependent gradient starvation under clipping: under-generated positives get clipped away at the low-IS tail, while over-generated negatives dominate the high-IS tail. ReSPO replaces clipping with a smooth two-branch sequence-level kernel from an alpha-divergence variational objective plus an exponential variance-control tilt. Code: yhangchen/ReSPO-code. HF Daily 2026-10-09. Beside CISPO / CARM.

## Key Contributions
1. Sign-dependent clip starvation: rare positives vanish, over-generated negatives dominate.
2. Two-branch sequence kernel from alpha-divergence plus exponential tilt, no hard clip.
3. Positive branch preserves rare-correct gradients; negative branch damps over-generated failures.

## Empirical Highlights
- Dense and MoE Qwen3: accelerates early optimization and raises held-out scores under rollout reuse.
- HF Daily 2026-10-09.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.35433`
- Code: `https://github.com/yhangchen/ReSPO-code` (`code_status: released`).
