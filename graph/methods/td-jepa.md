---
id: method:td-jepa
type: method
title: "TD-JEPA World Model"
category: "control"
status: active
papers:
  - paper:td-jepa
recipes:
  - recipe:td-jepa
claims:
  - benchmark: "Continuous Control World Models"
    metric: "representation collapse avoidance & sample efficiency"
    value: "Geodesic temporal-distance metric learning"
    baseline: "JEPA / TD-MPC2"
    date: "2026-08-26"
    verified: true
    notes: "Temporal-distance metric learning for stable non-generative world models."
tags:
  - control
  - world-models
  - jepa
  - td-jepa
---

# TD-JEPA World Model

## Method Overview
TD-JEPA regularizes latent world model state embeddings using temporal distance metric learning, preventing representation collapse without pixel decoding.

## When to Use
- Building non-generative latent world models for continuous control.
