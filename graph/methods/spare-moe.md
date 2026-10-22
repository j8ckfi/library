---
id: method:spare-moe
type: method
title: 'SPARE'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:pretrain-moe-frontier'
  reason: 'SPARE is an active plug-in; method:deepseek-v4 remains the first hop'
  use_instead: method:deepseek-v4
assumptions:
- 'Frozen MoE checkpoint. Routing entropy from Top-K gate weights on calibration data.'
last_reviewed: '2026-10-22'
papers:
- paper:spare-moe
recipes:
- recipe:spare-moe
claims:
- benchmark: 'Mixtral, Qwen3-30B-A3B, DeepSeek-R1 vs uniform expert prune'
  metric: 'average accuracy vs uniform allocation'
  value: 'Qwen3-30B-A3B 57.2% to 63.8%; DeepSeek-R1 math/code/science 80.1 to 82.8'
  baseline: 'uniform per-layer expert prune'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29662'
  notes: 'Does not retarget method:deepseek-v4.'
tags:
- moe
- pruning
- active
---

# SPARE

## Method Overview
SPARE is training-free: it prunes more experts in layers whose Top-K gate mass is diffuse (high routing entropy) and keeps experts where routing is peaked.

## When to Use
- Deploy-time MoE memory cuts when a calibration set exists and uniform layer-wise prune hurts.

## When NOT to Use
Choosing the frontier MoE template → `method:deepseek-v4` / `method:kimi-k3`. Communication-efficient layout → `method:ce-moe`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:deepseek-v4`.

## Gotchas & Failure Modes
- Not a pretrain architecture default.
- No public code.
- Selector-agnostic; still needs a calibration split.
