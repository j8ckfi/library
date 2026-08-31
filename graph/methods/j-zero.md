---
id: method:j-zero
type: method
title: "J-Zero (Challenger-Solver-Judge Co-Evolution from Zero Data)"
category: "rl-alignment"
status: sota
sota_for:
  - task:data-free-self-evolution
supersedes: []
papers:
  - paper:j-zero
recipes:
  - recipe:j-zero
claims:
  - benchmark: "Verifiable overall avg, Qwen3-4B-Base"
    metric: "mean of math / general-reasoning / IFEval averages"
    value: 54.38
    baseline: "R-Zero 49.64 / G-Zero 47.41 / base 44.91"
    date: "2026-08-31"
    verified: true
    notes: "Zero external training data. Frozen-Judge baselines plateau after ~2 iterations; J-Zero keeps improving through 10."
  - benchmark: "Verifiable overall avg, Qwen3-8B-Base"
    metric: "mean of math / general-reasoning / IFEval averages"
    value: 58.55
    baseline: "R-Zero 54.99 / G-Zero 53.07 / base 50.67"
    date: "2026-08-31"
    verified: true
    notes: "Same protocol as 4B. Paper abstract states +4.2 average verifiable gain vs baselines."
  - benchmark: "Unverifiable overall avg, Qwen3-4B-Base"
    metric: "mean of AlpacaEval 2.0 / Arena-Hard-v2.0 / EQ-Bench Creative Writing v3"
    value: 20.81
    baseline: "R-Zero 12.66 / G-Zero 10.89 / base 9.58"
    date: "2026-08-31"
    verified: true
    notes: "Judge co-adapts from loop-structure preference pairs, not from the Judge's own scores."
  - benchmark: "Unverifiable overall avg, Qwen3-8B-Base"
    metric: "mean of AlpacaEval 2.0 / Arena-Hard-v2.0 / EQ-Bench Creative Writing v3"
    value: 23.41
    baseline: "R-Zero 15.54 / G-Zero 15.31 / base 13.23"
    date: "2026-08-31"
    verified: true
    notes: "Paper abstract states +8.0 average unverifiable gain vs baselines."
tags:
  - post-training
  - self-evolution
  - data-free
  - self-play
  - unverifiable
  - j-zero
  - sota
---

# J-Zero (Challenger-Solver-Judge Co-Evolution from Zero Data)

## Method Overview
J-Zero is a unified Challenger–Solver–Judge loop with no external training data:
1. **Challenger–Solver GRPO**: Challenger generates tasks. Solver answers. Judge scores. Challenger is rewarded for tasks the Solver scores poorly on, plus repetition and format penalties. Solver is trained on high-dispersion frontier tasks to maximize Judge score. Inner optimizer is GRPO (verl).
2. **Judge Bradley–Terry co-adaptation**: Preference pairs are ordered from loop structure, not from the Judge's own scores.
   - **Role-asymmetry**: Solver answer $\succ$ Challenger answer on the same task (Solver is trained to answer; Challenger is trained to make tasks hard).
   - **Subtask-amplification**: divide-and-conquer composed answer $\succ$ Solver one-shot (iterated amplification).
3. **Why unverifiable domains work**: A frozen Judge saturates the distinctions it already knows, so R-Zero / G-Zero plateau after ~2 iterations. Co-adapting the Judge from structural preferences keeps the reward discriminative through 10 iterations.
4. **Initialization**: Judge is Skywork-Reward-V2-Llama-3.1-8B. Policies are Qwen3-4B-Base / Qwen3-8B-Base.

## When to Use
- When there is no external training corpus and the target includes unverifiable/open-ended domains as well as verifiable ones.
- When a frozen-Judge or majority-vote self-play loop has already plateaued.

## Relation to Existing SOTA
- First-hop for `task:data-free-self-evolution` only. Does **not** replace `method:u-opsd` (unlabeled existing math problems, no Challenger, consensus pseudo-solutions), `method:ttpo` (test-time, no training loop), or `method:cispo` / `method:sapo` / `method:sao` (labeled and agentic RL defaults).
- Does not supersede R-Zero or G-Zero as graph nodes; those papers are baselines in `paper:j-zero`, not first-hop methods here.

## Gotchas & Failure Modes
- **GRPO is the inner self-play optimizer, not a recommendation to use GRPO as this library's math/code RLVR default.** That default remains `method:cispo`. Using GRPO here does not change labeled RLVR routing.
- If the inner self-play loop needs Pass@K coverage or cannot afford a backward pass, `method:es-reasoning` is a possible GRPO substitute. This does not rewrite the J-Zero paper recipe (Challenger/Solver stay GRPO on verl).
- Judge labels must not be taken from the Judge's own scores; that reinforces Judge bias and re-imposes the frozen-Judge ceiling.
- Subtask-amplification pairs are unreliable in the first few iterations (Solver cannot yet solve the subtasks). Keep role-asymmetry pairs in the mix.
- Paper scale is 4B/8B base policies plus an 8B classifier Judge on 4x B200 + 4x H200. Larger CoT reasoners and a generative LLM-as-judge are untested in the paper.
