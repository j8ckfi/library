---
id: method:onepo
type: method
title: "OnePO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "general chat / instruct SFT stack"
    reason: "OLMo-3 Dolci remains the open instruct default; OnePO is RL-only domain adaptation from a base model"
    use_instead: "method:olmo-3"
  - when: "labeled dense Pass@1 math/code RLVR"
    reason: "CISPO remains Pass@1; OnePO is domain adaptation from a base checkpoint"
    use_instead: "method:cispo"
assumptions:
  - "Base (not already SFT'd) checkpoint, target-domain teacher traces you can retire. Paper: medical HealthBench; 20K samples for 67.2 Total."
  - "Code: FreedomIntelligence/HuatuoGPT-3 (`code_status: released`)."
last_reviewed: "2026-10-06"
papers:
  - paper:onepo
recipes:
  - recipe:onepo
claims:
  - benchmark: "HealthBench Total, RL-only medical adaptation, 20K samples"
    metric: "HealthBench Total"
    value: "67.2 (+2.7 vs SFT+RL / +7.4 vs pure RL)"
    baseline: "SFT+RL / pure RL"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05966"
    notes: "HuatuoGPT-3 27B: 70.1 Total / 71.4 Professional. Does not retarget OLMo-3 or CISPO."
tags:
  - post-training
  - rl-alignment
  - onepo
  - active
---

# OnePO

## Method Overview
OnePO (One-stage Policy Optimization) RL-adapts a base model to a domain without an SFT stage. Teacher traces are transient: the objective up-weights informative low-probability teacher tokens early, then retires those traces once the policy beats them.

## When to Use
- Domain adaptation from a base model where SFT+RL is shrinking exploration and you have teacher traces you are willing to retire.

## When NOT to Use
- General instruct stack → `method:olmo-3`. Math/code Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:instruct-sft-alignment` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OLMo-3 or CISPO.

## Gotchas & Failure Modes
- **code: released** FreedomIntelligence/HuatuoGPT-3 as of 2026-10-06.
- Teacher Retirement is required; leaving mixed-policy traces in late training is the paper's Teacher-Distribution Anchoring failure.
