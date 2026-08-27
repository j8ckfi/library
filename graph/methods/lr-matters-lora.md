---
id: method:lr-matters-lora
type: method
title: "Vanilla LoRA + rsLoRA + LR Sweep"
category: "peft"
status: sota
sota_for:
  - task:parameter-efficient-fine-tuning
  - task:lora-quality-tuning
supersedes:
  - method:dora
  - method:delora
papers:
  - paper:lr-matters-lora
  - paper:lora-unified-study
recipes:
  - recipe:lr-matters-lora
claims:
  - benchmark: "MMLU / GSM8k / GLUE Fine-Tuning"
    metric: "accuracy vs parameter overhead"
    value: "Matches/exceeds DoRA without magnitude parameter overhead"
    baseline: "DoRA / DeLoRA / Vanilla LoRA"
    date: "2026-08-26"
    verified: true
    notes: "Vanilla LoRA with rank-stabilized scaling (rsLoRA, alpha/sqrt(r)) and calibrated learning rate sweep."
tags:
  - peft
  - lora
  - rslora
  - sota
---

# Vanilla LoRA + rsLoRA + LR Sweep

## Method Overview
Re-evaluating low-rank adaptation reveals that with rank-stabilized scaling (\(\alpha / \sqrt{r}\)) and proper learning rate sweeping, standard vanilla LoRA achieves equal or superior accuracy compared to Weight-Decomposed LoRA (DoRA), without the VRAM memory overhead and runtime complexity of magnitude normalization.

## When to Use
- Default SOTA quality choice for 24GB single-GPU parameter-efficient fine-tuning (NOT DoRA).

## Supersession
- Supersedes `method:dora` and `method:delora` as the PEFT quality default.
