---
id: method:eden
type: method
title: 'EDEN'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: "activation-space steering exploration for RLVR (ASE)"
  reason: "EDEN perturbs embeddings; ASE steers activation-difference clusters"
  use_instead: "method:ase"
- when: 'single-turn dense math/code Pass@1 with CISPO as the loss'
  reason: 'CISPO remains Pass@1; EDEN is a rollout-source explorer on GRPO'
  use_instead: method:cispo
- when: 'exploration-preserving advantage shaping (surprisal + pass rate)'
  reason: 'ExPPO shapes advantages; EDEN perturbs rollout inputs'
  use_instead: method:exppo
- when: 'novelty-rewarded explorer policies distilled into a student'
  reason: 'ExpDis is explorer/distill split, not embedding noise'
  use_instead: method:expdis
assumptions:
- 'GRPO-family math RLVR with small groups that collapse. Paper: Qwen2.5-0.5B / Math-1.5B / Math-7B, 8x H100, verl.'
- 'Code: none found as of 2026-10-16.'
last_reviewed: '2026-10-21'
papers:
- paper:eden
recipes:
- recipe:eden
claims:
- benchmark: 'AIME24/25 Pass@256 and eight-bench Pass@1, Qwen2.5-0.5B / Math-1.5B / Math-7B vs GRPO'
  metric: 'Pass@256 avg; AIME25 Pass@256 on 7B; eight-bench avg'
  value: 'Pass@256 avg +6.67 vs GRPO; 7B AIME25 Pass@256 +13.33; Math-7B eight-bench 54.87 vs GRPO (paper table)'
  baseline: 'GRPO; higher T; entropy bonus; asymmetric clip; larger groups (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.16105'
  notes: 'Does not retarget CISPO. No public code as of 2026-10-16.'
tags:
- rlvr
- exploration
- active
---

# EDEN

## Method Overview
Keep most rollouts standard. Replace a few with the same policy on the prompt plus one appended embedding that is group-anchored Gaussian noise. Downweight those advantages. Leave decoding and inference unchanged.

## When to Use
- GRPO math RLVR whose groups are too similar and temperature/entropy/clip are not enough.

## When NOT to Use
Pass@1 default loss → `method:cispo`. Advantage shaping → `method:exppo`. Explorer/distill split → `method:expdis`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO.

## Gotchas & Failure Modes
- Noise and the shared anchor are complementary; either alone is weaker.
- Not a CISPO bake-off; host is GRPO in verl.

