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
  - method:olmo-3
  - method:olmo-2-curriculum
  - method:demix
  - method:causalmix
  - method:op-mix
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
