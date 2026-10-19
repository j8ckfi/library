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
  - when: "drift-aware streaming k-PCA GaLore-family low-rank LLM training (Ori)"
    to: "method:ori"
  - when: "losslessly compressed GPU train tensors (LCT Huffman)"
    to: "method:lct"
  - when: "4-bit AdamW optimizer-state quantization in preconditioner space (ZIP-SR)"
    to: "method:zip-sr"
  - when: "Nyström-sketched SOAP preconditioners / linear optimizer memory (Clean / Q-Clean)"
    to: "method:clean"
  - when: "low-rank gradient sketches + predicted-KL step control for RL memory"
    to: "method:logra"
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "ternary abs-max column-wise one-sparse optimizer for full-param LLM FT"
    to: "method:taco"
  - when: "native FP4 forward/backward hardware training from scratch"
    to: "task:fp4-hardware-training"
  - when: "quality LoRA on 24GB without a fully quantized checkpoint constraint"
    to: "task:lora-quality-tuning"
  - when: "mixed-precision scaling law for which pass to keep high precision (not optimizer-state memory)"
    to: "method:mixed-precision-scaling"
  - when: "structure-aware Muon on Monarch-factored weights (not SCALE subspace)"
    to: "method:monarch-muon"
  - when: "subspace Muon with residual correction (PMRC / SMRC)"
    to: "method:pmrc"
current_sota:
  - method: method:scale
    as_of: "2026-08-26"
    benchmark: "Full-Parameter 24GB Pretraining / Fine-Tuning"
    metric: "loss convergence & memory reduction"
    value: "Default SOTA for memory-efficient full-parameter training"
    notes: "SCALE (2506.16659, ICML 2026) not GaLore."
methods:
  - method:ori
  - method:lct
  - method:pmrc
  - method:mixed-precision-scaling
  - method:monarch-muon
  - method:zip-sr
  - method:clean
  - method:logra
  - method:scale
  - method:galore
  - method:taco
last_reviewed: '2026-10-19'
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
- **Optional 4-bit AdamW-state quantization (not this first hop)**: `method:zip-sr` (`arXiv:2610.12444`) on `task:llm-pretraining-optimization`. Preconditioner-space SR; up to 70% TorchAO gap cut. Does not replace SCALE, Muon2, or TACO.
- **Optional mixed-precision pass allocation (not this first hop)**: `method:mixed-precision-scaling` (`arXiv:2610.17637`) on `task:fp4-hardware-training`. Does not replace SCALE.
- **Optional Monarch-factored Muon (not this first hop)**: `method:monarch-muon` (`arXiv:2610.17429`). 6.89B H100 peak 68.87→52.94 GB. Loses to dense Muon at 257M. Does not replace SCALE or Muon2.
- **Optional residual-correction subspace Muon (not this first hop)**: `method:pmrc` (`arXiv:2610.19844`). LLaMA 1.3B C4 train 2.500 vs Fira 2.657 vs GaLore 2.842. No SCALE bake-off. No dedicated repo. Does not replace SCALE.

- **Optional lossless GPU train tensors**: `method:lct` (`arXiv:2610.22179`). NanoGPT −24.6% mem / +7.2% step-time; Qwen3-4B −23.8% peak. No public code. Does not replace SCALE.
- **Optional streaming k-PCA low-rank**: `method:ori` (`arXiv:2610.22794`). Up to 69.3% gap cut vs prior GaLore-family on 1B LLaMA. No SCALE bake-off. Does not replace SCALE.

