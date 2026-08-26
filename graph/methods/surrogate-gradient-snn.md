---
id: method:surrogate-gradient-snn
type: method
title: "Surrogate Gradient Direct SNN Training"
category: "spiking"
status: active
sota_for: []
supersedes: []
superseded_by: method:silif
papers:
  - paper:spikingjelly-paper
recipes:
  - recipe:spikingjelly-snn
claims:
  - benchmark: "Neuromorphic DVS-Gesture & ImageNet-1K"
    metric: "top-1 accuracy"
    value: 81.3
    baseline: "ANN-to-SNN Conversion (requires 100+ timesteps, high latency)"
    date: "2024-06"
    verified: true
    notes: "Direct end-to-end BPTT training with smooth Arctan surrogate gradient at T=4 timesteps."
tags:
  - snn
  - neuromorphic
  - surrogate-gradients
  - spikingjelly
---

# Surrogate Gradient Direct SNN Training

## Method Overview
Spiking Neural Networks utilize Leaky Integrate-and-Fire (LIF) neurons governed by subthreshold membrane potential dynamics:
\[
H[t] = V[t-1] + \frac{1}{\tau} \left( X[t] - (V[t-1] - V_{\text{reset}}) \right)
\]
When membrane potential \(H[t]\) exceeds threshold \(V_{\text{th}}\), the neuron emits a discrete spike \(S[t] = \Theta(H[t] - V_{\text{th}})\), and resets to \(V_{\text{reset}}\).

Because the Heaviside step function \(\Theta(x)\) has zero derivative everywhere (\(x \neq 0\)), **Surrogate Gradient Learning** replaces the derivative during backpropagation with a smooth surrogate function \(\sigma'(x)\), such as the derivative of the Arctan function:
\[
\frac{\partial S}{\partial H} \approx \frac{1}{\pi} \frac{\alpha}{1 + (\alpha \pi (H - V_{\text{th}}))^2}
\]
This allows Backpropagation Through Time (BPTT) across time steps \(T\).

## When to Use
- **Event-Camera & Neuromorphic Processing**: DVS cameras, neuromorphic audio/tactile sensor streams where data is naturally asynchronous and event-based.
- **Ultra-Low Energy Edge Inference**: Deployment on neuromorphic chips (Intel Loihi, SynSense, BrainScaleS).

## Gotchas & Failure Modes
1. **Vanishing/Exploding Spikes**: Deep SNNs can suffer from silent neurons (zero spikes generated) or saturated neurons (firing at every step). Batch normalization across time (BNTT or Neuromorphic BN) is essential.
2. **Memory Overhead During Training**: Direct BPTT requires storing intermediate membrane potentials across all \(T\) timesteps in GPU memory.
