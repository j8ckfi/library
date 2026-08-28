---
id: method:poseidon
type: method
title: Poseidon (PDE Foundation Model)
category: neural-operator
status: sota
sota_for:
- task:operator-foundation
- task:operator-grid-pde
supersedes: []
papers:
- paper:poseidon
recipes:
- recipe:poseidon
claims:
- benchmark: PDEBench / 15 Diverse 2D/3D PDE Datasets
  metric: fine-tuned relative L2 error & sample efficiency
  value: SOTA foundation operator model across multi-physics domains
  baseline: From-scratch FNO / U-Net / CNO
  date: '2026-08-28'
  verified: true
  notes: 'scOT (scaled Operator Transformer) with SwinV2 backbone, all2all pre-training
    on 2D/3D multiscale dynamics. Disambiguation: Poseidon PDE foundation model !=
    seismic POSEIDON.'
tags:
- scientific-ml
- neural-operator
- foundation-model
- poseidon
- sota
---

# Poseidon (PDE Foundation Model)

## Method Overview
Poseidon establishes the foundation operator standard across multiple PDE families:
1. **scOT SwinV2 Backbone**: Employs a scaled Operator Transformer (scOT) architecture based on Swin Transformer V2 for multi-scale spatial modeling.
2. **All2All Multi-Physics Pre-Training**: Pre-trained on 15 diverse 2D/3D fluid dynamics, wave, and transport PDE datasets.
3. **Downstream Fine-Tuning**: Rapidly fine-tunes to new physical regimes with minimal sample requirements.

Disambiguation: Poseidon PDE foundation model (Herde et al., 2405.19101) is for partial differential equations, distinct from seismic POSEIDON.

## When to Use
- Default SOTA foundation operator across PDE families; fine-tune when PDE family shifts.
