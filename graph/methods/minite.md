---
id: method:minite
type: method
title: 'miniTE'
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'native FP4 forward/backward hardware training from scratch'
  reason: 'miniTE is NVFP4 RL execution alignment, not Quartet-II pretrain'
  use_instead: method:quartet-ii
- when: 'rollout-guided QAT that caches mantissa/scale'
  reason: 'TRACE is the complementary dual-active hop; no head-to-head'
  use_instead: method:trace
assumptions:
- 'Separate train and sampling engines on native NVFP4. Paper: Qwen3-30B-A3B long-horizon RL on B300.'
- 'No official GitHub as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:minite
recipes:
- recipe:minite
claims:
- benchmark: 'Qwen3-30B-A3B native NVFP4 RL, single B300 node'
  metric: 'learner tokens/s vs BF16 and TE NVFP4; eval quality vs BF16'
  value: '33540 tok/s; 1.39x BF16 and 1.47x TE NVFP4 on complete learner updates; eval close to BF16, ahead of naive TE NVFP4'
  baseline: 'BF16; Transformer Engine NVFP4'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23928'
  notes: 'Matching weights and format is not enough. Dual-active with TRACE/TRIAGE. Does not replace Quartet-II.'
tags:
- quantization
- nvfp4
- rl
- active
---

# miniTE

## Method Overview
miniTE treats native NVFP4 RL as an execution-gap problem: diagnostics, cross-engine numerical alignment, and W4A4 GEMM with local activation-dependent scaling, native accumulation, and independent backward precision. Weight/format match is not sufficient.

## When to Use
- Native NVFP4 RL with a separate rollout engine where naive TE NVFP4 quality or train-rollout consistency fails.

## When NOT to Use
FP4 pretrain from scratch → `method:quartet-ii`. Rollout-guided QAT cache → `method:trace`.

## Relation to Existing SOTA
Active plug-in on `task:fp4-rl-train-rollout-alignment` (`sota_for: []`). Does **not** replace TRACE, TRIAGE, or Quartet-II.

## Gotchas & Failure Modes
- Operator composition, not just the format name, drives the gap.
- No public repo.
