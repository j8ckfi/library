---
id: paper:massive-activation-lifecycle
type: paper
title: 'The Life Cycle of a Massive Activation: Stochastic Birth, Weight-Decay-Driven
  Growth, and Competitive Consolidation'
authors:
- S. Aaron McClendon
- Jorge Gallego-Feliciano
- Antonios Saravanos
year: 2026
month: 10
arxiv_id: '2610.00423'
url: https://arxiv.org/abs/2610.00423
methods:
- method:muon2
cites:
- paper:muon2
tags:
- pretraining
- gotcha
- massive-activations
- weight-decay
---

# The Life Cycle of a Massive Activation

## Abstract Summary
Caution/evidence paper on LLM pretraining. Weight decay causally controls massive-activation magnitude (peak ~ λ^{-1/2}; timing log-linear in λ). Gotcha on `task:llm-pretraining-optimization` (attention sinks, low-bit training). Does not retarget Muon2.

## Key Contributions
1. Weight decay causally sets massive-activation magnitude.
2. Peak scale ~ λ^{-1/2}; timing log-linear in λ.
3. Implications for attention sinks and low-bit training.

## Empirical Highlights
- Life-cycle: stochastic birth, weight-decay-driven growth, competitive consolidation.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.00423`
- Code: `https://github.com/apd-smcclendon/massive_activations_2` (`code_status: released`).
