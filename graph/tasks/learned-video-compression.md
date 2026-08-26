---
id: task:learned-video-compression
type: task
title: "Learned Neural Video Compression"
domain: "video"
summary: "End-to-end rate-distortion neural video codecs utilizing learned optical flow, conditional inter-frame contexts, and cross-channel entropy models."
current_sota:
  - method: method:dcvcrt
    as_of: "2026-08-26"
    benchmark: "UVG / Real-Time Video Streaming"
    metric: "real-time decoding FPS & BD-Rate"
    value: ">60 FPS real-time decoding with VVC-parity compression"
    notes: "DCVC-RT (Real-Time DCVC). Must long-sequence finetune or PSNR collapses."
methods:
  - method:dcvcrt
  - method:dcvc-dc
tags:
  - video
  - compression
  - neural-codec
---

# Learned Neural Video Compression

## Problem Definition
Video streaming accounts for the majority of global internet bandwidth. Traditional standards (H.264, H.265/HEVC, H.266/VVC) rely on hand-engineered block motion compensation and discrete cosine transforms. Learned neural video compression optimizes rate-distortion autoencoders end-to-end with differentiable temporal contextual priors.

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**: UVG dataset, MCL-JCV, HEVC Class B/C/D/E test sequences.
- **Metrics**: Bjøntegaard Delta Rate (BD-Rate) across PSNR and MS-SSIM curves relative to reference VVC (VTM) test model.

## SOTA Landscape
The **DCVC-DC** (Deep Contextual Video Compression with Dual Context) architecture by Microsoft Research represents the leading neural video codec, outperforming the reference H.266/VVC test model by exploiting both temporal frame contexts and cross-channel conditional probability distribution models.
