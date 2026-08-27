---
id: paper:mlvc
type: paper
title: "MLVC: Mobile and Lightweight Neural Video Compression for Edge Deployment"
authors:
  - "Microsoft Research MLVC Authors"
year: 2026
month: 6
arxiv_id: "2606.28027"
url: "https://arxiv.org/abs/2606.28027"
methods:
  - method:mlvc
cites:
  - paper:dcvcrt
tags:
  - video
  - compression
  - neural-codec
  - edge
  - mobile
  - mlvc
---

# MLVC: Mobile and Lightweight Neural Video Compression for Edge Deployment

## Abstract Summary
MLVC presents a lightweight neural video codec optimized specifically for mobile NPU and edge deployment, achieving real-time decoding with ultra-low thermal and power overhead, establishing the deployable NVC SOTA default.

## Key Contributions
1. **Edge-Optimized Architecture**: Pruned contextual transforms tailored for mobile NPUs and edge DSPs.
2. **Deployable SOTA Default**: Real-time 60 FPS 1080p decoding on mobile SoCs with VVC-competitive compression.

## Open Source Repository
- Implementation: `https://github.com/microsoft/mlvc`
