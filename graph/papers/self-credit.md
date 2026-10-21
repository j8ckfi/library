---
id: paper:self-credit
type: paper
title: 'Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group Rescaling'
authors:
- 'Fangcong Yin'
- 'Ming Yin'
- 'Tanvi Bhandarkar'
- 'Aashu Singh'
- 'Eryk Helenowski'
- 'Shlok Kumar Mishra'
- 'Saghar Hosseini'
- 'Karthik Abinav Sankararaman'
- 'Greg Durrett'
- 'Dinkar Juyal'
year: 2026
month: 10
arxiv_id: '2610.28388'
url: https://arxiv.org/abs/2610.28388
methods:
- method:self-credit
cites:
- paper:canopy
tags:
- agentic-rl
- credit-assignment
- active
---

# Self-Credit

## Abstract Summary
Self-Credit densifies sparse outcome rewards by citing earlier turns, comparing those citations across successful and failed group rollouts, and reweighting advantages on the cited turns.

## Key Contributions
1. Self-generated citations plus intra-group rescaling for agentic RLVR.

## Empirical Highlights
- BrowseComp-Plus Qwen3-8B/32B +37.0/+36.2 vs base and +8.5/+5.6 vs strongest agentic RL; GAIA +4.9; xBench-DeepSearch +4.7.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28388`
- Code: `none found` (`code_status: none`).
