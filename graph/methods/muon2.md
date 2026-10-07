---
id: method:muon2
type: method
title: "Muon2 Optimizer"
category: "optimizer"
status: sota
sota_for:
  - task:pretrain-dense-7b
  - task:llm-pretraining-optimization
supersedes:
  - method:muon
  - method:muon-scalable
do_not_use_for:
  - when: "NorMuon adaptivity is orthogonalization geometry; decoupled geometry-aligned scaling"
    reason: "Muon2 remains the 7B default; DGA-Muon is a NorMuon-geometry fix"
    use_instead: "method:dga-muon"
  - when: "per-expert Muon step-size multipliers from update–gradient alignment"
    reason: "Muon2 remains the 7B default; ExpertMuon-Compass is an MoE per-expert step multiplier"
    use_instead: "method:expertmuon-compass"
  - when: "temporary strong soft-orthogonality early in Muon-family pretrain, then remove"
    reason: "Muon2 remains the 7B default; ORCA is a cooled spectral regularizer on that trainer"
    use_instead: "method:orca"
  - when: "full-param FT optimizer-state memory (ternary column-wise one-sparse)"
    reason: "Muon2 remains the ~7B pretrain optimizer; TACO is an FT memory geometry"
    use_instead: "method:taco"
  - when: "Muon-style norm-aware update for embedding tables (1->2) and LM head (2->inf) instead of AdamW"
    reason: "Muon2 remains the hidden-layer / 7B default; MuonIO only replaces AdamW on embeddings and the LM head"
    use_instead: "method:muonio"
  - when: "two-band Marchenko-Pastur spectral reweighting for Muon (BulkBoost)"
    reason: "Muon2 remains the 7B default; BulkBoost is a two-band spectral reweight"
    use_instead: "method:bulkboost"
last_reviewed: "2026-10-07"
papers:
  - paper:bulkboost
  - paper:orca
  - paper:muon2
recipes:
  - recipe:muon2-pretraining
claims:
  - benchmark: "Dense 7B Pretraining / FineWeb"
    metric: "token efficiency & step stability"
    value: "~2x token efficiency vs AdamW with improved stability"
    baseline: "Muon / AdamW"
    date: "2026-08-26"
    verified: true
    notes: "Second-generation matrix orthogonalization optimizer with refined Newton-Schulz iterations."
tags:
  - optimizer
  - pretraining
  - muon2
  - sota
---

# Muon2 Optimizer

## Method Overview
Muon2 is a second-generation matrix orthogonalization momentum optimizer designed for deep transformer layers. It applies accelerated Newton-Schulz polynomial iterations to orthogonalize gradient momentum matrices, enforcing optimal spectral norm properties during parameter updates.

## When to Use
- Default SOTA optimizer for pretraining dense 7B language models from scratch.
- Hidden matrix layers in multi-layer perceptrons and attention projections. Default I/O layers stay AdamW; use `method:muonio` when embeddings / `lm_head` should get Muon-style \(1\to 2\) / \(2\to\infty\) updates instead.
- Qwen3.8-Next's Muon+AdamW split (`method:qwen38-next`) is a production architecture recipe, not a replacement of this 7B optimizer default.
- Optional structured layer dropout (`method:layer-dropout`) is a residual-path regularizer, not a replacement of this optimizer.
- Overtraining-axis HP guidance (`method:optimizer-memory-schedules`) does not change this method's `sota_for`. ADANA (`method:adana`) is a named baseline in that 51M–253M study, not a 7B default.
- Optional spectral-clip Muon update (`method:musec`) is a stability plug-in. It does not change this method's `sota_for`.
- Full-param FT sparse geometry (`method:taco`) is not a replacement of this 7B optimizer default.

## Gotchas & Failure Modes
- Embedding tables, 1D vectors, and normalization scale factors should be optimized with standard AdamW rather than matrix orthogonalization, unless `method:muonio` is in scope for embeddings / `lm_head`.
- **MuonH** (Muon + hyperball; used in `method:puro-2b`) wraps scale-invariant 2D attn/MLP matrices, projects each back to $R=\|W_0\|_F$ after the step, and runs Hyperball LR at $10\times$ the AdamW base. It is a documented Muon/Muon2-family variant for consumer-GPU ~2B pretrain. It does **not** change this method's `sota_for`: dense ~7B still uses Muon2 (+ KL-SOAP if memory allows).
