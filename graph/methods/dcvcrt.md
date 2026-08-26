---
id: method:dcvcrt
type: method
title: "DCVC-RT (Real-Time Deep Contextual Video Compression)"
category: "codec"
status: sota
sota_for:
  - task:learned-video-compression
supersedes:
  - method:dcvc-dc
papers:
  - paper:dcvcrt
  - paper:mlvc
recipes:
  - recipe:dcvc-video-codec
claims:
  - benchmark: "UVG & Real-Time Video Streaming"
    metric: "real-time decoding FPS & BD-Rate"
    value: ">60 FPS real-time decoding with VVC-parity compression"
    baseline: "DCVC-DC"
    date: "2025-02"
    verified: true
    notes: "Requires long-sequence fine-tuning to prevent PSNR collapse in multi-frame streaming."
tags:
  - video
  - compression
  - real-time
  - codec
---

# DCVC-RT (Real-Time Deep Contextual Video Compression)

## Method Overview
DCVC-RT adapts deep contextual video compression for real-time decoding (>60 FPS at 1080p). It replaces slow serial autoregressive entropy models with parallel checkerboard contexts and simplified feature warping.

## Critical Training Rule
- **Long-Sequence Fine-Tuning**: You MUST fine-tune on long video sequences (e.g. 32+ frames) during final training epochs; otherwise, temporal context errors compound and PSNR collapses.

## Supersession
- Supersedes `method:dcvc-dc` for real-time streaming applications.
