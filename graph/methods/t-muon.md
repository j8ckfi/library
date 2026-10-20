---
id: method:t-muon
type: method
title: 'T-MUON'
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'T-MUON is a t-SVD grouping of Muon updates, not a 7B bake-off'
  use_instead: method:muon2
assumptions:
- 'Groups structurally related Transformer gradients into third-order tensors. Paper: GPT-2 / LLaMA-style 51M-1.3B FineWeb / FineWeb-Edu.'
- 'No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:t-muon
recipes:
- recipe:t-muon
claims:
- benchmark: 'GPT-2-style and LLaMA-style 51M-1.3B FineWeb / FineWeb-Edu'
  metric: 'validation perplexity vs AdamW / Muon / DFT-DCT-DST t-Muon'
  value: 'head-wise t-Muon with identity transform lowest val PPL among compared variants'
  baseline: 'AdamW; Muon; DFT/DCT/DST t-Muon'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24938'
  notes: 'Exact T-MUON update is steepest descent under star_M-spectral norm. Does not retarget Muon2.'
tags:
- optimizer
- muon
- t-svd
- active
---

# T-MUON

## Method Overview
T-MUON stacks structurally related matrix gradients into third-order tensors and applies a Muon-style update through the M-transform / t-SVD rather than unfolding tensors into independent matrices.

## When to Use
- Muon pretrain where attention-head (or other structured) grouping is available and you want a tensor polar update.

## When NOT to Use
Default ~7B optimizer → `method:muon2`.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** replace Muon2.

## Gotchas & Failure Modes
- Identity M-transform won in the paper; DFT/DCT/DST variants lagged.
- Scale is 1.3B, not 7B.
