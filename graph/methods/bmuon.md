---
id: method:bmuon
type: method
title: 'BMuon'
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains the 7B default; BMuon budgets Muon geometry for structured MLP prune'
  use_instead: method:muon2
- when: 'subspace / residual-correction memory pretrain (SCALE / PMRC)'
  reason: 'BMuon is a spectral-geometry prune budget on Muon, not a subspace optimizer'
  use_instead: method:scale
assumptions:
- 'Muon-family trainer. Paper: ViT-S/16 ImageNet and 1B LLaMA-style FineWeb; inter-block channel budget.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:bmuon
recipes:
- recipe:bmuon
claims:
- benchmark: '1B LLaMA-style FineWeb MLP channel prune; ViT-S/16 ImageNet structured MLP prune'
  metric: 'post-prune quality vs Muon'
  value: 'BMuon improves over Muon under post-training MLP channel pruning (1B) and gradual structured MLP prune (ViT-S/16)'
  baseline: 'Muon (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23571'
  notes: 'Does not retarget Muon2. No SCALE bake-off.'
tags:
- optimizer
- muon
- pruning
- active
---

# BMuon

## Method Overview
Budget Muon interpolates Muon's spectral-norm steepest descent toward structured sparse geometries so hidden channels across blocks compete for a shared allocation budget. The practical surrogate is a minorization-maximization allocation rather than a sparsity-penalty coefficient.

## When to Use
- Pretraining with Muon when you will prune MLP hidden channels after training and want the optimizer geometry to stay compressible.

## When NOT to Use
Default ~7B pretrain → `method:muon2`. Memory subspace FT → `method:scale`.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** replace Muon2.

## Gotchas & Failure Modes
- No public code.
- Gains are post-prune quality, not a FineWeb 7B bake-off against Muon2.
