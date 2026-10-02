---
id: task:full-param-memory-efficient-pretrain
type: task
title: "Full-Parameter Memory-Efficient Pretraining & Fine-Tuning"
domain: "efficiency"
summary: "Full-parameter optimization of large models on memory-constrained GPUs via low-rank gradient subspace projections or extreme-geometry sparse FT optimizers."
scope: "Full-parameter pretraining and fine-tuning when optimizer state or peak memory is the constraint. First hop is SCALE (subspace projections). TACO is the FT-axis ternary column-wise one-sparse plug-in. Not the ~7B pretrain optimizer."
out_of_scope:
  - "~7B dense pretrain optimizer (Muon2)"
  - "Native FP4 hardware training from scratch (Quartet-II)"
  - "Quality LoRA on 24GB (vanilla LoRA + rsLoRA + LR sweep)"
redirects:
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "ternary abs-max column-wise one-sparse optimizer for full-param LLM FT"
    to: "method:taco"
  - when: "native FP4 forward/backward hardware training from scratch"
    to: "task:fp4-hardware-training"
  - when: "quality LoRA on 24GB without a fully quantized checkpoint constraint"
    to: "task:lora-quality-tuning"
current_sota:
  - method: method:scale
    as_of: "2026-08-26"
    benchmark: "Full-Parameter 24GB Pretraining / Fine-Tuning"
    metric: "loss convergence & memory reduction"
    value: "Default SOTA for memory-efficient full-parameter training"
    notes: "SCALE (2506.16659, ICML 2026) not GaLore."
methods:
  - method:scale
  - method:galore
  - method:taco
last_reviewed: "2026-10-02"
tags:
  - efficiency
  - optimizer
  - memory-efficient
  - scale
---

# Full-Parameter Memory-Efficient Pretraining & Fine-Tuning

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **SCALE** (`method:scale`, 2506.16659, ICML 2026) — not GaLore.
- **Optional FT-axis sparse optimizer (not this first hop)**: `method:taco` (`arXiv:2610.02199`). Ternary abs-max column-wise one-sparse updates; 174× optimizer-state vs AdamW8bit on OPT-13B SST-2. Does not replace SCALE or Muon2.
