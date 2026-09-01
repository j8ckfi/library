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
last_reviewed: "2026-09-01"
tags:
  - pretraining
  - dense-lm
  - optimizer
---

# Pretrain Dense ~7B Language Model from Scratch

## Problem Definition
Training a ~7B dense language model from scratch requires optimizing billions of parameters over trillions of tokens with maximal compute and wall-clock efficiency.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Optimizer**: **Muon2** (`method:muon2`, 2604.09967) + **KL-SOAP** (`method:soap-muon-scale`, 2607.20548) if GPU memory allows. Keep embeddings and `lm_head` on AdamW.
- **Data Recipe**: **OLMo-3 / Dolma-3** (`paper:olmo-3`, 2512.13961).
- **Not this scale**: ~1.5-2B on consumer GPUs / tight budget is `method:puro-2b` (`task:budget-consumer-pretrain`), not this 7B default.
- **Adjacent hybrid residual / Qwen-style production architecture**: `method:qwen38-next`. Does not replace Muon2 as the 7B optimizer.
