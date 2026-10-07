---
id: method:privileged-context-drift
type: method
title: "Privileged Context as Drift"
category: "distillation"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing privileged-teacher OPSD"
    reason: "This is a controlled-study evidence card; VISTA remains the privileged-teacher first hop"
    use_instead: "method:vista"
  - when: "unlabeled consensus OPSD"
    reason: "u-OPSD remains the unlabeled first hop"
    use_instead: "method:u-opsd"
  - when: "OPSD collapse playbook rather than a content-vs-source study"
    reason: "The collapse review is the three-lever survey; this card isolates privileged-context content"
    use_instead: "method:opsd-collapse-review"
assumptions:
  - "Controlled OPSD study. Content (demo vs feedback vs rephrase) vs source. No trainer. No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:privileged-context-drift
recipes:
  - recipe:privileged-context-drift
claims:
  - benchmark: "Privileged-context OPSD drift, content vs source"
    metric: "KL / cosine contribution of content vs source"
    value: "content drives KL 5.1× more than source; cosine 0.571 vs 0.255"
    baseline: "source-of-context as the assumed drift driver"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07842"
    notes: "Evidence/niche. Does not retarget VISTA, u-OPSD, or the collapse review."
tags:
  - post-training
  - opsd
  - drift
  - privileged-context-drift
  - niche
---

# Privileged Context as Drift

## Method Overview
Evidence node, not a trainer. Privileged-context **content** (demo vs feedback vs rephrase) drives OPSD policy drift / forgetting more than which source wrote the context.

## When to Use
- Diagnosing VISTA / u-OPSD / collapse-review runs where the privileged prefix changed and the student forgot.

## When NOT to Use
- Privileged-teacher default → `method:vista`. Unlabeled consensus → `method:u-opsd`. Survey playbook → `method:opsd-collapse-review`.

## Relation to Existing SOTA
- Niche ontology on `task:privileged-teacher-opsd` (`sota_for: []`). Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- **code: none**. Do not cite this arXiv as a performance win.
