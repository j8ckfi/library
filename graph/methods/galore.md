---
id: method:galore
type: method
title: "GaLore (Gradient Low-Rank Projection)"
category: "optimizer"
status: superseded
superseded_by: method:scale
sota_for: []
supersedes: []
papers:
  - paper:galore
recipes:
  - recipe:galore-training
claims:
  - benchmark: "Full-Parameter 7B Pretraining & Fine-Tuning on 24GB GPU"
    metric: "memory reduction"
    value: "Up to 65.5% optimizer memory reduction"
    baseline: "Full-Rank AdamW"
    date: "2024-03"
    verified: true
    notes: "Projects gradient matrices into compact low-rank subspaces during optimization, maintaining full-rank weight updates."
tags:
  - optimizer
  - peft
  - memory-efficient
  - galore
---

# GaLore (Gradient Low-Rank Projection)

## Method Overview
GaLore projects weight gradient matrices into compact low-rank subspaces via periodic SVD updates.

## Supersession
- Superseded by `method:scale` (2506.16659, ICML 2026) for memory-efficient full-parameter pretraining.
