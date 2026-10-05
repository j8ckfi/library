---
id: paper:muonio
type: paper
title: "MuonIO: Principled Norm-Aware Descent for Embedding Tables and Language Model Heads"
authors:
  - "Linkai Ma"
  - "Xinyu Luo"
  - "Mengbo Wang"
  - "Ananth Grama"
  - "Petros Drineas"
  - "Brian Bullins"
year: 2026
month: 10
arxiv_id: "2610.02705"
url: "https://arxiv.org/abs/2610.02705"
methods:
  - method:muonio
cites:
  - paper:muon2
tags:
  - pretraining
  - optimizer
  - muon
  - embeddings
  - lm-head
---

# MuonIO: Principled Norm-Aware Descent for Embedding Tables and Language Model Heads

## Abstract Summary
Standard Muon orthogonalizes hidden linear layers under a spectral-norm / RMS-stability argument, but implementations still run AdamW on the embedding table and language-model head. MuonIO gives those I/O matrices a Muon-style norm-aware update: \(1\to 2\) column geometry on embeddings (one-hot inputs) and \(2\to\infty\) row geometry on the LM head (softmax Lipschitz). Polar Express IO is the same geometry on a Polar Express hidden-layer host. Active plug-in beside Muon2; embeddings / `lm_head` no longer default to AdamW when this geometry is in scope. No public code as of 2026-10-05.

## Key Contributions
1. **I/O norms**: embedding \(1\to 2\); LM head \(2\to\infty\); both are Muon-style steepest descent, not AdamW.
2. **Cost**: I/O FLOPs \(7Vd+3V\) vs AdamW \(13Vd\); optimizer state \(Vd\) vs \(2Vd\).
3. **C4 val PPL**: 60M / 130M / 1B MuonIO 28.366 / 23.617 / 14.374 vs Muon Tuned 28.502 / 24.238 / 14.527.

## Empirical Highlights
- Polar Express IO 1B 14.160 vs Polar Express Tuned 14.361.
- Ember is a named I/O baseline in the table, not a library method.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02705`
- Code: none found as of 2026-10-05 (`code_status: none`).
