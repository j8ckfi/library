---
id: paper:miles
type: paper
title: "Miles v0.1: Production-Level Post-Training"
authors:
  - "Tom Chen"
  - "Mao Cheng"
  - "Shi Dong"
  - "Kangrui Du"
  - "Yanbin Jiang"
  - "Jiajun Li"
  - "Yiming Li"
  - "Tao Lin"
  - "Yusheng Su"
  - "Andy Ye"
  - "Yueming Yuan"
  - "Zhichen Zeng"
year: 2026
month: 9
arxiv_id: "2609.08368"
url: "https://arxiv.org/abs/2609.08368"
methods:
  - method:miles
cites:
  - paper:opd
  - paper:grpo
tags:
  - systems
  - post-training
  - agentic
  - miles
---

# Miles v0.1: Production-Level Post-Training

## Abstract Summary
Miles v0.1 is a full-stack, production-ready system for frontier post-training, descended from slime. Each stage of the RL loop is designed to be verified, clean, and customizable. Rollout engines sit on SGLang; the trainer offers NVIDIA Megatron-LM or PyTorch FSDP; three weight-synchronization transports cover colocated and disaggregated topologies. Beyond full-parameter RL, the same stack supports LoRA RL, on-policy distillation, supervised fine-tuning, true-on-policy rollout–training alignment, and diffusion models. The report closes with fully asynchronous agentic RL on GLM-5.2 744B-A40B over terminal-use coding tasks on 64 NVIDIA GB300 GPUs (32 rollout / 32 train), median step time 263 seconds over the first 30 measured steps.

## Key Contributions
1. **Production RL loop**: SGLang rollouts, Megatron or FSDP trainer, three weight-sync transports, sample-granularity fully async scheduling.
2. **Fidelity**: token-in-token-out multi-turn sessions, optional rollout routing replay (R3) for MoE expert assignments, truncated IS for remaining train–rollout mismatch.
3. **Memory at frontier MoE**: actor offload, optimizer-state streaming to node-local disk (needed even at DP=4 for GLM-5.2).
4. **Same stack, several objectives**: LoRA RL, OPD, SFT, true-on-policy alignment, diffusion.

## Empirical Highlights
- GLM-5.2 744B-A40B, Terminal-bench-2, 64× GB300, TP2/PP4/CP4/EP8 train, BF16 train / FP8 serve: median step 263s (first 30 steps; step-0 warm-up 1042s clipped).
- Prefix-cache hit rate 96%; train–inference KL mean 0.0369 over 100 steps.
- Raw task reward 9-step moving average 0.438→0.556 on a single 100-step run (observation, not a bake-off).

## Open Source Repository & Resources
- Code: `https://github.com/radixark/miles`
- Website: `https://miles.radixark.com`
- Case-study launch: `examples/experimental/openenv/glm52_tbench2`
