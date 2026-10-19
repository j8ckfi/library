---
id: paper:metacurate
type: paper
title: 'MetaCurate: Evolving Curation Filters for High-Quality Agentic Coding Data'
authors:
- 'Donghoon Kim'
- 'Seunghyuk Oh'
- 'Kevin Galim'
- 'Minseo Kim'
- 'Minjae Lee'
- 'Younghyun Kim'
- 'Wooseok Seo'
- 'Hyung Il Koo'
- 'Wonjun Kang'
year: 2026
month: 10
arxiv_id: '2610.23134'
url: https://arxiv.org/abs/2610.23134
methods:
- method:metacurate
cites:
- paper:olmo-3
tags:
- sft
- curation
- swe
- active
---

# MetaCurate

## Abstract Summary
Supervised fine-tuning on agent trajectories is an effective way to improve coding agents, but selecting useful training examples requires more than identifying successful runs. A resolved patch may follow inefficient reasoning or unnecessary tool use, while a failed run may still contain useful intermediate steps. Training pipelines therefore rely on rules and qualitative assessments to filter trajectories, yet designing these filters typically requires substantial human expertise, and validating improvements through repeated training and evaluation is expensive. We introduce MetaCurate, a training-free framework that evolves executable trajectory curation filters using pairwise LLM judgmen

## Key Contributions
1. MetaCurate evolves a curation filter from pairwise LLM judgments: disagreements with the judge rewrite the filter's rules, rubric, and aggregation, then the filter scores trajectories independently at scale.

## Empirical Highlights
- highest mean among compared methods, including hand-authored filters and a 3.5x-cost training-loop baseline

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23134`
- Code: `none found` (`code_status: none`).
