---
id: task:neural-video-deploy
type: task
title: "Deployable Edge Neural Video Compression"
domain: "video"
summary: "Lightweight neural video codecs optimized for real-time mobile NPU and edge execution."
current_sota:
  - method: method:mlvc
    as_of: "2026-08-26"
    benchmark: "Mobile & Edge Video Deployment"
    metric: "edge decoding latency & BD-Rate"
    value: "Default SOTA Deployable NVC"
    notes: "MLVC (2606.28027)."
methods:
  - method:mlvc
  - method:dcvcrt
  - method:uiic
tags:
  - video
  - compression
  - edge
  - mobile
  - mlvc
---

# Deployable Edge Neural Video Compression

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **MLVC** (`method:mlvc`, 2606.28027).
