---
id: method:tulu3-rlvr
type: method
title: "Tülu-3 Stack (SFT -> On-Policy DPO -> RLVR)"
category: "rl-alignment"
status: superseded
superseded_by: method:olmo-3
sota_for: []
supersedes:
  - method:ppo-rlhf
papers:
  - paper:tulu3-rlvr
recipes:
  - recipe:simpo-alignment
claims:
  - benchmark: "AlpacaEval 2 / Arena-Hard / IFEval / GSM8k"
    metric: "open instruction benchmark average"
    value: "Leading Open Post-Training Stack"
    baseline: "RM-only RLHF / Llama 3.1 Post-Training"
    date: "2024-11"
    verified: true
    notes: "Curated SFT -> on-policy DPO -> RLVR (verifiable rewards without learned reward model noise)."
tags:
  - post-training
  - alignment
  - rlvr
  - tulu3
---

# Tülu-3 Stack (SFT -> On-Policy DPO -> RLVR)

## Method Overview
The Tülu-3 post-training pipeline is the historical 2024 open-source recipe for creating high-capability chat and instruct models.

## Supersession
- Superseded by `method:olmo-3` (Dolci stack) for open instruction alignment.
