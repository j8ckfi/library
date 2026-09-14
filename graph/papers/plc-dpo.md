---
id: paper:plc-dpo
type: paper
title: "PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization"
authors:
  - "Boryeong Cho"
  - "Sumyeong Ahn"
  - "Se-Young Yun"
year: 2026
month: 8
arxiv_id: "2608.30597"
url: "https://arxiv.org/abs/2608.30597"
methods:
  - method:plc-dpo
cites:
  - paper:dpo-paper
  - paper:simpo-paper
tags:
  - post-training
  - preference-alignment
  - dpo
  - plc-dpo
  - noisy-labels
---

# PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization

## Abstract Summary
DPO assumes observed pairwise preferences are reliable. Real data contains reversed, weak, or ambiguous labels that cause harmful policy updates. Posterior Label Correction DPO (PLC-DPO) routes each pair as a clean, flip, or tie case using the calibrated policy-reference margin as online evidence. Training then reinforces, reverses, or neutralize the pair instead of only filtering suspicious examples. EMA margin calibration, warm-up, and confidence-gated mixing stabilize routing. No auxiliary model is required.

## Key Contributions
1. **Three-way latent routing**: clean / flip / tie from a standardized policy-reference margin.
2. **Mixture of forward DPO, reversed DPO, and tie regularization** with confidence-gated mixing.
3. **EMNLP 2026 Findings**: 57 dataset-model-benchmark cells; best mean win rate against DPO 60.5 vs 55.5 for the next-best method.

## Empirical Highlights
- Headline: best mean win rate vs DPO 60.5 vs next-best 55.5 across 57 cells.
- Official repo reports per-model win rates vs one-epoch DPO on clean UltraFeedback Binarized (e.g. Qwen2.5-7B UFB 58.80 / Alpaca 58.14 / HH-RLHF 65.40).
- Injected-noise and tie stress tests plus human-disagreement analysis: routing distinguishes flipped from weakly directional pairs.

## Open Source Repository & Resources
- Code: `https://github.com/VennTum99/PLC-DPO` (Apache-2.0; released 2026-09-14).
- Train: `scripts/train.sh` with `configs/methods/plc-dpo-{aggressive,balanced,conservative}.yaml`. LoRA rank 16, LR 1e-5, one epoch, effective batch 64.
