---
id: method:uiic
type: method
title: "UIIC (Ultra-Fast Inter-frame Codec)"
category: "codec"
status: active
papers:
  - paper:uiic
recipes:
  - recipe:uiic
claims:
  - benchmark: "Interactive Video Streaming"
    metric: "encoding latency"
    value: "Sub-millisecond per-frame encoding"
    baseline: "Standard Neural Video Codec"
    date: "2026-08-26"
    verified: true
    notes: "Flow-free inter-frame residual completion."
tags:
  - video
  - compression
  - uiic
---

# UIIC (Ultra-Fast Inter-frame Codec)

## Method Overview
UIIC eliminates optical flow estimation, formulating video compression as conditional residual completion for sub-millisecond per-frame encoding.

## When to Use
- Interactive cloud rendering and screen sharing.
