---
id: method:kimi-linear
type: method
title: "Kimi-Linear Attention"
category: "architecture"
status: active
papers:
  - paper:kimi-linear
recipes:
  - recipe:kimi-linear
claims:
  - benchmark: "1M Context Needle-In-A-Haystack"
    metric: "retrieval accuracy & memory"
    value: "Constant KV cache memory across 1M token contexts"
    baseline: "Full Softmax Attention"
    date: "2026-08-26"
    verified: true
    notes: "Hardware-aligned linear attention kernels for ultra-long context inference."
tags:
  - architecture
  - linear-attention
  - long-context
  - kimi
---

# Kimi-Linear Attention

## Method Overview
Kimi-Linear implements Triton-optimized chunkwise state recurrent kernels, enabling language models to process 1M+ token prompts without exceeding accelerator VRAM limits.

## When to Use
- Ultra-long context applications (>100k tokens) where standard attention KV caching is prohibitive.
