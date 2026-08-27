---
id: paper:nemotron-3-super-latentmoe
type: paper
title: "Nemotron-3 Super: Latent Mixture-of-Experts with Compressed Routing"
authors:
  - "NVIDIA Nemotron Team"
year: 2026
month: 4
arxiv_id: "2604.12374"
url: "https://arxiv.org/abs/2604.12374"
methods:
  - method:nemotron-3-super-latentmoe
cites: []
tags:
  - architecture
  - moe
  - latent-moe
  - nemotron
---

# Nemotron-3 Super: Latent Mixture-of-Experts with Compressed Routing

## Abstract Summary
Nemotron-3 Super introduces Latent MoE routing, projecting token representations into low-dimensional latent subspaces before routing, drastically reducing cross-node expert dispatch communication.

## Key Contributions
1. **Latent MoE Routing**: Compresses inter-GPU expert routing tokens into low-rank latent spaces.
2. **Communication Reduction**: Cuts all-to-all expert communication bandwidth by up to 60%.

## Open Source Repository
- Implementation: `none found`
