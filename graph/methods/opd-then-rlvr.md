---
id: method:opd-then-rlvr
type: method
title: "OPD-then-RLVR"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "This is a stacking order on top of OPD then RLVR, not a new distill default"
    use_instead: "method:opd"
  - when: "choosing the dense math/code RLVR algorithm"
    reason: "The paper's RL stage is GRPO; Pass@1 labeled default remains CISPO"
    use_instead: "method:cispo"
  - when: "you want a single-step gated OPD+RLVR algorithm (ReLU correctness gating)"
    reason: "That shelf is OPDVR, not a two-stage schedule"
    use_instead: "method:opdvr"
  - when: "no teacher is available"
    reason: "Stage-1 OPD needs a white-box teacher; teacher-free is OPSA"
    use_instead: "method:opsa"
  - when: "you will run only RLVR or only OPD"
    reason: "There is nothing to sequence; use the matching first hop"
    use_instead: "method:cispo"
assumptions:
  - "You will run both OPD and RLVR. Paper: Qwen3-1.7B-Base student, Qwen3-8B non-thinking teacher, veRL, G=8, AdamW 1e-6, clip 0.2, no KL penalty, mask student EOS in the teacher term."
  - "Default switch S=60 of 150 (logic) / 120 (DeepMath) steps. Switch when OPD validation saturates, not on a fixed step if the curve is still climbing."
  - "Does not retarget method:opd or method:cispo. It is the stacking order when both are used, against joint one-step fusion."
last_reviewed: "2026-09-08"
papers:
  - paper:opd-then-rlvr
recipes:
  - recipe:opd-then-rlvr
claims:
  - benchmark: "Qwen3-1.7B-Base ← Qwen3-8B, Knights&Knaves / Zebra / Countdown pass@1 avg@32 mean"
    metric: "pass@1 mean (avg@32)"
    value: 80.6
    baseline: "GRPO 49.4 / OPD 53.9 / KDRL 62.8 / KDRL-Annealing 68.9 / teacher 59.9"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04108"
    notes: "Table 2. pass@32 98.3 vs OPD 94.9 vs GRPO 68.1. K&K pass@1 92.6 vs OPD 50.5 vs GRPO 28.1."
  - benchmark: "Qwen3-1.7B-Base ← Qwen3-8B, MATH-500 / AMC23 / AIME24 / AIME25 pass@1 avg@32 mean"
    metric: "pass@1 mean (avg@32)"
    value: 31.8
    baseline: "OPD 31.0 / GRPO 28.4 / SRPO 31.6 / KDRL 29.0"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04108"
    notes: "Table 2. pass@32 58.5 vs OPD 55.9. Bootstrap: significant vs six of nine methods on pass@1; tie with OPD / SRPO / KDRL-mask."
  - benchmark: "DeepMath cold start then GRPO, math pass@1 / pass@32 mean"
    metric: "pass@1 / pass@32 mean"
    value: "31.8 / 58.5"
    baseline: "SFT-then-GRPO 26.1 / 54.1; OPD-only 30.3 / 51.3; SFT-only 25.4 / 56.6"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04108"
    notes: "Table 8. OPD is the better cold start; SFT-then-RL drops pass@32."
tags:
  - post-training
  - distillation
  - rlvr
  - scheduling
  - opd
  - active
---

# OPD-then-RLVR

## Method Overview
When you will run both on-policy distillation and RLVR, **sequence them**. Stage 1: reverse-KL OPD on student rollouts ($A_t = d_t = \log\pi_T-\log\pi_\theta$). Stage 2: outcome GRPO ($A_t=\hat{A}$). Do not add $w_R\hat{A}+w_T d_t$ or rescale $\hat{A}$ by a teacher factor inside one step.

This is stacking-order guidance. It does **not** replace `method:opd` as the distill algorithm or `method:cispo` as the Pass@1 RLVR algorithm. It is what to do instead of joint one-step fusion (KDRL / SRPO / HDPO / TRRD / RLSD) when both signals are on the table. `method:opdvr` remains the single-step gated OPD+RLVR default on `task:distill-reasoner-verifier`.

Paper RL is GRPO. If the host Pass@1 trainer is CISPO, keep CISPO in stage 2 — the finding is "OPD then RL", not "revive GRPO".

## When to Use
- A white-box teacher and a verifier are both available, and you were about to mix their advantages in one update.
- You need a cold start for RLVR and can afford an OPD stage; switch when OPD val saturates.

## When NOT to Use
- Distill-only → `method:opd`.
- RLVR-only Pass@1 → `method:cispo`.
- Single-step ReLU-gated OPD+RLVR → `method:opdvr`.
- No teacher → `method:opsa`.

## Relation to Existing SOTA
- Active recipe-order note on `task:student-distillation` and `task:math-code-rl-dense`. Does **not** supersede `method:opd` or `method:cispo`. Does **not** supersede `method:opdvr`.
- Relative to joint one-step OPD+RL mixes: sequential is the reported default stacking order. That is not a graph `supersedes` edge on OPD, CISPO, or OPDVR.

## Gotchas & Failure Modes
- Switching before OPD val saturates caps the RL ceiling (K&K / Zebra). On Countdown, OPD saturates by step 20 and all switch points converge.
- Joint additive methods are $\beta$-sensitive; do not treat a bad $\beta$ as a reason to skip sequencing.
- Mask the student EOS token in the teacher term when tokenizers disagree (`<|endoftext|>` vs `<|im_end|>`).
- Math margins vs OPD/SRPO are small; logic is the load-bearing table.
