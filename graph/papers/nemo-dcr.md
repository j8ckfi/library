---
id: paper:nemo-dcr
type: paper
title: "NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale"
authors:
  - Songlin Jiang
  - Zhiyu Li
  - Terry Kong
  - Yu Yao
  - Youngeun Kwon
  - Bernard Nguyen
  - Ashwath Aithal
  - Mario Di Francesco
year: 2026
month: 10
arxiv_id: "2610.08430"
url: "https://arxiv.org/abs/2610.08430"
methods:
  - method:nemo-dcr
cites:
  - paper:miles
tags:
  - systems
  - training-systems
  - agentic
  - weight-sync
  - nemo-dcr
---

# NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale

## Abstract Summary
Disaggregated agentic RL at 1T scale spends most of the step on weight sync. ~1% of BF16 weights change per step. NeMo-DCR is bit-exact delta-compressed refit: a relay tree ships the changed coordinates. 1T relay-tree 150s vs 87.5 min; 12–40× faster at 3–5% change. NVIDIA NeMo RL PR #2444. Active infra plug-in beside Miles / Rufus-Air. Does not replace Miles.

## Key Contributions
1. **Bit-exact delta-compressed refit** for disaggregated agentic RL.
2. **~1% of BF16 weights change per step** at 1T.
3. **Relay-tree 150s vs 87.5 min** at 1T.

## Empirical Highlights
- 12–40× faster at 3–5% change fractions.
- Code: NVIDIA-NeMo/RL pull/2444.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.08430`
- Code: `https://github.com/NVIDIA-NeMo/RL/pull/2444` (`code_status: released`; HTTP 200 as of 2026-10-07).
