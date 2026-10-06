---
id: method:soap-muon-scale
type: method
title: "KL-SOAP (Scalable Second-Order Optimization)"
category: "optimizer"
status: sota
sota_for:
  - task:pretrain-dense-7b
supersedes:
  - method:soap
do_not_use_for:
  - when: "Nyström-sketched SOAP / linear optimizer-state memory (Clean / Q-Clean)"
    reason: "KL-SOAP remains unconstrained-memory large-batch SOAP; Clean is the linear-memory sketch"
    use_instead: "method:clean"
papers:
  - paper:clean
  - paper:soap-muon-scale
recipes:
  - recipe:muon-pretraining
claims:
  - benchmark: "NVIDIA Megatron-LM Pretraining (up to 100M token batch)"
    metric: "large-batch scaling loss"
    value: "Pareto superior to Muon at ultra-large batch sizes"
    baseline: "Muon & AdamW"
    date: "2026-07"
    verified: true
    notes: "Recommended over Muon when memory is unconstrained and batch sizes scale towards 100M tokens."
last_reviewed: "2026-10-06"
tags:
  - optimizer
  - megatron
  - large-batch
---

# KL-SOAP (Scalable Second-Order Optimization)

## Method Overview
KL-SOAP adapts SOAP for large-scale Megatron distributed pretraining, optimizing eigenspace preconditioning updates across tensor and pipeline parallel boundaries.

## When to Use
- When GPU memory budget can accommodate SOAP's additional state and training at massive batch sizes (up to ~100M tokens).

## Supersession
- Supersedes original small-scale `method:soap`.
