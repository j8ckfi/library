---
id: method:gapo
type: method
title: "GAPO (Group Adaptive Clipping Policy Optimization)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code RLVR default"
    reason: "GAPO is a clip-boundary plug-in on GRPO/GSPO; CISPO remains the Pass@1 default"
    use_instead: "method:cispo"
  - when: "single-teacher distillation is the goal"
    reason: "GAPO does not match a teacher token distribution"
    use_instead: "method:opd"
  - when: "teacher-free unlabeled self-adaptation"
    reason: "GAPO needs group-relative outcome advantages from a verifier"
    use_instead: "method:opsa"
  - when: "long-horizon outcome-only agent RL"
    reason: "Coverage / anti-drift at episode end is CANOPY, not a per-rollout clip schedule"
    use_instead: "method:canopy"
assumptions:
  - "Host RLVR already samples a group and has a binary (or thresholded) outcome verifier."
  - "Paper trains Qwen2.5-Math-1.5B, DeepSeek-R1-Distill-Qwen-1.5B, Llama-3.2-3B-Instruct, and DeepCoder-1.5B in verl. Group size k=8 or 16."
  - "Default linear scarcity: c=1 gets ε_hi^max, c=k gets ε_lo. Incorrect rollouts keep ε_lo."
last_reviewed: "2026-09-07"
papers:
  - paper:gapo
recipes:
  - recipe:gapo
claims:
  - benchmark: "DeepSeek-R1-Distill-Qwen-1.5B AIME24 / AIME25, DeepScaleR"
    metric: "Pass@1 / Pass@16"
    value: "44.0/76.7 and 30.8/56.7"
    baseline: "GSPO 41.3/73.3 and 29.4/50.0; F-GSPO 40.2/73.3 and 29.6/46.7"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.00444"
    notes: "Table 1. EMNLP 2026 Main accept. Temperature 0.6, n=16, Tmax=24576, group N=8."
  - benchmark: "Qwen2.5-1.5B-Math in-domain Pass@1 avg (AIME24/25 / AMC / MATH500 / Minerva / Olympiad)"
    metric: "Pass@1 average"
    value: 37.6
    baseline: "GRPO 36.7 / F-GRPO 36.3 / DrGRPO 33.8"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.00444"
    notes: "Table 3 token-IS GAPO with (ε_lo, ε_hi^max)=(0.2, 0.28). Sequence-IS GAPO 37.9 vs GSPO 37.7."
  - benchmark: "DeepCoder-1.5B LiveCodeBench-v5 / HumanEval+"
    metric: "Pass@1"
    value: "24.8 / 71.7"
    baseline: "Reproduced DeepCoder 22.4 / 68.2; base 16.9 / 58.3"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.00444"
    notes: "Table 2. Token-IS adaptive clip on the DeepCoder recipe, Tmax=24576."
tags:
  - post-training
  - rlvr
  - clipping
  - gapo
  - active
---

# GAPO (Group Adaptive Clipping Policy Optimization)

## Method Overview
GAPO is a clip-boundary plug-in for GRPO/GSPO-style RLVR. In a group of $k$ rollouts with $c$ correct, a correct rollout's advantage is $A_i=(k-c)/k$. A reverse-KL trust region says the optimal IS ratio scales as $\exp(A_i/\lambda)$, so scarce-correct (low $c$) traces need a wider upper clip. GAPO sets

\[
\epsilon_{\mathrm{hi}}(c)=\epsilon_{\mathrm{lo}}+(\epsilon_{\mathrm{hi}}^{\max}-\epsilon_{\mathrm{lo}})\cdot\frac{k-c}{k-1}
\]

for a correct rollout ($c=1$ gets $\epsilon_{\mathrm{hi}}^{\max}$; $c=k$ gets $\epsilon_{\mathrm{lo}}$). Incorrect rollouts and $c=0$ groups keep $\epsilon_{\mathrm{lo}}$. The PPO/GSPO surrogate is unchanged: only the per-rollout upper bound on the IS ratio (token-level or GSPO sequence geometric mean) moves. No reward shaping.

Paper token-IS defaults $(\epsilon_{\mathrm{lo}},\epsilon_{\mathrm{hi}}^{\max})=(0.2,0.28)$. Sequence-IS defaults $(3\times10^{-3},5\times10^{-3})$; longer-context R1-Distill runs use $(7\times10^{-5},3\times10^{-4})$.

## When to Use
- Optional add-on when already running GRPO/GSPO (or a CISPO-family trainer with an IS clip) and base pass rates are low, so rare correct hard-problem rollouts are the learning signal.
- When fixed clipping or advantage-shaping (F-GRPO, DrGRPO) is killing high-advantage traces.

## When NOT to Use
- Do not pick GAPO instead of `method:cispo` as the dense RLVR algorithm.
- Do not replace `method:opd`, `method:opsa`, or `method:canopy`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense`. Does **not** supersede `method:cispo`. DAPO stays a systems reference; GSPO stays the Qwen-Talker / SAPO-superseded sequence-IS cite.
- Distinct from `method:gmts` (token filter) and `method:diem` (example reweight): GAPO changes the clip width, not which tokens or examples enter the loss.

## Gotchas & Failure Modes
- Gains are for low base pass-rate math/code. Do not expect the same lift on already-saturated easy groups.
- Official code pins verl to `9bda8b9a` and applies `patches/gapo-verl-9bda8b9a.patch`. Bypass rollout correction and GAPO cannot be combined without that patch.
- Linear scarcity is the paper default. Harmonic / exact modes exist in `gapo/clip.py` but are not the reported main tables.
- CISPO still clips IS weights rather than group-relative magnitude; GAPO does not address `paper:spurious-advantage-grpo`.
