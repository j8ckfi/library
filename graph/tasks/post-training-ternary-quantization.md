---
id: task:post-training-ternary-quantization
type: task
title: "Post-Training Ternary Quantization of Existing LLMs"
domain: "compression"
summary: "Converting existing pre-trained FP16 foundation models to ternary 1.58-bit representations without pretraining from scratch."
current_sota:
  - method: method:scaleq-158
    as_of: "2026-08-26"
    benchmark: "Post-Training Ternarization Benchmark"
    metric: "perplexity recovery & throughput"
    value: "Default SOTA for ternarizing existing models"
    notes: "ScaleQ-1.58 (2608.01078)."
methods:
  - method:scaleq-158
  - method:sparse-bitnet
  - method:sherry
tags:
  - compression
  - quantization
  - ternary
  - ptq
---

# Post-Training Ternary Quantization of Existing LLMs

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **ScaleQ-1.58** (`method:scaleq-158`, 2608.01078).
