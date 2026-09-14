---
id: method:scope-opsd
type: method
title: "SCOPE-OPSD (Fisher-Conditioned Privileged Subspaces)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged-teacher OPSD first hop with gold solutions and a verifier"
    reason: "VISTA remains the privileged-teacher first hop; SCOPE is a hidden-state auxiliary on vanilla OPSD"
    use_instead: "method:vista"
  - when: "OPSD collapse / self-correction is the failure mode"
    reason: "NSD diverges from a negative condition; SCOPE adds a Fisher subspace on the privileged residual"
    use_instead: "method:nsd"
  - when: "teacher-free unlabeled self-adaptation"
    reason: "SCOPE needs a privileged self-teacher"
    use_instead: "method:opsa"
  - when: "single-teacher matching distillation from a frozen larger teacher"
    reason: "OPD remains the matching default"
    use_instead: "method:opd"
  - when: "labeled Pass@1 math/code RLVR"
    reason: "CISPO remains Pass@1; SCOPE is an OPSD plug-in"
    use_instead: "method:cispo"
assumptions:
  - "Same-size privileged self-teacher that sees a verified solution. Paper: Qwen3-1.7B/4B/8B, OpenThoughts Math OPSD 29434, 100 steps, batch 32, non-thinking student, thinking frozen teacher."
  - "Calibrate the rank-64 factor from 128 prompts per scale. Do not transfer factors across hidden widths."
  - "No official GitHub as of 2026-09-14. Host is VERL + SGLang eval."
last_reviewed: "2026-09-14"
papers:
  - paper:scope-opsd
recipes:
  - recipe:scope-opsd
claims:
  - benchmark: "AIME24 / AIME25 / HMMT25 Macro Avg@12, Qwen3-1.7B step 75"
    metric: "Macro Avg@12"
    value: 43.33
    baseline: "Pure OPSD 41.48 / matched Random 41.94 / local GRPO best 39.44"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.12579"
    notes: "Table 1 / Table 7. +1.85 vs Pure OPSD, +1.39 vs matched Random (two reruns). Shared checkpoint across benchmarks."
  - benchmark: "Same protocol, Qwen3-4B / 8B step 75 Macro Avg@12"
    metric: "Macro Avg@12"
    value: "63.80 / 65.28"
    baseline: "Pure OPSD 62.13 / 64.45; matched Random 63.43 / 64.35"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.12579"
    notes: "Never below Pure OPSD on 12 scale-checkpoint pairs except an exact tie at 4B step 25. Rank 64 preferred over 32/128."
tags:
  - post-training
  - distillation
  - opsd
  - privileged-teacher
  - scope-opsd
  - active
---

# SCOPE-OPSD (Fisher-Conditioned Privileged Subspaces)

## Method Overview
Vanilla OPSD uses privileged teacher information only through next-token KL. SCOPE-OPSD adds a second channel: the final-layer teacher-student residual projected onto a frozen rank-64 factor \(F\) fit from residual covariance and LM-head Fisher sensitivity. The student still samples problem-only prefixes. The auxiliary reuses those forwards. A matched Random control keeps rank and nonzero spectrum and matches initial gradient RMS so the comparison is orientation, not extra loss weight.

## When to Use
- Short-budget privileged OPSD where you already run vanilla OPSD forwards and want a cheap hidden-state auxiliary.
- When you can calibrate a per-scale rank-64 factor (paper: 128 prompts).

## When NOT to Use
- Privileged-teacher first hop that still works → `method:vista`. Collapse via imitation → `method:nsd`. No teacher → `method:opsa`. Pass@1 labels → `method:cispo`. Frozen larger teacher → `method:opd`.

## Relation to Existing SOTA
- Active sibling on `task:privileged-teacher-opsd`. Does **not** enter `current_sota`. VISTA remains the first hop. NSD remains the anti-collapse trainer.

## Gotchas & Failure Modes
- Do not treat the local GRPO 39.44 vs Structured 43.33 as a CISPO bake-off.
- Rank 64 is not claimed universally optimal; it won the paper's {32,64,128} sweep at 1.7B.
- No public code as of 2026-09-14.
