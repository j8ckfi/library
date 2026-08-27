---
id: method:sparse-bitnet
type: method
title: "Sparse-BitNet (1.58-Bit Native Pretraining)"
category: "quantization"
status: sota
sota_for:
  - task:1bit-extreme-quantization
supersedes:
  - method:bitnet-b158
papers:
  - paper:sparse-bitnet
recipes:
  - recipe:sparse-bitnet
claims:
  - benchmark: "1-Bit Pretraining & Perplexity (3B / 7B scales)"
    metric: "Joules / token & accuracy parity"
    value: "2026 BitNet SOTA line; parity with dense 2B4T baseline"
    baseline: "BitNet b1.58"
    date: "2026-08-26"
    verified: true
    notes: "Native 1.58-bit ternary pretraining with dynamic activation sparsity."
tags:
  - quantization
  - 1bit
  - ternary
  - sparse-bitnet
  - sota
---

# Sparse-BitNet (1.58-Bit Native Pretraining)

## Method Overview
Sparse-BitNet represents the 2026 BitNet generation, combining native 1.58-bit ternary {-1, 0, +1} weight optimization with dynamic activation sparsity:
1. **Ternary Pretraining**: Native addition-only BitLinear matrix projections.
2. **Dynamic Sparsity**: Sparse activation gating providing higher energy efficiency than dense 1.58-bit models.

## When to Use
- Default SOTA method for training native 1.58-bit ternary LLMs from scratch.

## Supersession
- Supersedes `method:bitnet-b158` as the active 2026 BitNet line (keep 2B4T dense baseline as download reference).
