---
id: method:ori
type: method
title: 'Ori'
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'full-parameter memory-efficient pretrain (SCALE default)'
  reason: 'SCALE remains the first hop; Ori is a GaLore-family streaming k-PCA tracker'
  use_instead: method:scale
- when: 'subspace Muon with residual correction (PMRC / SMRC)'
  reason: 'PMRC is residual-correction subspace; Ori is Oja-style streaming k-PCA'
  use_instead: method:pmrc
assumptions:
- 'GaLore-family gradient-subspace projection. Streaming k-PCA inspired by Oja++. Paper: 1B LLaMA pretrain; RoBERTa-Base FT.'
- 'Paper claims code at a URL; no resolvable GitHub as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:ori
recipes:
- recipe:ori
claims:
- benchmark: '1B LLaMA pretrain vs full-rank; RoBERTa-Base FT 16 scenarios'
  metric: 'gap to full-rank; win count'
  value: 'up to 69.3% gap cut vs prior low-rank optimizers on 1B; best on 10/16 RoBERTa-Base scenarios'
  baseline: 'prior GaLore-family low-rank optimizers / full-rank (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22794'
  notes: 'Does not retarget SCALE. No SCALE bake-off.'
tags:
- optimizer
- low-rank
- galore
- active
---

# Ori

## Method Overview
Ori tracks drifting LLM gradient principal directions with a streaming k-PCA (Oja++) update so the projection subspace stays current without expensive periodic SVDs.

## When to Use
- Very low-rank gradient-projection LLM training when the subspace drifts slowly and periodic SVD is too coarse.

## When NOT to Use
Default mem-efficient full-param → `method:scale`.

## Relation to Existing SOTA
Active plug-in on `task:full-param-memory-efficient-pretrain` (`sota_for: []`). Does **not** replace SCALE.

## Gotchas & Failure Modes
- GaLore family; not a SCALE comparison.
- Announced code URL did not resolve to a public GitHub as of ingest.
