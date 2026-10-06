---
id: task:open-data-recipe
type: task
title: "Open Foundation Data Recipe & Pretraining Mix"
domain: "pretraining"
summary: "Curating, filtering, and scheduling multi-trillion token open-source pretraining datasets and annealing curricula."
current_sota:
  - method: method:olmo-3
    as_of: "2026-08-26"
    benchmark: "Dolma-3 Open Token Mix"
    metric: "open pretraining representation quality"
    value: "Default SOTA open data recipe"
    notes: "OLMo-3 / Dolma-3 (2512.13961)."
methods:
  - method:repetition-count-selection
  - method:repeated-token-worth
  - method:olmo-3
  - method:olmo-2-curriculum
  - method:demix
  - method:causalmix
  - method:op-mix
  - method:ncp-archpreview
  - method:tiny-aya-l2-thinker
  - method:synth
  - method:self-play-pretraining
redirects:
  - when: "unique-token epoch / repetition geometry under a finite pretrain corpus (not the open mix)"
    to: "task:data-constrained-pretrain"
  - when: "in-language (L2) reasoning SFT rather than a pretrain mix"
    to: "task:multilingual-l2-reasoning-sft"
  - when: "fully synthetic single-stage LLM pretraining from Wikipedia/Wikibooks seeds (no web mix)"
    to: "task:synthetic-single-stage-pretrain"
  - when: "zero-natural-data self-play pretraining (generator proposes UTM programs)"
    to: "task:zero-natural-data-self-play-pretrain"
last_reviewed: "2026-10-06"
tags:
  - pretraining
  - open-data
  - data-curriculum
  - olmo3
---

# Open Foundation Data Recipe & Pretraining Mix

## Problem Definition
Constructing transparent, reproducible, and open multi-trillion token pretraining corpora with optimal domain mixing and staged annealing.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Data Recipe**: **OLMo-3 / Dolma-3** (`method:olmo-3`, 2512.13961).
- **Dynamic Mixing**: **DeMix** (`method:demix`, 2602.00747), **CausalMix** (`method:causalmix`, 2607.01104), **OP-Mix** (`method:op-mix`, 2605.15220).
- **Not a 7B substitute**: Consumer-GPU ~2B pretrain with a proxy-guided mix is `method:puro-2b`, not a replacement for Dolma-3.
- **Latent-space LM that used Dolma-3 (not this mix default)**: `method:ncp-archpreview` on `task:latent-space-lm-pretrain`.
- **L2 reasoning SFT mix (not this pretrain mix)**: `method:tiny-aya-l2-thinker` on `task:multilingual-l2-reasoning-sft`.
- **Fully synthetic single-stage pretrain (not this mix)**: `method:synth` on `task:synthetic-single-stage-pretrain`. Wikipedia/Wikibooks seeds, no Dolma-3 replacement.
- **Zero-natural-data self-play pretrain (not this mix)**: `method:self-play-pretraining` on `task:zero-natural-data-self-play-pretrain`.
