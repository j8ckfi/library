---
id: method:hymuon
type: method
title: 'HyMUON'
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains the hidden-layer default; HyMUON orthogonalizes a hybrid linear-plus-EMA momentum'
  use_instead: method:muon2
assumptions:
- 'Hybrid Momentum (linearly weighted history plus fast EMA) with Newton-Schulz on the hybrid direction.'
- 'Paper: IWSLT14, GPT-2 124M OpenWebText, LLaMA-1.3B C4. No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:hymuon
recipes:
- recipe:hymuon
claims:
- benchmark: 'IWSLT14; GPT-2 124M OpenWebText 100k/600k; LLaMA-1.3B C4 val loss'
  metric: 'translation / LM quality vs Muon; C4 val loss'
  value: 'HyMUON improves over Muon on IWSLT14 and both GPT-2 OpenWebText regimes; LLaMA-1.3B C4 val 2.777 vs Muon 2.903'
  baseline: 'Muon'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27674'
  notes: 'No 7B bake-off. Does not retarget Muon2.'
tags:
- optimizer
- muon
- momentum
- active
---

# HyMUON

## Method Overview
Hybrid Momentum (HyM) mixes a linearly weighted growing-history average with a fast EMA. HyMUON applies Newton-Schulz orthogonalization to that hybrid direction instead of to a single EMA.

## When to Use
- Muon-family pretrain where a single EMA timescale underweights older gradients.

## When NOT to Use
Default ~7B optimizer → `method:muon2`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:muon2`.

## Gotchas & Failure Modes
- Scale is 1.3B, not 7B.
- Linear history buffer grows with steps.
