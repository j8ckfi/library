---
id: method:respo
type: method
title: "ReSPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR loss"
    reason: "ReSPO is an off-policy sequence kernel; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "cancellation-aware off-policy response mask (absolute token log-ratios)"
    reason: "CARM is a keep-mask; ReSPO reshapes the sequence kernel"
    use_instead: "method:carm"
  - when: "MoE train-infer mismatch IS on log-odds displacement"
    reason: "CIS-RL caps engine mismatch; ReSPO is clip starvation on reused rollouts"
    use_instead: "method:cis-rl"
assumptions:
  - "Rollouts are reused across policy updates (off-policy IS mismatch). Sequence-level kernel."
  - "Code: yhangchen/ReSPO-code (`code_status: released`). HF Daily 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:respo
recipes:
  - recipe:respo
claims:
  - benchmark: "Off-policy RLVR with reused rollouts on dense and MoE Qwen3"
    metric: "whether rare positives keep a nonzero gradient weight vs clipped IS"
    value: "two-branch alpha-divergence kernel keeps under-generated positives and damps over-generated negatives; faster early training and higher held-out scores"
    baseline: "clipped IS / GRPO-family sequence clip"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.35433"
    notes: "HF Daily 2026-10-09. Does not retarget CISPO or CARM." 
tags:
  - post-training
  - rlvr
  - off-policy
  - respo
  - active
---

# ReSPO

## Method Overview
Replace the hard IS clip with a smooth two-branch sequence kernel. The positive branch stays nonzero at low importance weights so rare successes still train. The negative branch damps the high-weight tail so over-generated failures cannot dominate.

## When to Use
- Off-policy or reused-rollout RLVR where clipping starves rare correct traces.

## When NOT to Use
- On-policy Pass@1 kernel -> `method:cispo`. Absolute-log-ratio sequence mask -> `method:carm`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` (`sota_for: []`) with a mention on `task:frontier-rl-posttrain-stack`. Does **not** replace CISPO or CARM.

## Gotchas & Failure Modes
- **code: released** yhangchen/ReSPO-code as of 2026-10-09.
- Alpha and the tilt are real HPs. Not a drop-in for on-policy CISPO.
