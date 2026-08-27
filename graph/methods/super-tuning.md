---
id: method:super-tuning
type: method
title: "Super-Tuning (Subspace-Preserving Adaptation)"
category: "peft"
status: active
papers:
  - paper:super-tuning
recipes:
  - recipe:super-tuning
claims:
  - benchmark: "OOD Robustness Benchmark"
    metric: "out-of-distribution retention"
    value: "Preserves base model representation subspace"
    baseline: "Standard LoRA"
    date: "2026-08-26"
    verified: true
    notes: "Subspace-constrained low-rank parameter updates."
tags:
  - peft
  - subspace
  - super-tuning
---

# Super-Tuning (Subspace-Preserving Adaptation)

## Method Overview
Super-Tuning constrains adapter updates to remain within the principal spectral subspace of the pre-trained weights, avoiding representational drift.

## When to Use
- Fine-tuning where out-of-distribution robustness and retention of broad pre-trained world knowledge are essential.
