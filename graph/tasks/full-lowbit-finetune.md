---
id: task:full-lowbit-finetune
type: task
title: "Fully Low-Bit Fine-Tuning in Quantized Code Space"
domain: "efficiency"
summary: "Adapt an already-quantized model while keeping every targeted checkpoint in the same low-bit representation, with no high-precision residual adapter at inference."
scope: "Deployment-faithful fine-tuning over quantization codes and scales (NF4 / INT4 / MXFP4) so the optimized state is the deployed state."
out_of_scope:
  - "4-bit PEFT that keeps a high-precision LoRA adapter at inference (AQLoRA-Q / QLoRA)"
  - "Native FP4 hardware training from scratch (Quartet-II / MXFP4 pretrain)"
  - "24GB quality LoRA in BF16/FP16 (vanilla LoRA + rsLoRA + LR sweep)"
  - "Post-training ternarization of an existing SOTA LLM (ScaleQ-1.58)"
redirects:
  - when: "memory must fit a 4-bit stack but a mixed-precision adapter at inference is acceptable"
    to: "task:4bit-peft-quantization"
  - when: "native FP4 forward/backward hardware training from scratch"
    to: "task:fp4-hardware-training"
  - when: "quality LoRA on 24GB without a fully quantized checkpoint constraint"
    to: "task:lora-quality-tuning"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:gradcodes
    as_of: "2026-09-01"
    benchmark: "Llama-3.2-1B-Instruct GSM8K fully 4-bit"
    metric: "GSM8K accuracy"
    value: "GradCodeS Full 41.63 vs PV-Tuning 36.92 vs QLoRA-4Merge 24.79 vs Base-4 25.85"
    notes: "GradCodeS (2608.30908). Does not replace AQLoRA-Q as 4-bit PEFT default or Quartet-II as NVFP4 hardware training."
methods:
  - method:gradcodes
  - method:aqlora-q
  - method:autoqra
  - method:qlora
  - method:quartet-ii
tags:
  - efficiency
  - quantization
  - 4bit
  - low-bit
  - code-space
  - gradcodes
---

# Fully Low-Bit Fine-Tuning in Quantized Code Space

## Problem Definition
Fine-tune targeted transformer weights that must remain in a chosen low-bit datatype (NF4, INT4, or MXFP4) at every accepted checkpoint. Only datatype-permitted scale metadata is extra. Mixed-precision adapters and post-hoc requantization are out of scope because they make the optimized state differ from the deployed state.

## Evaluation Protocol & Benchmarks
- **Primary Benchmarks**: GSM8K accuracy, AlpacaEval win rate, MASSIVE en-US exact match on Qwen3-0.6B and Llama-3.2-1B/3B-Instruct under fully 4-bit deployment.
- **Evaluation Pitfalls**: Do not compare against QLoRA-16A or other mixed-precision adapters as if they were fully 4-bit. Do not treat this as native FP4 pretraining.

## SOTA Recommendation (as of 2026-09-01)
- **Primary Method**: **GradCodeS** (`method:gradcodes`, `paper:gradcodes` `arXiv:2608.30908`) for code-space surrogate gradients plus guided discrete search.
- **Not This Task**: `method:aqlora-q` remains the 4-bit PEFT speed/recipe default; `method:quartet-ii` remains NVFP4 hardware training.
