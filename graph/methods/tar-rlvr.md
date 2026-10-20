---
id: method:tar-rlvr
type: method
title: 'TAR'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'single-turn dense math/code Pass@1 RLVR default'
  reason: 'CISPO remains Pass@1; TAR is a diversity-preserving replay plug-in'
  use_instead: method:cispo
- when: 'novelty-rewarded explorer policies distilled without novelty'
  reason: 'ExpDis is a different explorer/distill split'
  use_instead: method:expdis
assumptions:
- 'GRPO-host RLVR. Paper: six math benches, Qwen2.5 two scales.'
- 'Code wenzhilics/tar as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:tar-rlvr
recipes:
- recipe:tar-rlvr
claims:
- benchmark: 'Six mathematical reasoning benches, two Qwen2.5 scales'
  metric: 'accuracy vs diversity; forgetting of correct base-model solutions'
  value: 'better accuracy-diversity balance than evaluated diversity-preserving methods; less forgetting of correct base solutions'
  baseline: 'on-policy diversity methods; offline replay'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24236'
  notes: 'Soft rollout gate plus token gate. Does not replace CISPO.'
tags:
- rl-alignment
- rlvr
- diversity
- replay
- active
---

# TAR

## Method Overview
TAR (Targeted Adaptive Replay) keeps a compact memory bank of diverse correct base-policy traces and replays them when on-policy RLVR undersamples a rewarded reasoning mode. Finite-sample GRPO can suppress equally rewarded modes; once under-sampled they rarely recover.

## When to Use
- RLVR where Pass@1 rises but distinct correct strategies disappear.

## When NOT to Use
Default Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO.

## Gotchas & Failure Modes
- Replay is gated; always-on replay can stall adaptation.
- Distinct from ExpDis novelty explorers.
