---
id: paper:expertmuon-compass
type: paper
title: "ExpertMuon-Compass: Alignment-Guided Step Sizes for Mixture-of-Experts Training"
authors:
  - Omatharv Bharat Vaidya
  - Ashwin Vinod
  - Pedram Akbarian
  - Aditya Sai Ellendula
  - Connor T. Jerzak
  - Nhat Ho
year: 2026
month: 10
arxiv_id: "2610.04140"
url: "https://arxiv.org/abs/2610.04140"
methods:
  - method:expertmuon-compass
cites:
  - paper:muon2
  - paper:muonclip-kimi-k2
tags:
  - pretraining
  - optimizer
  - moe
  - muon
  - expertmuon-compass
---

# ExpertMuon-Compass: Alignment-Guided Step Sizes for Mixture-of-Experts Training

## Abstract Summary
Shared-LR Muon gives same-shape MoE experts roughly the same step even when an expert's update is poorly aligned with its gradient. ExpertMuon-Compass multiplies each expert's Muon step by a family cosine factor vs other experts in the layer and a scalar radius from row-wise update–gradient alignment. Direction and Muon momentum stay unchanged. FineWeb-Edu pretraining: Compass with Nesterov on all matrices matches or beats Muon / NorMuon; adding the factors to NorMuon matches or lowers loss. Strongest when expert data mix shifts (blocked multilingual). Expert load stays balanced; router more decisive. Active plug-in beside Muon2 / MuonClip. No public code as of 2026-10-06.

## Key Contributions
1. **Family cosine**: scale each expert by alignment vs other experts in the layer.
2. **Scalar radius**: aggregate row-wise update–gradient alignment into one multiplier.
3. **Keeps Muon direction and momentum**; only the expert step length changes.

## Empirical Highlights
- FineWeb-Edu: Compass + Nesterov on all matrices matches or beats Muon, NorMuon, and other optimizers (weight decay matched to NorMuon on longer runs).
- Adding Compass factors to NorMuon: same or lower loss than NorMuon.
- Strongest when languages arrive in separate blocks.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.04140`
- Code: none found as of 2026-10-06 (`code_status: none`).
