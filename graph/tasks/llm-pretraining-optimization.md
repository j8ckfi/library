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
redirects:
  - when: "lossless multi-token / diffusion-augmented AR serving rather than the pretrain optimizer"
    to: "task:diffusion-augmented-ar"
  - when: "latent-space / next-concept LM architecture rather than the optimizer"
    to: "task:latent-space-lm-pretrain"
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
  - method:layer-dropout
  - method:optimizer-memory-schedules
  - method:adana
  - method:musec
last_reviewed: "2026-09-11"
tags:
  - pretraining
  - optimizer
  - language-models
---

# Large Language Model Pretraining Optimization

## Problem Definition
Pretraining modern neural network models involves minimizing cross-entropy loss over hundreds of billions or trillions of tokens with maximal parameter update efficiency.

## SOTA Landscape (as of 2026-09-08)
- **Default Optimizer**: **Muon2** (`method:muon2`, 2604.09967). Unchanged.
- **Large-Batch / High-Memory**: **KL-SOAP** (`method:soap-muon-scale`, 2607.20548).
- **Consumer ~2B MuonH wrapper**: Documented on `method:muon2`; used by `method:puro-2b`. Does not change this 7B default.
- **Optional layer sparsity**: `method:layer-dropout` (`arXiv:2609.05275`, ICML 2026) reintroduces structured layer dropout with $r_{\mathrm{train}}=1/\rho$. Same-FLOPs lower loss; same-steps up to ~25% FLOP save. Does not replace Muon2.
- **OT-horizon HP guidance**: `method:optimizer-memory-schedules` (`arXiv:2609.04577`) — preferred LR schedule can reverse across overtraining; WD $\sim\sqrt{\mathrm{OT}}$; longer OT favors longer fixed memory. ADANA (`method:adana`, 2602.05298) is a named baseline in that study, not a 7B default. Does not replace Muon2.
- **Optional Muon stability plug-in**: `method:musec` (`arXiv:2609.11655`) clips momentum singular values instead of flattening them. Does not replace Muon2 or MuonClip.
