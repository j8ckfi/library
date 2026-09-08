---
id: method:tgopd
type: method
title: "TGOPD (Teacher-Gated On-Policy Distillation)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "TGOPD is a prompt-level reliability gate on OPD, not a new distill default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR without a teacher"
    reason: "Labeled dense RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "no teacher is available"
    reason: "TGOPD still needs a frozen teacher for probes and dense OPD; teacher-free is OPSA"
    use_instead: "method:opsa"
  - when: "filtering teacher-OPD trajectories by outcome-alignment of G vs R"
    reason: "That is RA-OPD's (2R-1)G mask, a different plug-in"
    use_instead: "method:ra-opd"
  - when: "sampled-token entropy shrink on already-admitted OPD"
    reason: "IDA-OPD reweights tokens after the teacher is already in the loss"
    use_instead: "method:ida-opd"
  - when: "multi-teacher token-share balancing is the goal"
    reason: "Open-MOPD remains the multi-teacher distill default; TGOPD can wrap MOPD but does not replace it"
    use_instead: "method:open-mopd"
assumptions:
  - "White-box frozen teacher, a deterministic outcome verifier, and an asynchronous student-rollout / teacher-score loop so probes can occupy idle teacher time."
  - "Paper: Qwen3.5-4B and Qwen3.6-35B-A3B students; same-arch GRPO-trained domain teachers; slime + IcePop; K_T=3, τ=2/3; DAPO-Math-17K / CodeI/O / Nemotron-Cascade 2 IF."
  - "Branches are exclusive. Do not add OPD and GRPO advantages on the same prompt."
last_reviewed: "2026-09-08"
papers:
  - paper:tgopd
recipes:
  - recipe:tgopd
claims:
  - benchmark: "Qwen3.5-4B LiveCodeBench pass@1 (code-domain SOPD)"
    metric: "pass@1"
    value: 47.1
    baseline: "Vanilla OPD 42.3 / base 39.4 / teacher 53.3; TrOPD 49.6 / RG-OPD 45.6"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.02998"
    notes: "Table 1. Vanilla OPD closes 21% of the base-to-teacher LCB gap; TGOPD closes 55%. TrOPD is higher on this one column; TGOPD wins the code-domain pair with OJBench 20.0 vs TrOPD 18.1."
  - benchmark: "Qwen3.6-35B-A3B LiveCodeBench / OJBench (code-domain SOPD)"
    metric: "pass@1 / OJBench"
    value: "64.0 / 28.7"
    baseline: "Vanilla OPD 60.2 / 26.7; base 61.0 / 26.1; teacher 62.7 / 27.6"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.02998"
    notes: "Table 1. Only TGOPD is positive transfer on 35B LCB; other distill methods go below base."
  - benchmark: "Qwen3.5-4B AIME 2025 / AIME 2026 (math-domain SOPD)"
    metric: "accuracy"
    value: "64.8 / 73.5"
    baseline: "Vanilla OPD 61.1 / 71.2; teacher 63.4 / 73.4; base 47.8 / 58.1"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.02998"
    notes: "Table 1. HMMT-Feb 52.7 vs Vanilla OPD 54.3 vs TrOPD 56.8 — TGOPD is not uniformly best on every math column."
  - benchmark: "4B SOPD teacher-node GPU utilization"
    metric: "mean utilization (1-hour window)"
    value: "78.9% (0% idle)"
    baseline: "Vanilla OPD 9.8% (59% of samples below 5%)"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.02998"
    notes: "Table 3 / Figure 1. Cluster average 51.5% → 69.5%. MOPD 4B teacher 7.0% → 66.6%."
tags:
  - post-training
  - distillation
  - on-policy
  - teacher-gating
  - tgopd
  - active
---

# TGOPD (Teacher-Gated On-Policy Distillation)

## Method Overview
TGOPD is a prompt-level reliability gate in front of dense OPD. While the student decodes a group, the frozen teacher spends otherwise-idle time on $K_T$ probe rollouts. A verifier scores them; $q_T(x)=K_T^{-1}\sum_k r_k$. If $q_T(x)\ge\tau$, the update is sampled-token reverse-KL OPD. Otherwise the teacher signal is withheld and the update is verifier-grounded GRPO (zero if the student group has no reward variation). The selector is

\[
\hat A^{\mathrm{TGOPD}}_{i,t}=g(x)\,\hat A^{\mathrm{OPD}}_{i,t}+\bigl(1-g(x)\bigr)\,\hat A^{\mathrm{GRPO}}_{i,t},\qquad g(x)\in\{0,1\}.
\]

Default $K_T=3$, $\tau=2/3$. Sits beside `method:ra-opd` (trajectory mask after scoring) and `method:ida-opd` (token entropy shrink). None of them replace OPD.

## When to Use
- Already running asynchronous teacher OPD and the teacher is sometimes confidently wrong, especially on code.
- Reclaiming idle teacher GPUs is a bonus, not the reason to pick this over CISPO.

## When NOT to Use
- Distill default → `method:opd`. Labeled Pass@1 RLVR → `method:cispo`. No teacher → `method:opsa`.
- Trajectory alignment filter → `method:ra-opd`. Token entropy plug-in → `method:ida-opd`. Multi-teacher mix → `method:open-mopd`.

## Relation to Existing SOTA
- Active OPD plug-in on `task:student-distillation`. Optional mention on `task:math-code-rl-dense`. Does **not** supersede `method:opd`, `method:cispo`, `method:opsa`, or `method:open-mopd`.
- Distinct from RA-OPD (keep/drop already-scored student trajectories) and from VISTA (privileged same-model teacher adaptation).

## Gotchas & Failure Modes
- No official code as of 2026-09-08. Paper stack is slime + IcePop, not a drop-in for every OPD trainer.
- Do not interpolate OPD and GRPO on one prompt. The paper's point is exclusive routing.
- Not uniformly best on every column (4B HMMT-Feb, 4B LCB vs TrOPD). Use the domain average and the 35B LCB negative-transfer result.
- Probe overlap is substantial but not wall-clock free (Appendix D). Utilization ≠ zero overhead.
- GRPO here is the fallback branch, not a revival of GRPO as the library Pass@1 default.
