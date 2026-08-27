---
id: task:fp4-hardware-training
type: task
title: "Native FP4 Hardware Training"
domain: "compression"
summary: "End-to-end 4-bit floating-point forward and backward pass training on modern GPU accelerators."
current_sota:
  - method: method:quartet-ii
    as_of: "2026-08-26"
    benchmark: "NVFP4 Hardware Training Benchmarks"
    metric: "training throughput & numerical stability"
    value: "Default SOTA for NVFP4 hardware training"
    notes: "Quartet-II NVFP4 (2601.22813) / MXFP4 (2605.09825) / Kimi-K3 QAT."
  - method: method:mxfp4-mi355x
    as_of: "2026-08-26"
    benchmark: "Microscaled FP4 Benchmark"
    metric: "numerical stability"
    value: "Co-Default SOTA for microscaling FP4"
    notes: "MXFP4 (2605.09825)."
methods:
  - method:quartet-ii
  - method:mxfp4-mi355x
  - method:kimi-k3
tags:
  - compression
  - quantization
  - fp4
  - hardware-training
---

# Native FP4 Hardware Training

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **Quartet-II NVFP4** (`method:quartet-ii`, 2601.22813) / **MXFP4** (`method:mxfp4-mi355x`, 2605.09825) / **Kimi-K3 QAT**.
