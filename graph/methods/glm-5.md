---
id: method:glm-5
type: method
title: "GLM-5 General Foundation Architecture"
category: "architecture"
status: active
papers:
  - paper:glm-5
recipes:
  - recipe:glm-5
claims:
  - benchmark: "General Multilingual & Code Benchmarks"
    metric: "MMLU / Code / Math"
    value: "Frontier general language performance"
    baseline: "GLM-4"
    date: "2026-08-26"
    verified: true
    notes: "Hybrid sliding-window and global latent attention layers."
tags:
  - architecture
  - pretraining
  - glm-5
---

# GLM-5 General Foundation Architecture

## Method Overview
GLM-5 combines local sliding-window attention with global latent attention layers, balancing memory footprint during long-context pretraining with high general reasoning capabilities.

## When to Use
- Building general-purpose multilingual foundation models.
