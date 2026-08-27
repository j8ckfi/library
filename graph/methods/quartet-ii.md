---
id: method:quartet-ii
type: method
title: "Quartet-II (NVFP4 Hardware Training)"
category: "quantization"
status: sota
sota_for:
  - task:fp4-hardware-training
papers:
  - paper:quartet-ii
recipes:
  - recipe:quartet-ii
claims:
  - benchmark: "NVFP4 Hardware Training Benchmarks"
    metric: "training throughput & numerical stability"
    value: "Full-speed FP4 hardware training on Blackwell/Hopper"
    baseline: "FP8 / BF16"
    date: "2026-08-26"
    verified: true
    notes: "Hardware-aware 4-bit floating-point (NVFP4) training protocol."
tags:
  - quantization
  - fp4
  - nvfp4
  - hardware-training
  - quartet-ii
  - sota
---

# Quartet-II (NVFP4 Hardware Training)

## Method Overview
Quartet-II implements hardware-aware NVFP4 (4-bit floating point) training for deep transformer networks, utilizing specialized stochastic rounding, dynamic block scaling, and Blackwell tensor core instructions.

## When to Use
- Default SOTA method for native FP4 hardware training on modern GPU accelerators.
