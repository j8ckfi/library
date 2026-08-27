---
id: method:lords
type: method
title: "LoRDS (Low-Rank Decomposition with Dynamic Sparsity)"
category: "peft"
status: active
papers:
  - paper:lords
recipes:
  - recipe:lords
claims:
  - benchmark: "PEFT Benchmarks"
    metric: "sparsity vs task score"
    value: "Dynamic sparse low-rank adaptation"
    baseline: "LoRA"
    date: "2026-08-26"
    verified: true
    notes: "Sparse activation gating inside low-rank projections."
tags:
  - peft
  - sparsity
  - lords
---

# LoRDS (Low-Rank Decomposition with Dynamic Sparsity)

## Method Overview
LoRDS combines low-rank adapter projections with dynamic magnitude sparsity, focusing gradient updates on high-magnitude coordinate directions.

## When to Use
- Resource-constrained fine-tuning requiring sparse gradient memory.
