---
id: method:ida-opd
type: method
title: "IDA-OPD (Influence-Directed Adaptive OPD)"
category: "distillation"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "IDA-OPD is a sampled-token entropy plug-in on OPD, not a new distill default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "Labeled RLVR stays CISPO; this is still teacher OPD"
    use_instead: "method:cispo"
  - when: "no teacher is available"
    reason: "IDA-OPD still needs sampled-token teacher log-probs; teacher-free is OPSA"
    use_instead: "method:opsa"
  - when: "filtering teacher-OPD trajectories by outcome alignment"
    reason: "That is RA-OPD's (2R-1)G mask, a different plug-in"
    use_instead: "method:ra-opd"
  - when: "Pass@K RLVR without a teacher"
    reason: "Coverage/no-backward RLVR is ES-reasoning, not an OPD entropy shrink"
    use_instead: "method:es-reasoning"
assumptions:
  - "Running sampled-token (K1) OPD: A_y = log q(y|h) - log p(y|h). Student next-token distribution is available so D_y can be computed."
  - "Paper: Qwen3-8B/4B Non-Thinking students distilled from GRPO-trained same-size math/code teachers; DeepMath103K level-6; n=128 eval for unbiased pass@k."
last_reviewed: "2026-09-04"
papers:
  - paper:ida-opd
recipes:
  - recipe:ida-opd
claims:
  - benchmark: "Qwen3-8B-Non-Thinking AIME24/25 / HMMT Feb/Nov pass@16"
    metric: "unbiased pass@16"
    value: "83.3 / 76.7 / 56.7 / 63.3"
    baseline: "OPD 79.1 / 70.7 / 49.5 / 60.8"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.29846"
    notes: "Table 1. Pass@1 63.3 / 50.0 / 37.6 / 40.1 vs OPD 61.7 / 47.9 / 37.5 / 38.6."
  - benchmark: "Qwen3-4B-Non-Thinking AIME24 pass@16"
    metric: "unbiased pass@16"
    value: 83.3
    baseline: "OPD 78.7 / teacher 80.0"
    date: "2026-09-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.29846"
    notes: "HMMT Feb pass@16 60.0 vs OPD 51.7 (+8.3)."
tags:
  - post-training
  - distillation
  - on-policy
  - entropy
  - ida-opd
  - niche
---

# IDA-OPD (Influence-Directed Adaptive OPD)

## Method Overview
IDA-OPD is a sampled-token OPD plug-in for the pass@k / entropy collapse that reverse-KL on one emitted token produces. The first-order local entropy influence is $\mathcal{I}_H(y)=A_y D_y$, where $A_y=\log q_y-\log p_y$ and $D_y$ depends only on the student's current distribution. Keep expanding updates; shrink contracting ones by the scale-free disagreement

\[
w_y=\frac{|q_y-p_y|}{q_y+p_y},\qquad
\widetilde{A}_y=\begin{cases}A_y & \mathcal{I}_H(y)\ge 0,\\ w_y A_y & \mathcal{I}_H(y)<0.\end{cases}
\]

Near agreement $w_y A_y=\mathcal{O}(A_y^2)$; high-discrepancy corrections are left almost intact. No full-vocabulary Forward KL.

Sits beside `method:ra-opd` (trajectory filter on outcome alignment) and `method:opsa` (teacher-free). None of them replace OPD or CISPO.

## When to Use
- Already running sampled-token OPD and pass@1 is up but pass@k is flat vs the teacher.
- Full-vocabulary / top-K teacher logits are too expensive (AOPD/EOPD).

## When NOT to Use
- Default distill algorithm -> `method:opd`.
- Labeled Pass@1 RLVR -> `method:cispo`.
- No teacher -> `method:opsa`.
- Outcome-alignment trajectory drop -> `method:ra-opd`.

## Relation to Existing SOTA
- Niche plug-in on `task:student-distillation`. Does **not** supersede `method:opd`, `method:cispo`, `method:opsa`, or `method:ra-opd`.

## Gotchas & Failure Modes
- Uniform shrinkage of every $A_y$ (no $\mathcal{I}_H$ gate) is an ablation that loses the method. Gate on the sign.
- $D_y$ needs the student distribution, not just the sampled log-prob. If you only stored the emitted-token logp, you cannot run this.
- Pass@1 is "broadly maintained", not the optimization target. If Pass@1 is the goal and labels exist, that is still CISPO.
