---
id: method:online-draft-cotrain
type: method
title: "Online Draft Co-Training"
category: "training-systems"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "lossless multi-token / diffusion-augmented AR serving without a separate draft"
    reason: "Uno keeps AR weights and adds diffusion adapters; this co-trains a speculative draft inside RL"
    use_instead: "method:uno"
  - when: "choosing the Pass@1 RLVR loss"
    reason: "Systems speedup of rollouts, not CISPO"
    use_instead: "method:cispo"
  - when: "frontier post-train engine choice"
    reason: "Miles is the full stack; this is a NeMo RL draft path"
    use_instead: "method:miles"
assumptions:
  - "NeMo RL long-context RL with CP+PP. Paper up to 122B, 256K context."
last_reviewed: "2026-09-09"
papers:
  - paper:online-draft-cotrain
recipes:
  - recipe:online-draft-cotrain
claims:
  - benchmark: "Online draft co-train through 122B, CP at 256K"
    metric: "rollout / e2e speedup vs policy baseline"
    value: "drafts track the policy; substantial rollout and end-to-end speedups (paper)"
    baseline: "speculative decoding without online co-train; prior CP without branch attention"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.07108"
    notes: "NVIDIA technical report. Code: NVIDIA-NeMo/RL#3698. Niche systems."
tags:
  - systems
  - speculative-decoding
  - online-draft-cotrain
  - niche
---

# Online Draft Co-Training

## Method Overview
Online co-training of a speculative draft during long-context RL, with CP branch attention and TapChannel PP transport. Niche systems. Does not replace Uno, CISPO, or Miles.

## When to Use
- NeMo RL, long-context RL rollouts, you already have a draft model.

## When NOT to Use
- Diffusion-augmented AR serving → `method:uno`. Train kernel → `method:cispo`. Full stack → `method:miles`.

## Relation to Existing SOTA
- Niche mention on `task:diffusion-augmented-ar` (related serving/rollout speed) and `task:frontier-rl-posttrain-stack`. Does **not** supersede Uno or Miles.

## Gotchas & Failure Modes
- Implementation lives in a NeMo RL issue/PR, not a standalone repo.
