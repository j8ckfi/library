---
id: method:oprd
type: method
title: "OPRD (On-Policy Reverse Distillation)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "OPRD rescales a verifier gradient along a teacher shift; OPD remains the matching default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR without using a teacher shift"
    reason: "Labeled dense RLVR stays CISPO; OPRD still needs a teacher delta"
    use_instead: "method:cispo"
  - when: "matching a weak teacher on student prefixes (classic W2S-OPD)"
    reason: "W2S-OPD matches the weak policy; OPRD does not treat it as a target"
    use_instead: "method:w2s-opd"
  - when: "multi-teacher token-share balancing is the goal"
    reason: "Open-MOPD remains the multi-teacher distill default; OPRD's multi-teacher result is reverse-distill consolidation"
    use_instead: "method:open-mopd"
assumptions:
  - "Frozen teacher with a reference policy, student rollouts, and a deterministic outcome verifier. Paper: Qwen3 4B/8B (and 1.7B/0.6B strong-to-weak), DAPO-Math-17K, Reasoning Gym."
  - "Trained-policy tables average five checkpoints (speed + level), not a single best ckpt."
last_reviewed: "2026-09-09"
papers:
  - paper:oprd
recipes:
  - recipe:oprd
claims:
  - benchmark: "Qwen3-4B→8B math Mean@16 (AIME24/25, HMMT'25, Olympiad) checkpoint-average"
    metric: "Mean@16 average"
    value: 51.91
    baseline: "KDRL 43.99 / OPD 39.44 / GRPO 39.38 / teacher 38.66"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08798"
    notes: "Table 1. AIME'24 66.92 vs KDRL 53.46 vs OPD 46.92. +7.92 vs strongest baseline on math avg."
  - benchmark: "Qwen3-4B-Base→8B-Base Reasoning Gym Pass@1 checkpoint-average"
    metric: "Pass@1 average"
    value: 55.18
    baseline: "KDRL 44.38 / OPD 42.83 / GRPO 41.81 / teacher 44.65"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08798"
    notes: "Table 1. +10.80 vs strongest baseline. Surpasses the weak teacher."
  - benchmark: "4 task-specific 4B teachers → one 8B student, Reasoning Gym"
    metric: "Pass@1 average"
    value: 58.77
    baseline: "Mix-RL 47.68 / KDRL 47.47 / MOPD 43.10 / specialist mean 44.65"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08798"
    notes: "Table 2. Beats each specialist on all four tasks."
  - benchmark: "Paper 4B→8B mix vs concurrent W2S methods (AIME'24 / Knights / String avg)"
    metric: "checkpoint-average mix"
    value: 60.81
    baseline: "W2S-OPD 49.22 / S2L-PO 54.21 / Direct-OPD 37.81 / OPD 45.67"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08798"
    notes: "Table 3. Differentiation vs method:w2s-opd, not a graph supersession of OPD or CISPO."
tags:
  - post-training
  - distillation
  - weak-to-strong
  - oprd
  - active
---

# OPRD (On-Policy Reverse Distillation)

## Method Overview
OPRD is **weak-to-strong reverse distillation**. OPD matches teacher logps on student prefixes and can stall at the weak teacher's ceiling. OPRD instead forms the teacher's policy-shift direction (teacher vs its reference) on student rollouts and rescales the student's verifier-driven gradient along that direction. Only verifier-supported components are amplified, so RLVR stationary points stay; the teacher accelerates rather than redirects.

`method:w2s-opd` still matches a weak teacher. OPRD does not. Table 3 of this paper reports OPRD 60.81 vs a W2S-OPD reimplementation 49.22 on one mix — that is differentiation, not a library supersession of OPD or CISPO.

## When to Use
- A weaker (or same-family smaller) post-trained teacher should speed up a stronger student's RLVR without becoming the target.
- Multi-specialist consolidation where matching MOPD plateaus at the specialist average.

## When NOT to Use
- Distill default (match a strong teacher) → `method:opd`.
- Pass@1 without a teacher shift → `method:cispo`.
- Explicit weak-policy matching → `method:w2s-opd`.
- Multi-teacher token-share balancing → `method:open-mopd`.

## Relation to Existing SOTA
- Active on `task:student-distillation`. Does **not** supersede `method:opd`, `method:cispo`, `method:w2s-opd`, or `method:open-mopd`.
- Distinct from VISTA (privileged same-size gold teacher) and RISE (self-extrapolated teacher).

## Gotchas & Failure Modes
- Code: `https://github.com/raymin0223/on_policy_reverse_distillation` (early stub at 2026-09-09 ingest).
- Tables average five checkpoints; do not compare a single OPRD best ckpt to a GRPO last ckpt.
- Needs a teacher reference policy and a verifier. No labels → OPSA, not this.
- Cross-generation Qwen2.5→Qwen3 was out of the teacher's useful range in the paper's prelims.
