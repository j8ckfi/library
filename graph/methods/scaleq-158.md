---
id: method:scaleq-158
type: method
title: "ScaleQ-1.58 (Post-Training Ternarization)"
category: "quantization"
status: sota
sota_for:
  - task:post-training-ternary-quantization
papers:
  - paper:scaleq-158
recipes:
  - recipe:scaleq-158
claims:
  - benchmark: "LLM Post-Training Ternarization"
    metric: "perplexity recovery & inference throughput"
    value: "Default SOTA for ternarizing existing pretrained LLMs"
    baseline: "Standard Post-Training Quantization (PTQ)"
    date: "2026-08-26"
    verified: true
    notes: "Converts existing FP16 checkpoints into ternary {-1, 0, +1} weights without pretraining from scratch."
tags:
  - quantization
  - ternary
  - scaleq-158
  - sota
---

# ScaleQ-1.58 (Post-Training Ternarization)

## Method Overview
ScaleQ-1.58 enables post-training ternarization of existing pre-trained foundation models into ternary \(\{-1, 0, +1\}\) representations, avoiding the enormous compute cost of pretraining from scratch.

## When to Use
- Default SOTA method when you need to ternarize an existing pre-trained foundation LLM checkpoint.
