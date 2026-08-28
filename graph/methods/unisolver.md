---
id: method:unisolver
type: method
title: Unisolver (PDE-Conditional Universal Transformer)
category: neural-operator
status: sota
sota_for:
- task:operator-foundation
supersedes: []
papers:
- paper:unisolver
recipes:
- recipe:unisolver
claims:
- benchmark: Multi-PDE Benchmarks (Diffusion, Wave, Burgers, Navier-Stokes, Darcy)
  metric: zero-shot & few-shot relative L2 error across varying equations
  value: Co-default foundation operator conditioned on PDE equation symbols (ICML
    2025)
  baseline: DPOT / FNO / Prompt-conditioned ViT
  date: '2026-08-28'
  verified: true
  notes: PDE-conditional transformer decomposing equations into domain-wise and point-wise
    PDE mathematical representations.
tags:
- scientific-ml
- neural-operator
- foundation-model
- unisolver
- sota
---

# Unisolver (PDE-Conditional Universal Transformer)

## Method Overview
Unisolver provides a unified architecture for solving varying PDE families by explicitly conditioning on equation definitions:
1. **Symbolic PDE Tokenization**: Decomposes governing partial differential equations into domain-wise and point-wise symbolic mathematical representations.
2. **Conditional Cross-Attention**: Conditioned transformer layers modulate state propagation based on differential operators present in the target PDE.

## When to Use
- Co-default foundation operator when explicit conditioning on equation symbols and differential operator forms is required.
