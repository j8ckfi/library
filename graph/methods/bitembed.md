---
id: method:bitembed
type: method
title: "BitEmbed (Embedding Table Compression)"
category: "quantization"
status: active
papers:
  - paper:bitembed
recipes:
  - recipe:bitembed
claims:
  - benchmark: "Large Vocabulary Embedding Benchmarks"
    metric: "embedding memory savings"
    value: "Up to 85% embedding memory reduction"
    baseline: "FP16 Embeddings"
    date: "2026-08-26"
    verified: true
    notes: "1-bit / 2-bit coordinate factorization for large token vocabulary tables."
tags:
  - quantization
  - embeddings
  - compression
  - bitembed
---

# BitEmbed (Embedding Table Compression)

## Method Overview
BitEmbed compresses massive embedding tables in large-vocabulary foundation models to 1-bit and 2-bit representations.

## When to Use
- Deploying models with 128k+ token vocabularies onto memory-constrained accelerators.
