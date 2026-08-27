---
id: method:opd2
type: method
title: "OPD2 (Multi-Teacher On-Policy Distillation)"
category: "distillation"
status: active
papers:
  - paper:opd2
recipes:
  - recipe:opd2
claims:
  - benchmark: "Multi-Teacher Distillation"
    metric: "cross-domain transfer"
    value: "Ensemble teacher knowledge transfer"
    baseline: "Single-Teacher OPD"
    date: "2026-08-26"
    verified: true
    notes: "Dynamic routing across domain-specialist teachers."
tags:
  - post-training
  - distillation
  - opd2
---

# OPD2 (Multi-Teacher On-Policy Distillation)

## Method Overview
OPD2 extends on-policy distillation to heterogeneous multi-teacher ensembles, routing student queries to domain-specialist teacher models.

## When to Use
- Distilling multiple specialized models (e.g. math teacher, code teacher, writing teacher) into a single unified student.
