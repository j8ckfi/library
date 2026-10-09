---
id: method:spectrally-targeted-muon
type: method
title: "Spectrally Targeted Muon"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Spectrally Targeted Muon is a Muon ablation/plug-in; Muon2 remains the 7B default"
    use_instead: "method:muon2"
  - when: "two-band Marchenko-Pastur spectral reweighting for Muon"
    reason: "BulkBoost reweights two MP bands; this method thresholds which singular values get orthogonalized"
    use_instead: "method:bulkboost"
  - when: "clipping Muon momentum singular values instead of flattening them"
    reason: "Musec clips; Spectrally Targeted Muon interpolates via a tau threshold"
    use_instead: "method:musec"
assumptions:
  - "Muon-type matrix momentum on 2D weights. Paper: CIFAR-10 and NanoGPT speedruns."
  - "No official GitHub as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:spectrally-targeted-muon
recipes:
  - recipe:spectrally-targeted-muon
claims:
  - benchmark: "CIFAR-10 and NanoGPT speedruns, thresholded vs full Muon orthogonalization"
    metric: "whether small momentum singular values are the Muon gain"
    value: "orthogonalizing all but the few largest nearly matches Muon; top-only orthogonalization does not"
    baseline: "full Muon orthogonalization; normalized SGD"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.10965"
    notes: "Mechanism plug-in, not a 7B bake-off. Does not retarget Muon2." 
tags:
  - optimizer
  - muon
  - spectral
  - spectrally-targeted-muon
  - active
---

# Spectrally Targeted Muon

## Method Overview
Orthogonalize only the singular values of the momentum update that sit above or below a threshold tau. Isolate those subspaces with Newton-Schulz on a shifted Gram matrix. Varying tau interpolates normalized SGD and Muon. On LMs, amplify the small directions; shrinking the largest singular values is cheap spectral hygiene, not the loss driver.

## When to Use
- Diagnosing or cheapening Muon orthogonalization, or when you want a continuous interpolation to normalized SGD.

## When NOT to Use
- 7B default -> `method:muon2`. Two-band MP reweight -> `method:bulkboost`.

## Relation to Existing SOTA
- Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-09.
- On LMs every momentum singular value is far below one; targeting only the top will under-train.
