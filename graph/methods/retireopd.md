---
id: method:retireopd
type: method
title: "RetireOPD (Self-Retiring On-Policy Distillation)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains the outcome-only first hop; RetireOPD is privileged self-OPD then retirement on ALFWorld/WebShop"
    use_instead: "method:canopy"
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains async RL; Adaptive Retirement is a teacher schedule, not straggler replay"
    use_instead: "method:sao"
  - when: "single-teacher student distillation from a larger frozen teacher"
    reason: "OPD remains the distill default; RetireOPD is agent RL with a same-loop privileged teacher"
    use_instead: "method:opd"
  - when: "privileged-teacher math OPSD with a gold solution and a deterministic verifier"
    reason: "VISTA remains that first hop; RetireOPD retires the teacher into pure agent RL"
    use_instead: "method:vista"
  - when: "teacher-free / label-free on-policy self-adaptation"
    reason: "OPSA has no teacher; RetireOPD starts with a privileged teacher and then drops it"
    use_instead: "method:opsa"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "TSD calibration of teacher–student discrepancy during OPD (not a retirement schedule)"
    reason: "Cal-OPD is residual-advantage calibration during OPD; RetireOPD is when to drop the teacher in agent RL"
    use_instead: "method:cal-opd"
assumptions:
  - "Multi-turn agent with a programmatic outcome (ALFWorld / WebShop in the paper). Privileged teacher sees skill-conditioned information the student does not."
  - "Qwen2.5 1.5B–7B. Teacher is optimized first on environment rewards; student then trains with RL+OPD until Adaptive Retirement."
  - "No official GitHub as of 2026-09-18. Does not claim AppWorld TGC SOTA."
last_reviewed: "2026-09-21"
papers:
  - paper:retireopd
recipes:
  - recipe:retireopd
claims:
  - benchmark: "ALFWorld success rate, Qwen2.5 1.5B–7B"
    metric: "success rate vs RL"
    value: "+14.1% to +18.8%"
    baseline: "environment-reward RL without privileged OPD"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20784"
    notes: "Abstract. Student also surpasses its skill-conditioned teacher in every reported setting. Not an AppWorld / CANOPY bake-off."
  - benchmark: "WebShop accuracy, Qwen2.5 1.5B–7B"
    metric: "accuracy vs RL"
    value: "+11.8% to +19.0%"
    baseline: "environment-reward RL without privileged OPD"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20784"
    notes: "Abstract. Adaptive Retirement then pure RL; not a VISTA / OPD replacement."
tags:
  - post-training
  - agentic
  - distillation
  - opsd
  - retireopd
  - active
---

# RetireOPD (Self-Retiring On-Policy Distillation)

## Method Overview
Sparse trajectory rewards on multi-turn agents invite a privileged self-teacher. RetireOPD splits the loop: a skill-conditioned teacher is optimized on environment rewards, then a skill-free student trains with RL plus OPD. Adaptive Retirement watches two signals — student–teacher discrepancy and the student's success as a fraction of the teacher's — and drops OPD when discrepancy stops shrinking and the student has caught a target fraction of teacher success. After retirement, training is RL alone. Privilege is not treated as reliability, and teacher supervision is not a fixed schedule.

## When to Use
- Multi-turn agents with a checker where a privileged skill teacher can densify an otherwise sparse outcome, and you can afford to retire that teacher mid-run.

## When NOT to Use
- AppWorld coverage protocol → `method:canopy`. Async stragglers → `method:sao`. Larger-teacher distill → `method:opd`. Privileged math OPSD → `method:vista`. No teacher → `method:opsa`. Pass@1 → `method:cispo`. TSD calibration during OPD → `method:cal-opd`.

## Relation to Existing SOTA
- Active plug-in on `task:outcome-only-long-horizon-agent-rl`. Mentions on `task:agentic-async-rl`, `task:student-distillation`, and `task:privileged-teacher-opsd`. Does **not** enter `current_sota`. Does **not** supersede `method:canopy`, `method:sao`, `method:opd`, `method:vista`, or `method:opsa`. Cal-OPD is signal calibration, not this retirement schedule.

## Gotchas & Failure Modes
- A privileged teacher can still be a bad teacher. Do not freeze OPD for the whole run.
- Retirement is two conditions, not one: discrepancy plateau **and** a success-fraction gate.
- No public trainer as of 2026-09-18.
