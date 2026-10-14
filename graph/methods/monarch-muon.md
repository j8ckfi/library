---
id: method:monarch-muon
type: method
title: Monarch-Muon
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: choosing the ~7B dense pretrain optimizer
  reason: Dense Muon beats Monarch-Muon at 257M in this paper; Muon2 remains the 7B default
  use_instead: method:muon2
- when: full-param memory via subspace projections rather than Monarch factors
  reason: SCALE remains the memory-efficient full-param first hop
  use_instead: method:scale
assumptions:
- Weights are Monarch-factored. Paper reports 257M dense, 1B MoE, 6.89B H100 systems.
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:monarch-muon
recipes:
- recipe:monarch-muon
claims:
- benchmark: 257M dense / 1B MoE val loss; 6.89B H100 systems
  metric: val loss vs Monarch-AdamW; peak GB / opt-step ms
  value: 3.06 vs 3.09 (257M); 2.68 vs 2.77 (1B MoE); peak 68.87→52.94 GB; opt step
    1288.3→304.4 ms
  baseline: Monarch-AdamW; dense Muon 2.99 at 257M (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.17429
  notes: Loses to dense Muon at 257M. Does not retarget Muon2 or SCALE.
tags:
- pretraining
- optimizer
- muon
- monarch
- active
---

# Monarch-Muon

## Method Overview
Run Muon orthogonalization on Monarch factors instead of the reconstructed dense matrix. Cuts optimizer state and Newton-Schulz cost when the weight is already Monarch-factored.

## When to Use
- Pretrain or continue a Monarch-factored model and you want Muon-family updates without materializing dense optimizer state.

## When NOT to Use
Dense ~7B NTP → `method:muon2`. Full-param subspace memory → `method:scale`. Unfactored dense weights are not this recipe.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Mention on `task:full-param-memory-efficient-pretrain`. Does **not** replace Muon2 or SCALE.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Dense Muon 2.99 beats Monarch-Muon 3.06 at 257M. The paper's quality claim is vs Monarch-AdamW.
- 6.89B numbers are systems, not a 7B bake-off vs Muon2.
