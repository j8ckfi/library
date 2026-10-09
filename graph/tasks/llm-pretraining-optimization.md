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
  - when: "4-bit AdamW optimizer-state quantization in preconditioner space (ZIP-SR)"
    to: "method:zip-sr"
  - when: "thresholded Muon orthogonalization of small vs large singular values"
    to: "method:spectrally-targeted-muon"
  - when: "pilot-run cubic rule for Adam's shared beta (β1=β2=β)"
    to: "method:adam-beta-cubic"
  - when: "two-band Marchenko-Pastur spectral reweighting for Muon (BulkBoost)"
    to: "method:bulkboost"
  - when: "unique-token epoch / repetition geometry under a finite pretrain corpus"
    to: "task:data-constrained-pretrain"
  - when: "NorMuon adaptivity is orthogonalization geometry; decoupled geometry-aligned scaling (DGA-Muon)"
    to: "method:dga-muon"
  - when: "Nyström-sketched SOAP preconditioners / linear optimizer memory (Clean / Q-Clean)"
    to: "method:clean"
  - when: "per-expert Muon step-size multipliers from update–gradient alignment (ExpertMuon-Compass)"
    to: "method:expertmuon-compass"
  - when: "temporary strong soft-orthogonality early in Muon-family pretrain, then remove (ORCA)"
    to: "method:orca"
  - when: "lossless multi-token / diffusion-augmented AR serving rather than the pretrain optimizer"
    to: "task:diffusion-augmented-ar"
  - when: "latent-space / next-concept LM architecture rather than the optimizer"
    to: "task:latent-space-lm-pretrain"
  - when: "full-param FT optimizer-state memory (ternary column-wise one-sparse)"
    to: "method:taco"
  - when: "fully synthetic single-stage LLM pretraining from Wikipedia/Wikibooks seeds"
    to: "task:synthetic-single-stage-pretrain"
  - when: "zero-natural-data self-play pretraining (UTM programs, no natural text)"
    to: "task:zero-natural-data-self-play-pretrain"
  - when: "Muon-style norm-aware update for embedding tables (1->2) and LM head (2->inf) instead of AdamW"
    to: "method:muonio"
methods:
  - method:zip-sr
  - method:spectrally-targeted-muon
  - method:dga-muon
  - method:clean
  - method:expertmuon-compass
  - method:orca
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
  - method:taco
  - method:synth
  - method:self-play-pretraining
  - method:muonio
  - method:adam-beta-cubic
  - method:bulkboost
last_reviewed: "2026-10-09"
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
- **Not this task (full-param FT memory geometry)**: `method:taco` (`arXiv:2610.02199`) on `task:full-param-memory-efficient-pretrain`. Ternary column-wise one-sparse FT. Does not replace Muon2.
- **Optional Adam shared-β cubic rule (not this hidden-layer default)**: `method:adam-beta-cubic` (`arXiv:2610.08624`). 200-update pilot; 40.7% lower mean relative val gap vs β=0.95. Code AlbertoFdezHdez/Adam_beta_rule_cubic. Does not replace Muon2 or AdamW.
- **Optional two-band Muon spectral reweight**: `method:bulkboost` (`arXiv:2610.07497`). Fine-grained spectral maps unnecessary in the paper. Does not replace Muon2.
- **Optional I/O-layer Muon (not this hidden-layer default)**: `method:muonio` (`arXiv:2610.02705`). \(1\to 2\) embeddings / \(2\to\infty\) LM head instead of AdamW. C4 val PPL 60M/130M/1B 28.366/23.617/14.374 vs Muon Tuned 28.502/24.238/14.527. Does not replace Muon2.
- **Not this task (seed-grounded synthetic single-stage pretrain)**: `method:synth` (`arXiv:2609.37891`) on `task:synthetic-single-stage-pretrain`. AdamW NTP on SYNTH; not a Muon2 retarget.
- **Not this task (zero-natural-data UTM self-play)**: `method:self-play-pretraining` (`arXiv:2609.30063`) on `task:zero-natural-data-self-play-pretrain`. Experimental <25M.
- **Optional 4-bit AdamW-state quantization**: `method:zip-sr` (`arXiv:2610.12444`) stochastic rounding in preconditioner space. Up to 70% TorchAO gap cut vs 32-bit AdamW. No public code. Does not replace Muon2, SCALE, or TACO.
- **Optional thresholded Muon orthogonalization**: `method:spectrally-targeted-muon` (`arXiv:2610.10965`) small singular values carry the Muon gain. CIFAR-10 / NanoGPT speedruns, not a 7B bake-off. No public code. Does not replace Muon2, BulkBoost, or Musec.
