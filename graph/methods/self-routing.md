---
id: method:self-routing
type: method
title: "Self-Routing (Behavior-Conditioned Post-Training)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code RLVR optimizer"
    reason: "Self-Routing is a sample-level recipe router on top of GRPO/OPSD; CISPO remains the Pass@1 default"
    use_instead: "method:cispo"
  - when: "no verifier and no ground-truth answers"
    reason: "OPSD branch needs target answers; teacher-free unlabeled self-adaptation is OPSA"
    use_instead: "method:opsa"
  - when: "a strong external teacher is the point of the run"
    reason: "Self-Routing's OPSD teacher is the same model with the answer, not a frontier teacher"
    use_instead: "method:opd"
assumptions:
  - "Verifiable outcome reward plus ground-truth answers for the OPSD branch. Paper trains on DAPO-Math-17K."
  - "Group rollouts already collected (G=8 in the paper). Router uses those rollouts; no extra sampling."
  - "ms-swift implementation planned, not released as of 2026-09-04."
last_reviewed: "2026-09-04"
papers:
  - paper:self-routing
recipes:
  - recipe:self-routing
claims:
  - benchmark: "Qwen3-4B six-bench avg (GSM8K / MATH-500 / AIME24 / AIME25 / MMLU-Pro / GPQA-diamond)"
    metric: "macro average"
    value: 73.7
    baseline: "Naive-GRPO 66.8 / Naive-OPSD 70.4 / base 61.0"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.01422"
    notes: "Table 1. AIME24 83.6 vs GRPO 74.3 vs OPSD 79.4."
  - benchmark: "Qwen3.5-4B six-bench avg"
    metric: "macro average"
    value: 86.6
    baseline: "Naive-GRPO 79.8 / Naive-OPSD 83.0 / base 76.8"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.01422"
    notes: "Table 1. Gains widen with scale."
tags:
  - post-training
  - rlvr
  - routing
  - self-routing
  - active
---

# Self-Routing (Behavior-Conditioned Post-Training)

## Method Overview
Self-Routing is a sample-level router over four already-known recipes, with no external teacher:

| State | Recipe |
| :--- | :--- |
| Mixed / uncertain correctness | GRPO |
| Low accuracy, not confident-fail | on-policy self-distillation (same model + gold answer) |
| High accuracy + high relative confidence | KL regularization to the reference |
| Low accuracy + confident failure | skip |

Accuracy is a smooth three-way membership around 0 / 0.5 / 1, not a hard threshold. Confidence is mean token entropy, batch-normalized. Scores are normalized to a categorical draw so each sample hits one queue per step.

Active plug-in beside CISPO and OPSA. Does not replace either.

## When to Use
- Already collecting group rollouts for GRPO-style RLVR and uniform GRPO vs uniform OPSD is leaving mixed samples and confident failures on the same objective.
- You have answers for an OPSD branch but no external teacher.

## When NOT to Use
- Pass@1 labeled RLVR default -> `method:cispo`.
- No labels / no answers -> `method:opsa`.
- Frontier teacher distillation -> `method:opd`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` / `task:teacher-free-on-policy-self-adaptation` (OPSD branch is self-contained, not OPSA). Does **not** supersede `method:cispo` or `method:opsa`.

## Gotchas & Failure Modes
- OPSD in this paper is answer-conditioned same-model distillation, precomputed offline — not live teacher logits and not OPSA's entropy-adaptive negatives.
- Not cheaper than uniform OPSD (34.7 vs 24.0 normalized FLOPs at G=8). Cheaper than uniform GRPO (64.0).
- Weak models give noisier routing signals; the paper's gains widen with scale.
- ms-swift code was planned, not released as of 2026-09-04. Implement the router in the host trainer; do not wait for a package.
