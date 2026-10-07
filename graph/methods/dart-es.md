---
id: method:dart-es
type: method
title: "DART-ES"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "Pass@K / coverage / no-backward first hop"
    reason: "DART-ES reweights and replays on an ES trainer; ES-reasoning remains Pass@K"
    use_instead: "method:es-reasoning"
  - when: "labeled Pass@1 math/code RLVR"
    reason: "CISPO remains Pass@1; this is an ES plug-in"
    use_instead: "method:cispo"
assumptions:
  - "Evolution-strategies LLM fine-tuning host. Paper: GSM8K plus five hard math. Code: szs777/DART-ES-Code (`code_status: released`)."
last_reviewed: "2026-10-07"
papers:
  - paper:dart-es
recipes:
  - recipe:dart-es
claims:
  - benchmark: "GSM8K average after ES fine-tune"
    metric: "accuracy"
    value: 73.53
    baseline: "ES 72.07 / GRPO 73.26"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06993"
    notes: "Difficulty-aware reweighting + targeted replay. Does not replace ES-reasoning or CISPO."
  - benchmark: "Five hard math average"
    metric: "accuracy"
    value: 49.20
    baseline: "ES 48.34"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06993"
    notes: "15.2–50.2% faster and 21.1–51.1% less GPU mem vs GRPO in the paper."
tags:
  - post-training
  - evolution-strategies
  - dart-es
  - active
---

# DART-ES

## Method Overview
Difficulty-aware reweighting and targeted replay on evolution-strategies LLM fine-tuning. Keep the ES update; change which prompts and directions get mass.

## When to Use
- Already on ES-reasoning (or another ES host) and hard prompts are under-sampled.

## When NOT to Use
- Pass@K first hop → `method:es-reasoning`. Pass@1 labels → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:passk-reasoning-coverage` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace ES-reasoning or CISPO.

## Gotchas & Failure Modes
- **code: released** szs777/DART-ES-Code as of 2026-10-07.
- GRPO memory comparison is not a GRPO revival.
