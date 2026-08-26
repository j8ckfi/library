---
id: method:kimi-k3
type: method
title: "Kimi-K3 Architecture"
category: "architecture"
status: sota
sota_for:
  - task:pretrain-moe-frontier
supersedes:
  - method:deepseek-v3
papers:
  - paper:kimi-k3
recipes:
  - recipe:mamba2-training
claims:
  - benchmark: "Frontier 2026 MoE Pretraining"
    metric: "Pareto FLOP-to-accuracy efficiency"
    value: "Frontier MoE SOTA"
    baseline: "DeepSeek-V3 MLA Architecture"
    date: "2026-07"
    verified: true
    notes: "August 2026 architecture departure from DeepSeek-V3 MLA for high-throughput long-context reasoning."
tags:
  - architecture
  - moe
  - frontier
---

# Kimi-K3 Architecture

## Method Overview
Kimi-K3 represents the mid-2026 frontier architecture departure from DeepSeek-V3 Multi-Head Latent Attention (MLA), optimizing memory-bandwidth bounds during ultra-long context training and inference.

## When to Use
- Frontier MoE model design in 2026+.

## Supersession
- Supersedes `method:deepseek-v3` architecture for 2026 frontier deployments.
