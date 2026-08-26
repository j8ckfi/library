---
id: method:galore
type: method
title: "GaLore (Gradient Low-Rank Projection)"
category: "optimizer"
status: sota
sota_for:
  - task:parameter-efficient-fine-tuning
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
GaLore (Gradient Low-Rank Projection) projects weight gradient matrices \(G \in \mathbb{R}^{m \times n}\) into compact low-rank subspaces \(P^T G Q\) via periodic SVD updates. This allows tracking low-memory optimizer states in the projected space while maintaining full-rank parameter trajectory updates.

## When to Use
- Full-parameter pretraining or fine-tuning of 7B models on a single 24GB consumer GPU.
