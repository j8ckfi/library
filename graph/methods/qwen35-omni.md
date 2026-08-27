---
id: method:qwen35-omni
type: method
title: "Qwen3.5-Omni Architecture & Talker"
category: "architecture"
status: active
papers:
  - paper:qwen35-omni
recipes:
  - recipe:qwen35-omni
claims:
  - benchmark: "Omni Multimodal & Audio Reasoning"
    metric: "streaming speech-language latency & quality"
    value: "End-to-end omni streaming interaction"
    baseline: "Qwen2.5-VL"
    date: "2026-08-26"
    verified: true
    notes: "Unified multimodal architecture with Talker RL alignment."
tags:
  - architecture
  - omni
  - multimodal
  - speech
  - qwen
---

# Qwen3.5-Omni Architecture & Talker

## Method Overview
Qwen3.5-Omni integrates real-time audio and vision processing into a unified transformer backbone, utilizing GSPO and Talker RL for streaming speech turn-taking.

## When to Use
- Building real-time streaming conversational speech-vision agents.
