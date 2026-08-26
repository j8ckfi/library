---
id: method:muon
type: method
title: "Muon Optimizer"
category: "optimizer"
status: sota
sota_for:
  - task:llm-pretraining-optimization
supersedes:
  - method:adamw-optimizer
papers:
  - paper:muon-optimizer-paper
  - paper:muon-scalable
  - paper:muon2
recipes:
  - recipe:muon-pretraining
claims:
  - benchmark: "FineWeb-Edu NanoGPT (1.5B tokens)"
    metric: "validation loss"
    value: 3.21
    baseline: "AdamW (3.28 at equal steps, 2x wallclock training time)"
    date: "2025-02"
    verified: true
    notes: "Applied to 2D matrix weights (hidden layers); embeddings and 1D norms remain on AdamW."
tags:
  - optimizer
  - pretraining
  - orthogonalization
---

# Muon Optimizer

## Method Overview
Muon (Momentum Orthogonalized by Newton-Schulz) computes matrix-orthogonalized parameter updates for 2D hidden layer weight matrices using a hardware-efficient Newton-Schulz polynomial iteration.

## When to Use
- Transformer 2D internal linear layers.
- Native in PyTorch since 2.9 (`torch.optim.Muon`).

## Supersession
- Supersedes `method:adamw-optimizer` for hidden matrix parameters.
- Superseded at LLM scale by `method:muon-scalable`.
