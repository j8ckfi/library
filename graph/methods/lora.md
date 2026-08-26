---
id: method:lora
type: method
title: "LoRA (Low-Rank Adaptation)"
category: "peft"
status: active
superseded_by: method:dora
sota_for: []
supersedes: []
papers:
  - paper:lora-paper
recipes: []
claims:
  - benchmark: "GPT-3 175B / RoBERTa GLUE"
    metric: "accuracy"
    value: "Parity with full fine-tuning"
    baseline: "Full Model Fine-Tuning"
    date: "2021-06"
    verified: true
    notes: "Injected low-rank decomposition matrices into attention projections."
tags:
  - peft
  - baseline
---

# LoRA (Low-Rank Adaptation)

## Method Overview
LoRA freezes the pre-trained model weights \(W_0 \in \mathbb{R}^{d \times k}\) and injects trainable rank decomposition matrices \(\Delta W = B \cdot A\), where \(B \in \mathbb{R}^{d \times r}\) and \(A \in \mathbb{R}^{r \times k}\) with rank \(r \ll \min(d, k)\).

## When to Use
- Standard lightweight fine-tuning baseline across audio, vision, and language models.

## Gotchas & Failure Modes
- Couples directional and magnitude updates, causing sub-optimal capacity at small ranks (\(r \leq 8\)).
