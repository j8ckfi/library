---
id: method:mend
type: method
title: "MEND"
category: "diffusion-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "on-policy self-distillation with bounded intermediate clean-output targets (images)"
    reason: "DiffusionOPSD remains that hop; MEND is proximal velocity matching for flows"
    use_instead: "method:diffusion-opsd"
  - when: "teacher-free flow matching multi-objective alignment"
    reason: "Self-OPD remains teacher-free flow alignment; MEND is reward-capped velocity matching"
    use_instead: "method:self-opd"
assumptions:
  - "Flow / velocity model with a reward. Paper: ~100 updates vs Flow-GRPO ~4k."
  - "No public URL as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:mend
recipes:
  - recipe:mend
claims:
  - benchmark: "flow-model reward post-train vs Flow-GRPO"
    metric: "evaluators won at matched distance to base-model images"
    value: "5 of 6 evaluators after 100 updates vs Flow-GRPO ~4k"
    baseline: "Flow-GRPO (~4k updates) / ReFL / DiffusionNFT"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05954"
    notes: "Does not retarget DiffusionOPSD or Self-OPD. Do not invent PickScore 24.03 from outside the abstract."
tags:
  - diffusion
  - post-training
  - mend
  - active
---

# MEND

## Method Overview
MEND caps high rewards inside a prompt group, proposes a reward-gradient displacement only below the cap, accepts it when the capped gain beats a quadratic price, and trains the flow by matching that target velocity. No KL term and no frozen reference.

## When to Use
- Flow-model reward post-train where Flow-GRPO's thousands of updates are the cost, and you can run a velocity-matching inner step.

## When NOT to Use
- Image OPSD targets → `method:diffusion-opsd`. Teacher-free flow multi-objective → `method:self-opd`.

## Relation to Existing SOTA
- Active plug-in on `task:posttrain-diffusion` beside `method:diffusion-opsd` / `method:self-opd` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace DiffusionOPSD or Self-OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Samples already above the group cap get no move.
- Do not invent evaluator numbers absent from the abstract.
