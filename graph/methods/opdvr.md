---
id: method:opdvr
type: method
title: "OPDVR (On-policy Distillation with Verifiable Reward)"
category: "distillation"
status: sota
sota_for:
  - task:distill-reasoner-verifier
supersedes: []
papers:
  - paper:opdvr
recipes:
  - recipe:opdvr
claims:
  - benchmark: "AIME24 / AIME25 / AMC Reasoning Benchmarks"
    metric: "avg@16 accuracy & verifier alignment"
    value: "Outperforms standard OPD across all 6 reasoning benchmarks without extra hyperparameters"
    baseline: "Standard OPD / Vanilla RLVR"
    date: "2026-08-27"
    verified: true
    notes: "ReLU gating aligns token distillation direction with trajectory verifier correctness without weighted mixture trade-offs."
tags:
  - distillation
  - rlvr
  - reasoning
  - on-policy
  - opdvr
  - sota
---

# OPDVR (On-policy Distillation with Verifiable Reward)

## Method Overview
OPDVR integrates dense token-level on-policy teacher guidance with deterministic task-level verifiable rewards (RLVR):
1. **Implicit Reward Gating**: Reformulates sampled-token OPD implicit reward based on trajectory correctness. On correct trajectories, the token reward is $\text{ReLU}(\log(\pi_T / \pi_\theta))$; on incorrect trajectories, the token reward is $-\text{ReLU}(\log(\pi_\theta / \pi_T))$.
2. **Zero Extra Hyperparameters**: Eliminates heuristic loss weighting and trade-off knobs by directly conditioning token update directions on outcome verification while the teacher modulates magnitude.
3. **GRPD Variant**: Embeds the gated token reward into group-relative advantage estimation (GRPO/Dr.GRPO) for robust policy gradient training.

## When to Use
- When distilling mathematical, code, or logical reasoning capabilities from a strong teacher into a student policy while rule-based outcome verifiers are available.
- When standard OPD overfits to teacher errors or when pure RLVR suffers from sparse outcome credit assignment.

## Relation to Existing SOTA
- Complements `method:opd` (general distillation) and `method:cispo` (pure RL reasoning) specifically for verifiable reasoning distillation.
