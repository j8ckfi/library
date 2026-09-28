---
id: task:lora-skill-composition
type: task
title: "LoRA Skill Composition"
domain: "efficiency"
summary: "Compose independently trained LoRA adapters into one folded model by canonicalizing factors and training read-only couplings, without an inference router."
scope: "Composing / stacking independently trained LoRA skills without inference routers. First hop is READ. Not single-adapter quality, not 4-bit PEFT, not drift-budget instruct freeze."
out_of_scope:
  - "Single-adapter quality LoRA on 24GB (vanilla LoRA + rsLoRA + LR sweep)"
  - "4-bit PEFT stack (AQLoRA-Q / AutoQRA)"
  - "Instruct FT under a behavioral-drift budget / layer-selective freeze (DCO)"
  - "RLVR-stable rank-normalized LoRA A (NoRA)"
  - "Fully low-bit checkpoints with no high-precision adapter (GradCodeS)"
redirects:
  - when: "single-adapter quality LoRA / rsLoRA + LR sweep rather than stacking adapters"
    to: "task:lora-quality-tuning"
  - when: "memory must fit a 4-bit PEFT stack"
    to: "task:4bit-peft-quantization"
  - when: "instruct FT under a behavioral-drift budget / layer-selective freeze of instruct models rather than LoRA composition"
    to: "task:instruct-sft-alignment"
  - when: "deployed checkpoint must stay NF4/INT4/MXFP4 with no high-precision adapter"
    to: "task:full-lowbit-finetune"
current_sota:
  - method: method:read-lora
    as_of: "2026-09-28"
    benchmark: "Llama-3.2-3B SuperGLUE / Domain; Qwen3-4B GLUE; 32-lineage mean lift"
    metric: "suite-mean official primary metrics; mean vs per-lineage strongest foldable alternative"
    value: "SuperGLUE 0.783 vs 0.605; Domain 0.887 vs 0.846; Qwen GLUE 0.838 vs 0.775; +0.073 (95% CI +0.047–+0.101)"
    notes: "READ (2609.31600). Method status active. Does not replace lr-matters-lora or AQLoRA-Q."
methods:
  - method:read-lora
  - method:lr-matters-lora
  - method:aqlora-q
  - method:nora
  - method:iso-lora
  - method:anlr-lora
  - method:dco
last_reviewed: "2026-09-28"
tags:
  - efficiency
  - peft
  - lora
  - composition
  - read-lora
---

# LoRA Skill Composition

## Problem Definition
Independently trained LoRA skills accumulate. Adding their \(\Delta W\) in weight space interferes; retraining on all task data is expensive; routing keeps extra objects at serve time. This task owns **composition of already-trained adapters** into one folded model: canonicalize factor coordinates, then couple in one direction so a new skill may read old input subspaces but must not write old output subspaces.

This is **not** single-adapter quality tuning, not 4-bit PEFT, and not drift-budget instruct freeze.

## Evaluation Protocol
- **Primary Benchmarks**: sequential skill add on GLUE / SuperGLUE / Domain / BBH for Llama-3.2-3B and Qwen3-4B; terminal suite macros vs the strongest published foldable alternative built from the **same** source adapters; 32-lineage mean lift with bootstrap CI.
- **Evaluation Pitfalls**: Do not treat a 24GB LoRA quality number (`method:lr-matters-lora`) or a 4-bit PEFT speed number (`method:aqlora-q`) as this task. BBH is the paper's weak suite.

## SOTA Recommendation (as of 2026-09-28)
- **Primary Method (this task only)**: **READ** (`method:read-lora`, `paper:read-lora` `arXiv:2609.31600`). Status `active`. Listed here as first hop.
- **Not This Task**: `method:lr-matters-lora` remains 24GB LoRA quality; `method:aqlora-q` remains 4-bit PEFT; `method:dco` remains drift-budget instruct FT; `method:nora` remains RLVR-stable LoRA A.
