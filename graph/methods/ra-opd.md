---
id: method:ra-opd
type: method
title: "RA-OPD (Reward-Aligned On-Policy Distillation)"
category: "distillation"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "no teacher is available, or teacher logits are intentionally unused"
    reason: "RA-OPD is a filter on teacher OPD; teacher-free self-adaptation is OPSA"
    use_instead: "method:opsa"
  - when: "single-teacher distillation is the goal and no outcome verifier exists"
    reason: "The alignment mask needs a binary outcome reward; unfiltered OPD remains the distill default"
    use_instead: "method:opd"
  - when: "the teacher is a privileged same-size copy that sees a gold solution"
    reason: "That shelf is VISTA, not trajectory filtering of a frozen teacher"
    use_instead: "method:vista"
assumptions:
  - "Running reverse-KL OPD with a white-box teacher and a deterministic outcome verifier."
  - "Student already samples on-policy trajectories; RA-OPD adds no extra rollouts."
  - "Paper: Qwen3-4B/8B-Base students and DeepSeek-R1-Distill-Qwen-7B; math DAPO-Math-17K, code Eurus-2-RL-Data-Code-25K."
last_reviewed: "2026-09-01"
papers:
  - paper:ra-opd
recipes:
  - recipe:ra-opd
claims:
  - benchmark: "Qwen3-8B-Base seven-bench math avg@k"
    metric: "mean avg@k"
    value: 49.43
    baseline: "OPD 44.34 / ExOPD 46.95 / Uni-OPD 45.20"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.27960"
    notes: "Table 1. k=32 on AIME/AMC, k=8 otherwise. +5.09 vs OPD."
  - benchmark: "DeepSeek-R1-Distill-Qwen-7B seven-bench math avg@k"
    metric: "mean avg@k"
    value: 69.34
    baseline: "OPD 64.43 / Uni-OPD 66.55 / ExOPD 65.55"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.27960"
    notes: "Table 2. Teacher Skywork-OR1-Math-7B. Pass@k avg 83.48 vs OPD 80.81."
  - benchmark: "Qwen3-4B-Base code (HumanEval+ / MBPP+ / LiveCodeBench v6)"
    metric: "mean avg@4"
    value: 58.97
    baseline: "OPD +3.93 / ExOPD +2.87"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.27960"
    notes: "HumanEval+ 78.81, MBPP+ 70.97, LCB v6 27.14."
tags:
  - post-training
  - distillation
  - on-policy
  - ra-opd
  - niche
---

# RA-OPD (Reward-Aligned On-Policy Distillation)

## Method Overview
RA-OPD is a trajectory filter on teacher OPD. For each student rollout $\tau$, aggregate token log-ratios into a length-normalized distillation return

\[
G=\frac1{|\tau|}\sum_t\log\frac{\pi_T(o_t\mid s_t)}{\pi_\theta(o_t\mid s_t)}
\]

and keep the trajectory iff it agrees with the binary outcome reward $R\in\{0,1\}$:

\[
m=\mathbf{1}\bigl[(2R-1)G\geq 0\bigr]
\]

Correct trajectories need $G\geq 0$ (teacher more likely than student); incorrect ones need $G\leq 0$. Misaligned trajectories are dropped. If a batch has $Z=0$ kept tokens, the distillation gradient is zero for that step. No extra student rollouts or teacher forwards.

This sits in tension with OPSA: OPSA argues teacher OPD signals are noisy and often unnecessary; RA-OPD argues that *when you are running teacher OPD*, you should keep only reward-aligned trajectories. They are not substitutes.

## When to Use
- Already running teacher OPD on verifiable math/code and you can score $R$ with a deterministic verifier.
- Uni-OPD's group-margin is too expensive (four rollouts/prompt) or undefined on reward-homogeneous groups.

## When NOT to Use
- No teacher / no verifier -> not this method (`method:opsa` or `method:cispo`).
- Intentional unfiltered distillation without an outcome check -> `method:opd`.
- Privileged same-size teacher with gold solution -> `method:vista`.

## Relation to Existing SOTA
- Niche filter on `task:student-distillation`. Does **not** supersede `method:opd` or `method:opsa`.
- Beats ExOPD and Uni-OPD in the paper's OPD-variant bake-off; those are paper baselines, not library first-hops.

## Gotchas & Failure Modes
- Dropped fraction is large (about 49% Qwen3, 68% DeepSeek-R1 in the paper). Early training drops almost all *correct* trajectories because $G$ is typically negative.
- Training on *only* the dropped conflicts still beats the untrained base but loses to OPD (RA-Inv 43.41 vs OPD 44.34 vs RA-OPD 49.43 on Qwen3-8B). Do not invert the mask.
- Needs $R\in\{0,1\}$; not defined for dense non-verifiable rewards.
