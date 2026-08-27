---
id: task:pretrain-moe-frontier
type: task
title: "Pretrain Mixture-of-Experts (MoE) Architecture at Scale"
domain: "pretraining"
summary: "Frontier pretraining of sparse Mixture-of-Experts (MoE) architectures with multi-head latent attention and multi-token prediction."
current_sota:
  - method: method:deepseek-v4
    as_of: "2026-08-26"
    benchmark: "Frontier MoE Benchmarks & Throughput"
    metric: "compute-optimal loss"
    value: "Frontier Pareto SOTA"
    notes: "DeepSeek-V4 (2606.19348) + Kimi-K3 (2607.24653)."
  - method: method:kimi-k3
    as_of: "2026-08-26"
    benchmark: "Frontier MoE Benchmarks & Long-Context Throughput"
    metric: "Pareto FLOP-to-accuracy efficiency"
    value: "Frontier Co-Default SOTA"
    notes: "Kimi-K3 (2607.24653) architecture co-default with DeepSeek-V4."
methods:
  - method:deepseek-v4
  - method:kimi-k3
  - method:deepseek-v3
  - method:nemotron-3-ultra
  - method:nemotron-3-super-latentmoe
  - method:mixture-of-kittens
  - method:apertus
  - method:glm-5
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
- **Architecture**: **DeepSeek-V4** (`method:deepseek-v4`, 2606.19348) + **Kimi-K3** (`method:kimi-k3`, 2607.24653).
- **Optimizer**: **MuonClip** (`paper:muonclip-kimi-k2`) / **Muon2** (`method:muon2`).
- **NVL72 Systems Megakernel**: **Mixture-of-Kittens** (`method:mixture-of-kittens`, `task:train-moe-nvl72`).
