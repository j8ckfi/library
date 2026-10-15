---
id: method:cast-ssc
type: method
title: CAST (History-Adaptive Spectral Clipping)
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: choosing the ~7B dense pretrain optimizer
  reason: CAST-SSC is pre-AdamW spectral clipping; Muon2 remains the 7B default
  use_instead: method:muon2
- when: clipping Muon momentum singular values instead of flattening them
  reason: Musec clips Muon momentum; CAST-SSC clips AdamW-bound gradients
  use_instead: method:musec
- when: cross-tokenizer chunk credit alignment (CAST OPD)
  reason: method:cast is credit alignment after chunk correspondence, not spectral clipping
  use_instead: method:cast
assumptions:
- Pre-optimizer SSC on selected matrices before AdamW. Paper: 19.08B MoE, 83.89B tokens, 5000 steps.
- No public code as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:cast-ssc
recipes:
- recipe:cast-ssc
claims:
- benchmark: 19.08B MoE pretrain, 83.89B tokens, 5000 steps, 20 validation subsets
  metric: mean val loss vs SSC-constant / SSC-cosine; steps to AdaGC final smoothed loss
  value: 1.26e-2 below SSC-constant, 2.10e-2 below SSC-cosine; AdaGC loss at step 4639 (7.2% fewer); 5.5% less time vs 5000 ClipByValue
  baseline: SSC-constant, SSC-cosine, AdaGC, ClipByValue (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.19761
  notes: Distinct from method:cast (cross-tokenizer OPD). Does not retarget Muon2.
tags:
- optimizer
- spectral-clipping
- pretraining
- active
---

# CAST (History-Adaptive Spectral Clipping)

## Method Overview
Pre-optimizer soft spectral clipping with two histories. Historical scaling uses row and column summaries of AdamW's previous second moment. An EMA of the clipped output's estimated spectral norm sets each matrix's threshold. The clipped gradient is restored to original coordinates before the AdamW update.

## When to Use
- AdamW pretrain where gradient spikes and a fixed SSC threshold fight the changing gradient scale.

## When NOT to Use
~7B optimizer default → `method:muon2`. Muon momentum spectral clip → `method:musec`. Cross-tokenizer OPD CAST → `method:cast`.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** replace Muon2 or Musec. Slug `cast-ssc` avoids colliding with `method:cast` (2610.13257).

## Gotchas & Failure Modes
- **code: none** as of 2026-10-15.
- SSC-cosine lost to SSC-constant in the paper; the history-based threshold is the load-bearing piece.
