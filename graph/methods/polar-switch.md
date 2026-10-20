---
id: method:polar-switch
type: method
title: 'Polar Switch'
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains the hidden-layer default; Polar Switch is a faster polar-factor polynomial'
  use_instead: method:muon2
- when: 'two-band MP spectral reweight rather than polynomial circuits'
  reason: 'BulkBoost reweights singular values; Polar Switch changes the orthogonalization circuit'
  use_instead: method:bulkboost
assumptions:
- 'Drop-in Muon orthogonalizer. Paper: Modded-NanoGPT #91, Qwen3-0.6B, Gemma 3-1B.'
- 'Code zhehangdu/polar-switch as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:polar-switch
recipes:
- recipe:polar-switch
claims:
- benchmark: 'Polar Express / Gram Newton-Schulz GPU runtime; NanoGPT / Qwen3-0.6B / Gemma 3-1B pretrain'
  metric: 'orthogonalization runtime; final val loss vs established polar methods'
  value: '15.5-18.7% lower runtime vs Polar Express on squares; 8.6-16.2% vs Gram NS on aspect 3.25/3.5/8; similar final val loss'
  baseline: 'Polar Express; Gram Newton-Schulz'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.26742'
  notes: 'Does not retarget Muon2. Polynomial circuits of degree up to 2^{k+1}+1.'
tags:
- optimizer
- muon
- orthogonalization
- active
---

# Polar Switch

## Method Overview
Polar Switch orthogonalizes Muon momentum with polynomial circuits: a short sequence of symmetric matrix products on a few square buffers, reaching a given odd polynomial degree at lower FLOP cost than quintic Newton-Schulz / Polar Express iterations.

## When to Use
- Implementing Muon-family pretrain and the polar-factor kernel is the step cost.

## When NOT to Use
Default ~7B optimizer → `method:muon2`.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** replace Muon2.

## Gotchas & Failure Modes
- Coefficients are designed, not the classical Newton-Schulz cubic.
- No 7B bake-off.
