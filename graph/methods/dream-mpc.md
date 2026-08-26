---
id: method:dream-mpc
type: method
title: "Dream-MPC"
category: "servo-control"
status: sota
sota_for:
  - task:continuous-control-world-model
supersedes: []
papers:
  - paper:dream-mpc
recipes:
  - recipe:dream-mpc-placeholder
claims:
  - benchmark: "High-Speed Robot Control Benchmarks"
    metric: "planning latency & sample efficiency"
    value: "Faster online planning than MPPI"
    baseline: "TD-MPC2 with MPPI Planner"
    date: "2026-05"
    verified: true
    notes: "Code: none found (ICML 2026). Replaces costly sampling iterations with accelerated latent trajectory planning."
tags:
  - control
  - robotics
  - mpc
  - dream-mpc
---

# Dream-MPC

## Method Overview
Dream-MPC (ICML 2026) replaces expensive iterative trajectory sampling (like MPPI in TD-MPC2) with accelerated latent planning, reducing online action computation latency by orders of magnitude for high-frequency servo control.

## Status & Code
- **Code**: `none found` (ICML 2026). Do not invent a repository URL.
