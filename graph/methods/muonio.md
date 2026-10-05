---
id: method:muonio
type: method
title: "MuonIO"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Muon2 remains the hidden-layer / 7B default; MuonIO only replaces AdamW on embeddings and the LM head"
    use_instead: "method:muon2"
  - when: "full-param FT optimizer-state memory (ternary column-wise one-sparse)"
    reason: "TACO is an FT memory geometry, not an I/O-layer Muon update"
    use_instead: "method:taco"
  - when: "Muon spectral-clip of hidden-layer momentum singular values"
    reason: "Musec clips hidden Muon momentum; MuonIO changes I/O layer geometry"
    use_instead: "method:musec"
assumptions:
  - "Muon or Polar Express already updates hidden matrices. Embeddings are one-hot; the LM head feeds softmax."
  - "Paper: 60M / 130M / 1B C4 val PPL. I/O FLOPs 7Vd+3V vs AdamW 13Vd; state Vd vs 2Vd."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:muonio
recipes:
  - recipe:muonio
claims:
  - benchmark: "C4 val PPL, 60M / 130M / 1B"
    metric: "validation perplexity"
    value: "28.366 / 23.617 / 14.374"
    baseline: "Muon Tuned 28.502 / 24.238 / 14.527; Plain Muon 36.963 / 28.513 / 15.116"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02705"
    notes: "Table 1. Does not retarget Muon2 as the ~7B hidden-layer default."
  - benchmark: "C4 val PPL, Polar Express IO 1B"
    metric: "validation perplexity"
    value: "14.160"
    baseline: "Polar Express Tuned 14.361"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02705"
    notes: "Same I/O geometry on a Polar Express hidden-layer host."
  - benchmark: "I/O matrix optimizer cost, one V×d update"
    metric: "FLOPs / optimizer-state entries"
    value: "7Vd+3V FLOPs / Vd state"
    baseline: "AdamW 13Vd FLOPs / 2Vd state"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02705"
    notes: "Table 3 / Appendix C. ~50% I/O optimizer state vs AdamW."
tags:
  - pretraining
  - optimizer
  - muon
  - embeddings
  - muonio
  - active
---

# MuonIO

## Method Overview
Muon2 still orthogonalizes hidden matrices. Keep that. MuonIO replaces the usual AdamW split on the embedding table \(\mathbf{E}\in\mathbb{R}^{d\times V}\) and LM head \(\mathbf{L}\in\mathbb{R}^{V\times d}\): \(1\to 2\) column-norm steepest descent on embeddings (one-hot inputs) and \(2\to\infty\) row-norm descent on the head (softmax Lipschitz). Polar Express IO is the same I/O geometry when Polar Express is the hidden host.

## When to Use
- Configuring Muon's non-hidden layers instead of AdamW on embeddings / `lm_head`.

## When NOT to Use
- ~7B hidden-layer optimizer → `method:muon2`. FT sparse optimizer state → `method:taco`. Hidden momentum spectral clip → `method:musec`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` and `task:pretrain-dense-7b` beside `method:muon2` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- Do not cite 60M–1B C4 PPL as a 7B FineWeb token-efficiency retarget of Muon2.
- Ember in the paper table is not a library method.
