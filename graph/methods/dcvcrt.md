---
id: method:dcvcrt
type: method
title: "DCVC-RT (Real-Time Deep Contextual Video Compression)"
category: "codec"
status: active
superseded_by: method:dcvc-uf
sota_for: []
supersedes:
  - method:dcvc-dc
papers:
  - paper:dcvcrt
recipes:
  - recipe:dcvc-video-codec
claims:
  - benchmark: "UVG & Real-Time Video Streaming"
    metric: "real-time decoding FPS & BD-Rate"
    value: ">60 FPS real-time decoding with VVC-parity compression"
    baseline: "DCVC-DC"
    date: "2025-02"
    verified: true
    notes: "Maintained as 2025 realtime neural video citation."
tags:
  - video
  - compression
  - real-time
  - codec
---

# DCVC-RT (Real-Time Deep Contextual Video Compression)

## Method Overview
DCVC-RT adapts deep contextual video compression for real-time decoding (>60 FPS at 1080p). Retained as the 2025 realtime citation.

## Supersession
- Superseded by `method:dcvc-uf` (2606.04410) for GPU video compression and `method:mlvc` (2606.28027) for deployable edge video.
