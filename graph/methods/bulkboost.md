---
id: method:bulkboost
type: method
title: "BulkBoost"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "BulkBoost is two-band spectral reweight on Muon; Muon2 remains the 7B default"
    use_instead: "method:muon2"
  - when: "clipping Muon momentum singular values instead of two-band reweight"
    reason: "Musec clips; BulkBoost reweights two MP-calibrated bands"
    use_instead: "method:musec"
  - when: "temporary strong soft-orthogonality then remove"
    reason: "ORCA is a cooled regularizer, not a spectral reweight"
    use_instead: "method:orca"
assumptions:
  - "Muon-type matrix momentum on 2D weights. Paper: Pythia 14M–410M. Fine-grained spectral maps (Freon) are the weaker baseline."
  - "No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:bulkboost
recipes:
  - recipe:bulkboost
claims:
  - benchmark: "Pythia 14M–410M, Muon spectral reweight"
    metric: "loss reduction vs Muon flat"
    value: "0.073–0.147%"
    baseline: "Muon flat; Freon 0.022%"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07497"
    notes: "Two-band Marchenko–Pastur noise-calibrated reweight. Argues fine-grained maps are unnecessary. Does not replace Muon2."
tags:
  - optimizer
  - muon
  - spectral
  - bulkboost
  - active
---

# BulkBoost

## Method Overview
Two-band, Marchenko–Pastur noise-calibrated spectral reweighting of Muon momentum. The paper's claim is that fine-grained spectral maps are unnecessary once the bulk and spike bands are split.

## When to Use
- Muon-family runs where a spectral map is being considered and a two-band split is cheaper than a fine-grained kernel.

## When NOT to Use
- 7B default → `method:muon2`. Singular-value clip → `method:musec`. Cooled orthogonality → `method:orca`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-07.
- Pythia 14M–410M is not a 7B FineWeb bake-off.
