---
id: paper:monarch-muon
type: paper
title: 'Monarch-Muon: Structure-Aware Muon for Fast and Memory-Efficient Pretraining'
authors:
- Alexander Miasnikov
- Ruslan Kabirov
- Gleb Molodtsov
- Dmitrii Vlashchuk
- Vladimir Aletov
- Nail Bashirov
- Daniil Tikhonov
- Maxim Krutikov
- Aleksandr Shestakov
- Aleksandr Beznosikov
year: 2026
month: 10
arxiv_id: '2610.17429'
url: https://arxiv.org/abs/2610.17429
methods:
- method:monarch-muon
cites:
- paper:muon2
- paper:scale
tags:
- pretraining
- optimizer
- muon
- monarch
---

# Monarch-Muon

## Abstract Summary
Structure-aware Muon on Monarch-factored weights. Beats Monarch-AdamW at 257M dense and 1B MoE. Dense Muon at 257M is still better (2.99 vs 3.06). 6.89B H100 systems numbers cut optimizer-state memory and step time.

## Key Contributions
1. Muon Newton-Schulz applied in Monarch factor space rather than full matrices.
2. Quality vs Monarch-AdamW, not vs dense Muon2.
3. 6.89B H100 peak-memory / optimizer-step timing.

## Empirical Highlights
- 257M 2-block Monarch-Muon 3.06 vs Monarch-AdamW 3.09; dense Muon 2.99 (single-paper).
- 1B MoE 2-block 2.68 vs Monarch-AdamW 2.77.
- 6.89B H100: peak 68.87→52.94 GB; Muon state 14.60→6.77 GB; opt step 1288.3→304.4 ms; full-step −45%, peak mem −23%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.17429`
- Code: `none found` (`code_status: none`).
