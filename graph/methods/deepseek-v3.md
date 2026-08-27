---
id: method:deepseek-v3
type: method
title: "DeepSeek-V3 MoE Architecture"
category: "architecture"
status: superseded
superseded_by: method:deepseek-v4
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
DeepSeek-V3 established the open-weights architecture for large sparse Mixture-of-Experts models.

## Supersession
- Superseded by `method:deepseek-v4` as the canonical architecture template.
