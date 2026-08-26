---
id: task:pretrain-dense-7b
type: task
title: "Pretrain Dense ~7B Language Model from Scratch"
domain: "pretraining"
summary: "Pretraining a dense ~7B parameter transformer language model from scratch targeting maximum token efficiency and loss reduction."
current_sota:
  - method: method:muon-scalable
    as_of: "2026-08-26"
    benchmark: "Moonlight Scaling Laws / FineWeb Token Mix"
    metric: "token efficiency"
    value: "~2x token efficiency vs AdamW"
    notes: "Muon with Moonshot scale-up fixes: weight decay + per-parameter update-RMS matching. If GPU memory allows and big batch, KL-SOAP is recommended."
methods:
  - method:muon-scalable
  - method:muon
  - method:soap-muon-scale
  - method:adamw-optimizer
tags:
  - pretraining
  - dense-lm
  - optimizer
---

# Pretrain Dense ~7B Language Model from Scratch

## Problem Definition
Training a ~7B dense language model from scratch requires optimizing billions of parameters over trillions of tokens with maximal compute and wall-clock efficiency.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Optimizer**: Use **Muon** (`method:muon-scalable`) with Moonshot's two scale-up fixes: weight decay + per-parameter update-RMS matching. Keep embeddings and `lm_head` on AdamW.
- **Large-Batch / High-Memory Alternative**: If GPU memory is not the bottleneck and you can pay SOAP's extra state, NVIDIA's Jul-2026 Megatron study recommends **KL-SOAP** (`method:soap-muon-scale`) over Muon at large batch (up to ~100M tokens).
- **Architecture**: Dense Llama-like architecture is the open default.
- **Data Recipe**: Two-stage OLMo-2 curriculum (`paper:olmo-2-curriculum`): broad web mix, then high-quality anneal / Dolmino-style soup. Do not Chinchilla-copy an AdamW token budget—Muon is ~2x more token-efficient in Moonshot's scaling laws.
