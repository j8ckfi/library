---
id: paper:esrl
type: paper
title: "Expert-Space Exploration in MoE Reinforcement Learning"
authors:
  - "Hongyi He"
  - "Zhenghao Lin"
  - "Xiao Liu"
  - "Peng Cheng"
  - "Yan Lu"
  - "Yeyun Gong"
year: 2026
month: 9
arxiv_id: "2609.13058"
url: "https://arxiv.org/abs/2609.13058"
methods:
  - method:esrl
cites:
  - paper:grpo
  - paper:gspo
  - paper:sapo
tags:
  - post-training
  - moe
  - rl-alignment
  - esrl
  - routing
---

# Expert-Space Exploration in MoE Reinforcement Learning

## Abstract Summary
MoE RL work has mostly treated expert selection as a fixed component. Token-dependent routing determines the sparse computation paths that induce output distributions, so expert selection is an extra source of rollout diversity, similar to raising decoding temperature. Unrestricted perturbation activates unsuitable experts and hurts quality. ESRL keeps high-confidence experts as anchors, samples remaining experts from a plausible candidate pool, adapts noise with router entropy, and replays rollout expert IDs during policy optimization (R3) so the path is consistent while routing weights are recomputed.

## Key Contributions
1. **Anchored expert sampling**: fixed high-confidence experts; remaining slots from a bounded noisy candidate pool.
2. **Entropy-adaptive routing noise**: stronger when the router is sharp.
3. **Rollout Routing Replay (R3)**: record expert IDs at rollout; replay them on the training-side logp recompute.

## Empirical Highlights
- Qwen3-30B-A3B MATH post-train: ESRL average Pass@1 / Pass@8 42.1 / 64.2 vs GRPO 38.9 / 59.7 (+3.2 / +4.5) vs GSPO 41.6 / 63.3. Also Sigma-20B-A0.5B (top-1) and Moonlight-16B-A3B (shared experts).
- No extra sampling or compute vs the GRPO host. Complements the loss; does not replace SAPO.
- Code: `https://github.com/strawberrymaster111/ESRL-Release` (slime + SGLang + Megatron patches).

## Open Source Repository & Resources
- Official: `https://github.com/strawberrymaster111/ESRL-Release`
- Host: THUDM/slime. Example: Qwen3-30B-A3B, 8 GPUs, `scripts/Qwen-3-30BA3B-n010-t080-singlenode.sh`.
