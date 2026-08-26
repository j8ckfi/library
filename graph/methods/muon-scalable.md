---
id: method:muon-scalable
type: method
title: "Scalable Muon (Moonlight)"
category: "optimizer"
status: sota
sota_for:
  - task:pretrain-dense-7b
supersedes:
  - method:muon
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

## When to Use
- Default optimizer when training ~7B dense language models from scratch.
- ~2x more token-efficient than AdamW under empirical scaling laws.

## Supersession
- Supersedes raw `method:muon` defaults at LLM scale.
- Superseded at trillion-token MoE scale by `method:muonclip-kimi-k2`.
