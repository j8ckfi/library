---
id: method:deeponet
type: method
title: DeepONet (Deep Operator Network)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:deeponet
recipes:
- recipe:deeponet
claims:
- benchmark: ODE/PDE Operator Benchmarks (Antiderivative, Gravity Pendulum, 1D/2D
    Advection)
  metric: relative L2 error
  value: Universal operator approximation baseline
  baseline: Fully connected NN
  date: '2026-08-28'
  verified: true
  notes: Branch and trunk network decomposition based on the universal approximation
    theorem for operators.
tags:
- scientific-ml
- neural-operator
- deeponet
- baseline
---

# DeepONet (Deep Operator Network)

## Method Overview
DeepONet learns continuous nonlinear operators by decomposing the operator into two subnetworks:
1. **Branch Net**: Encodes the input discrete function values sampled at fixed sensor locations.
2. **Trunk Net**: Encodes continuous evaluation query coordinates.
3. **Inner Product Merging**: Computes the scalar product of branch and trunk feature representations to yield the output field value.

## When to Use
- Classical baseline for operator learning and continuous functional mapping.
