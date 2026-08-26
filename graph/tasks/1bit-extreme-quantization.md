---
id: task:1bit-extreme-quantization
type: task
title: "1-Bit / Ternary Extreme Weight Quantization"
domain: "compression"
summary: "Training ultra-low-bitwidth (-1, 0, 1) foundation models from scratch with native integer-addition matrix kernels."
current_sota:
  - method: method:bitnet-b158
    as_of: "2026-08-26"
    benchmark: "Zero-shot CommonSense & Perplexity (3B / 7B scales)"
    metric: "perplexity / energy ratio"
    value: "Parity with FP16 at 4x energy savings"
    notes: "If pretraining: train BitNet b1.58 from scratch and infer with bitnet.cpp kernels. Do not PTQ all the way to 1.58-bit."
methods:
  - method:bitnet-b158
tags:
  - compression
  - quantization
  - ternary
---

# 1-Bit / Ternary Extreme Weight Quantization

## Problem Definition
Post-training quantization often suffers significant degradation at sub-4-bit precision (e.g. 2-bit or 1-bit). Extreme quantization training seeks to pretrain language models natively using ternary weights \(\{-1, 0, +1\}\), replacing expensive floating-point multiplications in linear matrix projections with pure integer additions.

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**: WikiText-2 / C4 zero-shot perplexity, MMLU, ARC, HellaSwag, alongside energy efficiency (Joules/token) and memory bandwidth utilization.

## SOTA Landscape
Microsoft Research's **BitNet b1.58** demonstrated that 1.58-bit ternary models trained from scratch match standard full-precision FP16 transformer performance at equivalent model and dataset scales, establishing a new Pareto frontier for edge and low-power inference.
