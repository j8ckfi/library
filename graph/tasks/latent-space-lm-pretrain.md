---
id: task:latent-space-lm-pretrain
type: task
title: "Latent-Space Language Model Pretraining"
domain: "pretraining"
summary: "Pretrain an autoregressive LM that jointly predicts tokens and discrete multi-token concepts in a latent space built from hidden states, rather than NTP-only."
scope: "Latent-space / next-concept LM pretrain architecture (product-quantized concepts, concept module, joint NTP+NCP). Experimental first hop is NCP-ArchPreview."
out_of_scope:
  - "~7B dense NTP optimizer choice (Muon2)"
  - "Open pretrain mix / Dolma-3 recipe (OLMo-3)"
  - "Frontier MoE architecture (DeepSeek-V4 / Kimi-K3)"
  - "Diffusion-augmented AR serving (Uno)"
  - "Linear-time SSM sequence models (Mamba-2)"
redirects:
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "open pretrain mix / Dolma-3 recipe"
    to: "task:open-data-recipe"
  - when: "standard dense ~7B NTP from scratch"
    to: "task:pretrain-dense-7b"
  - when: "frontier MoE architecture"
    to: "task:pretrain-moe-frontier"
  - when: "lossless multi-token / diffusion-augmented AR serving"
    to: "task:diffusion-augmented-ar"
current_sota:
  - method: method:ncp-archpreview
    as_of: "2026-09-11"
    benchmark: "8.9B NCP-ArchPreview vs OLMo-3-7B on Dolma-3 / downstream macro"
    metric: "token efficiency + macro-average"
    value: "51.3% tokens to match OLMo-3-7B Stage-1 loss; +2.45 macro; +5.99 GSM8K"
    notes: "Experimental first hop for latent-space LM pretrain only (2609.10715). Does not replace Muon2 or OLMo-3."
methods:
  - method:ncp-archpreview
  - method:muon2
  - method:olmo-3
last_reviewed: "2026-09-11"
tags:
  - pretraining
  - architecture
  - latent-lm
  - ncp
---

# Latent-Space Language Model Pretraining

## Problem Definition
Train a language model that is still autoregressive at the token level but also predicts discrete multi-token concepts in a latent vocabulary derived from hidden states. This is not the 7B optimizer question and not the open-data mix question.

## Evaluation Protocol
- **Primary Benchmarks**: pretrain loss vs OLMo-3-7B / matched-parameter NTP; downstream macro (GSM8K and the paper's suite); optional drafter MAL.
- **Evaluation Pitfalls**: Do not treat 8.9B vs 7B as a matched-size optimizer bake-off. Do not retarget Muon2 or Dolma-3.

## SOTA Recommendation (as of 2026-09-11)
- **Experimental first hop (this task only)**: **NCP-ArchPreview** (`method:ncp-archpreview`, `paper:ncp-archpreview` `arXiv:2609.10715`).
- **Not This Task**: `method:muon2` remains the ~7B optimizer; `method:olmo-3` remains the open mix; `method:uno` remains diffusion-augmented AR serving.
