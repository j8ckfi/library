---
id: method:u-opsd
type: method
title: "u-OPSD (Unsupervised On-Policy Self-Distillation)"
category: "distillation"
status: sota
sota_for:
  - task:label-free-reasoner-posttrain
supersedes: []
papers:
  - paper:u-opsd
recipes:
  - recipe:u-opsd
claims:
  - benchmark: "AIME24 / AIME25 / HMMT25 / MATH500 / AMC23"
    metric: "math accuracy without ground-truth labels"
    value: "+8.5% to +10.7% over base on Qwen3 non-thinking (4B/8B); outperforms supervised OPSD by +3.2% (4B) and +2.3% (8B); matches/beats GRPO and supervised OPSD on thinking mode"
    baseline: "Base Model / Supervised OPSD / Supervised GRPO"
    date: "2026-08-28"
    verified: true
    notes: "Constructs pseudo-solution via self-consistency threshold (tau=0.5) and distills solution-conditioned distribution along disagreeing rollouts."
tags:
  - post-training
  - distillation
  - self-distillation
  - label-free
  - reasoning
  - u-opsd
  - sota
---

# u-OPSD (Unsupervised On-Policy Self-Distillation)

## Method Overview
Unsupervised On-Policy Self-Distillation (u-OPSD) enables genuine self-distillation for mathematical reasoning using only the model's internal consistency:
1. **Sample**: For each unlabeled problem $x$, draw $G$ independent rollouts $y^{(1)}, \dots, y^{(G)} \sim \bar{\pi}(\cdot \mid x)$ and parse candidate answers $a^{(g)}$.
2. **Vote**: Extract the majority vote pseudo-answer $\tilde{a}(x)$. Partition rollouts into agreeing set $\mathcal{Y}^+_x$ and disagreeing set $\mathcal{Y}^-_x$. If self-consistency confidence $c(x) < \tau$ ($\tau=0.5$), the prompt is skipped. The longest agreeing rollout $y^+ \in \mathcal{Y}^+_x$ is selected as the pseudo-solution context.
3. **Distill**: Distill the pseudo-solution conditioned teacher distribution $\bar{\pi}(\cdot \mid x, y^+, y^-_{<t})$ into the student $\pi_\theta(\cdot \mid x, y^-_{<t})$ along prefixes of disagreeing rollouts $y^- \in \mathcal{Y}^-_x$.

## When to Use
- When post-training language models on large unlabeled math, science, or reasoning datasets where ground-truth solutions and outcome verifiers are unavailable.
- Especially effective for non-thinking reasoning modes and compact models (4B–8B).

## Relation to Existing SOTA
- When ground truth or rule-based verifiers are available, prefer `method:opdvr` (for verifiable distillation) or `method:cispo` (for RLVR). In purely unlabeled regimes (existing problems, no Challenger), `method:u-opsd` is the date-stamped SOTA.
- For data-free self-evolution covering unverifiable/open-ended domains with a Challenger–Solver–Judge loop, use `method:j-zero`. For privileged-teacher OPSD with gold solutions, use `method:vista`.
- Teacher-free on-policy self-adaptation without consensus pseudo-solutions is `method:opsa` on `task:teacher-free-on-policy-self-adaptation`. That does not replace u-OPSD.
