---
id: method:muon-scalable
type: method
title: "Scalable Muon (Moonlight)"
category: "optimizer"
status: superseded
superseded_by: method:muon2
sota_for: []
supersedes:
  - method:muon
  - method:muon-optimizer
papers:
  - paper:muon-scalable
recipes:
  - recipe:muon-pretraining
claims:
  - benchmark: "Moonlight Scaling Laws / 7B Dense LM"
    metric: "token efficiency"
    value: "~2x token efficiency vs AdamW"
    baseline: "AdamW"
    date: "2025-02"
    verified: true
    notes: "Adds weight decay and per-parameter update-RMS matching to scale Muon to multi-billion parameter dense models."
tags:
  - optimizer
  - pretraining
  - scale-up
---

# Scalable Muon (Moonlight)

## Method Overview
Moonlight's Scalable Muon introduces two essential fixes enabling Muon to scale reliably to multi-billion parameter LLM pretraining:
1. **Decoupled Weight Decay**: Proper matrix-level weight decay.
2. **Per-Parameter Update-RMS Matching**: Calibrates the spectral update norm across layers of varying aspect ratios.

## Supersession
- Superseded by `method:muon2` as the primary pretraining optimizer implementation.
