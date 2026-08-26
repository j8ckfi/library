---
id: task:parameter-efficient-fine-tuning
type: task
title: "Parameter-Efficient Fine-Tuning (PEFT) & Low-Rank Adaptation"
domain: "efficiency"
summary: "Adapting large base models to downstream domain tasks with minimal trainable parameter updates and negligible compute overhead."
current_sota:
  - method: method:qlora
    as_of: "2026-08-26"
    benchmark: "Single GPU PEFT / MMLU"
    metric: "memory reduction & performance retention"
    value: "24GB 1-GPU SOTA Default"
    notes: "Default is QLoRA (NF4 + LoRA). Quality bump: DoRA or DeLoRA (bounded Frobenius update, robust to long/LR runs). Full-rank alternative: GaLore."
methods:
  - method:qlora
  - method:delora
  - method:dora
  - method:galore
  - method:lora
tags:
  - efficiency
  - peft
  - low-rank
---

# Parameter-Efficient Fine-Tuning (PEFT) & Low-Rank Adaptation

## Problem Definition
Full fine-tuning of multi-billion parameter foundation models requires storing optimizer states, gradients, and activation checkpoints for every weight parameter, exceeding single-node GPU memory. Parameter-efficient methods inject small low-rank adapter matrices to approximate full parameter rank updates while freezing the base model weights.

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**: GLUE, CommonsenseQA (ARC, BoolQ, PIQA, HellaSwag, WinoGrande, OpenBookQA), GSM8k instruction tuning.
- **Evaluation Hazards**: Rank saturation and initialization variance.

## SOTA Landscape
While standard LoRA (Hu et al.) adds low-rank delta matrices \(\Delta W = B \cdot A\), **DoRA** decomposes the weight update into magnitude and directional components, matching or exceeding full fine-tuning performance across benchmarks. For extreme memory savings, **QLoRA** quantizes base weights into 4-bit NormalFloat while training LoRA adapters in 16-bit precision.
