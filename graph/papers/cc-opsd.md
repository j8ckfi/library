---
id: paper:cc-opsd
type: paper
title: 'A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation
  for Reasoning'
authors:
- Mayug Maniparambil
- Ayush Rai
- Ekansh Verma
- Noel E. O'Connor
- Fergal Reid
year: 2026
month: 10
arxiv_id: '2610.13744'
url: https://arxiv.org/abs/2610.13744
methods:
- method:cc-opsd
cites:
- paper:vista
- paper:srd
tags:
- post-training
- distillation
- opsd
- cc-opsd
---

# A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning

## Abstract Summary
A privileged teacher that only scores the student's rollout does not localize errors or downweight erroneous tokens. Locating an error is a search problem the scorer is never asked to do. The same model, allowed to generate a critique first, does localize. CC-OPSD generates that critique, then conditions the scoring teacher on it. The signal becomes corrective inside error spans and shifts mass toward backtracking tokens (Wait/But/Actually). Cold-start GRPO can use it when verifier groups are silent.

## Key Contributions
1. Scoring-only privileged OPSD fails gold error-span tests.
2. Critique-then-score teacher: localizing, corrective, backtracking-token shift.
3. Test-time resume and silent-prompt GRPO advantage.

## Empirical Highlights
- See `method:cc-opsd` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13744`
- Code: `none found` (`code_status: none`).
