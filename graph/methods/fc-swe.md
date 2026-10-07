---
id: method:fc-swe
type: method
title: "FC-SWE"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "category see-saw on heterogeneous SWE RL"
    reason: "FC-SWE reuses a failed patch as recovery context; Category-Aware SWE Experts remain the see-saw first hop"
    use_instead: "method:category-aware-swe-experts"
  - when: "GitHub issue to patch / SWE harness loop"
    reason: "mini-SWE-agent remains the start/eval loop"
    use_instead: "method:mini-swe-agent"
  - when: "production post-train stack"
    reason: "Miles remains the engine"
    use_instead: "method:miles"
assumptions:
  - "Executable SWE instances with a verifier. Paper: SWE-bench Verified 500, Qwen3.5-4B + SWE-agent."
  - "No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:fc-swe
recipes:
  - recipe:fc-swe
claims:
  - benchmark: "SWE-bench Verified 500, Qwen3.5-4B + SWE-agent"
    metric: "Resolved@1 / @2 / @11"
    value: "41.7 / 52.8 / 70.7"
    baseline: "GRPO 38.9 / 48.5 / 67.3"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07898"
    notes: "Reuse failed patch + verifier feedback as recovery context. Does not replace Category-Aware SWE Experts."
tags:
  - post-training
  - agentic
  - swe
  - fc-swe
  - active
---

# FC-SWE

## Method Overview
Failure-conditioned RL for SWE agents. After a failed patch, keep the patch and the verifier feedback in context for the recovery attempt instead of restarting blank.

## When to Use
- Long-horizon SWE RL where recovery attempts currently discard the failed trajectory.

## When NOT to Use
- Category see-saw → `method:category-aware-swe-experts`. Issue-to-patch harness → `method:mini-swe-agent`.

## Relation to Existing SOTA
- Active plug-in on `task:swe-agent-category-expert-rl` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Category-Aware SWE Experts.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-07.
- Resolved@k on Verified 500 is not a Pro-618 category-expert card.
