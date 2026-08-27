---
id: method:bitnet-b158
type: method
title: "BitNet b1.58 (1.58-Bit Ternary Pretraining)"
category: "quantization"
status: active
superseded_by: method:sparse-bitnet
sota_for: []
supersedes: []
papers:
  - paper:bitnet-b158
  - paper:bitnet-b158-paper
recipes:
  - recipe:bitnet-b158
claims:
  - benchmark: "Perplexity & Downstream Zero-Shot (3B-7B models)"
    metric: "accuracy / latency parity with FP16"
    value: "Parity with FP16 Transformer at 4.1x throughput"
    baseline: "Llama-like FP16 Baseline"
    date: "2024-02"
    verified: true
    notes: "Replaces FP16 matrix multiplication with addition-only BitLinear kernels."
tags:
  - quantization
  - ternary
  - 1bit
  - compression
---

# BitNet b1.58 (1.58-Bit Ternary Pretraining)

## Method Overview
BitNet b1.58 proves that language models can be trained natively from scratch where every parameter in linear projections is ternary: \(W \in \{-1, 0, +1\}\). Retained as the downloadable dense 2B4T baseline citation.

## Supersession
- Superseded by `method:sparse-bitnet` (2603.05168) as the active 2026 BitNet line.
