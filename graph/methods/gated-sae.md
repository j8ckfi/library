---
id: method:gated-sae
type: method
title: "Gated Sparse Autoencoders (Gated SAE)"
category: "circuits"
status: sota
sota_for:
  - task:mechanistic-interpretability-dictionaries
supersedes:
  - method:standard-sae
papers:
  - paper:gated-sae-paper
recipes:
  - recipe:gated-sae-training
claims:
  - benchmark: "Gemma-2-9B & Claude-3 Residual Stream (Layer 12/20)"
    metric: "Loss Recovery vs L0 Pareto frontier"
    value: "Pareto dominates Standard SAE across all L0 regimes"
    baseline: "Standard L1 ReLU SAE"
    date: "2024-04"
    verified: true
    notes: "Eliminates feature shrinkage by estimating magnitude through a jump-linear pathway decoupled from gate gating."
tags:
  - interpretability
  - mechanistic
  - circuits
  - sae
---

# Gated Sparse Autoencoders (Gated SAE)

## Method Overview
In mechanistic interpretability, standard Sparse Autoencoders (SAEs) reconstruct activation vectors \(x \in \mathbb{R}^d\) by mapping to an overcomplete latent space \(f(x) = \text{ReLU}(W_{\text{enc}}(x - b_{\text{dec}}) + b_{\text{enc}})\) trained with MSE reconstruction loss plus an \(L_1\) sparsity penalty \(\lambda \|f(x)\|_1\). The \(L_1\) penalty introduces systematic shrinkage bias, underestimating feature activations and distorting reconstructions.

**Gated SAEs** solve shrinkage bias by decomposing the encoder into two paths:
1. **Gating Path**: Evaluates whether a feature is active via a Heaviside step \(\pi_{\text{gate}}(x) = \Theta(W_{\text{gate}}(x - b_{\text{dec}}) + b_{\text{gate}})\).
2. **Magnitude Path**: Directly estimates activation magnitude via a linear projection \(\tilde{f}(x) = \text{ReLU}(W_{\text{mag}}(x - b_{\text{dec}}) + b_{\text{mag}})\).
3. **Combined Latent**:
   \[
   f_{\text{gated}}(x) = \pi_{\text{gate}}(x) \odot \tilde{f}(x)
   \]
Sparsity is penalized solely on the pre-activation of the gating network using a smooth surrogate, leaving the magnitude path unbiased.

## When to Use
- **Dictionary Learning for Large LLMs**: Extracting monosemantic feature dictionaries from transformer residual streams, MLP activations, or attention head outputs.
- **Circuit Tracing & Steering**: Isolating clean directional steering vectors for safety and capability steering.

## Gotchas & Failure Modes
1. **Dead Features**: Features whose gating threshold drifts too high will never activate. Dead feature resampling or auxiliary loss schemes must be maintained during training.
2. **Hyperparameter Tuning**: Balancing gate learning rate vs magnitude learning rate is critical to prevent the gating path from lagging behind.
