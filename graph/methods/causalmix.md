---
id: method:causalmix
type: method
title: "CausalMix (Causal Data Scheduling)"
category: "data-curriculum"
status: active
papers:
  - paper:causalmix
recipes:
  - recipe:causalmix
claims:
  - benchmark: "Pretraining Curricula"
    metric: "knowledge retention & downstream transfer"
    value: "Graph-ordered scheduling reduces catastrophic forgetting"
    baseline: "Uniform Sampling"
    date: "2026-08-26"
    verified: true
    notes: "Orders domain datasets according to estimated prerequisite dependency graphs."
tags:
  - pretraining
  - data-curriculum
  - causalmix
---

# CausalMix (Causal Data Scheduling)

## Method Overview
CausalMix estimates causal dependency graphs between concepts and topics, scheduling foundational conceptual tokens before specialized reasoning corpora.

## When to Use
- Constructing multi-phase pretraining schedules for reasoning-focused models.
