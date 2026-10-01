---
id: method:pivotopd
type: method
title: "PivotOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the outcome-only AppWorld TGC default"
    reason: "CANOPY remains coverage / anti-drift; PivotOPD is multi-turn OPD at pivotal mistakes"
    use_instead: "method:canopy"
  - when: "single-teacher matching distillation from a strong frozen teacher (default OPD)"
    reason: "OPD remains text matching; PivotOPD is prevent+recover multi-turn agent OPD"
    use_instead: "method:opd"
  - when: "build a SWE / issue-to-patch harness rather than train a policy"
    reason: "mini-SWE-agent is the harness; the SWE-Bench Verified number is a distill transfer, not a loop ranking"
    use_instead: "method:mini-swe-agent"
  - when: "act-first / reason-later multi-turn OPD (inverse dynamics + async full-response distill)"
    reason: "ActFirst-OPD is a wall-clock acting/reasoning split, not pivotal-mistake credit"
    use_instead: "method:actfirst-opd"
assumptions:
  - "Multi-turn interactive env with a group RL host. Teacher names gold and recovery actions in hindsight; a privileged self-teacher (frozen student + action hint) supplies token targets."
  - "Paper: Qwen3-1.7B/8B on ALFWorld / WebShop / Search-QA vs 13 baselines; Nemotron-3.5 SWE-Bench Verified transfer."
  - "Project page as of 2026-10-01: https://research.nvidia.com/labs/lpr/pivotopd/"
last_reviewed: "2026-10-01"
papers:
  - paper:pivotopd
recipes:
  - recipe:pivotopd
claims:
  - benchmark: "ALFWorld vs strongest of 13 baselines, Qwen3-1.7B"
    metric: "success-rate lift"
    value: "+5.5"
    baseline: "Strongest reported baseline on that split; also strongest average on ALFWorld/WebShop/Search-QA for 1.7B and 8B"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.40285"
    notes: "Vanilla OPD leaves pivotal-turn failures almost unchanged. Not a CANOPY retarget."
  - benchmark: "SWE-Bench Verified, Nemotron-3.5 student"
    metric: "resolve-rate lift"
    value: "+3.2"
    baseline: "Standard OPD +0.2"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.40285"
    notes: "Soft related evidence for task:software-engineering-agent-harness. Not a mini-SWE-agent retarget."
tags:
  - post-training
  - distillation
  - agentic
  - on-policy
  - pivotopd
  - active
---

# PivotOPD

## Method Overview
A turn is pivotal when the committed action lengthens the remaining optimal trajectory. PivotOPD has a teacher read each rollout, name candidate gold actions, and treat disagreement as a pivotal turn. Preventive distillation reverse-KL's the student toward a privileged self-teacher hinted with the gold action. Recovery distillation forward-KL's the student onto responses the hinted self-teacher writes for the next \(K\) recovery turns, executed in a replayed env copy. Both terms share a PPO/group-RL update.

## When to Use
- Multi-turn agent OPD where failures concentrate on an early recoverable mistake, including SWE-style tool loops.

## When NOT to Use
- AppWorld TGC coverage → `method:canopy`. Frozen-teacher text matching → `method:opd`. Issue-to-patch harness → `method:mini-swe-agent`. Wall-clock act-first distill → `method:actfirst-opd`.

## Relation to Existing SOTA
- Active plug-in on `task:outcome-only-long-horizon-agent-rl` beside `method:opd`, with a SWE-Bench mention on `task:software-engineering-agent-harness`. Does **not** enter `current_sota`. Does **not** replace CANOPY, OPD, or mini-SWE-agent.

## Gotchas & Failure Modes
- Project page, no dedicated public GitHub as of 2026-10-01.
- Pivot detection is a teacher estimate; ALFWorld oracle labeling is analysis-only.
- Recovery needs env replay from the post-mistake state. Do not skip the forward-KL recovery term and call it PivotOPD.
- Do not treat +3.2 SWE-Verified as a harness ranking.
