---
id: paper:thundersyncrl
type: paper
title: "ThunderSyncRL: Lossless Acceleration of Agentic Reinforcement Learning"
authors:
  - Seil Kang
  - Hangoo Kang
  - Tarun Suresh
  - Youngeun Kim
  - Shreyas Pimpalgaonkar
  - Seong Jae Hwang
  - Azalia Mirhoseini
year: 2026
month: 10
arxiv_id: "2610.05935"
url: "https://arxiv.org/abs/2610.05935"
methods:
  - method:thundersyncrl
cites:
  - paper:sao
  - paper:miles
  - paper:grpo
  - paper:opd
tags:
  - post-training
  - training-systems
  - agentic
  - thundersyncrl
---

# ThunderSyncRL: Lossless Acceleration of Agentic Reinforcement Learning

## Abstract Summary
Synchronous agentic RL leaves the learner idle until rollout/verify finish; async overlap pays policy staleness. ThunderSyncRL starts the gradient as soon as required inputs are fixed, with no staleness. GRPO: per-trajectory score gradient when that reward arrives, without waiting for the group. OPD: per-turn teacher-scored actions while tool calls run. Same GRPO/OPD updates as batch-sync (proved). SWE-bench Verified and Terminal Bench 4.0: same performance up to 1.9x faster than sync; vs async at fixed budget up to +2.47pp. No GitHub URL in the abstract (`code_status: none`). Beside Miles on agentic-async-rl; does not retarget SAO or Miles.

## Key Contributions
1. **Lossless overlap**: gradient as soon as inputs are fixed; no policy staleness.
2. **GRPO streaming**: per-trajectory gradient when the reward arrives.
3. **OPD streaming**: per-turn teacher scores while tools run.

## Empirical Highlights
- Same SWE-bench Verified / Terminal Bench 4.0 performance up to 1.9× vs synchronous.
- Vs asynchronous at a fixed budget: up to +2.47 percentage points (zero staleness).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05935`
- Code: none found as of 2026-10-06 (`code_status: none`). Abstract mentions a blog post / GitHub without a URL.
