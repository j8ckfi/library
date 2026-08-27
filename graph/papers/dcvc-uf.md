---
id: paper:dcvc-uf
type: paper
title: "DCVC-UF: Ultra-Fast Neural Video Compression with GPU Acceleration"
authors:
  - "Microsoft Research DCVC Authors"
year: 2026
month: 6
arxiv_id: "2606.04410"
url: "https://arxiv.org/abs/2606.04410"
methods:
  - method:dcvc-uf
cites:
  - paper:dcvcrt
tags:
  - video
  - compression
  - neural-codec
  - gpu
  - dcvc-uf
---

# DCVC-UF: Ultra-Fast Neural Video Compression with GPU Acceleration

## Abstract Summary
DCVC-UF achieves ultra-fast neural video compression on GPUs through parallelized spatial-temporal entropy modeling and tensor-core-aligned motion compensation, establishing the 2026 GPU neural video codec SOTA default.

## Key Contributions
1. **Ultra-Fast Parallel Entropy Modeling**: Replaces serial contextual models with parallel GPU tensor-core kernels.
2. **GPU SOTA Default**: Superior rate-distortion BD-rate and >120 FPS decoding throughput.

## Open Source Repository
- Implementation: `https://github.com/microsoft/DCVC`
