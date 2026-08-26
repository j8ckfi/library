---
id: task:llm-pretraining-optimization
type: task
title: "Large Language Model Pretraining Optimization"
domain: "pretraining"
summary: "Optimization of transformer and non-transformer language model weights from scratch using first- and second-order momentum and orthogonalized matrix updates."
current_sota:
  - method: method:muon-optimizer
    as_of: "2025-02"
    benchmark: "FineWeb-Edu NanoGPT (1.5B tokens)"
    metric: "validation loss"
    value: 3.21
    notes: "Achieves target validation loss in ~50% fewer steps compared to tuned AdamW baselines."
methods:
  - method:muon-optimizer
  - method:adamw-optimizer
tags:
  - pretraining
  - optimizer
  - language-models
---

# Large Language Model Pretraining Optimization

## Problem Definition
Pretraining modern neural network models (typically autoregressive language models) involves minimizing cross-entropy loss over hundreds of billions or trillions of tokens. The primary challenge is maximizing parameter update efficiency per unit of GPU compute (FLOPS) and wall-clock time while maintaining training stability at scale.

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**:
  - Training loss and validation cross-entropy on held-out splits of FineWeb, FineWeb-Edu, RedPajama, or C4.
  - Downstream zero-shot accuracy evaluations (e.g. ARC, HellaSwag, MMLU, GSM8k) evaluated at iso-FLOP and iso-step checkpoints.
- **Evaluation Hazards**:
  - Learning rate schedule truncation artifacts (e.g. testing loss before cosine decay completion).
  - Comparing optimizers with unequal hyperparameter tuning budgets (momentum, weight decay, warmup).

## SOTA Landscape
For over a decade, Adam and AdamW served as the default standard for deep learning optimization. Starting in late 2024 and 2025, matrix-orthogonalizing momentum optimizers such as **Muon** (Momentum Orthogonalized by Newton-Schulz) have demonstrated substantial speedups (up to 2x step-efficiency) over AdamW on 2D matrix weights in transformer backbones.
