---
id: method:tropd
type: method
title: "TrOPD (Trust-Region On-Policy Distillation)"
category: "distillation"
status: active
papers:
  - paper:tropd
recipes:
  - recipe:tropd
claims:
  - benchmark: "Student Distillation Benchmarks"
    metric: "training stability"
    value: "Trust-region bounded teacher matching"
    baseline: "Standard OPD"
    date: "2026-08-26"
    verified: true
    notes: "Bounds student policy divergence across distillation steps."
tags:
  - post-training
  - distillation
  - tropd
---

# TrOPD (Trust-Region On-Policy Distillation)

## Method Overview
TrOPD incorporates trust-region bounds into on-policy distillation, stabilizing student training trajectories when exploring low-probability teacher branches.

## When to Use
- Distilling long conversational or agentic reasoning traces where student exploration can destabilize.
