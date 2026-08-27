---
id: method:sae-causal-audit
type: method
title: "SAE Causal Audit"
category: "interpretability"
status: active
papers:
  - paper:sae-causal-audit
recipes:
  - recipe:sae-causal-audit
claims:
  - benchmark: "Causal Feature Validation Benchmark"
    metric: "intervention consistency & faithfulness"
    value: "Standardized auditing protocol for SAE causal claims"
    baseline: "Manual Inspection"
    date: "2026-08-26"
    verified: true
    notes: "Automated causal auditing suite for sparse autoencoder features."
tags:
  - interpretability
  - sae
  - causal-audit
---

# SAE Causal Audit

## Method Overview
SAE Causal Audit provides an automated benchmark protocol to test whether SAE dictionary features possess genuine causal necessity and sufficiency.

## When to Use
- Validating SAE dictionaries before downstream steering or safety interventions.
