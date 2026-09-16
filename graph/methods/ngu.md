---
id: method:ngu
type: method
title: "Never Give Up (NGU)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR loss"
    reason: "NGU is an async sampler; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "MoE/VL RLVR loss"
    reason: "SAPO remains the MoE/VL algorithm; NGU does not change the surrogate"
    use_instead: "method:sapo"
  - when: "cold-start prompt selection / silent-group waste before the first target-policy rollout"
    reason: "ThinkPrior ranks prompts with a zero-rollout Beta prior; NGU keeps resampling one prompt until ≥1 correct"
    use_instead: "method:thinkprior"
  - when: "reweighting whole examples by gradient alignment"
    reason: "DIEM reweights a minibatch after rollouts exist; NGU changes how many samples a prompt gets"
    use_instead: "method:diem"
  - when: "token-level truncation inside an already-computed GRPO/CISPO loss"
    reason: "GMTS filters tokens; NGU is a prompt sampler"
    use_instead: "method:gmts"
  - when: "evaluating whether data policies beat uniform GRPO on final accuracy"
    reason: "DataFlex-RL is the accuracy-null platform; NGU is a compute-reallocation sampler, not a data-policy bake-off"
    use_instead: "method:dataflex-rl"
  - when: "variable tool latency / async stragglers"
    reason: "SAO owns straggler replay; NGU only uses async so filtered easy prompts free generator time for hard ones"
    use_instead: "method:sao"
assumptions:
  - "Host is GRPO-family RLVR with a verifier. Paper uses off-policy async RL (in-flight updates), Deepspeed + vLLM. NGU needs that async loop so dropping easy prompts reallocates compute."
  - "Math: Qwen3-4B-Base on a 10k Deepscaler subset, eval AIME 2025 + BRUMO Nov 2025, ~120 H100 hours, three seeds. Code: Qwen3-4B-Instruct-2507 on Manufactoria, 2x8 H100, p_NGU=0.95."
  - "Does not claim Pass@1 SOTA. Does not replace CISPO / SAPO / GRPO loss. Claimed GitHub was 404 as of 2026-09-16."
last_reviewed: "2026-09-16"
papers:
  - paper:ngu
recipes:
  - recipe:ngu
claims:
  - benchmark: "Deepscaler, Qwen3-4B-Base, AIME 25 + BRUMO 25 average pass@1 (~120 H100 hours, 3 seeds)"
    metric: "pass@1"
    value: "26.5 ± 0.6 (NGU p=0.875 on N=8, K=16)"
    baseline: "GRPO N=8 K=16 24.8±1.0 / N=4 K=32 25.3±0.5 / N=2 K=64 24.5±0.5; Darling* 25.9 (different 10k subset)"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13443"
    notes: "Table 2. Not a CISPO bake-off. AIME 25: NGU p=0.5 22.0±0.7 vs K=16 20.0±1.5."
  - benchmark: "Deepscaler hard-subset Δpass@1 vs Qwen3-4B-Base (pass@64=0 at init)"
    metric: "pass@1 improvement"
    value: "4.3 ± 1.2 (NGU p=0.875)"
    baseline: "GRPO K=16 1.6±0.3 / K=32 2.5±1.1 / K=64 2.5±0.2; sampling curriculum 4.0±1.1 but easy Δ 22.7 vs NGU 26.8"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13443"
    notes: "Table 3. NGU p=0.75 easy Δ 28.1±0.2, hard Δ 3.0±1.2. Compute-matched, not Pass@1 SOTA."
  - benchmark: "Manufactoria, Qwen3-4B-Instruct-2507, per-test reward"
    metric: "all-tests pass vs GRPO stall"
    value: "NGU p=0.95 keeps solving harder tests until full-problem solves"
    baseline: "GRPO plateaus; ~80% tests solved but no all-tests pass on even one eval problem"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.13443"
    notes: "Figure 9. Per-test NGU from a stagnant GRPO ckpt matches restarting with all-tests reward (Figure 10). No scalar table."
tags:
  - post-training
  - rl-alignment
  - rlvr
  - adaptive-sampling
  - ngu
  - active
---

# Never Give Up (NGU)

## Method Overview
NGU is an **asynchronous adaptive sampler** for GRPO-family RLVR. Sample $K$ completions. All-correct $\to$ drop (too easy). Mixed rewards $\to$ train. All-wrong $\to$ with probability $p_{\mathrm{NGU}}$ put the prompt back on the generator and keep prior completions, else give up. Expected samples on an unsolved prompt are $K/(1-p)$. Keep completions younger than $T$ steps in the loss; older negatives can still enter the group baseline, with negative advantages rescaled so the update group still sums to zero ("anchor positives"). The host loss does not change.

Sits beside CISPO (loss), ThinkPrior (cold-start prompt rank), DIEM/GMTS (example/token reweight), and DataFlex-RL (data-policy accuracy null). Distinct from SAO (tool-latency stragglers).

## When to Use
- Async GRPO-family math/code RLVR where easy prompts hog the batch and hard prompts stay unsolved.
- Coding with per-test rewards where the model oscillates on medium tests and never passes the hardest tests.

## When NOT to Use
- Pass@1 kernel $\to$ `method:cispo`. MoE/VL loss $\to$ `method:sapo`. Cold-start prompt pool $\to$ `method:thinkprior`. Example/token reweight $\to$ `method:diem` / `method:gmts`. Async tool stragglers $\to$ `method:sao`.
- If the pool is almost all unsolvable, NGU spends time retrying instead of moving on.

## Relation to Existing SOTA
- Active sampling plug-in on `task:math-code-rl-dense`. Mention on `task:agentic-async-rl` (async infrastructure only). Does **not** enter `current_sota`. Does **not** supersede `method:cispo`, `method:sapo`, `method:grpo`, `method:thinkprior`, `method:diem`, `method:gmts`, `method:dataflex-rl`, or `method:sao`.

## Gotchas & Failure Modes
- Claimed GitHub `mnoukhov/never-give-up` was HTTP 404 as of 2026-09-16. Blog: `https://mnoukhov.github.io/posts/ngu`.
- Needs async refill. In a sync loop, retrying one hard prompt stalls the batch.
- Stale negatives: $T=4$ helped; $T\in\{8,16\}$ hurt. Downsampling negatives to 1:1 was worse than anchoring positives.
- Curriculum that freezes $K$ from initial pass rate matches hard-subset gains but regresses easy prompts; difficulty moves during training.
- NGU's sample-wait-sample loop is more off-policy than drawing $K/(1-p)$ up front.
