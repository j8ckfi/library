---
id: method:nemotron-3-super-latentmoe
type: method
title: "Nemotron-3 Super Latent MoE"
category: "architecture"
status: active
papers:
  - paper:nemotron-3-super-latentmoe
recipes:
  - recipe:nemotron-3-super-latentmoe
claims:
  - benchmark: "Large-Scale MoE Pretraining"
    metric: "cross-node communication overhead"
    value: "Up to 60% reduction in all-to-all dispatch latency"
    baseline: "Standard MoE All-to-All"
    date: "2026-08-26"
    verified: true
    notes: "Low-rank latent projection of tokens prior to inter-GPU expert dispatch."
tags:
  - architecture
  - moe
  - latent-moe
  - nemotron
---

# Nemotron-3 Super Latent MoE

## Method Overview
Nemotron-3 Super introduces Latent MoE routing, compressing token representations into low-rank latent vectors before dispatching across inter-node network fabrics, resolving all-to-all bandwidth bottlenecks.

## When to Use
- Pretraining MoE models on clusters with constrained inter-node interconnect bandwidth.
