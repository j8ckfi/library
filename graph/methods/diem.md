---
id: method:diem
type: method
title: "DIEM (Dynamic Important Example Mining)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code RLVR optimizer"
    reason: "DIEM is a batch-reweight plug-in, not an RL objective; CISPO remains the Pass@1 default"
    use_instead: "method:cispo"
  - when: "token-level truncation inside an already-computed GRPO/CISPO loss"
    reason: "That shelf is GMTS; DIEM reweights examples, not tokens"
    use_instead: "method:gmts"
  - when: "training-data attribution / LOO influence as a diagnostic"
    reason: "DIEM's alignment score is a cheap RFT proxy, not MAGIC/Bergson LDS"
    use_instead: "method:magic"
assumptions:
  - "Host RFT already computes per-sample policy gradients in the minibatch (GRPO/PPO/GPG-family)."
  - "Paper: veRL, Qwen 1.7B-7B math and Qwen2.5-VL-7B/32B; prompt batch 64, 8 rollouts, mini-batch 32, lr 1e-6, 16x H200."
last_reviewed: "2026-09-04"
papers:
  - paper:diem
recipes:
  - recipe:diem
claims:
  - benchmark: "Qwen3-4B five-bench math avg (MATH-500 / Gaokao23en / AMC-23 / AIME24 / AIME25)"
    metric: "average accuracy"
    value: 40.66
    baseline: "GRPO 37.30 / LIMR 39.42 / HVS 38.14"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.29252"
    notes: "Table 1. AMC-23 is an outlier (DIEM 55.0 vs GRPO 58.5) on this backbone only."
  - benchmark: "Qwen2.5-VL-7B six-bench avg (MathVista / MathVerse / MathVision / MMStar / MMMU / AI2D)"
    metric: "average score"
    value: 61.8
    baseline: "Vanilla RFT 59.1 / SPEED-RL 60.0 / PCL 58.8"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.29252"
    notes: "Table 2. Qwen2.5-VL-32B: DIEM 67.3 vs RFT 64.9."
tags:
  - post-training
  - rlvr
  - data-selection
  - diem
  - active
---

# DIEM (Dynamic Important Example Mining)

## Method Overview
DIEM is an RFT/RLVR data-utilization plug-in, in the same optional-add-on class as `method:gmts`. Each step:

1. Score sample $z$ by gradient alignment $\hat{\mathcal{I}}_t(z)=\eta_t\langle\mathcal{G}_z,\mathcal{G}_{\mathcal{B}}\rangle$.
2. Solve for weights that maximize $I^\top W$ while keeping $\|W^\top G\|_2$ equal to the unweighted gradient norm. Closed form uses the N×N Gram matrix $P=GG^\top$. Clip negative weights to 0, then step on $W^\top G$.

It does not change the host RL loss. Like GMTS, it does not replace CISPO.

## When to Use
- Optional add-on when already running GRPO/PPO-family RFT and static difficulty / pass-rate curricula are leaving GPU-weeks on the table.
- Multimodal RFT on Qwen2.5-VL-class models, where the paper's larger lifts showed up.

## When NOT to Use
- Do not pick DIEM instead of `method:cispo`.
- Token truncation -> `method:gmts`. Query-conditioned LDS diagnostics -> `method:magic`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` / `task:reasoning-rl-alignment`. Does **not** supersede `method:cispo` or `method:gmts`.

## Gotchas & Failure Modes
- Negative weights are clipped; do not interpret the raw Lagrange solution as signed influence.
- Gram invert is cheap only because N is the minibatch, not the parameter dimension. Do not materialize full-parameter outer products.
- AMC-23 on Qwen3-4B is a reported outlier vs GRPO; do not treat every bench as uniformly up.
