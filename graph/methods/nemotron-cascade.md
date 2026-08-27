---
id: method:nemotron-cascade
type: method
title: "Nemotron-Cascade Alignment"
category: "rl-alignment"
status: active
papers:
  - paper:nemotron-cascade
recipes:
  - recipe:nemotron-cascade
claims:
  - benchmark: "Instruction & Reasoning Suites"
    metric: "AlpacaEval 2 / Arena-Hard"
    value: "Cascaded alignment progression"
    baseline: "Single-Stage SFT"
    date: "2026-08-26"
    verified: true
    notes: "Multi-stage supervised fine-tuning and reasoning distillation."
tags:
  - post-training
  - alignment
  - reasoning
  - nemotron
---

# Nemotron-Cascade Alignment

## Method Overview
Nemotron-Cascade sequences supervised fine-tuning, reasoning distillation, and preference optimization across multiple distinct stages to build capable reasoning models.

## When to Use
- Constructing multi-phase alignment pipelines.
