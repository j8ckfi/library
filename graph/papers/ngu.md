---
id: paper:ngu
type: paper
title: "Learning to Solve Hard Problems in RL for LLMs by Never Giving Up"
authors:
  - "Michael Noukhovitch"
  - "Hamish Ivison"
  - "Nathan Lambert"
  - "Aaron Courville"
year: 2026
month: 9
arxiv_id: "2609.13443"
url: "https://arxiv.org/abs/2609.13443"
methods:
  - method:ngu
cites:
  - paper:grpo
  - paper:dapo
tags:
  - post-training
  - rlvr
  - adaptive-sampling
  - async-rl
  - ngu
---

# Learning to Solve Hard Problems in RL for LLMs by Never Giving Up

## Abstract Summary
RL on LLMs does not lift a dataset evenly. Easy prompts that the initial model already solves improve a lot; hard prompts barely move. The paper names this the Matthew Effect ("the rich get richer") and argues that fixed-$K$ GRPO-family sampling wastes compute on easy prompts (a rare wrong sample keeps them in the batch) instead of only undersampling hard ones. Never Give Up (NGU) is an asynchronous adaptive sampler: start at small $K$, stop if any completion is correct, otherwise put the prompt back on the generator with probability $p_{\mathrm{NGU}}$ until a correct sample appears. Easy prompts filter quickly; hard prompts accumulate a larger group. On Deepscaler (Qwen3-4B-Base, ~120 H100 hours) NGU raises hard-subset and average pass@1 over compute-matched GRPO $K\in\{16,32,64\}$. On Manufactoria, GRPO with a per-test reward stalls short of full-problem solves; GRPO+NGU keeps solving harder tests until all-tests pass. Loss is unchanged. Claimed GitHub `mnoukhov/never-give-up` was 404 at ingest (2026-09-16); blog is live.

## Key Contributions
1. **Matthew Effect in RL for LLMs**: gains scale with initial competence (Olmo 3.1 RL-Zero math, DeepCoder, DeepSWE).
2. **Signal efficiency, not just signal loss**: smaller $K$ can beat larger $K$ under a fixed $N\times K$ budget by filtering easy prompts faster.
3. **NGU adaptive sampling** on async RL: geometric retry until $\ge 1$ correct, with staleness cutoff $T$ and "anchor positives" GRPO baseline using stale negatives.
4. **Harness-aware Matthew Effect** on coding tests: classify difficulty after prompt/harness adaptation, not only at step 0.

## Empirical Highlights
- Deepscaler (Qwen3-4B-Base, AIME 25 / BRUMO 25, three seeds, ~120 H100 hours): NGU $p=0.875$ average pass@1 $26.5\pm0.6$ vs GRPO $N=8,K=16$ $24.8\pm1.0$ / $N=4,K=32$ $25.3\pm0.5$; hard-subset $\Delta$pass@1 $4.3\pm1.2$ vs $1.6\pm0.3$ for $K=16$.
- Manufactoria (Qwen3-4B-Instruct-2507, $p_{\mathrm{NGU}}=0.95$): GRPO plateaus on hard tests and does not pass all tests on even one eval problem; NGU continues on hard tests and reaches all-tests solves.
- GSM8k Platinum (Qwen2.5-0.5B-Instruct): $K=4$ + NGU $p=0.95$ beats GRPO $K\in\{4,8,16,32\}$ on extra-hard; keep completions with age $T=4$, not $T\ge8$.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.13443`
- Blog: `https://mnoukhov.github.io/posts/ngu`
- Claimed code `https://github.com/mnoukhov/never-give-up` returned HTTP 404 on 2026-09-16. Recipe is a paper/blog stub (`code_status: partial`; `repo_url: none found`).
