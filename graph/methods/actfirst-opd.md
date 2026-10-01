---
id: method:actfirst-opd
type: method
title: "ActFirst-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the outcome-only AppWorld TGC default"
    reason: "CANOPY remains coverage / anti-drift; ActFirst-OPD is a wall-clock acting/reasoning split for multi-turn OPD"
    use_instead: "method:canopy"
  - when: "single-teacher matching distillation from a strong frozen teacher (default OPD)"
    reason: "OPD remains matching; ActFirst-OPD still distills full think-then-act responses, only acting is off the critical path"
    use_instead: "method:opd"
  - when: "multi-turn agent OPD at pivotal early mistakes (prevent reverse-KL + recover forward-KL)"
    reason: "PivotOPD is credit at pivotal turns; ActFirst-OPD is inverse-dynamics rollout speed"
    use_instead: "method:pivotopd"
assumptions:
  - "Multi-turn env plus a reference trajectory that supplies next observations. Student infers actions from (context, reference next obs); switches to autonomous next-action prediction after deviation."
  - "Paper: Qwen3-0.6B/1.7B/4B on ALFWorld, WebShop, ScienceWorld vs Vanilla OPD under matched hardware and update steps."
  - "Review-anonymous code as of 2026-10-01: anonymous.4open.science/r/ActFirst-OPD."
last_reviewed: "2026-10-01"
papers:
  - paper:actfirst-opd
recipes:
  - recipe:actfirst-opd
claims:
  - benchmark: "ALFWorld / WebShop / ScienceWorld wall-clock vs Vanilla OPD"
    metric: "mean training speedup"
    value: "2.3× / 1.8× / 4.9×"
    baseline: "Vanilla think-then-act OPD, matched hardware and update steps"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36608"
    notes: "Reasoning is 81–95% of per-turn rollout time on Qwen3-1.7B ALFWorld. Not a CANOPY retarget."
  - benchmark: "Nine benchmark–model settings, mean task success vs compared OPD baselines"
    metric: "settings matching or exceeding baselines"
    value: "8 / 9"
    baseline: "Compared OPD baselines in the paper"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36608"
    notes: "Naive direct-action rollouts are not ActFirst-OPD: they raise repetition and cut successes per transition."
tags:
  - post-training
  - distillation
  - agentic
  - on-policy
  - actfirst-opd
  - active
---

# ActFirst-OPD

## Method Overview
ActFirst-OPD splits the multi-turn OPD loop. During interaction the student emits an action from inverse dynamics \(a_t\sim\pi(\cdot\mid c_t, o^{\mathrm{ref}}_{t+1})\) and steps the env. If the resulting observation leaves the reference, it switches to autonomous next-action prediction for the rest of the rollout. Off the critical path, the same student writes full think-then-act responses from collected contexts (without the reference next observation) for reverse-KL teacher OPD.

## When to Use
- Multi-turn agent OPD whose wall-clock is dominated by pre-action reasoning, when a reference trajectory is available for local next-obs targets.

## When NOT to Use
- AppWorld TGC → `method:canopy`. Frozen-teacher text matching → `method:opd`. Pivotal-mistake prevent/recover → `method:pivotopd`.

## Relation to Existing SOTA
- Active plug-in on `task:outcome-only-long-horizon-agent-rl` beside `method:opd`. Does **not** enter `current_sota`. Does **not** replace CANOPY, OPD, or PivotOPD.

## Gotchas & Failure Modes
- Review-anonymous code as of 2026-10-01. Not a named public GitHub.
- Reference next observations are for *acting*, not for the distill context. Putting them in the OPD prefix is not the paper.
- Dropping the deviation switch (always inverse-dynamics) is the direct-action ablation that loses quality.
- Needs reference trajectories. Pure online exploration without a reference is vanilla OPD.
