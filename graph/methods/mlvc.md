---
id: method:mlvc
type: method
title: "MLVC (Deployable Neural Video Codec)"
category: "codec"
status: sota
sota_for:
  - task:learned-video-compression
  - task:neural-video-deploy
supersedes:
  - method:dcvcrt
papers:
  - paper:mlvc
recipes:
  - recipe:mlvc
claims:
  - benchmark: "Mobile & Edge Deployment / UVG"
    metric: "decode latency & BD-Rate"
    value: "Default SOTA neural video deploy standard"
    baseline: "DCVC-RT / H.265"
    date: "2026-08-26"
    verified: true
    notes: "Lightweight multi-level neural video coding optimized for mobile NPU and edge deployment."
tags:
  - video
  - compression
  - neural-codec
  - edge
  - mobile
  - mlvc
  - sota
---

# MLVC (Deployable Neural Video Codec)

## Method Overview
MLVC is the state-of-the-art deployable neural video codec designed specifically for mobile NPUs and edge hardware:
1. **Lightweight Entropy Contexts**: Pruned transforms tailored for edge DSP/NPU compute limits.
2. **Edge SOTA**: Real-time 60 FPS 1080p playback with ultra-low thermal consumption.

## When to Use
- Default SOTA method for deployable edge and mobile neural video compression.

## Supersession
- Supersedes `method:dcvcrt` as the deployable edge NVC standard.
