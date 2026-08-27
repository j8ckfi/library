---
id: method:grasp
type: method
title: "GRASP Generative Action Planning"
category: "control"
status: active
papers:
  - paper:grasp
recipes:
  - recipe:grasp
claims:
  - benchmark: "Robotic Manipulation Benchmarks"
    metric: "task success rate"
    value: "Smooth multimodal action trajectory generation"
    baseline: "Diffusion Policy"
    date: "2026-08-26"
    verified: true
    notes: "Generative flow-matched robotic action synthesis."
tags:
  - control
  - robotics
  - grasp
---

# GRASP Generative Action Planning

## Method Overview
GRASP uses flow-matched continuous action generation conditioned on real-time visual tactile streams for multimodal manipulation tasks.

## When to Use
- Reactive physical robot manipulation under visual occlusions.
