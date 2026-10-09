---
id: method:grpodropout
type: method
title: "GRPODropout"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR loss"
    reason: "GRPODropout is a rollout filter on a GRPO-family host; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "asymmetric entropy x sign exploration credit on tokens (not rollout drop)"
    reason: "EAPO redistributes token advantage; GRPODropout drops easy positive rollouts"
    use_instead: "method:eapo"
  - when: "MoE/VL RLVR loss rather than a GRPO-family rollout filter"
    reason: "SAPO remains MoE/VL"
    use_instead: "method:sapo"
assumptions:
  - "GRPO-family group rollouts with sequence advantages."
  - "Code: hexuandeng/GRPODropout (`code_status: released`)." 
last_reviewed: "2026-10-09"
papers:
  - paper:grpodropout
recipes:
  - recipe:grpodropout
claims:
  - benchmark: "GRPO-family math RLVR vs original GRPO"
    metric: "accuracy and actor entropy at matched sampling budget"
    value: "higher accuracy than GRPO while updating on fewer rollouts; higher actor entropy"
    baseline: "GRPO"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.11854"
    notes: "Changes which rollouts enter the update, not the Pass@1 kernel. Does not retarget CISPO." 
tags:
  - post-training
  - rlvr
  - grpo
  - entropy
  - grpodropout
  - active
---

# GRPODropout

## Method Overview
Inside a GRPO-family group, rank positive-advantage rollouts by log-probability. Drop a small high-probability set. Recenter the remaining advantages so deletion does not silently boost the rest. Sample the usual group size; update on a subset.

## When to Use
- GRPO/CISPO-family run whose entropy collapsed because easy correct traces dominate the group.

## When NOT to Use
- Pass@1 kernel -> `method:cispo`. Token entropy x sign credit -> `method:eapo`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO.

## Gotchas & Failure Modes
- **code: released** hexuandeng/GRPODropout as of 2026-10-09.
- Recentering after deletion is required. Dropping negatives as well can raise entropy but lose accuracy.
