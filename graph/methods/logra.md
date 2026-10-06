---
id: method:logra
type: method
title: "LoGRA"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "labeled dense Pass@1 RLVR loss"
    reason: "CISPO remains Pass@1; LoGRA is an RL memory sketch"
    use_instead: "method:cispo"
  - when: "full-param pretrain/FT subspace projection (SCALE)"
    reason: "SCALE remains the memory-efficient pretrain hop; LoGRA is RL post-train sketches"
    use_instead: "method:scale"
assumptions:
  - "RL post-train where optimizer/activation memory is the bottleneck. Paper: 27B on 8 GPUs, 1100+ steps."
  - "No public URL as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:logra
recipes:
  - recipe:logra
claims:
  - benchmark: "RL post-train memory vs dense Adam"
    metric: "average training-memory reduction"
    value: "up to 45.7%"
    baseline: "dense Adam RL"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06647"
    notes: "27B, 1100+ steps, 8 GPUs. Does not retarget CISPO or SCALE."
tags:
  - post-training
  - optimizer
  - logra
  - active
---

# LoGRA

## Method Overview
LoGRA stores RL gradients as low-rank sketches (enough for the update and for policy sync) and rescales the step with a predicted KL so large sketched updates do not jump the policy.

## When to Use
- RL post-train where dense Adam optimizer state OOMs (paper: 27B / 8 GPUs).

## When NOT to Use
- Pass@1 loss → `method:cispo`. Full-param pretrain memory → `method:scale`.

## Relation to Existing SOTA
- Active plug-in on `task:full-param-memory-efficient-pretrain` with a mention on `task:math-code-rl-dense` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO or SCALE.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06 (Molt named, no URL).
- Predicted-KL is a step controller, not a KL penalty vs a frozen reference.
