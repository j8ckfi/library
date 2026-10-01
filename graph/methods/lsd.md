---
id: method:lsd
type: method
title: "LSD"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "LSD routes solved groups to EMA OPD; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "choosing the frontier post-train engine"
    reason: "Miles is the stack; LSD is a length-tax mix on an RLVR host"
    use_instead: "method:miles"
  - when: "hybrid Think/NoThink length control from offline accuracy/token stats"
    reason: "When2Think is IDAC length control; LSD is online solved-prompt distillation"
    use_instead: "method:when2think"
  - when: "single-teacher matching distillation from a strong frozen teacher"
    reason: "OPD remains distill default; LSD's teacher is an EMA of the RL policy"
    use_instead: "method:opd"
assumptions:
  - "Group-relative RLVR host with a binary verifier. Route a group to OPD when empirical solve rate meets the threshold (paper default: all-correct). Teacher is an EMA checkpoint of the online policy."
  - "Paper: Qwen3-4B-Base, DAPO-Math-17K, max 4096 tokens; AMC 2023 / AIME 2025 / AIME 2026. Also a multi-turn agentic LST split."
  - "No public GitHub as of 2026-10-01. SG-FKL is the reported default estimator."
last_reviewed: "2026-10-01"
papers:
  - paper:lsd
recipes:
  - recipe:lsd
claims:
  - benchmark: "Single-turn LST on a frozen easy set vs RL"
    metric: "length-scaling tax"
    value: "-3.7%"
    baseline: "RL 19.0%"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.38854"
    notes: "Comparable or better Pass@1. Easy set frozen at the RL anchor. Not a CISPO retarget."
  - benchmark: "Multi-turn agentic LST vs RL"
    metric: "length-scaling tax"
    value: "13.7%"
    baseline: "RL 31.4%"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.38854"
    notes: "Preserves concise behavior on solved queries; unsolved groups stay on RLVR."
tags:
  - post-training
  - rlvr
  - distillation
  - lsd
  - active
---

# LSD

## Method Overview
LST measures excess mean length on a frozen easy-query set relative to the shortest later checkpoint that still meets the accuracy threshold. LSD (Length Self-Distillation) uses current-group solve rate to route: solved → on-policy distillation against an EMA teacher; unsolved → the host RLVR loss (CISPO/GRPO-family). No external teacher. Supervised-gradient forward KL (SG-FKL) is the reported default among FKL / RKL / sampled RKL.

## When to Use
- RLVR runs where easy prompts get longer without accuracy, and you can keep an EMA of the online policy.

## When NOT to Use
- Pass@1 default → `method:cispo`. Production engine → `method:miles`. Offline Think/NoThink IDAC → `method:when2think`. Frozen larger teacher → `method:opd`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` beside `method:cispo` and `method:miles`. Does **not** enter `current_sota`. Does **not** replace CISPO, Miles, When2Think, or OPD.

## Gotchas & Failure Modes
- No public code as of 2026-10-01.
- All-correct routing is the paper default; lowering the threshold distills unsolved groups and can cap exploration.
- EMA half-life is a trade-off: too fast copies the verbose policy, too slow regularizes toward a stale short policy.
- Dynamic sampling that *drops* all-correct groups is the failure mode LSD is written against.
