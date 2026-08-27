---
id: method:dcvc-uf
type: method
title: "DCVC-UF (GPU Neural Video Codec)"
category: "codec"
status: sota
sota_for:
  - task:learned-video-compression
  - task:neural-video-gpu
supersedes:
  - method:dcvcrt
papers:
  - paper:dcvc-uf
recipes:
  - recipe:dcvc-uf
claims:
  - benchmark: "UVG / HEVC Class B-E / GPU Real-Time Video"
    metric: "BD-Rate & GPU FPS"
    value: "Default SOTA GPU neural video codec (>120 FPS at 1080p)"
    baseline: "DCVC-RT / VVC"
    date: "2026-08-26"
    verified: true
    notes: "Ultra-fast neural video compression with GPU tensor core parallelism."
tags:
  - video
  - compression
  - neural-codec
  - gpu
  - dcvc-uf
  - sota
---

# DCVC-UF (GPU Neural Video Codec)

## Method Overview
DCVC-UF establishes the state-of-the-art GPU neural video codec standard:
1. **Parallel Contextual Transforms**: Replaces slow serial entropy models with parallel GPU tensor core execution.
2. **Ultra-Fast Throughput**: Delivers >120 FPS 1080p decoding with VVC-competitive compression rates.

## When to Use
- Default SOTA method for GPU neural video compression training and real-time GPU streaming.

## Supersession
- Supersedes `method:dcvcrt` as the GPU neural video codec standard.
