---
id: task:neural-video-gpu
type: task
title: "GPU Neural Video Compression"
domain: "video"
summary: "High-throughput GPU-accelerated neural video encoding and decoding."
current_sota:
  - method: method:dcvc-uf
    as_of: "2026-08-26"
    benchmark: "UVG / GPU Real-Time Streaming"
    metric: "GPU FPS & BD-Rate"
    value: "Default SOTA GPU NVC"
    notes: "DCVC-UF (2606.04410)."
methods:
  - method:dcvc-uf
  - method:dcvcrt
  - method:gvc-rt
tags:
  - video
  - compression
  - gpu
  - dcvc-uf
---

# GPU Neural Video Compression

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **DCVC-UF** (`method:dcvc-uf`, 2606.04410).
