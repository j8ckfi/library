---
id: method:off-policy-grafting
type: method
title: "Off-Policy Grafting"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "multi-stage agent capability stacking (ACLArena / routed LoRA experts)"
    reason: "ACLArena remains the agent-CL first hop; grafting is a merge recipe vs OPSD"
    use_instead: "method:aclarena"
  - when: "multi-model all-fail GRPO salvage by peer trajectory exchange"
    reason: "method:graft is GRAFT on math RLVR, not this continual-learning merge"
    use_instead: "method:graft"
  - when: "privileged-teacher OPSD as the train kernel"
    reason: "VISTA remains privileged OPSD; this card is a CL caveat against OPSD"
    use_instead: "method:vista"
assumptions:
  - "Post-trained model, new off-policy data, forgetting is the complaint. Paper: Chen Henry Wu, Thomas Zhang, Aditi Raghunathan."
  - "No public code as of 2026-10-06 (`code_status: none`). Not GRAFT (`method:graft`)."
last_reviewed: "2026-10-06"
papers:
  - paper:off-policy-grafting
recipes:
  - recipe:off-policy-grafting
claims:
  - benchmark: "continual learning vs on-policy self-distillation (abstract)"
    metric: "off-policy merging vs OPSD"
    value: "off-policy merging beats OPSD for continual learning"
    baseline: "on-policy self-distillation (OPSD)"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05872"
    notes: "Does not retarget ACLArena. Distinct from GRAFT (method:graft). No numeric table in the abstract."
tags:
  - post-training
  - continual-learning
  - off-policy-grafting
  - active
---

# Off-Policy Grafting

## Method Overview
Grafting SFT's a donor copy of the checkpoint on the new data, then scaled-merges those weights back so the useful SFT signal does not overwrite existing capabilities. The paper uses this as a caveat against OPSD for continual learning.

## When to Use
- Continual add of off-policy data on a post-trained model where OPSD collapse is the alternative you were about to run.

## When NOT to Use
- Agent stage stacking → `method:aclarena`. All-fail GRPO salvage → `method:graft`. Privileged OPSD kernel → `method:vista`.

## Relation to Existing SOTA
- Active plug-in / caveat on `task:agent-continual-learning` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace ACLArena.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Do not confuse with `method:graft` (GRAFT).
- Abstract has no numeric table; do not invent one.
