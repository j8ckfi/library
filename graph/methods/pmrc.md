---
id: method:pmrc
type: method
title: PMRC (Projected Muon Residual Correction)
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: choosing the memory-efficient full-parameter first hop
  reason: SCALE remains subspace-projection SOTA; PMRC is residual-correction Muon, no head-to-head
  use_instead: method:scale
- when: choosing the ~7B dense pretrain optimizer
  reason: Muon2 remains the 7B default
  use_instead: method:muon2
assumptions:
- Optimizer states in a low-rank SVD subspace plus residual gradient in the orthogonal complement. Paper: LLaMA C4 60M-1.3B; SMRC is the momentum-SGD sibling.
- Host gist OptimAI-Lab/Minimalist_LLM_Pretraining; no dedicated PMRC repo as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:pmrc
recipes:
- recipe:pmrc
claims:
- benchmark: LLaMA C4 1.3B pretrain (20480 steps, ~26.84B tokens)
  metric: train / val loss vs GaLore / Fira
  value: train 2.500 vs Fira 2.657 vs GaLore 2.842; val 2.570 vs Fira 2.730 vs GaLore 2.875
  baseline: GaLore, Fira, GUM (single-paper; no SCALE bake-off)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19844
  notes: Does not retarget SCALE or Muon2.
tags:
- optimizer
- memory-efficient
- muon
- active
---

# PMRC (Projected Muon Residual Correction)

## Method Overview
Keep optimizer state in a leading singular subspace and add the orthogonal residual gradient to the update. SMRC does this for momentum SGD. PMRC applies the matrix sign to the projected momentum (Muon). Multi-stage variants refresh the basis and apply a boundary correction so virtual iterates stay consistent.

## When to Use
- Full-param pretrain where GaLore-style subspaces lose the residual and you want a Muon update in the projected coordinates.

## When NOT to Use
Memory-efficient first hop → `method:scale`. ~7B optimizer → `method:muon2`.

## Relation to Existing SOTA
Active plug-in on `task:full-param-memory-efficient-pretrain` (`sota_for: []`). No SCALE bake-off. Does **not** replace SCALE.

## Gotchas & Failure Modes
- **code: none** dedicated as of 2026-10-15 (experiments sit on OptimAI-Lab/Minimalist_LLM_Pretraining).
- Full-space Muon still has lower 1.3B train loss (2.414) than PMRC (2.500).
