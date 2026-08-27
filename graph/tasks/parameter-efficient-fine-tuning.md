---
id: task:parameter-efficient-fine-tuning
type: task
title: "Parameter-Efficient Fine-Tuning (PEFT) & Low-Rank Adaptation"
domain: "efficiency"
summary: "Adapting large base models to downstream domain tasks with minimal trainable parameter updates and negligible compute overhead."
current_sota:
  - method: method:lr-matters-lora
    as_of: "2026-08-26"
    benchmark: "Single GPU PEFT / MMLU / GSM8k"
    metric: "accuracy vs parameter overhead"
    value: "Vanilla LoRA + rsLoRA + LR sweep SOTA (NOT DoRA)"
    notes: "Vanilla LoRA + rsLoRA + LR sweep (2602.04998, 2601.22708). 4-bit must: AQLoRA-Q (2608.23816) or AutoQRA (2602.22268)."
  - method: method:aqlora-q
    as_of: "2026-08-26"
    benchmark: "4-Bit Single GPU PEFT"
    metric: "speed and accuracy retention"
    value: "4-Bit SOTA Speed/Recipe Default"
    notes: "AQLoRA-Q (2608.23816) or AutoQRA (2602.22268)."
methods:
  - method:lr-matters-lora
  - method:aqlora-q
  - method:autoqra
  - method:scale
  - method:lora-unified-study
  - method:lords
  - method:beft
  - method:super-tuning
  - method:qlora
  - method:delora
  - method:dora
  - method:galore
  - method:lora
tags:
  - efficiency
  - peft
  - low-rank
  - lora
---

# Parameter-Efficient Fine-Tuning (PEFT) & Low-Rank Adaptation

## Problem Definition
Adapting multi-billion parameter base models to downstream tasks with minimal trainable parameters on single GPU hardware.

## SOTA Recommendation (as of 2026-08-26)
- **LoRA Quality 24GB**: **Vanilla LoRA + rsLoRA + LR sweep** (`method:lr-matters-lora`, 2602.04998, 2601.22708) — NOT DoRA.
- **LoRA Must 4-Bit**: **AQLoRA-Q** (`method:aqlora-q`, 2608.23816) or **AutoQRA** (`method:autoqra`, 2602.22268).
- **Full-Parameter Memory-Efficient Pretrain**: **SCALE** (`method:scale`, 2506.16659) — not GaLore.
