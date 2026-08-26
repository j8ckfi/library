---
id: method:soap
type: method
title: "SOAP (Second-Order Optimization for Any Preconditioner)"
category: "optimizer"
status: active
sota_for: []
supersedes: []
papers:
  - paper:soap
recipes: []
claims:
  - benchmark: "Transformer Pretraining"
    metric: "preconditioning efficiency"
    value: "Faster convergence than AdamW"
    baseline: "AdamW / Shampoo"
    date: "2024-09"
    verified: true
    notes: "Maintains second-order preconditioning in eigenbasis without full Kronecker inverse costs."
tags:
  - optimizer
  - second-order
---

# SOAP (Second-Order Optimization for Any Preconditioner)

## Method Overview
SOAP performs second-order optimization by rotating gradients into the eigenspace of the gradient covariance matrix, performing coordinate-wise scaling, and rotating back.

## Supersession
- Supersedes classical Shampoo.
- Superseded at scale by `method:soap-muon-scale`.
