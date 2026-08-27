---
id: method:w2s-opd
type: method
title: "W2S-OPD (Weak-to-Strong On-Policy Distillation)"
category: "distillation"
status: active
papers:
  - paper:w2s-opd
recipes:
  - recipe:w2s-opd
claims:
  - benchmark: "Weak-to-Strong Generalization"
    metric: "student performance boost"
    value: "Elicits latent student capabilities beyond weak teacher limits"
    baseline: "Standard Distillation"
    date: "2026-08-26"
    verified: true
    notes: "Iterative bootstrapping of strong students using weak supervision."
tags:
  - post-training
  - distillation
  - weak-to-strong
  - w2s-opd
---

# W2S-OPD (Weak-to-Strong On-Policy Distillation)

## Method Overview
W2S-OPD enables weaker teacher models to elicit latent capabilities in stronger base student models via on-policy verification and self-correction.

## When to Use
- Bootstrapping large capable base models with smaller, fast supervisor teachers.
