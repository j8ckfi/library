---
id: paper:bmuon
type: paper
title: 'BMuon: Budgeting Muon''s Spectral Geometry for Structured Compressibility'
authors:
- 'Rida Assalouh'
- 'Tom Jacobs'
- 'Rebekka Burkholz'
- 'Yani Ioannou'
- 'Umut Şimşekli'
year: 2026
month: 10
arxiv_id: '2610.23571'
url: https://arxiv.org/abs/2610.23571
methods:
- method:bmuon
cites:
- paper:muon2
tags:
- optimizer
- muon
- pruning
- active
---

# BMuon

## Abstract Summary
Muon has emerged as a strong optimizer for neural network training and admits an interpretation as steepest descent under a spectral-norm geometry. Yet we find that Muon-trained Transformers can degrade sharply when their MLP hidden channels are pruned after training. To reconcile Muon's optimization performance with structured compressibility, we introduce Budget Muon (BMuon), which modifies Muon's spectral geometry so that hidden channels across blocks compete for a shared allocation budget. The resulting oracle is exactly normalized steepest descent under a family of norms that interpolate between Muon's geometry and structured sparse geometries. Our principal sparsity control is an inter

## Key Contributions
1. Budget Muon interpolates Muon's spectral-norm steepest descent toward structured sparse geometries so hidden channels across blocks compete for a shared allocation budget. The practical surrogate is a minorization-maximization allocation rather than a sparsity-penalty coefficient.

## Empirical Highlights
- BMuon improves over Muon under post-training MLP channel pruning (1B) and gradual structured MLP prune (ViT-S/16)

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23571`
- Code: `none found` (`code_status: none`).
