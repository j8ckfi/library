---
id: method:olmo-2-curriculum
type: method
title: "OLMo 2 Two-Stage Data Curriculum"
category: "data-curriculum"
status: superseded
superseded_by: method:olmo-3
sota_for: []
supersedes: []
papers:
  - paper:olmo-2-curriculum
recipes: []
claims:
  - benchmark: "Open Pretraining Mix / Evaluation Suite"
    metric: "downstream benchmark score"
    value: "Historical open data recipe standard"
    baseline: "Dolma 1.7"
    date: "2025-01"
    verified: true
    notes: "Two-stage curriculum: broad web pretraining followed by high-quality annealing."
tags:
  - pretraining
  - data-curriculum
  - olmo
---

# OLMo 2 Two-Stage Data Curriculum

## Method Overview
OLMo 2 establishes the two-stage open pretraining data curriculum: broad web pretraining followed by targeted high-quality domain annealing.

## Supersession
- Superseded by `method:olmo-3` (Dolma-3 mix).
