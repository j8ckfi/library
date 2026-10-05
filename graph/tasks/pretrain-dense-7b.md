---
id: task:pretrain-dense-7b
type: task
title: "Pretrain Dense ~7B Language Model from Scratch"
domain: "pretraining"
summary: "Pretraining a dense ~7B parameter transformer language model from scratch targeting maximum token efficiency and loss reduction."
current_sota:
  - method: method:muon2
    as_of: "2026-08-26"
    benchmark: "Moonlight Scaling Laws / FineWeb Token Mix"
    metric: "token efficiency"
    value: "~2x token efficiency vs AdamW"
    notes: "Muon2 (2604.09967) + KL-SOAP (2607.20548) if memory allows."
redirects:
  - when: "latent-space / next-concept LM architecture rather than dense NTP 7B"
    to: "task:latent-space-lm-pretrain"
  - when: "fully synthetic single-stage LLM pretraining from Wikipedia/Wikibooks seeds"
    to: "task:synthetic-single-stage-pretrain"
  - when: "zero-natural-data self-play pretraining (UTM programs, no natural text)"
    to: "task:zero-natural-data-self-play-pretrain"
  - when: "Muon-style norm-aware update for embedding tables (1->2) and LM head (2->inf) instead of AdamW"
    to: "method:muonio"
methods:
  - method:muon2
  - method:soap-muon-scale
  - method:muon-scalable
  - method:muon
  - method:mona
  - method:htmuon
  - method:variance-adaptive-muon
  - method:sf-normuon
  - method:newton-muon
  - method:nemotron-3-nano
  - method:adamw-optimizer
  - method:qwen38-next
  - method:layer-dropout
  - method:optimizer-memory-schedules
  - method:musec
  - method:ncp-archpreview
  - method:synth
  - method:self-play-pretraining
  - method:muonio
last_reviewed: "2026-10-05"
tags:
  - pretraining
  - dense-lm
  - optimizer
---

# Pretrain Dense ~7B Language Model from Scratch

## Problem Definition
Training a ~7B dense language model from scratch requires optimizing billions of parameters over trillions of tokens with maximal compute and wall-clock efficiency.

## SOTA Recommendation (as of 2026-09-08)
- **Primary Optimizer**: **Muon2** (`method:muon2`, 2604.09967) + **KL-SOAP** (`method:soap-muon-scale`, 2607.20548) if GPU memory allows. Default I/O layers stay AdamW; optional `method:muonio` (`arXiv:2610.02705`) for embedding \(1\to 2\) / LM-head \(2\to\infty\). Unchanged hidden-layer default.
- **Data Recipe**: **OLMo-3 / Dolma-3** (`paper:olmo-3`, 2512.13961).
- **Not this scale**: ~1.5-2B on consumer GPUs / tight budget is `method:puro-2b` (`task:budget-consumer-pretrain`), not this 7B default.
- **Adjacent hybrid residual / Qwen-style production architecture**: `method:qwen38-next`. Does not replace Muon2 as the 7B optimizer.
- **Optional layer sparsity**: `method:layer-dropout` (`arXiv:2609.05275`). Does not replace Muon2.
- **OT-horizon HP guidance**: `method:optimizer-memory-schedules` (`arXiv:2609.04577`). 51M–253M study; do not retarget this 7B optimizer.
- **Optional Muon stability plug-in**: `method:musec` (`arXiv:2609.11655`). Does not replace Muon2.
- **Latent-space LM architecture (not this task)**: `method:ncp-archpreview` on `task:latent-space-lm-pretrain`.
- **Fully synthetic single-stage pretrain (not this 7B web/open NTP)**: `method:synth` on `task:synthetic-single-stage-pretrain`. Baguettotron-600M is 594M on SYNTH, not a 7B Dolma run.
- **Zero-natural-data self-play pretrain (not this task)**: `method:self-play-pretraining` on `task:zero-natural-data-self-play-pretrain`.
