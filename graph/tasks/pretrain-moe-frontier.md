---
id: task:pretrain-moe-frontier
type: task
title: "Pretrain Mixture-of-Experts (MoE) Architecture at Scale"
domain: "pretraining"
summary: "Frontier pretraining of sparse Mixture-of-Experts (MoE) architectures with multi-head latent attention and multi-token prediction."
current_sota:
  - method: method:kimi-k3
    as_of: "2026-08-26"
    benchmark: "Frontier MoE Benchmarks & Throughput"
    metric: "compute-optimal loss"
    value: "Frontier Pareto SOTA"
    notes: "Kimi-k3 architecture departure from DeepSeek-V3 MLA. Pretrain optimizer: MuonClip (kimi-k2)."
methods:
  - method:kimi-k3
  - method:deepseek-v3
  - method:muonclip-kimi-k2
tags:
  - pretraining
  - moe
  - frontier
---

# Pretrain Mixture-of-Experts (MoE) Architecture at Scale

## Problem Definition
Training sparse Mixture-of-Experts models enables scaling parameter capacity into hundreds of billions of parameters while keeping active FLOPs per token bounded.

## SOTA Recommendation (as of 2026-08-26)
- **Architecture**: DeepSeek-V3 architecture (`paper:deepseek-v3`) with Multi-Head Latent Attention (MLA), DeepSeekMoE fine-grained routing, and multi-token prediction. For 2026-frontier departures, follow Kimi-k3 (`paper:kimi-k3`).
- **Optimizer**: MuonClip / Kimi-k2 recipe (`paper:muonclip-kimi-k2`) for stable trillion-token MoE scaling.
