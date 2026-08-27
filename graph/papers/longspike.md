---
id: paper:longspike
type: paper
title: "LongSpike: Ultra-Long Sequence Spiking Neural Networks with SSM State Transitions"
authors:
  - "Xinrui He et al."
year: 2026
month: 6
arxiv_id: "2606.12895"
url: "https://arxiv.org/abs/2606.12895"
methods:
  - method:longspike
cites:
  - paper:silif
tags:
  - snn
  - neuromorphic
  - ssm
  - longspike
---

# LongSpike: Ultra-Long Sequence Spiking Neural Networks with SSM State Transitions

## Abstract Summary
LongSpike introduces structured state-space continuous transitions into deep Spiking Neural Networks, enabling SNN processing of long context sequences without vanishing or exploding membrane potentials, superseding SiLIF as the default SSM-SNN architecture.

## Key Contributions
1. **SSM State Dynamics**: Bridges linear state space recurrence with discrete spiking thresholds.
2. **Ultra-Long Sequences**: SNN sequence modeling scaled beyond 32k time steps.

## Open Source Repository
- Implementation: `https://github.com/xinruihe389-commits/LongSpike`
