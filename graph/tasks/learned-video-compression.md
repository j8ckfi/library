---
id: task:learned-video-compression
type: task
title: "Learned Neural Video Compression"
domain: "video"
summary: "End-to-end rate-distortion neural video codecs utilizing learned optical flow, conditional inter-frame contexts, and cross-channel entropy models."
current_sota:
  - method: method:dcvc-uf
    as_of: "2026-08-26"
    benchmark: "UVG / GPU Real-Time Video Streaming"
    metric: "GPU decoding FPS & BD-Rate"
    value: "Default SOTA GPU Neural Video Codec"
    notes: "DCVC-UF (2606.04410) for GPU video."
  - method: method:mlvc
    as_of: "2026-08-26"
    benchmark: "Mobile & Edge Video Deployment / UVG"
    metric: "edge decoding latency & BD-Rate"
    value: "Default SOTA Deployable Video Codec"
    notes: "MLVC (2606.28027) for deployable mobile/edge video."
methods:
  - method:dcvc-uf
  - method:mlvc
  - method:dcvcrt
  - method:uiic
  - method:gvc-rt
  - method:dcvc-mb
  - method:dcvc-dc
tags:
  - video
  - compression
  - neural-codec
---

# Learned Neural Video Compression

## SOTA Recommendation (as of 2026-08-26)
- **Neural Video GPU**: **DCVC-UF** (`method:dcvc-uf`, 2606.04410).
- **Neural Video Deploy**: **MLVC** (`method:mlvc`, 2606.28027).
- **2025 Realtime Reference**: **DCVC-RT** (`method:dcvcrt`).
