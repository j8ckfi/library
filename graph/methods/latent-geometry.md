---
id: method:latent-geometry
type: method
title: "Latent Geometry Control"
category: "control"
status: active
papers:
  - paper:latent-geometry
recipes:
  - recipe:latent-geometry
claims:
  - benchmark: "Continuous Robot Trajectory Optimization"
    metric: "trajectory smoothness"
    value: "Geodesic curve planning in Riemannian latent spaces"
    baseline: "TD-MPC2"
    date: "2026-08-26"
    verified: true
    notes: "Riemannian metric pullback for continuous latent spaces."
tags:
  - control
  - geometry
  - latent-spaces
---

# Latent Geometry Control

## Method Overview
Latent Geometry equips learned control representations with Riemannian metrics, synthesizing dynamically feasible trajectories along geodesic paths.

## When to Use
- High-speed servo control where trajectory smoothness and physical consistency are critical.
