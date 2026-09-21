---
id: method:cal-opd
type: method
title: "Cal-OPD (Calibrated On-Policy Distillation)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-teacher student distillation is the goal and TSD calibration is not the bottleneck"
    reason: "OPD remains the distill default; Cal-OPD is a residual-advantage plug-in on top of OPD"
    use_instead: "method:opd"
  - when: "privileged-teacher math OPSD with a gold solution and a deterministic verifier (teacher update)"
    reason: "VISTA adapts the privileged teacher; Cal-OPD calibrates the student advantage and does not update the teacher"
    use_instead: "method:vista"
  - when: "Adaptive Retirement of a privileged self-OPD teacher then pure agent RL"
    reason: "RetireOPD is a teacher schedule on ALFWorld/WebShop; Cal-OPD is signal calibration during OPD"
    use_instead: "method:retireopd"
  - when: "teacher-free / label-free on-policy self-adaptation"
    reason: "Cal-OPD needs a white-box teacher and intervention probes"
    use_instead: "method:opsa"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1; Cal-OPD is an OPD plug-in"
    use_instead: "method:cispo"
assumptions:
  - "White-box teacher that can be forwarded under extra context while the student trajectory is held fixed. Paper: DAPO-17K filtered by Qwen3-235B-A22B-Instruct-2507; Avg@16 on AMC23/AIME24/25/26/HMMT26/MATH500."
  - "Default interventions are positive and negative evaluative feedback, not solution-level privilege. Relaxation λ=5. Implemented in verl on 8×H20 (4 student + 4 teacher), 100 steps, 256 trajectories/step, lr 1e-6, train response 16384."
  - "No public GitHub as of 2026-09-21. Reimplement the residual advantage on verl."
last_reviewed: "2026-09-21"
papers:
  - paper:cal-opd
recipes:
  - recipe:cal-opd
claims:
  - benchmark: "AMC23 / AIME24 / AIME25 / AIME26 / HMMT26 / MATH500 Avg@16, Qwen3-4B-Thinking-2507 → Qwen3-1.7B"
    metric: "Avg@16"
    value: 53.1
    baseline: "student 49.2 / OPD 50.8 / ExOPD 51.8 / EOPD 51.9 / Uni-OPD 50.5 / Privileged-OPD 49.3"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.21619"
    notes: "Table 3. +3.9 vs student, +2.3 vs OPD. Retains ~52–65% of original discrepancy (C_eval)."
  - benchmark: "AMC23 / AIME24 / AIME25 / AIME26 / HMMT26 / MATH500 Avg@16, Qwen3-30B-A3B-Thinking-2507 → Qwen3-4B"
    metric: "Avg@16"
    value: 69.0
    baseline: "student 66.6 / OPD 65.9 / Uni-OPD 67.6 / Privileged-OPD 64.0"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.21619"
    notes: "Table 3. +2.4 vs student, +3.1 vs OPD. Privileged-OPD degrades the student."
tags:
  - post-training
  - distillation
  - on-policy
  - opd
  - cal-opd
  - active
---

# Cal-OPD (Calibrated On-Policy Distillation)

## Method Overview
Standard OPD uses \(A^{\mathrm{OPD}}_t=\ell^T_t-\ell^S_t\) as a token advantage. Teacher log-likelihood also moves when extra context is prepended to a frozen student trajectory. That movement is Teacher Self-Deviation (TSD). Privileged OPD, which conditions the teacher on answers or solutions, enlarges it.

Cal-OPD probes the teacher with a positive and a negative intervention \(c^{\mathrm{pos}},c^{\mathrm{neg}}\) and estimates a relaxed TSD interval

\[
\hat{\mathcal{R}}^T_t=\bigl[\ell^T_t-\lambda\hat{d}^\downarrow_t,\;\ell^T_t+\lambda\hat{d}^\uparrow_t\bigr]
\]

with \(\lambda=5\) by default. The calibrated advantage is the residual outside that interval:

\[
A^{\mathrm{Cal}}_t=\bigl[L^T_t-\ell^S_t\bigr]_+-\bigl[\ell^S_t-U^T_t\bigr]_+.
\]

If the student log-likelihood sits inside \(\hat{\mathcal{R}}^T_t\), \(A^{\mathrm{Cal}}_t=0\). The student update is ordinary OPD with this advantage. Interventions are probes; they are not distilled.

## When to Use
- Running OPD (including privileged OPD) where teacher self-deviation is mixed into the discrepancy, and you can afford two extra teacher forwards per token for calibration.

## When NOT to Use
- Default single-teacher distill → `method:opd`. Privileged-teacher adaptation → `method:vista`. Teacher retirement in agent RL → `method:retireopd`. No teacher → `method:opsa`. Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation`. Mention on `task:privileged-teacher-opsd`. Does **not** enter `current_sota`. Does **not** replace `method:opd`, `method:vista`, or `method:retireopd`.
- RetireOPD is a retirement *schedule*. Cal-OPD is signal *calibration* during OPD.

## Gotchas & Failure Modes
- Default probes are evaluative feedback (`C_eval`). Solution-level privilege (`C_sol`) over-filters (avg 49.0; ~20% retained) and can drop below the student.
- \(\lambda=5\) is the reported optimum (~52% retained). Larger \(\lambda\) expands the TSD region and over-filters (λ=80 is −1.7 vs λ=1).
- Privileged-OPD as a *distill target* is the failure mode this method is built against. Do not skip calibration and distill the privileged teacher wholesale.
