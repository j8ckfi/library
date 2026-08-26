---
id: method:delora
type: method
title: "DeLoRA (Decoupled Low-Rank Adaptation)"
category: "peft"
status: sota
sota_for:
  - task:parameter-efficient-fine-tuning
supersedes:
  - method:dora
papers:
  - paper:delora
recipes:
  - recipe:delora-finetuning
claims:
  - benchmark: "Commonsense Reasoning & Long-Horizon Fine-Tuning"
    metric: "Frobenius stability & accuracy"
    value: "Superior stability on long/LR-sensitive fine-tuning runs"
    baseline: "DoRA & LoRA"
    date: "2025-03"
    verified: true
    notes: "Bounds the Frobenius norm update to prevent gradient divergence across long fine-tuning runs."
tags:
  - peft
  - low-rank
  - delora
---

# DeLoRA (Decoupled Low-Rank Adaptation)

## Method Overview
DeLoRA bounds the Frobenius norm of low-rank adapter updates, decoupling parameter updates across layers to ensure robust training stability across wide learning rate sweeps and extended multi-epoch fine-tuning runs.

## Supersession
- Supersedes `method:dora` for long, learning-rate-sensitive training runs.
