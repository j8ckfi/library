---
id: paper:f-adapter
type: paper
title: 'F-Adapter: Frequency-Adaptive Parameter-Efficient Fine-Tuning in Scientific
  Machine Learning'
authors:
- Hangwei Zhang
- Chun Kang
- Yan Wang
- Difan Zou
year: 2025
month: 9
arxiv_id: '2509.23173'
url: https://arxiv.org/abs/2509.23173
methods:
- method:f-adapter
cites:
- paper:fno
- paper:dpot
tags:
- scientific-ml
- neural-operator
- peft
- fourier-adapter
- f-adapter
- sota
---

# F-Adapter: Frequency-Adaptive Parameter-Efficient Fine-Tuning in Scientific Machine Learning

## Abstract Summary
Parameter-efficient fine-tuning (PEFT) of powerful pre-trained models for complex downstream tasks has proven effective in vision and language processing, yet this paradigm remains unexplored in scientific machine learning, where the objective is to model complex physical systems. We conduct the first systematic study of PEFT for pre-trained Large Operator Models (LOMs) obtained by scaling variants of Fourier Neural Operator. First, we observe that the widely used Low-Rank Adaptation (LoRA) yields markedly poorer performance on LOMs than Adapter tuning. Then, we further theoretically establish that stacked LoRA incurs a depth-amplified lower bound on approximation error within Fourier layers, whereas adapters retain universal approximation capacity and, by concentrating parameters on energy-dominant low-frequency modes, attain exponentially decaying error with bottleneck width in the Fourier domain. Motivated by the robust empirical gains of adapters and by our theoretical characterization of PDE solutions as spectrally sparse, we introduce Frequency-Adaptive Adapter (F-Adapter). F-Adapter allocates adapter capacity based on spectral complexity, assigning higher-dimension modules to low-frequency components and lower-dimension modules to high-frequency components. Our F-Adapters establish state-of-the-art (SOTA) results on multiple challenging 3D Navier-Stokes benchmarks, markedly enhancing both generalization and spectral fidelity over LoRA and other PEFT techniques commonly used in LLMs. To the best of our knowledge, this work is the first to explore PEFT for scientific machine-learning and establishes F-Adapter as an effective paradigm for this domain.

## Key Contributions
- Formulates and evaluates `f-adapter` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/fogradio/F-Adapter`
