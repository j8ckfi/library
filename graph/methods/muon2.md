---
id: method:muon2
type: method
title: "Muon2 Optimizer"
category: "optimizer"
status: sota
sota_for:
  - task:pretrain-dense-7b
  - task:llm-pretraining-optimization
supersedes:
  - method:muon
  - method:muon-scalable
papers:
  - paper:muon2
recipes:
  - recipe:muon2-pretraining
claims:
  - benchmark: "Dense 7B Pretraining / FineWeb"
    metric: "token efficiency & step stability"
    value: "~2x token efficiency vs AdamW with improved stability"
    baseline: "Muon / AdamW"
    date: "2026-08-26"
    verified: true
    notes: "Second-generation matrix orthogonalization optimizer with refined Newton-Schulz iterations."
tags:
  - optimizer
  - pretraining
  - muon2
  - sota
---

# Muon2 Optimizer

## Method Overview
Muon2 is a second-generation matrix orthogonalization momentum optimizer designed for deep transformer layers. It applies accelerated Newton-Schulz polynomial iterations to orthogonalize gradient momentum matrices, enforcing optimal spectral norm properties during parameter updates.

## When to Use
- Default SOTA optimizer for pretraining dense 7B language models from scratch.
- Hidden matrix layers in multi-layer perceptrons and attention projections. Keep embeddings and `lm_head` on AdamW.

## Gotchas & Failure Modes
- Embedding tables, 1D vectors, and normalization scale factors should be optimized with standard AdamW rather than matrix orthogonalization.
- **MuonH** (Muon + hyperball; used in `method:puro-2b`) wraps scale-invariant 2D attn/MLP matrices, projects each back to $R=\|W_0\|_F$ after the step, and runs Hyperball LR at $10\times$ the AdamW base. It is a documented Muon/Muon2-family variant for consumer-GPU ~2B pretrain. It does **not** change this method's `sota_for`: dense ~7B still uses Muon2 (+ KL-SOAP if memory allows).
