---
id: task:direct-preference-alignment
type: task
title: "Direct Preference Alignment & Offline Post-Training"
domain: "post-training"
summary: "Offline instruction tuning and preference alignment without online policy rollouts or separate reference model inference."
current_sota:
  - method: method:olmo-3
    as_of: "2026-08-26"
    benchmark: "AlpacaEval 2 / Arena-Hard"
    metric: "length-controlled win rate"
    value: "OLMo-3 Dolci Open Stack"
    notes: "OLMo-3 Dolci (2512.13961) supersedes standalone offline DPO."
methods:
  - method:olmo-3
  - method:nemotron-cascade-2
  - method:tulu3-rlvr
  - method:simpo
  - method:dpo
tags:
  - post-training
  - preference-alignment
---

# Direct Preference Alignment & Offline Post-Training

## SOTA Recommendation (as of 2026-08-26)
- **Primary Stack**: **OLMo-3 Dolci** (`method:olmo-3`, 2512.13961).
