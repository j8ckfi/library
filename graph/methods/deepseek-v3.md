---
id: method:deepseek-v3
type: method
title: "DeepSeek-V3 MoE Architecture"
category: "architecture"
status: active
sota_for: []
supersedes: []
papers:
  - paper:deepseek-v3
recipes: []
claims:
  - benchmark: "671B MoE (37B active parameters)"
    metric: "compute-optimal loss & throughput"
    value: "Open Frontier MoE Standard"
    baseline: "Dense Transformers / Llama 3.1 405B"
    date: "2024-12"
    verified: true
    notes: "Multi-Head Latent Attention (MLA), DeepSeekMoE fine-grained expert routing, multi-token prediction."
tags:
  - architecture
  - moe
  - mla
---

# DeepSeek-V3 MoE Architecture

## Method Overview
DeepSeek-V3 establishes the standard open-weights architecture for large sparse Mixture-of-Experts models:
1. **Multi-Head Latent Attention (MLA)**: Compresses key-value activations into low-dimensional latent vectors to minimize KV-cache footprint.
2. **DeepSeekMoE**: 256 fine-grained routed experts + 1 shared expert with load-balancing loss without auxiliary loss degradation.
3. **Multi-Token Prediction (MTP)**: Predicts multiple future tokens simultaneously during training.

## Supersession
- Superseded for 2026-frontier designs by `method:kimi-k3`.
