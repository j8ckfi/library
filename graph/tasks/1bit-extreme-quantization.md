---
id: task:1bit-extreme-quantization
type: task
title: "1-Bit / Ternary Extreme Weight Quantization"
domain: "compression"
summary: "Training ultra-low-bitwidth (-1, 0, 1) foundation models from scratch with native integer-addition matrix kernels."
current_sota:
  - method: method:sparse-bitnet
    as_of: "2026-08-26"
    benchmark: "Zero-shot CommonSense & Perplexity (3B / 7B scales)"
    metric: "energy efficiency & accuracy parity"
    value: "2026 BitNet SOTA line; parity with dense 2B4T baseline"
    notes: "Sparse-BitNet (2603.05168); keep 2B4T as dense cite."
methods:
  - method:sparse-bitnet
  - method:scaleq-158
  - method:quartet-ii
  - method:mxfp4-mi355x
  - method:sherry
  - method:bitembed
  - method:bitnet-b158
tags:
  - compression
  - quantization
  - ternary
  - sparse-bitnet
---

# 1-Bit / Ternary Extreme Weight Quantization

## Problem Definition
Training foundation models natively using ternary weights \(\{-1, 0, +1\}\), replacing expensive floating-point multiplications with integer additions.

## SOTA Recommendation (as of 2026-08-26)
- **Native 1.58-Bit Pretrain**: **Sparse-BitNet** (`method:sparse-bitnet`, 2603.05168); keep 2B4T as dense baseline citation.
- **Ternary Existing SOTA LLM**: **ScaleQ-1.58** (`method:scaleq-158`, 2608.01078).
- **FP4 Hardware Train**: **Quartet-II NVFP4** (`method:quartet-ii`, 2601.22813) / **MXFP4** (`method:mxfp4-mi355x`, 2605.09825).
