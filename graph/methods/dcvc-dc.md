---
id: method:dcvc-dc
type: method
title: "DCVC-DC (Deep Contextual Video Compression with Dual Context)"
category: "codec"
status: sota
sota_for:
  - task:learned-video-compression
supersedes: []
papers:
  - paper:dcvc-dc-paper
recipes:
  - recipe:dcvc-video-codec
claims:
  - benchmark: "UVG & MCL-JCV Datasets"
    metric: "BD-Rate reduction vs H.266/VVC (VTM)"
    value: "-28.4% BD-Rate (PSNR)"
    baseline: "H.266/VVC Reference Software (VTM-13.0)"
    date: "2024-03"
    verified: true
    notes: "First learned neural video compression framework to comprehensively outperform VVC on standard benchmark suites."
tags:
  - video
  - compression
  - neural-codec
  - entropy-model
---

# DCVC-DC (Deep Contextual Video Compression with Dual Context)

## Method Overview
DCVC-DC (Deep Contextual Video Compression with Dual Context) addresses temporal correlation and entropy coding limitations in neural video coding.

Traditional learned video codecs transmit residual error frames after motion compensation. DCVC-DC replaces residual coding with **Conditional Contextual Coding**:
1. **Temporal Context Mining**: Multi-scale feature offsets are propagated from previously decoded reference frames using learned optical flow vectors.
2. **Dual-Context Entropy Model**: The probability distribution of quantized latent representations \(\hat{y}_t\) is conditioned on both:
   - Temporal contextual features from preceding video frames.
   - Spatial-channel causal contexts within the current frame's latent tensor.
3. **End-to-End Rate-Distortion Optimization**:
   \[
   \mathcal{L} = R_{\text{flow}} + R_{\text{context}} + \lambda D(x_t, \hat{x}_t)
   \]

## When to Use
- **Next-Generation Video Compression Research**: Developing learned video streaming architectures with superior perceptual fidelity to HEVC/VVC.
- **Differentiable Video Pipelines**: When video compression must be embedded into end-to-end differentiable computer vision models.

## Gotchas & Failure Modes
1. **Decoding Latency on CPU**: Autoregressive spatial-channel entropy decoding is computationally intensive; requires GPU acceleration or parallel checkerboard entropy models.
2. **Long Group of Pictures (GOP) Error Accumulation**: In long streaming sequences without periodic I-frames, reconstruction artifacts in temporal context features can compound over time.
