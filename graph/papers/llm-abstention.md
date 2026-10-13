---
id: paper:llm-abstention
type: paper
title: Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer
  Selection
authors:
- Juan Terven
- Diana-Margarita Córdova-Esparza
- Ruben Gomez
- Carlos Miranda Rocha
- Julio-Alejandro Romero-González
- Edgar Chavez-Urbiola
year: 2026
month: 10
arxiv_id: '2610.13821'
url: https://arxiv.org/abs/2610.13821
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- post-training
- gotcha
- abstention
- reasoning-rl
---

# Can Language Models Learn When to Abstain?

## Abstract Summary
Caution/evidence paper. RL variants did not consistently improve abstention on Qwen3-14B. A learned answer selector raised TriviaQA coverage 20.2%→30.9% and cut error 23.0%→14.5%. Note on `task:reasoning-rl-alignment`. Does not retarget CISPO.

## Key Contributions
1. RL variants failed to consistently improve abstention on Qwen3-14B.
2. Learned answer selector: TriviaQA coverage 20.2%→30.9%, error 23.0%→14.5%.

## Empirical Highlights
- Abstention is not a free side-effect of reasoning RLVR.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13821`
- Code: `https://github.com/jrterven/Can-LLMs-learn-to-abstain` (`code_status: released`).
