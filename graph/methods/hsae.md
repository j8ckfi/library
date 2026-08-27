---
id: method:hsae
type: method
title: "H-SAE (Hierarchical Sparse Autoencoder)"
category: "interpretability"
status: active
papers:
  - paper:hsae
recipes:
  - recipe:hsae
claims:
  - benchmark: "Hierarchical Feature Extraction"
    metric: "reconstruction fidelity vs granularity"
    value: "Tree-structured semantic feature taxonomies"
    baseline: "Standard TopK SAE"
    date: "2026-08-26"
    verified: true
    notes: "Hierarchical multi-tier sparse dictionary learning."
tags:
  - interpretability
  - sae
  - hierarchical
  - hsae
---

# H-SAE (Hierarchical Sparse Autoencoder)

## Method Overview
H-SAE extracts hierarchical multi-scale dictionaries from neural activations, structuring features into tree-structured taxonomies.

## When to Use
- Multi-scale semantic feature analysis across coarse and fine conceptual granularities.
