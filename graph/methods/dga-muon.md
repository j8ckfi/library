---
id: method:dga-muon
type: method
title: "DGA-Muon"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "DGA-Muon is a NorMuon-geometry fix, not a Muon2 replacement"
    use_instead: "method:muon2"
  - when: "scale-free LR transfer across widths"
    reason: "SF-NorMuon remains the scale-free transfer card; DGA-Muon decouples NorMuon-style adaptive scaling"
    use_instead: "method:sf-normuon"
assumptions:
  - Host is Muon / NorMuon. Paper analyzes NorMuon adaptivity under exact vs approximate orthogonalization.
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:dga-muon
recipes:
  - recipe:dga-muon
claims:
  - benchmark: "NorMuon vs DGA-Muon (paper empirical validation)"
    metric: "optimizer quality vs NorMuon"
    value: "superior to NorMuon (abstract; no numeric table)"
    baseline: "NorMuon"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06578"
    notes: "Does not retarget Muon2 or SF-NorMuon. Do not invent a loss table."
tags:
  - pretraining
  - optimizer
  - dga-muon
  - active
---

# DGA-Muon

## Method Overview
DGA-Muon (Decoupled Geometry-Aligned Muon) computes adaptive scales from raw gradients instead of the orthogonalized update, and uses row-wise scales on wide matrices and column-wise scales on tall ones. That is the paper's fix for NorMuon's Orthogonalization–Adaptivity Paradox.

## When to Use
- Muon/NorMuon pretrain where you want adaptive scaling that is not an orthogonalization artifact.

## When NOT to Use
- Default 7B optimizer → `method:muon2`. Scale-free LR transfer → `method:sf-normuon`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` beside `method:sf-normuon` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2 or SF-NorMuon.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Abstract has no numeric bake-off table; do not invent one.
- SF-NorMuon is scale-free transfer, not this geometry diagnosis.
