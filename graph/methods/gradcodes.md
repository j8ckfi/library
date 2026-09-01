---
id: method:gradcodes
type: method
title: "GradCodeS (Gradient-Guided Search in Quantized Code Space)"
category: "quantization"
status: sota
sota_for:
  - task:full-lowbit-finetune
supersedes: []
do_not_use_for:
  - when: "4-bit PEFT with a mixed-precision adapter at inference is acceptable"
    reason: "AQLoRA-Q remains the 4-bit stack speed/recipe default"
    use_instead: "method:aqlora-q"
  - when: "native FP4 hardware training from scratch"
    reason: "Quartet-II / MXFP4 remain the FP4 hardware-training defaults"
    use_instead: "method:quartet-ii"
  - when: "24GB quality LoRA without a fully quantized checkpoint constraint"
    reason: "Vanilla LoRA + rsLoRA + LR sweep remains the quality default"
    use_instead: "method:lr-matters-lora"
assumptions:
  - "Targeted linear layers stay in NF4, INT4, or MXFP4 at every accepted checkpoint; embeddings and lm_head may stay unquantized (paper setting)."
  - "One backward pass per search step plus M forward evaluations of deployable candidates."
  - "Paper scale is Qwen3-0.6B and Llama-3.2-1B/3B-Instruct, three seeds."
last_reviewed: "2026-09-01"
papers:
  - paper:gradcodes
recipes:
  - recipe:gradcodes
claims:
  - benchmark: "Llama-3.2-1B-Instruct GSM8K fully 4-bit"
    metric: "accuracy"
    value: 41.63
    baseline: "PV-Tuning 36.92 / QLoRA-4Merge 24.79 / Base-4 25.85 / 16-bit SFT 38.93"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30908"
    notes: "Table 1, GradCodeS Full. Mixed QLoRA-16A is a different deployment regime."
  - benchmark: "Qwen3-0.6B GSM8K fully 4-bit"
    metric: "accuracy"
    value: 45.72
    baseline: "PV-Tuning 38.70 / 16-bit SFT 39.65 / QLoRA-4Merge 26.46"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30908"
    notes: "Table 1, GradCodeS LoRA parameterization."
  - benchmark: "Llama-3.2-1B-Instruct datatype sweep GSM8K"
    metric: "accuracy"
    value: "NF4 41.6 / MXFP4 41.1 / INT4 38.9"
    baseline: "PV-Tuning adaptive 36.9"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30908"
    notes: "Table 4."
tags:
  - quantization
  - peft
  - low-bit
  - gradcodes
  - sota
---

# GradCodeS (Gradient-Guided Search in Quantized Code Space)

## Method Overview
GradCodeS fine-tunes quantization codes $Z$ and scales $s$ so every accepted iterate is already the deployed low-bit model $\widehat W=S(s)\odot\mathcal C(Z)$.

A weight-space gradient is the wrong direction in code space because group scales and non-uniform codebook gaps rescale a unit code step. The code surrogate is

\[
\nabla_Z L=\nabla_{\widehat W}L\odot D,\qquad D=S(s)\odot\bigl(G^+(Z)\odot\sigma_-+G^-(Z)\odot\sigma_+\bigr)
\]

with $\sigma=\mathrm{sign}(\nabla_{\widehat W}L)$ and $G^\pm$ the adjacent codebook gaps. Each step: (1) projected gradient on scales with $Z$ fixed, (2) $Z^{\mathrm{ref}}=Z-\eta_Z\nabla_Z L$, (3) sample $M$ nearby valid codes biased toward $Z^{\mathrm{ref}}$, (4) keep the candidate with lowest realized deployed loss.

Works on full matrices or a LoRA code parameterization, and on NF4 / INT4 / MXFP4.

## When to Use
- The deployed checkpoint must stay fully low-bit (no FP16 adapter, no merge-then-requantize).
- First-hop for `task:full-lowbit-finetune`.

## When NOT to Use
- Mixed-precision 4-bit PEFT -> `method:aqlora-q`.
- Native FP4 pretrain -> `method:quartet-ii`.
- Unquantized quality LoRA -> `method:lr-matters-lora`.

## Relation to Existing SOTA
- First-hop only for fully low-bit code-space fine-tuning. Does **not** overwrite `method:aqlora-q` or `method:quartet-ii`.

## Gotchas & Failure Modes
- Mapped $\nabla_{\widehat W}$ proposals underperform the code surrogate; do not skip the effective-step correction.
- On 167k-example GSM8K, 16-bit SFT overtakes GradCodeS; the low-bit parameterization looks like a small-data regularizer, not a universal quality win.
- INT4 is weaker than NF4/MXFP4 in the paper sweep.
- Each step costs one backward plus $M$ forwards; not the cheapest step, the point is fewer wasted discrete trials.
