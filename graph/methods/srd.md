---
id: method:srd
type: method
title: "SRD"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR loss"
    reason: "SRD is hindsight-to-foresight when groups are silent; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "all-zero verifier groups as a skip/filter problem"
    reason: "VeriGate gates process supervision; SRD distills hindsight into foresight"
    use_instead: "method:verigate"
  - when: "privileged same-size gold teacher OPSD"
    reason: "VISTA remains privileged-teacher first hop; SRD has no gold teacher"
    use_instead: "method:vista"
  - when: "verifier-grounded trajectory-balance self-improvement"
    reason: "FlowBalance is trajectory-balance; SRD is foresight distillation"
    use_instead: "method:flowbalance"
assumptions:
  - "Group rollouts exist. Useful when many groups are all-equal / silent."
  - "Code: SalesforceAIResearch/SRD (`code_status: released`). Top HF Daily 2026-10-08." 
last_reviewed: "2026-10-09"
papers:
  - paper:srd
recipes:
  - recipe:srd
claims:
  - benchmark: "10 tool-integrated / long-horizon tasks; 2B all-failure groups"
    metric: "success vs RLVR when group advantages vanish"
    value: "up to +24.2 pp; 2B 98% all-fail groups RLVR 0.0% vs SRD 60.6% at matched rollouts"
    baseline: "GRPO-family outcome RLVR (zero advantage on all-equal groups)"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.08077"
    notes: "Top HF Daily 2026-10-08. Does not retarget CISPO, VISTA, or VeriGate." 
tags:
  - post-training
  - rlvr
  - distillation
  - srd
  - silent-groups
  - active
---

# SRD

## Method Overview
After a group finishes, build a hindsight description of what mattered and what failed. Distill that into a foresight head or prefix of the same policy that sees only the pre-act context. Use it when the verifier assigned the same reward to every rollout, so GRPO-family advantages are zero.

## When to Use
- Silent / all-equal RLVR groups whose traces still show task structure, including tool-integrated agents.

## When NOT to Use
- Pass@1 kernel -> `method:cispo`. Gold privileged teacher -> `method:vista`. Skip silent groups -> `method:verigate`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` (`sota_for: []`) with a mention on `task:all-zero-verifier-groups`. Does **not** replace CISPO, VISTA, VeriGate, or FlowBalance.

## Gotchas & Failure Modes
- **code: released** SalesforceAIResearch/SRD as of 2026-10-09.
- Foresight that leaks hindsight tokens at deploy is a train/serve bug.
