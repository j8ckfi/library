---
id: method:gvc-rt
type: method
title: "GVC-RT (Generative Video Codec)"
category: "codec"
status: active
papers:
  - paper:gvc-rt
recipes:
  - recipe:gvc-rt
claims:
  - benchmark: "Low-Bitrate Real-Time Streaming"
    metric: "perceptual quality (LPIPS) & FPS"
    value: "Photorealistic streaming at sub-100 kbps"
    baseline: "DCVC-RT"
    date: "2026-08-26"
    verified: true
    notes: "Generative single-step diffusion decoding for video streaming."
tags:
  - video
  - compression
  - generative
  - gvc-rt
---

# GVC-RT (Generative Video Codec)

## Method Overview
GVC-RT leverages generative diffusion priors to reconstruct ultra-low-bitrate video streams with photorealistic detail.

## When to Use
- Bandwidth-constrained streaming environments where perceptual quality is prioritized over pixel-exact MSE.
