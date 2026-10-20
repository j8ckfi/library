---
id: method:nvfp4-pretrain-recipe
type: method
title: 'NVFP4 Pretrain Recipe'
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'native FP4 hardware training default'
  reason: 'Quartet-II / MXFP4 remain locked SOTA; this card is a medium-scale recipe ablation'
  use_instead: method:quartet-ii
- when: 'FP4 RL train-rollout mismatch'
  reason: 'That is TRACE/TRIAGE/miniTE'
  use_instead: task:fp4-rl-train-rollout-alignment
assumptions:
- 'Nemotron-family dense 8B and 30B-A3B MoE trained up to 1T tokens.'
- 'ICML 2026 AdaptFM workshop. No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:nvfp4-pretrain-recipe
recipes:
- recipe:nvfp4-pretrain-recipe
claims:
- benchmark: 'Nemotron dense 8B and 30B-A3B MoE, up to 1T tokens, loss gap to BF16'
  metric: 'which NVFP4 ingredients recover accuracy; stacked-recipe loss gap'
  value: 'paper: strongest FP4 loss-gap-to-BF16 result at this scale; selective high-precision layers required; not all backward tensors benefit equally from de-biasing'
  baseline: 'NVIDIA 2025 NVFP4 recipe; Quartet-II; TetraJet; stochastic rounding'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24343'
  notes: 'Does not retarget Quartet-II. Recipe ingredients, not a new kernel.'
tags:
- quantization
- nvfp4
- pretrain
- active
---

# NVFP4 Pretrain Recipe

## Method Overview
A medium-scale bake-off of NVFP4 pretrain ingredients on 8B dense and 30B-A3B MoE up to 1T tokens. The stacked recipe uses unbiased gradient estimation with lower quantization error than stochastic rounding, and keeps selective high-precision layers.

## When to Use
- Choosing which NVFP4 pretrain knobs to keep at 8B / 30B-A3B scale.

## When NOT to Use
Locked native FP4 default → `method:quartet-ii`.

## Relation to Existing SOTA
Active plug-in on `task:fp4-hardware-training` (`sota_for: []`). Does **not** replace Quartet-II or MXFP4.

## Gotchas & Failure Modes
- Workshop paper; not a 7B Muon2 bake-off.
- Backward de-biasing is tensor-selective.
