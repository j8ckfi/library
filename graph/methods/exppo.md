---
id: method:exppo
type: method
title: "ExPPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "labeled dense Pass@1 RLVR loss"
    reason: "CISPO remains Pass@1; ExPPO reshapes an existing group advantage"
    use_instead: "method:cispo"
  - when: "asymmetric entropy×sign exploration credit"
    reason: "EAPO is entropy×sign; ExPPO is surprisal + pass-rate shaping"
    use_instead: "method:eapo"
assumptions:
  - GRPO-family host with a verifier. Paper reports coverage / diversity, not a Pass@1 bake-off vs CISPO.
  - "Code: jinhangzhan/ExPPO (`code_status: released`)."
last_reviewed: "2026-10-06"
papers:
  - paper:exppo
recipes:
  - recipe:exppo
claims:
  - benchmark: "in-domain / OOD reasoning coverage under group-relative RLVR"
    metric: "coverage / aggregate accuracy / verified-correct diversity"
    value: "improved in-domain and OOD coverage; higher aggregate accuracy; more diverse verified-correct modes"
    baseline: "group-relative equal-advantage (GRPO-family)"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.04011"
    notes: "Does not retarget CISPO. No numeric table in the abstract."
tags:
  - post-training
  - rl-alignment
  - exppo
  - active
---

# ExPPO

## Method Overview
ExPPO redistributes a GRPO-family group's advantages using prompt-relative length-normalized surprisal and prompt pass rate, with shared normalization so the verifier sign and the group's total absolute advantage mass stay approximately the same.

## When to Use
- GRPO-family RLVR where equal credit on equal rewards is collapsing rare correct modes.

## When NOT to Use
- Pass@1 default → `method:cispo`. Entropy×sign credit → `method:eapo`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` beside `method:cispo` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO.

## Gotchas & Failure Modes
- **code: released** jinhangzhan/ExPPO as of 2026-10-06.
- Do not break verifier polarity; shaping is bounded.
- No numeric Pass@1 table in the abstract.
