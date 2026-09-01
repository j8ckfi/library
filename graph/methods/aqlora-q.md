---
id: method:aqlora-q
type: method
title: "AQLoRA-Q (4-Bit Quantized LoRA)"
category: "peft"
status: sota
sota_for:
  - task:parameter-efficient-fine-tuning
  - task:4bit-peft-quantization
supersedes:
  - method:qlora
papers:
  - paper:aqlora
recipes:
  - recipe:aqlora
claims:
  - benchmark: "Single-GPU 24GB 4-Bit PEFT"
    metric: "dequantization throughput & task accuracy"
    value: "Default SOTA speed and recipe on 4-bit stack"
    baseline: "QLoRA (NF4)"
    date: "2026-08-26"
    verified: true
    notes: "Accurate 4-bit quantized low-rank adaptation with accelerated kernels."
tags:
  - peft
  - quantization
  - 4bit
  - aqlora
  - sota
---

# AQLoRA-Q (4-Bit Quantized LoRA)

## Method Overview
AQLoRA-Q is the state-of-the-art 4-bit quantized adapter fine-tuning method:
1. **Accurate Quantization Grids**: Non-uniform grids minimizing quantization distortion on sensitive projection layers.
2. **Accelerated Kernels**: Faster on-the-fly dequantization during backward passes than standard bitsandbytes NF4.

## When to Use
- Default SOTA method when fine-tuning memory must fit on a 4-bit stack.

## Relation to Existing SOTA
- Remains the 4-bit PEFT speed/recipe default. Fully low-bit checkpoints with no high-precision adapter are `method:gradcodes` on `task:full-lowbit-finetune`, which does not replace AQLoRA-Q.

## Supersession
- Supersedes `method:qlora` as the speed and recipe default on 4-bit fine-tuning stacks.
