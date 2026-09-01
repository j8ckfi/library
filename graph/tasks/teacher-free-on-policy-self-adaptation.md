---
id: task:teacher-free-on-policy-self-adaptation
type: task
title: "Teacher-Free Label-Free On-Policy Self-Adaptation"
domain: "post-training"
summary: "Train-time on-policy improvement of a reasoning policy from its own token log-probabilities and entropies, without a teacher, reward model, ground-truth labels, or hint-conditioned self-teacher."
scope: "Train-time supervision-free on-policy self-adaptation that suppresses low-logp tokens with entropy-adaptive negative advantages."
out_of_scope:
  - "Labeled math/code RLVR with verifiable rewards (CISPO)"
  - "Single-teacher or multi-teacher student distillation (OPD / Open-MOPD)"
  - "Privileged-teacher OPSD with gold solutions (VISTA)"
  - "Unlabeled existing math problems using rollout-consensus pseudo-solutions (u-OPSD)"
  - "Test-time unlabeled adaptation (TTPO)"
  - "Data-free Challenger-Solver-Judge curriculum generation (J-Zero)"
  - "Teacher-free flow-matching / diffusion alignment (Self-OPD)"
redirects:
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "a strong teacher is available and the goal is intentional distillation"
    to: "task:student-distillation"
  - when: "unlabeled existing math problems with majority-vote pseudo-solutions"
    to: "task:label-free-reasoner-posttrain"
  - when: "test-time adaptation on unlabeled queries"
    to: "task:label-free-test-time-reasoner"
  - when: "zero external problems, including unverifiable domains"
    to: "task:data-free-self-evolution"
  - when: "flow matching or continuous diffusion post-training"
    to: "task:posttrain-diffusion"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:opsa
    as_of: "2026-09-01"
    benchmark: "AIME24 / AIME25 / HMMT25 Avg@32 (Qwen3-1.7B non-thinking)"
    metric: "Avg@32 accuracy"
    value: "OPSA 48.85 / 35.31 / 23.33 vs base 13.44 / 9.69 / 5.73; beats OPD 32.08 / 20.52 / 13.85 and GRPO 33.96 / 25.31 / 15.10"
    notes: "OPSA (2608.31046). Supervision-free. Does not replace CISPO when labels exist or OPD when intentional teacher distillation is the goal."
methods:
  - method:opsa
  - method:ra-opd
  - method:u-opsd
  - method:ttpo
  - method:opd
  - method:cispo
tags:
  - post-training
  - on-policy
  - teacher-free
  - label-free
  - self-adaptation
  - opsa
---

# Teacher-Free Label-Free On-Policy Self-Adaptation

## Problem Definition
Improve a reasoning policy at train time using only on-policy rollouts and the policy's own token log-probabilities and entropies. No teacher logits, no verifiable outcome reward, no hint-conditioned self-teacher, and no majority-vote pseudo-solution. The typical failure of nearby methods is either requiring external supervision (OPD, RLVR) or collapsing Pass@K by sharpening around a consensus mode (TTRL-style self-reward).

## Evaluation Protocol & Benchmarks
- **Primary Benchmarks**: AIME24, AIME25, HMMT25 Avg@32 and Pass@32 on Qwen3 / Qwen3.5 non-thinking models trained on DAPO-17k questions only.
- **Evaluation Pitfalls**: Do not treat OPSA wins over OPD as a reason to drop teachers when the actual goal is knowledge transfer. Do not swap CISPO for OPSA when labels exist.

## SOTA Recommendation (as of 2026-09-01)
- **Primary Method**: **OPSA** (`method:opsa`, `paper:opsa` `arXiv:2608.31046`) for supervision-free entropy-adaptive negative advantages on the lowest-logp tokens.
- **Not This Task**: `method:cispo` remains labeled dense RLVR; `method:opd` remains single-teacher distillation; `method:u-opsd` remains unlabeled consensus distillation; `method:ttpo` remains test-time; `method:j-zero` remains data-free self-evolution; `method:self-opd` remains flow matching.
