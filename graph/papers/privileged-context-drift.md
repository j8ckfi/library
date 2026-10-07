---
id: paper:privileged-context-drift
type: paper
title: "Privileged Context as Drift in On-Policy Self-Distillation"
authors:
  - Ravenor Davion
  - Nick Rui
year: 2026
month: 10
arxiv_id: "2610.07842"
url: "https://arxiv.org/abs/2610.07842"
methods:
  - method:privileged-context-drift
  - method:vista
  - method:u-opsd
  - method:opsd-collapse-review
cites:
  - paper:vista
  - paper:u-opsd
  - paper:opsd-collapse-review
tags:
  - post-training
  - opsd
  - drift
  - privileged-context-drift
---

# Privileged Context as Drift in On-Policy Self-Distillation

## Abstract Summary
Controlled study: privileged-context **content** (demo vs feedback vs rephrase) drives policy drift / forgetting more than the source of the context. KL 5.1× more from content than source; cosine 0.571 vs 0.255. Niche evidence node on the OPSD family (u-OPSD, VISTA, OPSD collapse review). Not a trainer. Does not retarget VISTA.

## Key Contributions
1. **Content > source** for OPSD drift.
2. **Demo vs feedback vs rephrase** is the lever, not which teacher wrote it.
3. **Ontology note**, not a train kernel.

## Empirical Highlights
- KL 5.1× more from content than source; cosine 0.571 vs 0.255.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07842`
- Code: none found as of 2026-10-07 (`code_status: none`).
