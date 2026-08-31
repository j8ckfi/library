---
id: task:llm-pretraining-optimization
type: task
title: "Large Language Model Pretraining Optimization"
domain: "pretraining"
summary: "Optimization of transformer and non-transformer language model weights from scratch using first- and second-order momentum and orthogonalized matrix updates."
current_sota:
  - method: method:muon2
    as_of: "2026-08-26"
    benchmark: "Moonlight 7B Pretraining / FineWeb"
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
  - method:attnres
  - method:mhc
  - method:adamw-optimizer
  - method:puro-2b
tags:
  - pretraining
  - optimizer
  - language-models
---

# Large Language Model Pretraining Optimization

## Problem Definition
Pretraining modern neural network models involves minimizing cross-entropy loss over hundreds of billions or trillions of tokens with maximal parameter update efficiency.

## SOTA Landscape (as of 2026-08-26)
- **Default Optimizer**: **Muon2** (`method:muon2`, 2604.09967).
- **Large-Batch / High-Memory**: **KL-SOAP** (`method:soap-muon-scale`, 2607.20548).
- **Consumer ~2B MuonH wrapper**: Documented on `method:muon2`; used by `method:puro-2b`. Does not change this 7B default.
