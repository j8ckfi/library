---
id: method:lora-unified-study
type: method
title: "Unified LoRA Rank Scaling"
category: "peft"
status: active
papers:
  - paper:lora-unified-study
recipes:
  - recipe:lora-unified-study
claims:
  - benchmark: "LoRA Variant Benchmark Suite"
    metric: "rank scaling consistency"
    value: "Consistent rank scaling across model scales"
    baseline: "Standard LoRA"
    date: "2026-08-26"
    verified: true
    notes: "Empirical scaling laws for adapter rank and learning rate."
tags:
  - peft
  - lora
  - scaling-laws
---

# Unified LoRA Rank Scaling

## Method Overview
Unified empirical scaling laws establishing stable rank selection, alpha scaling, and learning rate transfer across base model architectures.

## When to Use
- Determining adapter rank and hyperparameter search grids for new base models.
