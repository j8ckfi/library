---
id: method:opsd-collapse-review
type: method
title: "OPSD Collapse Levers"
category: "distillation"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing privileged-teacher OPSD"
    reason: "This is a survey playbook; VISTA remains the privileged-teacher first hop"
    use_instead: "method:vista"
  - when: "teacher-free / label-free self-adaptation"
    reason: "OPSA remains that first hop; the review is not a substitute trainer"
    use_instead: "method:opsa"
  - when: "labeled Pass@1 RLVR"
    reason: "CISPO remains the Pass@1 kernel; GRPO stays retired"
    use_instead: "method:cispo"
assumptions:
  - "Mathematical reasoning OPSD/OPSD-adjacent literature. No new experiments in the paper."
last_reviewed: "2026-09-09"
papers:
  - paper:opsd-collapse-review
recipes:
  - recipe:opsd-collapse-review
claims:
  - benchmark: "Survey of OPSD collapse in math reasoning (no new runs)"
    metric: "playbook coverage"
    value: "three levers: token weights / privileged info / teacher dynamics"
    baseline: "papers that name collapse differently without a shared vocabulary"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.25936"
    notes: "Ontology note, not a train kernel. Does not retarget VISTA, OPSA, or CISPO."
tags:
  - post-training
  - opsd
  - survey
  - opsd-collapse-review
  - niche
---

# OPSD Collapse Levers

## Method Overview
Playbook, not a trainer. OPSD collapse (narrowing of reasoning paths) is one symptom with three levers:

1. **Where** the signal is applied — token weights / keep-masks.
2. **What** the teacher is shown — gold, plan, environment feedback.
3. **When** the signal changes — teacher dynamics and guidance decay.

Privileged information aggravates collapse; GRPO-family entropy collapse is a cousin, not the same lever set. OPSA avoids a privileged teacher and is a different shelf. Use this node to route; do not train from it.

## When to Use
- Diagnosing OPSD / privileged-teacher runs that peaked then narrowed.
- Writing a method node so VISTA / FlowBalance / Self-Routing sit on the right lever.

## When NOT to Use
- Privileged-teacher default → `method:vista`. No teacher → `method:opsa`. Pass@1 labels → `method:cispo`.
- Actionable anti-collapse trainer → `method:nsd` (this node stays the survey).

## Relation to Existing SOTA
- Niche ontology on `task:privileged-teacher-opsd` and `task:teacher-free-on-policy-self-adaptation`. Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- No code, no new numbers. Do not cite this arXiv as a performance win.
- Collapse is not uniquely OPSD; do not blame the student-teacher KL alone.
