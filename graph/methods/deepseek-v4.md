---
id: method:deepseek-v4
type: method
title: "DeepSeek-V4 MoE Architecture"
category: "architecture"
status: sota
sota_for:
  - task:pretrain-moe-frontier
supersedes:
  - method:deepseek-v3
papers:
  - paper:deepseek-v4
recipes:
  - recipe:deepseek-v4
claims:
  - benchmark: "Frontier MoE Benchmarks & Compute Scaling"
    metric: "compute-optimal loss & inference throughput"
    value: "Frontier SOTA MoE Architecture Template"
    baseline: "DeepSeek-V3"
    date: "2026-08-26"
    verified: true
    notes: "Advanced Multi-Head Latent Attention (MLA), dynamic multi-token prediction heads, and ultra-fine-grained expert routing."
tags:
  - architecture
  - moe
  - frontier
  - deepseek-v4
  - sota
---

# DeepSeek-V4 MoE Architecture

## Method Overview
DeepSeek-V4 establishes the state-of-the-art sparse Mixture-of-Experts architecture:
1. **Multi-Head Latent Attention (MLA)**: Low-rank key-value projection compression reducing KV cache footprint during generation.
2. **Fine-Grained Expert Routing**: Expanded expert pool with auxiliary-loss-free load balancing.
3. **Multi-Token Prediction**: Speculative prediction heads trained natively to accelerate inference throughput.
4. **Manifold-Constrained Hyper-Connections (mHC)**: Residual stream expanded to \(n \times d\) (\(n=4\)) with doubly stochastic Sinkhorn projection (`method:mhc`).

## Systems & Megakernel Training
- Distributed pretraining on Blackwell NVL72 clusters is accelerated using **Mixture-of-Kittens** (`method:mixture-of-kittens`), fusing dispatch, SwiGLU FFN, and combine into a single deterministic megakernel.

## When to Use
- Default SOTA architecture template for pretraining large-scale sparse MoE models. Co-default with Kimi-K3 for frontier deployments.

## Relation to Existing SOTA
- Remains the frontier MoE architecture co-default with `method:kimi-k3`. `method:qwen38-next` is an adjacent Qwen-style hybrid residual recipe; `method:ce-moe` is an optional expert-layout niche. Neither replaces DeepSeek-V4.

## Supersession
- Supersedes `method:deepseek-v3` as the canonical architecture template.
