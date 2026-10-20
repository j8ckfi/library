---
id: method:framegrpo
type: method
title: 'FrameGRPO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'video MLLM annotation-as-rollout without CoT'
  reason: 'OraRL remains first hop; FrameGRPO varies frames inside a GRPO group'
  use_instead: method:orarl
- when: 'dense/sparse paired-view video RL with reliability-gated reward'
  reason: 'SAVER is the paired-view plug-in'
  use_instead: method:saver
assumptions:
- 'Video GRPO where every rollout in a group would otherwise share the same frames.'
- 'No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:framegrpo
recipes:
- recipe:framegrpo
claims:
- benchmark: 'Video-MME / TempCompass / VideoEval-Pro / MMVU / VSI-Bench / NExT-GQA / Video-MMMU'
  metric: 'within-group reward variation; all-correct/all-incorrect groups; video-reasoning accuracy vs fixed-ratio GRPO'
  value: 'more within-group reward variation; fewer unanimous groups; gains across seven video benches vs GRPO'
  baseline: 'fixed-frame GRPO'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.26022'
  notes: 'Multi-frame rollouts plus gated temporal efficiency credit. Does not replace OraRL.'
tags:
- rl-alignment
- video-mllm
- grpo
- active
---

# FrameGRPO

## Method Overview
FrameGRPO samples complementary frame sets inside a GRPO group so video rewards are not homogeneous, then applies gated temporal-efficiency credit. Standard video GRPO varies only text while sharing frames.

## When to Use
- Video RLVR groups that go silent because every rollout saw the same frames.

## When NOT to Use
Annotation-as-rollout default → `method:orarl`.

## Relation to Existing SOTA
Active plug-in on `task:rl-video-mllm` (`sota_for: []`). Does **not** replace OraRL or SAVER.

## Gotchas & Failure Modes
- Extra frame sampling is the compute trade.
- Not OSWorld / desktop CUA.
