---
id: task:parameter-efficient-fine-tuning
type: task
title: "Parameter-Efficient Fine-Tuning (PEFT) & Low-Rank Adaptation"
domain: "efficiency"
summary: "Adapting large base models to downstream domain tasks with minimal trainable parameter updates and negligible compute overhead."
current_sota:
  - method: method:dora
    as_of: "2024-02"
    benchmark: "LLaMA-7B/13B Commonsense Reasoning (8 tasks)"
    metric: "mean accuracy"
    value: 78.7
    notes: "Weight-Decomposed Low-Rank Adaptation decoupling directional updates from magnitude updates."
methods:
  - method:dora
  - method:lora
  - method:qlora
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
