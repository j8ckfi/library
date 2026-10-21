---
id: method:lr-matters-lora
type: method
title: "Vanilla LoRA + rsLoRA + LR Sweep"
category: "peft"
status: sota
sota_for:
  - task:parameter-efficient-fine-tuning
  - task:lora-quality-tuning
supersedes:
  - method:dora
  - method:delora
do_not_use_for:
  - when: "MuPACE Muon for LoRA (meta-learned global step size)"
    reason: "Quality default remains vanilla LoRA + rsLoRA + LR sweep; MuPACE paces Muon LoRA"
    use_instead: "method:mupace"
  - when: "block-wise Toeplitz adaptation (ToPA)"
    reason: "Quality default remains vanilla LoRA + rsLoRA + LR sweep; ToPA is block-wise Toeplitz PEFT"
    use_instead: "method:topa"
  - when: "rank measures of fine-tuning updates need a noise baseline"
    reason: "Gotcha on ΔW rank summaries; does not retarget the LR sweep"
    use_instead: "paper:rank-noise-baseline"
  - when: "two-stage residual-gradient complementary LoRA (ReGRA)"
    reason: "Quality default remains vanilla LoRA + rsLoRA + LR sweep; ReGRA is a staged adapter"
    use_instead: "method:regra"
  - when: "dynamic tangent LoRA branch via residual-gradient SVD"
    reason: "Quality default remains vanilla LoRA + rsLoRA + LR sweep; DT-LoRA is a vision/detection plug-in"
    use_instead: "method:dt-lora"
  - when: "stacking independently trained LoRA adapters / sequential skill add without an inference router"
    reason: "Quality default is a single-adapter recipe; READ owns multi-skill composition"
    use_instead: "method:read-lora"
papers:
  - paper:lr-matters-lora
  - paper:lora-unified-study
  - paper:topa
  - paper:rank-noise-baseline
recipes:
  - recipe:lr-matters-lora
claims:
  - benchmark: "MMLU / GSM8k / GLUE Fine-Tuning"
    metric: "accuracy vs parameter overhead"
    value: "Matches/exceeds DoRA without magnitude parameter overhead"
    baseline: "DoRA / DeLoRA / Vanilla LoRA"
    date: "2026-08-26"
    verified: true
    notes: "Vanilla LoRA with rank-stabilized scaling (rsLoRA, alpha/sqrt(r)) and calibrated learning rate sweep."
tags:
  - peft
  - lora
  - rslora
  - sota
---

# Vanilla LoRA + rsLoRA + LR Sweep

## Method Overview
Re-evaluating low-rank adaptation reveals that with rank-stabilized scaling (\(\alpha / \sqrt{r}\)) and proper learning rate sweeping, standard vanilla LoRA achieves equal or superior accuracy compared to Weight-Decomposed LoRA (DoRA), without the VRAM memory overhead and runtime complexity of magnitude normalization.

## When to Use
- Default SOTA quality choice for 24GB single-GPU parameter-efficient fine-tuning (NOT DoRA).

## Relation to Existing SOTA
- Remains the 24GB LoRA quality default. `method:nora` is a recommended RLVR-stable adapter upgrade (status active) and is not a completed supersession of this protocol. `method:anlr-lora` is an optional per-rank LR plug-in. `method:iso-lora` is an active optimizer-shape / effective-rank note. Neither replaces the LR sweep.
- Stacking independently trained LoRA skills is `method:read-lora` on `task:lora-skill-composition` (`arXiv:2609.31600`). Does **not** retarget this quality default.

## Supersession
- Supersedes `method:dora` and `method:delora` as the PEFT quality default.
