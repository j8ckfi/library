---
id: method:duoopd
type: method
title: "DuoOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "gap-aware budget / token-share balancing defaults across labeled domain teachers"
    reason: "Open-MOPD remains the multi-teacher default; DuoOPD is a single-teacher four-outcome rule"
    use_instead: "method:open-mopd"
  - when: "multi-teacher OPD subspace protection / task cycling"
    reason: "PMOPD projects interfering update directions; DuoOPD gates one teacher's token weights by joint outcomes"
    use_instead: "method:pmopd"
  - when: "single-teacher matching distillation from a strong frozen teacher (default OPD)"
    reason: "OPD remains reverse-KL matching; DuoOPD reshapes those log-ratios by who was correct"
    use_instead: "method:opd"
  - when: "ReLU correctness gating of OPD without joint teacher–student support"
    reason: "OPDVR gates direction from the student only; DuoOPD also changes teacher context and shared magnitudes"
    use_instead: "method:opdvr"
assumptions:
  - "One frozen teacher, one student, multiple tasks with verifiers. Cache one verified teacher response per question. Paper: Qwen3 and Llama mixtures including science / IF / code."
  - "Student outcome sets sign; joint outcome selects Softplus(teacher log-ratio), teacher-answer-conditioned log-ratio, or within-task shared weight."
  - "Official code YongYuanDeAo/DuoOPD released as of 2026-10-01."
last_reviewed: "2026-10-01"
papers:
  - paper:duoopd
recipes:
  - recipe:duoopd
claims:
  - benchmark: "Qwen3 multi-task mean macro accuracy vs OPD"
    metric: "mean macro accuracy lift"
    value: "+2.58"
    baseline: "OPD; also leads five baselines including gated OPD"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.33711"
    notes: "Gains on both teacher-solved and teacher-failed questions. Not an Open-MOPD retarget."
  - benchmark: "Llama multi-task mean macro accuracy vs OPD"
    metric: "mean macro accuracy lift"
    value: "+5.98"
    baseline: "OPD"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.33711"
    notes: "Direction-only ablation stays near OPDVR; joint-outcome support supplies most of the gain."
tags:
  - post-training
  - distillation
  - multi-teacher
  - on-policy
  - duoopd
  - active
---

# DuoOPD

## Method Overview
For each student response, \(\sigma=2r_S-1\) is the sign. Magnitude \(m_t\) depends on the joint outcome: agreement uses \(\mathrm{softplus}(\sigma\,d_0)\); teacher-only success uses the teacher’s verified answer as extra context when scoring the failed student response; student-only success uses a positive weight \(\bar m_k\) shared within the task so a failing teacher cannot reshape a correct response. Every token of a success is reinforced and every token of a failure is suppressed.

## When to Use
- Multi-task OPD from one teacher into one student where the teacher is wrong on a non-trivial slice of prompts the student already solves.

## When NOT to Use
- Multi-teacher token-share default → `method:open-mopd`. Subspace cycling → `method:pmopd`. Frozen-teacher matching → `method:opd`. Student-only ReLU gate → `method:opdvr`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:open-mopd` and `method:pmopd`. Does **not** enter `current_sota`. Does **not** replace Open-MOPD, PMOPD, OPD, or OPDVR.

## Gotchas & Failure Modes
- Needs a verifier on both teacher cache and student rollouts. Unverifiable tasks are out of scope.
- Direction-only (OPDVR-style) is not DuoOPD.
- Shared student-success weights are per-task, not a learned router. Do not confuse with Open-MOPD token-share.
