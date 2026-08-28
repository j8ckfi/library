---
id: method:ttpo
type: method
title: "TTPO (Test-Time Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:label-free-test-time-reasoner
supersedes: []
papers:
  - paper:ttpo
recipes:
  - recipe:ttpo
claims:
  - benchmark: "AIME24 / AIME25 / AMC23 / MATH500 / OlympiadBench Test-Time Adaptation"
    metric: "accuracy under test-time training (TTT)"
    value: "Matches label-supervised OPSD without labels; Qwen3-1.7B gains 38.0% -> 45.2%; +25.2% to +36.4% on non-thinking baselines"
    baseline: "Unsupervised Majority-Vote Distillation / Base Model / Supervised OPSD"
    date: "2026-08-28"
    verified: true
    notes: "Asymmetric objective: distill agreeing rollouts via OPSD, penalize disagreeing rollouts with Grouped RL with token-level filtering."
tags:
  - test-time-training
  - reasoning
  - rl-alignment
  - distillation
  - ttpo
  - sota
---

# TTPO (Test-Time Policy Optimization)

## Method Overview
Test-Time Policy Optimization (TTPO) resolves the brittleness of consensus pseudo-labels during test-time adaptation:
1. **Asymmetric Error Exploitation**: While an erroneous majority vote corrupts standard distillation teachers, completions that disagree with the vote are almost universally wrong. TTPO therefore decouples agreed vs. disagreed trajectories.
2. **Dual Optimization Formulation**:
   - **Agreeing Rollouts**: Distilled via token-level on-policy self-distillation (OPSD) conditioned on the consensus pseudo-solution. Down-weights already-converged token positions.
   - **Disagreeing Rollouts**: Penalized via Grouped RL policy gradients, focusing specifically on confident incorrect tokens.
3. **Dynamic Self-Supervision**: As test-time policy adaptation progresses, majority-vote accuracy rises, progressively tightening the self-supervision signal without human or teacher intervention.

## When to Use
- When deploying reasoning models at test time with compute budgets allocated for dynamic problem adaptation (Test-Time Training / TTT).
- When operating in open domains or math/code competitions where ground-truth verification and external teachers are unavailable.

## Relation to Existing SOTA
- Complementary to `method:opdvr` (which requires ground-truth verifiers/teachers during training) and `method:cispo` (train-time reinforcement learning with verifiable rewards). TTPO provides the label-free test-time reasoning standard.
