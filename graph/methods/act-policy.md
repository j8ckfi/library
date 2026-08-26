---
id: method:act-policy
type: method
title: "ACT (Action Chunking with Transformers)"
category: "servo-control"
status: active
superseded_by: method:diffusion-policy
sota_for: []
supersedes: []
papers:
  - paper:act-paper
recipes: []
claims:
  - benchmark: "ALOHA Bimanual Manipulation"
    metric: "success rate"
    value: 89.5
    baseline: "Behavior Cloning MLP"
    date: "2023-04"
    verified: true
    notes: "CVAE-based transformer policy predicting action sequences with temporal ensembling."
tags:
  - control
  - robotics
  - baseline
---

# ACT (Action Chunking with Transformers)

## Method Overview
Action Chunking with Transformers (ACT) treats visuomotor policy learning as sequence modeling using a Conditional Variational Autoencoder (CVAE) and a Transformer encoder-decoder. It predicts chunks of future actions and combines overlapping predictions using exponential temporal ensembling.

## When to Use
- Baseline imitation learning policy for dual-arm robotic teleoperation.

## Gotchas & Failure Modes
- CVAE Gaussian latent prior struggles to capture highly multimodal action distributions compared to diffusion models.
