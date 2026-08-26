---
id: method:bitnet-b158
type: method
title: "BitNet b1.58 (1.58-Bit Ternary Pretraining)"
category: "quantization"
status: sota
sota_for:
  - task:1bit-extreme-quantization
supersedes: []
papers:
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
BitNet b1.58 proves that language models can be trained natively from scratch where every parameter in linear projections is ternary: \(W \in \{-1, 0, +1\}\), which mathematically represents \(\log_2(3) \approx 1.58\) bits per weight.

The core component is the **BitLinear** layer:
1. **Weight Quantization (Absmean)**:
   \[
   W_{\text{quant}} = \text{RoundClip}\left(\frac{W}{\gamma + \epsilon}, -1, 1\right), \quad \gamma = \frac{1}{nm} \sum_{i,j} |W_{i,j}|
   \]
2. **Activation Quantization (Absmax)**:
   Activations are scaled to 8-bit integers \([ -Q_b, Q_b ]\) where \(Q_b = 2^{b-1}\).
3. **Multiplication-Free Matrix Multiply**:
   Linear layer execution reduces to integer addition and subtraction operations on hardware.

## When to Use
- **Edge Deployment & Embedded Accelerators**: Ultra-low wattage CPUs, FPGAs, and mobile SoCs where hardware matrix multipliers are memory-bandwidth-bound.
- **Large-Scale Green Computing**: Pretraining dedicated models targeting 3x–5x energy reduction.

## Gotchas & Failure Modes
1. **Requires Training From Scratch**: You cannot simply quantize a standard pretrained FP16 model to BitNet b1.58 post-hoc; weights must be optimized with straight-through estimators (STE) from initialization.
2. **Standard GPUs Need Custom Kernels**: NVIDIA Hopper/Blackwell GPUs are optimized for FP8/FP16; real throughput gains require specialized BitNet / 2-bit integer GEMM kernels (e.g. bitnet.cpp).
