---
id: method:automixer
type: method
title: "AutoMixer (Proxy-Swarm Data Mixture Search)"
category: "training-systems"
status: active
sota_for: []
supersedes: []
papers:
  - paper:laguna-m1-xs2
claims:
  - benchmark: "AutoMixer vs hand mix (3B proxy, 1.5T tokens; report Table 3)"
    metric: "HumanEval+ relative change"
    value: "+43%"
    baseline: "manually designed prior mix"
    date: "2026-08"
    verified: true
    notes: "Laguna M.1/XS.2 §3.2.3. Also MBPP+ +15%, GSM8K +41%; commonsense small regressions (ARC-C -6.8%, WinoGrande -1.4%). Component of the factory, not the open-data SOTA."
tags:
  - systems
  - training-systems
  - data-mix
  - automixer
  - factory-component
---

# AutoMixer (Proxy-Swarm Data Mixture Search)

## Method Overview
AutoMixer is Poolside's automated pretraining-mix search, reported in Laguna M.1/XS.2 §3.2.3. It is a **factory component**, status `active`. It does **not** supersede `method:olmo-3` and is **not** SOTA for `task:open-data-recipe`.

Mechanism:
1. Train a swarm of ~60 proxy 0.5B MoEs on ~60B tokens each, mixtures sampled as Dirichlet around a hand-designed prior \(x_0\) with an L1 ball constraint \(\|x-x_0\|_1 < \epsilon\).
2. Fit a surrogate \(f_j(x) \approx y_j\) per capability group (coding, math, STEM, commonsense, general knowledge).
3. Optimize \(\max_x \sum_j w_j f_j(x)\) with simplex constraints and KL regularization \(\lambda D_{\mathrm{KL}}(x \| x_0)\) so the mix cannot collapse onto a few sources.

Reported vs the hand prior (Table 3): HumanEval+ +43%, MBPP+ +15%, Crux-I/O +54%/+48%, MultiPL-E +27%, GSM8K +41%, MMLU +5%; held-out MATH +25%, LiveCodeBench +39%; commonsense regressions ARC-C -6.8%, WinoGrande -1.4%, PIQA -0.9%, HellaSwag -1.3%.

XS.2 mix (report Table 4): raw code 30.6%, web 25.2%, synth/code-text 25.4%, math 9.0%, knowledge 6.6%, instruction-like 1.4%, academic papers 1.1%, books 0.7%.

## When to Use
- Inside a factory that can afford a proxy swarm and already has a documented prior mix.
- Not as a replacement for Dolma-3 / OLMo-3 open data recipes.

## Scale-down (few-GPU / small lab)
**Skip** AutoMixer until you can afford ~60 proxy runs. Keep a **documented prior mix** (committed config, unique run ID) and change weights as configuration (`method:blender-streaming`). Revisit the swarm later if a small-lab cluster exists.

## Gotchas & Failure Modes
- Optimizing coding/math surrogates trades off commonsense (Table 3).
- Running 60×0.5B×60B-token proxies is cluster work; doing a single proxy and calling it AutoMixer is not the method.
- Do not retarget `task:open-data-recipe` current_sota.

## Supersession
Does not supersede `method:olmo-3`. Active component of `method:poolside-model-factory` only.
