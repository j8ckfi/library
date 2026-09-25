# Graph Change Log

Audit log for all mutations to the knowledge graph: new nodes, supersessions, status changes, and
staleness reviews. One entry per mutation, newest first. Reverts append a reversion receipt — never
rewrite history. Format: [docs/ingestion-guide.md](../docs/ingestion-guide.md) §5.

---

### 2026-09-25 — weekday SOTA sweep (Rufus-Air, LastOPD, SLCA-GRPO, S2D-OPD)
- MUST 1–4. One new task (`task:tool-agent-segment-credit`). No current_sota retarget of Miles / OPD / Open-MOPD / CISPO / CANOPY / SAO / ACE / omp2 / TTPO / FoldGRPO / PACT / Cal-OPD / IER-OPD.
- Window: America/Denver 2026-09-25 Librarian weekday sweep after 2609.27334 / HF Daily through 09-24. New arXiv 2609.28845, 2609.29050, 2609.29142, 2609.29421.

### 2026-09-25 — ingest method:rufus-air (active on task:frontier-rl-posttrain-stack; does not supersede method:miles)
- Added paper:rufus-air (2609.29421), method:rufus-air, recipe:rufus-air (`code_status: none`; `repo_url: https://github.com/THUDM/slime`; no dedicated Rufus-Air GitHub). Reverse redirect from Miles for full open post-train recipe / stage order / agentic RL infra playbook.
- Status active (`sota_for: []`). 8-stage serial pipeline on GLM-4.5-Air-Base (106B-A12B): SFT → Reasoning RL → Coding RL → IF RL → General Agent → Coding Agent → Search Agent → RLHF. Amazon.
- Evidence: vs GLM-4.5-Air IFBench 76.9 vs 33.6, LCB v6 76.4 vs 59.6, TB2.1 42.7 vs 24.7, SWE-Verified 65.6 vs 50.6 (arXiv:2609.29421); verified: true; evidence_level: preprint.
- Scope checks: Miles remains the engine; SAO remains async; CISPO remains Pass@1.

### 2026-09-25 — ingest method:lastopd (active on task:student-distillation; does not supersede method:opd / method:open-mopd / method:cal-opd / method:oprd)
- Added paper:lastopd (2609.28845), method:lastopd, recipe:lastopd (`code_status: announced`; Muyiiiii/LastOPD 404 as of 2026-09-25). Reverse redirect for latent OPD collapse / last-layer crossfade.
- Status active (`sota_for: []`). Last-layer pre-LM-head latent loss, then ~10-step crossfade into reverse top-k token OPD. Visa Research.
- Evidence: Qwen3-4B/8B → 1.7B-Base MATH-500 +5.55 / +4.02 vs token-only OPD; ~half the steps to token-OPD final score (arXiv:2609.28845); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; Open-MOPD remains multi-teacher; Cal-OPD remains TSD calibration; same-lineage latent-only stays OPRD-Vanilla.

### 2026-09-25 — ingest method:slca-grpo (new task:tool-agent-segment-credit; does not supersede method:foldgrpo / method:sao / method:pact / method:critical-state-rl / method:cispo)
- Added paper:slca-grpo (2609.29050), method:slca-grpo, recipe:slca-grpo (`code_status: announced`; SLCA-GRPO/SLCA-GRPO 404 as of 2026-09-25; HF YanZhanPKU/SLCA-GRPO-Datasets). New task first hop; method status active (`sota_for: []`). Reverse redirects from long-horizon-tool-agent / agentic-async-rl / math-code-rl-dense / token-level-critic-rl.
- Status active. Segment-locked GRPO: tool advantages to tool tokens, summary advantages to summary tokens. SGLS + HierR. Tencent PCG / PKU.
- Evidence: Qwen2.5-7B matched GRPO +2.53 pp Toucan Success@0.9 / +1.36 pp BFCL / +9.15 pp τ²-Bench (arXiv:2609.29050); verified: true; evidence_level: preprint.
- Scope checks: FoldGRPO remains folding; SAO remains async; PACT remains Actor-then-Critic; Critical-State RL remains which-turn trainability; CISPO remains Pass@1.

### 2026-09-25 — ingest method:s2d-opd (active Direct-OPD plug-in on task:student-distillation; does not supersede method:opd)
- Added paper:s2d-opd (2609.29142), method:s2d-opd, recipe:s2d-opd (`code_status: announced`; review-anonymous `anonymous.4open.science/r/S2D-OPD-8868`). Reverse redirect for Direct-OPD JSD keep-mask.
- Status active (`sota_for: []`). Direct-OPD log-ratio is mass-invariant; keep top ~10% student states by teacher–reference JSD. ECNU.
- Evidence: +0.95 mean held-out Acc over dense Direct-OPD (7/8 settings; 95% CI 0.40–1.54); no extra forwards (arXiv:2609.29142); verified: true; evidence_level: preprint.
- Scope checks: OPD remains strong-teacher matching; Cal-OPD / IER-OPD / LastOPD are different axes; OPRD remains reverse distill.

### 2026-09-24 — weekday SOTA sweep (PACT, JitMem, VHD-Play, RewardVerse)
- MUST 1–4. One new task. No current_sota retarget of CISPO / CANOPY / SAO / OPD / omp2 / TTPO / Miles / ACE / BPCO / CodeMidas / DiffusionOPSD / Self-OPD.
- Window: HF Daily 2026-09-23/24 + arXiv ≳2609.26800. FLAG: UECR-GRPO, RL-Starts-before-RL, AEWM, MemoryAthena, Agensh, JEV-as-a-Judge, EmbodiedSWE, LatentPort, WhatWorkedBench, GeoPair, FLEET.

### 2026-09-24 — ingest method:pact (active on task:token-level-critic-rl; does not supersede method:bpco / method:cispo / method:sao)
- Added paper:pact (2609.26355), method:pact, recipe:pact (`code_status: announced`; AllSpark-Research/PACT empty stub).
- Evidence: agentic-math avg 72.87% (+8.80 GRPO / +13.16 PPO); SWE-Verified 67.4% (+3.8 SAO); verified: true; preprint.

### 2026-09-24 — ingest method:jitmem (active on task:agent-memory; does not supersede method:ace)
- Added paper:jitmem (2609.27334), method:jitmem, recipe:jitmem (`code_status: none`).
- Evidence: ALFWorld/WebShop/τ² +16.2/+16.3/+3.9 abs vs strongest write-time baseline; verified: true; preprint.

### 2026-09-24 — ingest method:vhd-play (new task:mechanism-grounded-agentic-rl-env; does not supersede method:codemidas)
- Added paper:vhd-play (2609.27321), method:vhd-play, recipe:vhd-play (`code_status: none`), task:mechanism-grounded-agentic-rl-env.
- Evidence: 0.204→0.815 five-family diagnostic; E-Commerce Bench > Qwen3.7-Max; verified: true; preprint.

### 2026-09-24 — ingest method:rewardverse (active video-RM plug-in on task:posttrain-diffusion; does not supersede method:diffusion-opsd / method:self-opd)
- Added paper:rewardverse (2609.22947), method:rewardverse, recipe:rewardverse (`code_status: released`; 2kxx/RewardVerse).
- Evidence: EvalVerse SOTA pointwise/pairwise; rubric mitigates scalar drift; verified: true; preprint.

### 2026-09-23 — weekday SOTA sweep (BPO, FP8 Calibrated Clipping, ACLArena, Category-Aware SWE Experts, AIDE2)
- MUST 1–5. Two new tasks (`task:agent-continual-learning`, `task:swe-agent-category-expert-rl`). No `current_sota` retargets of CISPO / CANOPY / SAO / OPD / Open-MOPD / VISTA / omp2-harness / TTPO / Miles / Claude computer-use / ACE / mini-SWE-agent / Muon2 / NeoHorse-1 / Code2Skill / Cal-OPD / RecreationWorld / CodeMidas / Vision-RL2 / EPS / Harness-Zero / Jev-Mem / RRSI / IER-OPD / sol-pi / Critical-State RL.
- Window: America/Denver 2026-09-23 Librarian weekday sweep. SKIP: Tasteful Agent / Taste-Bench, RULER SVG, Flash-dLLM, Agensh, JEV-as-a-Judge, onPanda, EDGEGEN, SkillSpec, LatentPort, ALPINE, collusion study, StableVQ, VideoGen-Agent, already-ingested PR29 set (IER-OPD / RRSI / Harness-Zero / Jev-Mem / Critical-State RL).

### 2026-09-23 — ingest method:bpo (active critic-free PMD candidate; does not supersede method:cispo / method:sapo / method:sao)
- Added paper:bpo (2609.15987), method:bpo, recipe:bpo (`code_status: none`; `repo_url: none found`). Wired to task:math-code-rl-dense. Reverse redirect from CISPO for Bellman telescoping vs Pass@1 default.
- Status active (`sota_for: []`). Not dense Pass@1 SOTA. Practical loss replaces the IS ratio with a smoothed complementary-token mismatch weight (ε, C). Authors Apodex / Princeton.
- Evidence: Qwen3-30B-A3B-Base + DAPO-Math-17k peak AIME24–26 Avg@32 50.5% vs CISPO 47.4% (+3.1), GRPO-ClipHigher 39.5% (+11.0); also beats GSPO/DPPO under matched settings (arXiv:2609.15987); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; SAO remains async.

### 2026-09-23 — ingest method:fp8-calibrated-clipping (active FP8 clip plug-in; does not supersede method:miles / method:cispo)
- Added paper:fp8-calibrated-clipping (2609.22870), method:fp8-calibrated-clipping, recipe:fp8-calibrated-clipping (`code_status: none`; `repo_url: none found`; VeRL experiments). Wired to task:frontier-rl-posttrain-stack beside Miles. Reverse redirect from Miles for full-pipeline FP8 clip calibration.
- Status active (`sota_for: []`). Match FP8 lower-bound clipping quantile to BF16 and rebalance the upper bound. ByteDance Seed / UW–Madison.
- Evidence: restores BF16-level quality; tensorwise up to ~1.5× BF16 throughput; blockwise ~10–20%; GRPO/DAPO, 8B–32B, VeRL + vLLM + TorchAO (arXiv:2609.22870); verified: true; evidence_level: preprint.
- Scope checks: Miles remains the engine; CISPO remains Pass@1; skip on BF16-only stacks.

### 2026-09-23 — ingest method:aclarena (new task:agent-continual-learning; does not supersede method:cispo / method:sao / method:canopy / method:miles / method:mini-swe-agent)
- Added paper:aclarena (2609.23989), method:aclarena, recipe:aclarena (`code_status: released`; WillDreamer/ACLArena; HF willhx/aclarena). New task first hop; method status active (`sota_for: []`). Reverse redirects from task:math-code-rl-dense / task:agentic-async-rl / task:outcome-only-long-horizon-agent-rl / task:frontier-rl-posttrain-stack / task:software-engineering-agent-harness / task:student-distillation.
- Status active. Offline replay of high-quality trajectories plus routed LoRA experts specialized via RL. Built on slime.
- Evidence: MLE AIME26 21.04 / NQ 49.7 / τ³-Retail 32.9 / IF-Eval 85.0 vs Seq-Final 10.21 / 33.5 / 29.6 / 84.8 (arXiv:2609.23989); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAO remains async; CANOPY remains AppWorld TGC; Miles remains the engine; mini-SWE-agent remains the loop; OPD / Open-MOPD remain text distill defaults.

### 2026-09-23 — ingest method:category-aware-swe-experts (new task:swe-agent-category-expert-rl; does not supersede method:codemidas / method:sao / method:mini-swe-agent / method:miles)
- Added paper:category-aware-swe-experts (2609.23377), method:category-aware-swe-experts, recipe:category-aware-swe-experts (`code_status: released`; alibaba/AgenticBigBang). New task first hop; method status active (`sota_for: []`). Reverse redirects from task:coding-agent-rl-environment-construction / task:agentic-async-rl / task:software-engineering-agent-harness / task:frontier-rl-posttrain-stack / task:student-distillation. SKIP'd 2026-09-22 for no public code; repo is live.
- Status active. SWE Labeler + RRE experts + label-routed MOPD (ReLU-gated reward extrapolation). No external teacher trajectories. Alibaba Logics-SWE-Qwen3.6-27B line.
- Evidence: Pro-618 58.04% (+5.39 vs base); SWE-bench Multilingual 59.00% (+2.78) (arXiv:2609.23377); verified: true; evidence_level: preprint.
- Scope checks: CodeMidas remains source-only env construction; SAO remains async; mini-SWE-agent remains issue-to-patch; Miles remains the engine.

### 2026-09-23 — ingest method:aide2 (active recursive harness RSI; does not supersede method:omp2-harness / method:rrsi / method:neohorse-1 / method:harness-zero)
- Added paper:aide2 (2609.26457), method:aide2, recipe:aide2 (`code_status: none`; `repo_url: none found`). Mention on task:agent-harness-runtime and task:agentic-rsi-routing-posttrain. Reverse redirects from both tasks, task:harness-distillation, and sibling methods. Authors Weco AI.
- Status active (`sota_for: []`). Outer-loop research agent rewrites its own harness; accepted rewrite becomes the next incumbent.
- Evidence: 8-day autonomous run, 7 accepted improvements, incumbent grade 0.703→0.778 vs AIDE_human 0.749; reward hacking 55%→32% vs human 39% (arXiv:2609.26457); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains kernel spec; RRSI remains regularized frozen-backbone search; NeoHorse-1 remains routing-harness weight post-train; Harness-Zero remains harness-behavior SFT.

### 2026-09-22 — weekday SOTA sweep (IER-OPD, RRSI, Harness-Zero, Jev-Mem, Critical-State RL)
- MUST 1–5. One new task (`task:harness-distillation`). No `current_sota` retargets of CISPO / CANOPY / SAO / OPD / Open-MOPD / VISTA / omp2-harness / TTPO / Miles / Claude computer-use / ACE / mini-SWE-agent / Muon2 / NeoHorse-1 / Code2Skill / Cal-OPD / RecreationWorld / CodeMidas / Vision-RL2 / EPS / sol-pi.
- Window: America/Denver 2026-09-22 Librarian weekday sweep. SKIP: OSWorld-Pro, onPanda, Complex KDA, VideoGen-Agent, EDGEGEN, IncLoRA+Muon, iSDFT, InfoPPO, Category-Aware SWE 2609.23377 (no public code).

### 2026-09-22 — ingest method:ier-opd (active sparse-OPD reliability plug-in; does not supersede method:opd / method:cispo / method:sparse-opd-supervision / method:ida-opd / method:cal-opd)
- Added paper:ier-opd (2609.24432), method:ier-opd, recipe:ier-opd (`code_status: released`; BruceSheng1202/IER-OPD). Wired to task:student-distillation beside sparse-opd-supervision and ida-opd. Reverse redirects from student-distillation and sibling methods.
- Status active (`sota_for: []`). Not distill SOTA. IER = teacher-gradient SNR under an optimal scalar baseline; candidate-set ranking fused with usefulness (IER-OR / IER-AND); keep sampled reverse-KL OPD.
- Evidence: 0.1%–1% token budgets match/exceed full OPD on math + HealthBench (JustRL-Qwen3-4B→1.7B Bayes@32 AIME25 15.8 vs full OPD 14.4; HealthBench TIP+IER-OR 46.08 vs 45.77) (arXiv:2609.24432); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1; sparse-opd-supervision remains usefulness keep-mask; IDA-OPD remains entropy A_y reweight; Cal-OPD remains TSD calibration.

### 2026-09-22 — ingest method:rrsi (active regularized harness RSI; does not supersede method:omp2-harness / method:neohorse-1 / method:sol-pi / method:mini-swe-agent / method:harness-onpolicy-correction)
- Added paper:rrsi (2609.24972), method:rrsi, recipe:rrsi (`code_status: released`; google-research/rrsi). Mention on task:agent-harness-runtime and task:agentic-rsi-routing-posttrain. Reverse redirects from both tasks and sibling methods.
- Status active (`sota_for: []`). Frozen-backbone harness search with annealed edit budget, unexplored-component proposer, critic+pruner against evolve-set memorization.
- Evidence: Terminal-Bench 2.1 evolve 64.6→78.7 (+14.1) Gemini 3.5 Flash; up to +4.7 on five OOD benches; ~30% fewer policy tokens vs unregularized; 8 benches (arXiv:2609.24972); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains kernel spec; NeoHorse-1 remains routing-harness weight post-train; SoL-Pi remains Pi token-efficiency; mini-SWE-agent remains issue-to-patch; harness-onpolicy-correction remains the evolved-harness SFT gotcha.

### 2026-09-22 — ingest method:harness-zero (new task:harness-distillation; does not supersede method:omp2-harness / method:neohorse-1 / method:opd / method:open-mopd / method:sao / method:canopy)
- Added paper:harness-zero (2609.24974), method:harness-zero, recipe:harness-zero (`code_status: released`; metaevo-ai/harness-zero). New task first hop; method status active (`sota_for: []`). Reverse redirects from task:agent-harness-runtime / task:agentic-rsi-routing-posttrain / task:student-distillation / task:software-engineering-agent-harness / task:agentic-async-rl.
- Status active. Agent-as-harness corrects student replies into the target action space before execution, then SFT; drop the specialized harness at deploy.
- Evidence: Qwen3.5-9B macro success 23.3%→44.3% without specialized harness (vs 41.7% with harness); agent-as-harness 81.1% vs code-as-harness 78.1%; 82.3% recovery of 28 patterns (arXiv:2609.24974); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains kernel; NeoHorse-1 remains routing RSI post-train; OPD / Open-MOPD remain text distill; mini-SWE-agent remains the loop (used here as target harness h); SAO remains async; CANOPY remains AppWorld TGC.

### 2026-09-22 — ingest method:jev-mem (active on task:agent-memory; does not supersede method:ace / method:code2skill)
- Added paper:jev-mem (2609.23986), method:jev-mem, recipe:jev-mem (`code_status: released`; libingzheren/Jev-Mem). Wired to task:agent-memory alongside ACE and Code2Skill. Redirect when System-One control of memory ops.
- Status active. Not memory SOTA. Typed System-One control plane (typing, routing, budget, traversal, scoring, stop) plus multi-relational store; System Two only for hard reasoning.
- Evidence: LoCoMo judge 0.777 vs MAGMA 0.700 (+11% rel); construction 158 s (6.6× vs Nemori 1,044 s); query 0.93 s (−36.7% vs MAGMA 1.47 s) (arXiv:2609.23986); verified: true; evidence_level: preprint.
- Scope checks: ACE remains playbook/memory default; Code2Skill remains repository-grounded skills.

### 2026-09-22 — ingest method:critical-state-rl (active multi-turn trainability diagnostic; does not supersede method:sao / method:canopy / method:cispo / method:foldgrpo)
- Added paper:critical-state-rl (2609.24985), method:critical-state-rl, recipe:critical-state-rl (`code_status: none`; `repo_url: none found`). Wired to task:agentic-async-rl. Reverse redirect for nested-sampling diagnostic vs straggler replay.
- Status active (`sota_for: []`). Diagnose which multi-turn calls are trainable (action-sufficiency, headroom, nested sampling vs continuation noise), then contextual-bandit at selected states.
- Evidence: BFCL v4 miss_func Gemma-4-26B-A4B 0.14→0.283±0.015 (~+14 pp); alternatives flat/worse (arXiv:2609.24985); verified: true; evidence_level: preprint.
- Scope checks: SAO remains async first hop; CANOPY remains AppWorld coverage; CISPO remains Pass@1; FoldGRPO remains folding.

### 2026-09-21 — weekday SOTA sweep (Cal-OPD, CodeMidas, RecreationWorld, Code2Skill, Vision-RL2)
- MUST 1–5. Three new tasks. No `current_sota` retargets of CISPO / CANOPY / SAO / OPD / Open-MOPD / VISTA / omp2-harness / TTPO / Miles / Claude computer-use / ACE / mini-SWE-agent / Muon2 / EPS.
- Window: HF Daily 2026-09-19/20 empty weekend; 2026-09-21 + arXiv ~2609.20800–2609.22086. WATCH/SKIP: GraphSkillEvo 2609.21749, IntBMoE 2609.21346, λ-Controlled GRPO 2609.22041, Matrix AdaGrad 2609.21815, Abstention and Noise Filtering 2609.22005.

### 2026-09-21 — ingest method:cal-opd (active TSD-calibration plug-in; does not supersede method:opd / method:vista / method:retireopd)
- Added paper:cal-opd (2609.21619), method:cal-opd, recipe:cal-opd (`code_status: none`; `repo_url: none found`; verl reimplementation, λ=5, 8×H20). Wired to task:student-distillation; mention on task:privileged-teacher-opsd. Reverse redirect from privileged-teacher-opsd for TSD calibration vs teacher update.
- Status active. Not distill SOTA. Probes teacher self-deviation with positive+negative privileged interventions; residual discrepancy (~52–65%) is the OPD advantage. Differentiates from RetireOPD (retirement timing).
- Evidence: Qwen3-4B→1.7B Avg@16 53.1 vs OPD 50.8; Qwen3-30B-A3B→4B 69.0 vs OPD 65.9 (arXiv:2609.21619); verified: true; evidence_level: preprint.
- Scope checks: OPD remains student distill; VISTA remains privileged-teacher adaptation; RetireOPD remains agent-RL retirement.

### 2026-09-21 — ingest method:codemidas (new task:coding-agent-rl-environment-construction; does not supersede method:canopy / method:sao / method:miles / method:mini-swe-agent)
- Added paper:codemidas (2609.22068), method:codemidas, recipe:codemidas (`code_status: none`; project `https://mimo.xiaomi.com/rl/`; no public GitHub as of 2026-09-21). New task first hop; method status active (`sota_for: []`). Mentions and reverse redirects from task:outcome-only-long-horizon-agent-rl / task:agentic-async-rl / task:software-engineering-agent-harness.
- Status active. Source-code-only env factory (explore → specs → execution-grounded tests → filter) then GRPO. 5,545 tasks / 3,185 repos / 23 languages.
- Evidence: MiMo-V2.5 GRPO DeepSWE 10.0→21.7, ProgramBench Almost Solved 4.5→21.5, Terminal-Bench v2.1 +8.5pp (arXiv:2609.22068); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld coverage; SAO remains async; Miles remains the engine; mini-SWE-agent remains the loop.

### 2026-09-21 — ingest method:recreationworld (new task:hybrid-computer-use-agent-rl; does not demote method:claude-computer-use)
- Added paper:recreationworld (2609.22000), method:recreationworld, recipe:recreationworld (`code_status: released`; QwenLM/RecreationWorld; RecreationBench 250; HF `Qwen/RecreationBench`). New task first hop; method status active. Reverse redirect from task:computer-use-agent for hybrid GUI+code training.
- Status active. Hybrid CUA train/eval (GUI + code interleaved) across Ubuntu/macOS/Windows/Android/Web; reference-as-oracle rewards; OOD transfer.
- Evidence: GPT-6 Astra RecreationBench 58.1% overall / 2.8% full programmatic; OOD up to +17.9 pp (arXiv:2609.22000); verified: true; evidence_level: preprint.
- Scope checks: Claude computer-use remains OSWorld 2.0 ranking; mini-SWE-agent remains issue-to-patch; CANOPY remains AppWorld.

### 2026-09-21 — ingest method:code2skill (active on task:agent-memory; does not supersede method:ace)
- Added paper:code2skill (2609.05571), method:code2skill, recipe:code2skill (`code_status: partial`; ant-intl/Code2Skill pre-release; HF `ant-intl/DeveloperSkills-Code2Skill`). Wired to task:agent-memory alongside ACE. Redirect when repository-grounded skills before interaction.
- Status active. Not memory SOTA. Pipeline lifts code units into verified atomic/composite/pattern skills; CodeSkillBank ~1.0M from 19,769 repos.
- Evidence: +11.7% avg over matched baselines across 72 evals / 8 benches (42.90→47.90, 57/72); vs Trace2Skill 31.0 / ExpeL 27.9 / SkillRL-Bank 32.8, Code2Skill 49.5 (arXiv:2609.05571); verified: true; evidence_level: preprint.
- Scope checks: ACE remains playbook/memory default; mini-SWE-agent remains the loop with no bank.

### 2026-09-21 — ingest method:vision-rl2 (new task:mllm-finegrained-perception-rl; does not supersede method:eps-prompt-scaffolding)
- Added paper:vision-rl2 (2609.19745), method:vision-rl2, recipe:vision-rl2 (`code_status: released`; YuHengsss/VisionRL2). New task first hop; method status active. Reverse redirects from task:mllm-rl-prompt-curriculum / task:rl-video-mllm.
- Status active. Region-level RL on a lightweight RoI proposal network; frozen MLLM reader scores leave-one-out likelihood; sparse encoding cuts visual tokens ~4×.
- Evidence: Qwen3.5-9B six-bench avg 80.1 vs base 74.6 / Vision-OPD-9B 78.7; 4B aligned 71.1 vs SD-RPN 66.6 with 4.2× fewer tokens (arXiv:2609.19745); verified: true; evidence_level: preprint.
- Scope checks: EPS remains prompt-curriculum first hop; OraRL remains video annotation-as-rollout; CISPO remains Pass@1.

### 2026-09-18 — weekday SOTA sweep (RetireOPD, When2Think, ActObs, OPD-EOS, SoL-Pi, bias-only TTRL)
- MUST 1–6. Active/niche only. No new tasks. No false supersessions of CISPO / CANOPY / SAO / VISTA / OPD / OPSA / TTPO / omp2-harness / mini-swe-agent / NeoHorse-1 / Muon2.
- Housekeeping: `paper:deepseek-v41-flash` `arxiv_id` set to 2609.19969.

### 2026-09-18 — ingest method:retireopd (active Adaptive Retirement; does not supersede method:canopy / method:sao / method:opd / method:vista / method:opsa)
- Added paper:retireopd (2609.20784), method:retireopd, recipe:retireopd (`code_status: none`; `repo_url: none found`). Wired to task:outcome-only-long-horizon-agent-rl; mention on task:agentic-async-rl / task:student-distillation / task:privileged-teacher-opsd. Reverse redirect from agentic-async-rl for privileged self-OPD then retire to RL.
- Status active. Not AppWorld TGC SOTA. Drop the privileged teacher when discrepancy stops shrinking and the student hits a fraction of teacher success, then pure RL.
- Evidence: Qwen2.5 1.5B–7B ALFWorld SR +14.1–18.8% vs RL; WebShop +11.8–19.0%; student beats its skill-conditioned teacher in every reported setting (arXiv:2609.20784); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains checker protocol; SAO remains async; OPD remains student distill; VISTA remains privileged math OPSD.

### 2026-09-18 — ingest method:when2think (active IDAC Think/NoThink plug-in; does not supersede method:cispo)
- Added paper:when2think (2609.19671), method:when2think, recipe:when2think (`code_status: partial`; GitHub JJunShim/When2Think stub README). Wired to task:math-code-rl-dense as an efficiency plug-in.
- Status active. Not Pass@1 SOTA. Offline reference accuracy/token stats shape Think vs NoThink.
- Evidence: AIME24 Pass@3 +10.0% with tokens −27.9% vs base; AIME25 Pass@3 40.0% over compression/routing-only (arXiv:2609.19671); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; ES-reasoning remains Pass@K / no-backward.

### 2026-09-18 — ingest method:actobs (active observation-token SFT; does not supersede method:sao / method:mini-swe-agent / method:canopy)
- Added paper:actobs (2609.20715), method:actobs, recipe:actobs (`code_status: none`; `repo_url: none found`). Wired to task:agentic-async-rl; mention on task:software-engineering-agent-harness / task:outcome-only-long-horizon-agent-rl. Reverse redirect from the SWE harness for observation-token SFT before GRPO.
- Status active. SFT looks similar; GRPO exploration changes.
- Evidence: Qwen3-4B Terminal-Bench 2.0 higher pass@k at every budget vs action-only; Qwen3-8B +3.4 pp pass@16; aider-polyglot +4.2 pp pass@1 at 4B (arXiv:2609.20715); verified: true; evidence_level: preprint.
- Scope checks: SAO remains async stragglers; mini-SWE-agent remains the loop; CANOPY remains coverage.

### 2026-09-18 — ingest paper:opd-eos / method:opd-eos (niche gotcha + semantic-class stop; does not supersede method:opd)
- Added paper:opd-eos (2609.20511), method:opd-eos (status niche), recipe:opd-eos. Code: UNCSciML/opd-eos. Wired to task:student-distillation. Gotchas added on method:opd and recipe:opd (same pattern as paper:spurious-advantage-grpo).
- Teacher/student EOS mismatch inflates length under OPD; decoding-stop alignment is insufficient; semantic-class stop is the fix. Late K2-Horizon inflation can remain.
- Evidence: Qwen stop-mass → ~0 by step 150 without the fix; Gemma 7168-clip ~100% → mean ~2000 tokens (arXiv:2609.20511); verified: true; evidence_level: preprint.
- Scope checks: OPD remains student-distill default.

### 2026-09-18 — ingest method:sol-pi (active Pi token-efficiency sibling; does not supersede method:omp2-harness / method:mini-swe-agent / method:neohorse-1)
- Added paper:sol-pi (2609.20519), method:sol-pi, recipe:sol-pi. Code: NVlabs/SoL-Pi. Wired to task:agent-harness-runtime; mention on task:agentic-rsi-routing-posttrain. Reverse redirect from NeoHorse's task for Pi harness mechanisms vs routing-guided OPD.
- Status active. Action Fusion / ObservationPack / Evidence-Preserving Reducer / Online Context Compact. Opt-in, default off.
- Evidence: EdgeBench 51-task Pi parity at −44.7–49.0% token traffic / ~−1/3 API cost (arXiv:2609.20519); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains the kernel spec; mini-SWE-agent remains issue-to-patch; NeoHorse-1 remains routing-harness post-train.

### 2026-09-18 — ingest method:bias-only-ttrl (niche bias-subspace TTRL; does not supersede method:ttpo)
- Added paper:bias-only-ttrl (2609.18587), method:bias-only-ttrl, recipe:bias-only-ttrl (`code_status: none`; `repo_url: none found`). Wired to task:label-free-test-time-reasoner beside TTPO.
- Status niche. Majority-vote rewards on ~100K bias params; backbone frozen.
- Evidence: MATH-500 76.67%; ~76,000× fewer trainable params than full TTRL (arXiv:2609.18587); verified: true; evidence_level: preprint.
- Scope checks: TTPO remains label-free TTT; u-OPSD remains train-time unlabeled; CISPO remains Pass@1.

### 2026-09-16 — weekday SOTA sweep (NGU, DCO)
- MUST 1–2. Active plug-ins only. No new tasks. No false supersessions of CISPO / SAPO / GRPO / ThinkPrior / DIEM / GMTS / DataFlex-RL / NoRA / Iso-LoRA / lr-matters-lora / OLMo-3 / Delta Learning / Open-MOPD.

### 2026-09-16 — ingest method:ngu (active async sampler; does not supersede method:cispo / method:sapo / method:grpo / method:thinkprior / method:diem / method:gmts / method:dataflex-rl / method:sao)
- Added paper:ngu (2609.13443), method:ngu, recipe:ngu (`code_status: partial`; `repo_url: none found`; claimed `mnoukhov/never-give-up` HTTP 404 on 2026-09-16; blog `mnoukhov.github.io/posts/ngu`). Wired to task:math-code-rl-dense; mention on task:agentic-async-rl / task:reasoning-rl-alignment. Reverse redirect from agentic-async-rl for math/code until-correct sampling.
- Status active. Not Pass@1 SOTA. Keep sampling a prompt until ≥1 correct; reallocates async compute off easy prompts onto hard ones (Matthew Effect / signal efficiency).
- Evidence: Deepscaler Qwen3-4B-Base NGU p=0.875 avg pass@1 26.5±0.6 vs GRPO K=16 24.8±1.0, hard-subset Δ 4.3±1.2 vs 1.6±0.3; Manufactoria GRPO+NGU reaches all-tests solves where GRPO stalls (arXiv:2609.13443); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; GRPO stays retired as the loss; ThinkPrior remains cold-start prompt select; DIEM/GMTS remain example/token reweight; DataFlex-RL remains the accuracy-null; SAO remains async stragglers.

### 2026-09-16 — ingest method:dco (active drift-budget instruct FT; does not supersede method:olmo-3 / method:lr-matters-lora / method:nora / method:iso-lora / method:delta-learning / method:open-mopd)
- Added paper:dco (2609.13680), method:dco, recipe:dco. Code: CONE-MT/DCO (LLaMA-Factory freeze LST; confirmed). HF collection LLaMAX/dco. Wired to task:instruct-sft-alignment; mention on task:parameter-efficient-fine-tuning. Cross-redirects PEFT ↔ instruct for drift-budget vs LoRA quality.
- Status active. Not instruct SOTA. Optimize update direction (coarse layer-selective probe) under an anchored-KL budget; reverses QA-only FT failure while keeping reasoning; stronger RL init.
- Evidence: Qwen3-8B LST b4t16 FLORES-101 xCOMET 52.66/55.60 vs ref 47.07/51.40 and Seed-X-PPO-7B 47.76/51.31; SmolInstruct FFT 59.65 dumps general avg 42.22→33.60 while LST b4t16 29.61 / 44.03 (arXiv:2609.13680); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains open instruct; lr-matters-lora remains 24GB LoRA quality; NoRA / Iso-LoRA remain LoRA-geometry; Delta Learning remains activation-space deltas; Open-MOPD remains multi-teacher distill.

### 2026-09-15 — weekday SOTA sweep (EPS prompt scaffolding)
- Ingested arXiv:2609.15051 (EMNLP 2026 main). New narrow task `task:mllm-rl-prompt-curriculum`. No false supersessions of CISPO / SAPO / OraRL / DataFlex / GRPO / CANOPY / DIEM.

### 2026-09-15 — ingest method:eps-prompt-scaffolding (new task:mllm-rl-prompt-curriculum; does not supersede method:orarl / method:dataflex-rl / method:cispo / method:sapo / method:grpo / method:canopy / method:diem)
- Added paper:eps-prompt-scaffolding (2609.15051), method:eps-prompt-scaffolding, recipe:eps-prompt-scaffolding (`code_status: partial`; `repo_url: none found`; project page only). Reverse redirects from task:rl-video-mllm / task:math-code-rl-dense. DataFlex mention: static-policy null vs online adaptive scaffolding.
- Status sota for the multimodal prompt-curriculum task only. EPS from on-policy GRPO rewards; teacher task-preserving rewrites; dynamic pool.
- Evidence: Qwen3-VL-4B Geo3K 65.39 vs GRPO 60.57; MMK12 71.15 vs 68.05; 2B MMK12 relatives +9.7% in-domain / +11.5% MathVision / +11.1% MMMU-Pro (arXiv:2609.15051); verified: true; evidence_level: peer-reviewed.
- Scope checks: OraRL remains video annotation-as-rollout; CISPO remains Pass@1; SAPO remains MoE/VL loss; DataFlex remains the static-policy null; GRPO stays the host; CANOPY remains outcome-only agents; DIEM remains example-reweight.

### 2026-09-14 — weekday SOTA sweep (SCOPE-OPSD, MInTRL, ESRL, PLC-DPO, SAS, Tiny Aya L2-Thinker, CanvasAnneal, EvoRS, DDO, Iso-LoRA)
- MUST 1–6 plus optional 7–10. Two new narrow tasks (`task:posttrain-attention-sparsification`, `task:multilingual-l2-reasoning-sft`). No false supersessions of CISPO / SAPO / OLMo-3 / SimPO / VISTA / OPSA / Muon2 / Miles / DeepSeek-V4 / Kimi-K3.
- Skipped: DataFlex-RL (already ingested), NSD / Musec / Nemotron IMO Gold / NCP / RLT / SMELT / V4.1-Flash (already in), COBRA-Skills, HyQuant, Thai TTS/OCR, robotics LIT. Weekend HF Daily 09-12/13 empty.

### 2026-09-14 — ingest method:iso-lora (active optimizer-shape LoRA note; does not supersede method:lr-matters-lora / method:nora / method:anlr-lora)
- Added paper:iso-lora (2609.12123), method:iso-lora, recipe:iso-lora (`code_status: partial`; `repo_url: none found`). Wired to task:lora-quality-tuning / task:parameter-efficient-fine-tuning.
- Status active. Nominal LoRA rank is capacity; AdamW vs Muon shapes effective rank. Iso-LoRA spectrally couples BA updates.
- Evidence: LLaMA-2-7B GSM8K rank-128 EM 61.87 vs Full FT 59.52 / LoRA-Pro 59.20 (arXiv:2609.12123); verified: true; evidence_level: preprint.
- Scope checks: lr-matters-lora remains the 24GB quality default; NoRA remains RLVR-stable A; AnLR remains per-rank LR.

### 2026-09-14 — ingest method:ddo (active successful-strategy coverage; does not supersede method:olmo-3 / method:simpo / method:canopy / method:draco)
- Added paper:ddo (2609.10052), method:ddo, recipe:ddo. Code: koguma00/direct_diverse_optimization. Wired to task:direct-preference-alignment; mention on task:outcome-only-long-horizon-agent-rl.
- Status active. DTC branch sets + RTO odds matching over successful alternatives.
- Evidence: strongest among DPO / DivFreq / DivProb / TieDPO on BabyAI / BabaIsAI / WebShop (arXiv:2609.10052); verified: true; evidence_level: preprint.
- Scope checks: Dolci / SimPO remain preference defaults; CANOPY / DRACO remain outcome-only first hops.

### 2026-09-14 — ingest method:evors (active Reward-DAG evolution; does not supersede method:canopy / method:draco)
- Added paper:evors (2609.12459), method:evors, recipe:evors (`code_status: partial`; `repo_url: none found`). Wired to task:outcome-only-long-horizon-agent-rl.
- Status active. On-policy designer edits an executable Reward-DAG under success / anti-hack / health / informativeness guards. Writing/roleplay domain, not AppWorld TGC.
- Evidence: WritingBench + CoSER three-judge average vs static and dynamic rubric RL (arXiv:2609.12459); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains checker protocol; DRACO remains frozen-judge step credit.

### 2026-09-14 — ingest method:canvasanneal (active discrete-DLM curriculum; does not supersede method:diffusion-opsd / method:self-opd / method:uno)
- Added paper:canvasanneal (2609.13060), method:canvasanneal, recipe:canvasanneal (`code_status: partial`; `repo_url: none found`). Wired to task:posttrain-diffusion; reverse redirect from task:diffusion-augmented-ar.
- Status active. Teacher-trace canvas anneal on LLaDA-7B-A1B-Instruct + diffu-GRPO.
- Evidence: MATH500 +6.0 / +2.0 / +0.4 vs diffu-GRPO at gen 128/256/512; GSM8K mixed (arXiv:2609.13060); verified: true; evidence_level: preprint.
- Scope checks: DiffusionOPSD / Self-OPD remain image/flow defaults; Uno remains AR serving.

### 2026-09-14 — ingest method:tiny-aya-l2-thinker (new task:multilingual-l2-reasoning-sft; does not supersede method:olmo-3 / method:cispo)
- Added paper:multilingual-bridges (2609.10445), method:tiny-aya-l2-thinker, recipe:tiny-aya-l2-thinker (`code_status: partial`; HF weights CohereLabs/tiny-aya-l2-thinker, no train GitHub), task:multilingual-l2-reasoning-sft. Reverse redirects from task:open-data-recipe / task:instruct-sft-alignment / task:math-code-rl-dense.
- Status sota for the L2-fidelity task only. MR+NR+English reasoning mix; >93% L2 rate across 60 languages at 3.35B.
- Evidence: L2 rate >93% on 6 benchmarks; PolyMath 11.1 vs Qwen3.5-4B 40.3 is a gotcha, not Pass@1 SOTA (arXiv:2609.10445); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains open instruct / Dolma-3; CISPO remains Pass@1.

### 2026-09-14 — ingest method:sas (new task:posttrain-attention-sparsification; does not supersede method:rlm / method:mamba-2 / method:uno)
- Added paper:sas (2609.13141), method:sas, recipe:sas. Code: Tencent-Hunyuan/Simple-Attention-Sparsification (branch `release`); HF tencent/Simple-Attention-Sparsification. Reverse redirects from task:long-context-prompt-offload / task:linear-time-sequence-modeling / task:software-engineering-agent-harness.
- Status sota for the narrow budgeted-selector task only. End-to-end LM-loss gates vs Top-K + dense-attention distillation.
- Evidence: +6.0–7.7 MATH500 and +10.6–15.5 GPQA-Diamond vs SeerAttention-R at budget 1024 on Qwen3-4B/8B/14B (arXiv:2609.13141); verified: true; evidence_level: preprint.
- Scope checks: RLM remains dumped-prompt offload; Mamba-2 remains SSM pretrain; Uno remains diffusion-augmented AR serving.

### 2026-09-14 — ingest method:plc-dpo (active noisy-label DPO; does not supersede method:olmo-3 / method:simpo)
- Added paper:plc-dpo (2608.30597), method:plc-dpo, recipe:plc-dpo. Code: VennTum99/PLC-DPO. Wired to task:direct-preference-alignment.
- Status active. Routes each pair as clean / flip / tie from a calibrated policy-reference margin. EMNLP 2026 Findings.
- Evidence: mean win rate 60.5 vs next-best 55.5 across 57 cells (arXiv:2608.30597); verified: true; evidence_level: peer-reviewed.
- Scope checks: OLMo-3 Dolci remains the open stack; SimPO remains the clean reference-free baseline.

### 2026-09-14 — ingest method:esrl (active MoE routing exploration; does not supersede method:sapo)
- Added paper:esrl (2609.13058), method:esrl, recipe:esrl. Code: strawberrymaster111/ESRL-Release (slime + SGLang patches). Wired to task:math-code-rl-moe.
- Status active. Anchored noisy expert sampling + entropy-adaptive noise + rollout expert-ID replay (R3).
- Evidence: Qwen3-30B-A3B MATH avg Pass@1/Pass@8 42.1/64.2 vs GRPO 38.9/59.7 (arXiv:2609.13058); verified: true; evidence_level: preprint. Not a SAPO bake-off.
- Scope checks: SAPO remains the MoE/VL loss default; RPB remains the router soft-anchor; CISPO remains dense Pass@1.

### 2026-09-14 — ingest method:mintrl (active sparse-intervention RLVR plug-in; does not supersede method:cispo / method:sapo / method:sao)
- Added paper:mintrl (2609.12419), method:mintrl, recipe:mintrl (`code_status: partial`; `repo_url: none found`). Wired to task:math-code-rl-dense.
- Status active. Judge Keep/Revise on short suffixes inside otherwise on-policy rollouts; sequence-level advantage regression (no IS). Paper lists long-horizon agentic eval as future work.
- Evidence: Qwen3-1.7B MInTRL-Const 35.45 math / 61.95 code vs stronger of GRPO and OPD (arXiv:2609.12419); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; SAO remains async stragglers; CANOPY remains outcome-only agents.

### 2026-09-14 — ingest method:scope-opsd (active Fisher-subspace OPSD auxiliary; does not supersede method:vista / method:nsd / method:opsa / method:opd / method:cispo)
- Added paper:scope-opsd (2609.12579), method:scope-opsd, recipe:scope-opsd (`code_status: partial`; `repo_url: none found`). Wired to task:privileged-teacher-opsd beside VISTA / NSD.
- Status active. Projects the privileged teacher-student residual onto a frozen rank-64 Fisher-sensitive factor; matched Random control; reuses OPSD forwards.
- Evidence: Qwen3-1.7B/4B/8B step-75 Macro Avg@12 43.33 / 63.80 / 65.28 vs Pure OPSD 41.48 / 62.13 / 64.45 (arXiv:2609.12579); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-teacher first hop; NSD remains anti-collapse; OPSA remains teacher-free; OPD remains matching distill; CISPO remains Pass@1.

### 2026-09-12 — ingest method:recurrent-looped-transformer (experimental; does not supersede method:muon2 / method:deepseek-v4 / method:deepseek-v41-flash / method:ncp-archpreview)
- Added paper:recurrent-looped-transformer (tech report 2026-09-12, no arXiv), method:recurrent-looped-transformer, recipe:recurrent-looped-transformer (`code_status: partial`; GitHub yifanzhang-pro/recurrent-looped-tranformer, note spelling), task:recurrent-encoder-decoder-lm. Reverse redirects from task:latent-space-lm-pretrain / task:pretrain-moe-frontier / task:software-engineering-agent-harness / task:agent-harness-runtime.
- Status experimental. Causal encoder KV + all-token recurrent decoder; shared pretrain/SFT/sample/current-policy replay; 48+48 reference; no measured efficiency or scaling.
- Evidence: mechanisms only; verified: false; evidence_level: self-reported.
- Scope checks: Muon2 remains ~7B optimizer; NCP remains latent-space; DeepSeek-V4 / Kimi-K3 remain MoE pretrain; V4.1-Flash remains CED serving; mini-SWE-agent remains the harness.

### 2026-09-12 — ingest method:smelt (active looped-MoE recipe; does not supersede method:deepseek-v4 / method:kimi-k3 / method:ce-moe)
- Added paper:smelt (2609.01343), method:smelt, recipe:smelt (`repo_url: none found`), task:compute-matched-moe-looped-pretrain. Wired as sibling of method:ce-moe on task:pretrain-moe-frontier with reverse redirect.
- Status active. Loop middle 50% of MoE layers twice; narrow width; raise experts; residual scale 1/2; match FLOPs / non-embedding params / KV. Scales to 54B non-embedding.
- Evidence: 6.8–18.0% training FLOPs saved on the compute-optimal sparse-grid frontier; DCLM Completion 96/96; Code largest; second visit reduces attention sink (arXiv:2609.01343); verified: true; evidence_level: preprint.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain MoE architecture co-defaults; CE-MoE remains the communication-layout niche.

### 2026-09-12 — ingest method:deepseek-v41-flash (new task:input-heavy-agentic-moe-serving; does not supersede method:deepseek-v4 / method:kimi-k3)
- Added paper:deepseek-v41-flash (HF tech report, no arXiv), method:deepseek-v41-flash, recipe:deepseek-v41-flash (`code_status: partial`; HF weights + inference/ + deepseek-ai/deepseek-recipe). Reverse redirect on task:pretrain-moe-frontier. Cross-link method:mhc (Single-Pass mHC) and method:recurrent-looped-transformer (experimental conceptual sibling). No prior method:deepseek-v4-flash node.
- Status sota for the serving task only. 552B CED 20+20; 8B prefill / 16B decode; CSA2; FP4 main KV ~890 B/token (~1/4 V4-Flash); SWA Bounded Replay (~1/8 persistent KV); Engram; DSpark. API news: V4-Flash / V4-Flash-Vision-Exp retired; V4-Pro routing to V4.1-Flash from 2026-09-14.
- Evidence: vendor card Terminal-Bench 2.1 90.6 / DeepSWE v1.1 74.2 / 890 B/token (HF model card + DeepSeek_V41_Tech_Report.pdf); verified: true; evidence_level: self-reported.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain pretrain co-defaults. CISPO / Muon2 / OPD / VISTA / OPSA / CANOPY / SAO / Miles / NeoHorse-1 / mini-SWE-agent / Iris / Poolside / MAGIC / Nemotron IMO Gold / NCP-ArchPreview first hops unchanged.

### 2026-09-11 — wire verified artifact pointers on the 2026-09-11 sweep (no first-hop retarget)
- NSD: collection slug is `PassionPrc/nsd-negative-self-distillation` (not bare `PassionPrc/nsd`); train/eval stay in-repo verl at Prongcan/NSD (`scripts/4B_NSD/`, `scripts/eval/`).
- Nemotron IMO Gold: collection `nvidia/nemotron-labs-imo-2026`; dataset `nvidia/Nemotron-IMO-Bench`; Skills `recipes/nemotron-imo-tts`; NeMo-RL `imo-26-ultra-v3` guide; SFT/RL ckpts and Math-Proofs datasets already named.
- NCP: `ArchSpace-Collection/NCP_ArchPreview_*`; eval LUMIA-Group/ncp_olmo_eval; serving LuckySJTU/vllm_ncp_archpreview (obsolete fork; successor LuckySJTU/vllm `dev/ncp-archpreview`). `recipe:ncp-archpreview` `code_status: partial` (no official train GitHub).
- Revisiting traces: `https://github.com/naver-ai/revisiting-trace` confirmed. Harness on-policy correction stays niche stub (`repo_url: none found`).
- First hops unchanged: VISTA / CISPO / Muon2 / OLMo-3 / mini-SWE-agent. Skipped AgentGrad / HyQuant / AdamX / OPD-gating-TweetEval.

### 2026-09-11 — ingest 2026-09-11 weekday SOTA sweep (NSD, Musec, Nemotron IMO Gold, NCP, harness on-policy correction, partial traces, MoE repetition, T1)
- MUST 1–6 plus optional 7–8. Two new narrow tasks (`task:latent-space-lm-pretrain`, `task:olympiad-math-posttrain`). No false supersessions of CISPO / Muon2 / OPD / OPSA / VISTA / CANOPY / SAO / ES-reasoning / Miles / NeoHorse-1 / mini-SWE-agent / Iris / Poolside.
- Skipped WATCH: AdamX 2609.11867, unified per-token OPD gating 2609.11768, AgentGrad, HyQuant, LILA, TF-IDF CE.

### 2026-09-11 — ingest method:nsd (active sibling; does not supersede method:vista / method:cispo / method:opd / method:opsa)
- Added paper:nsd (2609.11699), method:nsd, recipe:nsd. Code: Prongcan/NSD. Wired to task:privileged-teacher-opsd; mention on task:teacher-free-on-policy-self-adaptation and method:opsd-collapse-review.
- Status active. Diverges from a self-generated negative condition instead of imitating privileged traces.
- Evidence: Qwen3-1.7B/4B/8B ΔAvg +2.3 / +7.5 / +6.0 vs OPSD/Intuitor/TTRL (Table 1, arXiv:2609.11699); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-teacher first hop; CISPO remains Pass@1; OPD remains matching distill; OPSA remains teacher-free; opsd-collapse-review stays the niche survey.

### 2026-09-11 — ingest method:musec (active Muon stability plug-in; does not supersede method:muon2 / method:muonclip-kimi-k2)
- Added paper:musec (2609.11655), method:musec, recipe:musec (Soft Musec stub on kellerjordan/modded-nanogpt). Wired to task:llm-pretraining-optimization; mention on task:pretrain-dense-7b.
- Status active. Spectral clip of momentum singular values vs Muon flattening.
- Evidence: Soft Musec stays stable where Muon variants diverge on modded-nanogpt; matches them when already well-tuned (arXiv:2609.11655); verified: true; evidence_level: preprint.
- Scope checks: Muon2 remains ~7B optimizer; MuonClip remains trillion-scale MoE recipe.

### 2026-09-11 — ingest method:nemotron-imo-gold (new task:olympiad-math-posttrain; does not supersede method:cispo / method:nemotron-3-ultra)
- Added paper:nemotron-imo-gold (2609.10712), method:nemotron-imo-gold, recipe:nemotron-imo-gold, task:olympiad-math-posttrain. Reverse redirect on task:math-code-rl-dense. Cross-link method:nemotron-3-ultra.
- Status active. SFT+RL specialists + NL generate–verify–refine TTC. Artifacts: NVIDIA-NeMo/Skills recipes/nemotron-imo-tts; NeMo-RL imo-26-ultra-v3 guide; nvidia/Nemotron-3-Labs-Ultra-Math-{SFT,RL}.
- Evidence: IMO 2026 30/42 gold threshold (arXiv:2609.10712); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; Ultra remains the base architecture; OLMo-3 remains instruct SFT.

### 2026-09-11 — ingest method:ncp-archpreview (new task:latent-space-lm-pretrain; experimental; does not supersede method:muon2 / method:olmo-3)
- Added paper:ncp-archpreview (2609.10715), method:ncp-archpreview, recipe:ncp-archpreview, task:latent-space-lm-pretrain. Reverse redirects on task:llm-pretraining-optimization / task:pretrain-dense-7b / task:open-data-recipe.
- Status experimental. Joint NTP + Next Concept Prediction; 8.9B on 5.73T Dolma-3. Weights: ArchSpace-Collection/ncp-archpreview. Eval: LUMIA-Group/ncp_olmo_eval.
- Evidence: 51.3% tokens to match OLMo-3-7B Stage-1 loss; +2.45 macro; +5.99 GSM8K (arXiv:2609.10715); verified: true; evidence_level: preprint.
- Scope checks: Muon2 remains the optimizer; OLMo-3 remains the open mix.

### 2026-09-11 — ingest method:harness-onpolicy-correction (niche gotcha; does not supersede method:mini-swe-agent / method:miles / method:neohorse-1)
- Added paper:harness-onpolicy-correction (2609.09134), method:harness-onpolicy-correction, recipe:harness-onpolicy-correction (stub; no official code). Wired to task:software-engineering-agent-harness / task:agent-harness-runtime / task:agentic-rsi-routing-posttrain.
- Status niche. Full expert-trajectory LoRA-SFT after model-specific harness evolution regresses (−4 to −30 pts); on-policy failing-turn rewrite is the fix.
- Evidence: all seven enterprise tasks, Qwen3-Coder and Gemma 4 (arXiv:2609.09134); verified: true; evidence_level: preprint.
- Scope checks: mini-SWE-agent remains the harness; Miles remains the stack; NeoHorse-1 remains RSI routing post-train.

### 2026-09-11 — ingest method:partial-reasoning-traces (active SFT-data plug-in; does not supersede method:olmo-3 / method:nemotron-cascade-2)
- Added paper:partial-reasoning-traces (2609.07103), method:partial-reasoning-traces, recipe:partial-reasoning-traces. Code: naver-ai/revisiting-trace. Wired to task:instruct-sft-alignment; mention on task:math-code-rl-dense.
- Status active. Full long CoT SFT is overfed; partial/truncated traces work; intermediate tokens contribute little.
- Evidence: EMNLP 2026 Findings; attention + token-removal studies (arXiv:2609.07103); verified: true; evidence_level: peer-reviewed.
- Scope checks: OLMo-3 / Nemotron-Cascade 2 remain instruct defaults; CISPO remains Pass@1.

### 2026-09-11 — ingest method:moe-data-repetition (niche gotcha; does not supersede method:deepseek-v4 / method:kimi-k3)
- Added paper:moe-data-repetition (2609.11917), method:moe-data-repetition, recipe:moe-data-repetition (no code). Wired to task:pretrain-moe-frontier / task:train-moe-nvl72.
- Status niche. MoEs degrade from ~4× repeats; dense 80M tolerated 8×; effect scales with total params.
- Evidence: 80M–1B active / 8.5B total (arXiv:2609.11917); verified: true; evidence_level: preprint.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain MoE architecture defaults.

### 2026-09-11 — ingest method:t1-terminal-rl (active; does not supersede method:canopy / method:sao / method:miles)
- Added paper:t1-terminal-rl (2609.11042), method:t1-terminal-rl, recipe:t1-terminal-rl. Host: THUDM/slime v0.3.0. Project: jyyang26.github.io/t1. Wired as mention on task:outcome-only-long-horizon-agent-rl / task:frontier-rl-posttrain-stack / task:agentic-async-rl.
- Status active. 122B MoE terminal RL, TITO + R3. Not a new first hop.
- Evidence: Terminal-Bench 2.1 43.8%→64.0%; Long-Horizon Terminal Bench 27.9% (arXiv:2609.11042); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld coverage; SAO remains async algorithm; Miles remains the production stack.

### 2026-09-09 — refine 2026-09-09 sweep (OPRD code, VERPO, RPB, group-correlation, OPSD collapse review)
- Corrections on the open PR: OPRD recipe now points at raymin0223/on_policy_reverse_distillation. ACE MoE PEFT was already ingested (`method:ace-moe-peft`, UbiquitousAILab/ACE). No CISPO / Muon2 / OPD / OPSA / CANOPY retarget.
- Added method:verpo (2609.06100), method:rpb (2609.08115), method:rlvr-group-correlation (2609.06386), method:opsd-collapse-review (2608.25936). WATCH skipped: FEE EnvAsScaffold 2609.08404. AnLR-LoRA / MoE HP scaling / AF1 / DataFlex-RL already landed in the first commit.
- Scope checks: VISTA remains privileged-teacher first hop; SAPO remains MoE/VL RLVR; CISPO remains Pass@1.

### 2026-09-09 — ingest method:verpo (active; does not supersede method:vista / method:cispo)
- Added paper:verpo (2609.06100), method:verpo, recipe:verpo (stub; no official code). Wired to task:privileged-teacher-opsd; mention on task:math-code-rl-dense.
- Status active. Privileged evidence as a proposal (Fisher contrast + ZPD gate) on an outcome objective.
- Evidence: five scientific/tool tasks, best-variant averages Qwen3-4B 0.6857 vs 0.6826, Qwen3-8B 0.7058 vs 0.6895, Llama-3.2-1B 0.5657 vs 0.4751 (arXiv:2609.06100); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-teacher SOTA; CISPO remains Pass@1.

### 2026-09-09 — ingest method:rpb (active MoE routing candidate; does not supersede method:sapo)
- Added paper:rpb (2609.08115), method:rpb, recipe:rpb. Wired to task:math-code-rl-moe. Claimed GitHub naver-ai/rpb was 404 at ingest.
- Status active. Soft router anchoring vs re-applied LBL or unanchored FT.
- Evidence: Moonlight-16B-A3B in-domain 45.77 vs LBL 31.91 vs unanchored 29.44 (arXiv:2609.08115); verified: true; evidence_level: preprint.
- Scope checks: SAPO remains MoE/VL current_sota.

### 2026-09-09 — ingest method:rlvr-group-correlation (niche analysis; does not supersede method:cispo)
- Added paper:rlvr-group-correlation (2609.06386), method:rlvr-group-correlation, recipe:rlvr-group-correlation. Code: ethxin0011/rlvr_group_correlation. Wired as gotcha on task:math-code-rl-dense / method:grpo / method:cispo.
- Status niche. Within-group verifier-error ICC, not an optimizer.
- Evidence: ρ=0.530 [0.500, 0.560] on 24,998 k=8 groups; Kish n_eff=1.70; advantage-sign disagreement ≤0.83% (arXiv:2609.06386); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; sibling gotcha remains paper:spurious-advantage-grpo.

### 2026-09-09 — ingest method:opsd-collapse-review (niche playbook; does not supersede method:vista / method:opsa / method:cispo)
- Added paper:opsd-collapse-review (2608.25936), method:opsd-collapse-review, recipe:opsd-collapse-review (no code). Wired to task:privileged-teacher-opsd and task:teacher-free-on-policy-self-adaptation.
- Status niche. Three levers for OPSD collapse (where / what / when). Survey; no new experiments.
- Evidence: structural review only (arXiv:2608.25936); verified: true; evidence_level: preprint.
- Scope checks: VISTA / OPSA / CISPO first hops unchanged.

### 2026-09-09 — OPRD recipe code pointer (method:oprd already ingested)
- Set recipe:oprd repo_url to https://github.com/raymin0223/on_policy_reverse_distillation. Repo is an early stub at ingest; algorithm snippet unchanged. Does not retarget OPD or CISPO.

### 2026-09-09 — ingest 2026-09-09 weekday SOTA sweep (Miles, NeoHorse-1, ThinkPrior, RouteOPD, TV-OPD, DATPO, OPRD + optionals)
- Added two new first-hop tasks (`task:frontier-rl-posttrain-stack`, `task:agentic-rsi-routing-posttrain`) plus fifteen methods. No false supersessions of CISPO / Muon2 / OPD / OPSA / CANOPY / Poolside / SAO / ES-reasoning / mini-SWE-agent / Iris / Uno / W2S-OPD.
- MUST: Miles, NeoHorse-1, ThinkPrior, RouteOPD, TV-OPD, DATPO, OPRD. OPTIONAL (all landed): ACE MoE PEFT, AnLR-LoRA, KBBQ, AF1, CircuitLens, Online Draft Co-Training, DataFlex-RL, MoE sparsity HP scaling. Skipped none of the requested optionals. Already-in-library items (TGOPD, Uno, FlowBalance, Iris, sparse-OPD, OPD-then-RLVR, GAPO, RISE, layer-dropout) were not re-ingested.
- Scope checks: CISPO, Muon2, OPD, OPSA, CANOPY remain first hops on their tasks. Miles is sota only for the new frontier stack. NeoHorse-1 is sota only for the new RSI routing-harness task.

### 2026-09-09 — ingest method:miles (new task:frontier-rl-posttrain-stack)
- Added paper:miles (2609.08368), method:miles, recipe:miles, task:frontier-rl-posttrain-stack. Reverse redirects on task:industrial-model-building, task:agentic-async-rl, task:software-engineering-agent-harness, task:outcome-only-long-horizon-agent-rl.
- Status sota for the production post-train engine only. Code: radixark/miles.
- Evidence: GLM-5.2 744B-A40B Terminal-bench-2 64× GB300 median 263s (first 30 steps); KL 0.0369; reward 0.438→0.556 single run (Table 9 / Figure 5, arXiv:2609.08368); verified: true; evidence_level: preprint.
- Scope checks: Poolside remains factory process; SAO remains async algorithm; CISPO remains Pass@1; Muon2 remains 7B optimizer; mini-SWE-agent remains the harness.

### 2026-09-09 — ingest method:neohorse-1 (new task:agentic-rsi-routing-posttrain)
- Added paper:neohorse-1 (2609.08183), method:neohorse-1, recipe:neohorse-1, task:agentic-rsi-routing-posttrain. Reverse redirects on SWE harness, SAO, CANOPY, Iris, CISPO, OPD shelves.
- Status sota for routing-harness RSI post-train only. Code: TokenRhythm/NeoHorse. Weights: TokenRhythm/neohorse-1.
- Evidence: 4B 58.94→64.87 and 9B 65.60→69.04 ten-bench macro vs Qwen3.5 same size (Table 1, arXiv:2609.08183); verified: true; evidence_level: preprint.
- Scope checks: mini-SWE-agent remains the harness; SAO remains async; CANOPY remains AppWorld; Iris remains search-agent climbing; CISPO remains Pass@1; OPD remains text distill.

### 2026-09-09 — ingest method:thinkprior (active RLVR data-policy plug-in; does not supersede method:cispo / method:gapo / method:verigate)
- Added paper:thinkprior (2609.09075), method:thinkprior, recipe:thinkprior (stub; project page only). Wired to task:math-code-rl-dense; mention on task:all-zero-verifier-groups.
- Status active. Zero-rollout Beta difficulty prior for GRPO cold-start prompt selection. Loss/optimizer unchanged.
- Evidence: silent groups 23.8%→10.6%; ThinkPrior+DAPO 8256→7381 generated rollouts at 3840-update budget; accuracy +0.7 with CI crossing 0 (arXiv:2609.09075); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; GAPO remains clip-width; VeriGate remains PRM gating; DataFlex-RL is the accuracy-null cousin.

### 2026-09-09 — ingest method:routeopd (active OPD plug-in; does not supersede method:opd)
- Added paper:routeopd (2609.08337), method:routeopd, recipe:routeopd (stub; no official code). Wired to task:student-distillation.
- Status active. Pairwise log-odds transport vs sampled reverse-KL OPD.
- Evidence: four settings macro +2.70 Avg@16 vs sampled-RKL; JustRL-DeepSeek 65.53 vs 63.34 (Table 1, arXiv:2609.08337); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; RA-OPD / IDA-OPD / TGOPD remain sibling plug-ins.

### 2026-09-09 — ingest method:tv-opd (active OPD stability plug-in; does not supersede method:opd / method:ra-opd / method:tropd / method:stable-opd)
- Added paper:tv-opd (2609.08341), method:tv-opd, recipe:tv-opd (stub; no official code). Wired to task:student-distillation.
- Status active. Sign of token advantages ≈ full OPD; TV-shaped shared scale for late training.
- Evidence: late AIME24 49.58 vs Raw 46.11; LateMean 43.06 vs 40.87 (Table 2, arXiv:2609.08341); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; RA-OPD remains trajectory mask; TrOPD remains trust-region matching; Stable-OPD remains control variates.

### 2026-09-09 — ingest method:datpo (active Pass@K sibling; does not supersede method:es-reasoning / method:cispo)
- Added paper:datpo (2609.08650), method:datpo, recipe:datpo (GRPO-Zero host). Wired to task:passk-reasoning-coverage; mention on task:math-code-rl-dense.
- Status active. Difficulty-adaptive sentence-entropy tree-structured PO.
- Evidence: Qwen2.5-3B 22.4/54.9 avg@k/pass@k vs GRPO 20.7/48.2; Qwen3-4B 31.3/60.4 vs GRPO 30.1/58.3 (Table 2, arXiv:2609.08650); verified: true; evidence_level: preprint.
- Scope checks: ES-reasoning remains Pass@K / no-backward first hop; CISPO remains Pass@1.

### 2026-09-09 — ingest method:oprd (active reverse distill; does not supersede method:w2s-opd / method:opd / method:cispo)
- Added paper:oprd (2609.08798), method:oprd, recipe:oprd (stub; no official code). Wired to task:student-distillation. Updated method:w2s-opd differentiation / do_not_use_for.
- Status active. Weak-to-strong: amplify verifier-supported student gradient along teacher policy-shift. Not matching.
- Evidence: 4B→8B math avg 51.91 vs KDRL 43.99 / OPD 39.44; multi-teacher 58.77 vs Mix-RL 47.68 (Tables 1/3, arXiv:2609.08798); verified: true; evidence_level: preprint.
- Scope checks: W2S-OPD remains matching; OPD remains distill default; CISPO remains Pass@1. Table 3 vs W2S-OPD is differentiation, not a graph supersession.

### 2026-09-09 — ingest method:ace-moe-peft (active MoE PEFT; does not supersede method:lr-matters-lora or method:ace)
- Added paper:ace-moe-peft (2609.06072, EMNLP 2026), method:ace-moe-peft, recipe:ace-moe-peft. Wired to task:parameter-efficient-fine-tuning. Slug avoids collision with method:ace (Agentic Context Engineering).
- Status active. Expert-adapter consolidation. Code: UbiquitousAILab/ACE.
- Evidence: best mean on 3/4 MoE backbones; 1.31×–1.48× faster vs expert-wise LoRA (arXiv:2609.06072); verified: true; evidence_level: peer-reviewed.
- Scope checks: lr-matters-lora remains 24GB quality default; method:ace remains agent memory.

### 2026-09-09 — ingest method:anlr-lora (active LoRA LR plug-in; does not supersede method:lr-matters-lora / method:nora)
- Added paper:anlr-lora (2609.05885), method:anlr-lora, recipe:anlr-lora (stub). Wired to task:lora-quality-tuning and task:parameter-efficient-fine-tuning.
- Status active. Anisotropic per-rank learning rates, mean-normalized so the global LR is unchanged.
- Evidence: lift vs uniform-LR LoRA on commonsense / NLG / visual instruction-tuning (arXiv:2609.05885); verified: true; evidence_level: preprint.
- Scope checks: quality default remains vanilla LoRA + rsLoRA + LR sweep; NoRA remains rank-normalize A.

### 2026-09-09 — ingest method:kbbq (active W4A4 niche; does not supersede method:quartet-ii / method:mxfp4-mi355x)
- Added paper:kbbq (2609.08135), method:kbbq, recipe:kbbq (stub). Wired to task:fp4-hardware-training as a mention only.
- Status active. Predictive noise law / spectrum-flattening limits for FP4 W4A4.
- Evidence: outperforms prior flatten SOTA with no extra deploy-time compute (arXiv:2609.08135); verified: true; evidence_level: preprint.
- Scope checks: Quartet-II / MXFP4 remain native FP4 hardware-training current_sota.

### 2026-09-09 — ingest method:af1 (active 1-bit PTQ; does not supersede method:sparse-bitnet)
- Added paper:af1 (2609.06161, EMNLP 2026 Main), method:af1, recipe:af1. Wired to task:1bit-extreme-quantization. Claimed GitHub Kishon-zzx/AF1 was 404 at ingest.
- Status active. Genuine 1-bit PTQ of existing LLMs under a 1.0-BPW budget.
- Evidence: best among compared binarization PTQ; ~2.5× inference vs BF16 (arXiv:2609.06161); verified: true; evidence_level: peer-reviewed.
- Scope checks: Sparse-BitNet remains native 1.58-bit pretrain; ScaleQ-1.58 remains ternary post-train.

### 2026-09-09 — ingest method:circuitlens (active RLVR data-selection signal; does not supersede method:cispo)
- Added paper:circuitlens (2609.07183, EMNLP 2026 Findings), method:circuitlens, recipe:circuitlens (stub). Wired to task:math-code-rl-dense.
- Status active. CRS circuit-engagement ranking; low-engagement decile wins on 7B medium math.
- Evidence: lowest-CRS decile +2.0 / +1.6 / +2.9 pp vs random on GSM8K / OlympiadBench / Minerva (arXiv:2609.07183); verified: true; evidence_level: peer-reviewed.
- Scope checks: CISPO remains Pass@1; ThinkPrior remains silent-group prior; DataFlex-RL remains the accuracy-null.

### 2026-09-09 — ingest method:online-draft-cotrain (niche; does not supersede method:miles / method:uno)
- Added paper:online-draft-cotrain (2609.07108), method:online-draft-cotrain, recipe:online-draft-cotrain. Wired to task:frontier-rl-posttrain-stack; mention + redirect from task:diffusion-augmented-ar.
- Status niche. Speculative decoding co-train for long-context RL. Code: NVIDIA-NeMo/RL#3698.
- Evidence: drafts track the policy through 122B / 256K CP with rollout and e2e speedups (arXiv:2609.07108); verified: true; evidence_level: preprint.
- Scope checks: Miles remains the frontier stack; Uno remains diffusion-augmented AR serving; CISPO remains Pass@1.

### 2026-09-09 — ingest method:dataflex-rl (active negative result; does not supersede method:cispo / method:thinkprior)
- Added paper:dataflex-rl (2609.06107), method:dataflex-rl, recipe:dataflex-rl (stub). Wired to task:math-code-rl-dense.
- Status active. Controlled finding: RLVR data policies do not beat uniform GRPO at 95% CI.
- Evidence: uniform +7.76 pp vs untrained on Qwen2.5-7B-Base 12-bench; no selection method 95% CI vs uniform excludes 0 (arXiv:2609.06107); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; ThinkPrior remains the waste-cut prior (not an accuracy claim).

### 2026-09-09 — ingest method:moe-sparsity-hp-scaling (active MoE HP guidance; does not supersede method:deepseek-v4 / method:kimi-k3)
- Added paper:moe-sparsity-hp-scaling (2609.08690), method:moe-sparsity-hp-scaling, recipe:moe-sparsity-hp-scaling (stub). Wired to task:pretrain-moe-frontier.
- Status active. LR/batch vs activation-ratio transfer laws.
- Evidence: ~1,800 MoE pretrain runs; held-out 12B 1/64 predicted HPs close to observed optima (arXiv:2609.08690); verified: true; evidence_level: preprint.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain architecture current_sota; Muon2 remains dense optimizer.

### 2026-09-08 — catch-up ingest method:iris / method:sparse-opd-supervision / method:opd-then-rlvr (completes the weekday sweep to seven)
- Completes the 2026-09-08 weekday sweep. Original four (FlowBalance, TGOPD, OT optimizer schedules, Uno) unchanged. Added Iris (new `task:web-search-agent-rl`), sparse OPD supervision, and OPD-then-RLVR. No false supersessions of CISPO / Muon2 / OPD / OPSA / CANOPY / RISE / GAPO / OPDVR / SAO / mini-SWE-agent / FoldGRPO.
- Still skipped (WATCH): FactoSR, Refuse-without-Refusal, over-editing, CoSkill, ConsensusBench, Multi-Harness RL, Scale-QLoRA, Train-What-You-Deploy, OPSD survey 2608.25936, EmbodiedSkills, ENEAS, revision-propagation, 2609.04575, 2609.04453, 2609.05309, 2609.05274.
- Scope checks: CISPO, Muon2, OPD, CANOPY, SAO remain first hops on their tasks. Uno remains sota only for `task:diffusion-augmented-ar`. Iris is sota only for the new search-agent task.

### 2026-09-08 — ingest method:iris (new task:web-search-agent-rl)
- Added paper:iris (2609.04304), method:iris, recipe:iris, task:web-search-agent-rl. Reverse redirects on task:agentic-async-rl, task:outcome-only-long-horizon-agent-rl, task:long-horizon-tool-agent, task:software-engineering-agent-harness, task:math-code-rl-dense.
- Status sota for live-web search-agent training only. Code/weights: AllSpark-Research/Iris.
- Evidence: Iris-mini 82.2/84.8/86.9/52.3 and Iris-pro 88.6/85.1/92.9/56.4 on BrowseComp / BrowseComp-ZH / DeepSearchQA / HLE-text with discard-all CM (Table 1); no-CM BrowseComp 64.7 / 72.6 (Table 2, arXiv:2609.04304); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld; SAO remains async; mini-SWE-agent remains the harness; FoldGRPO remains folding; CISPO remains Pass@1.

### 2026-09-08 — ingest method:sparse-opd-supervision (active OPD plug-in; does not supersede method:opd / method:cispo)
- Added paper:sparse-opd-supervision (2609.04565), method:sparse-opd-supervision, recipe:sparse-opd-supervision (stub; no official code). Wired to task:student-distillation; optional mention on task:math-code-rl-dense.
- Status active. Keep-mask on sampled-token OPD: 1–2 tokens (~0.05%) can match/beat full-token OPD.
- Evidence: Family 8 avg@8 mean pctltail 0.05% 30.1 vs plain OPD 27.5; Family 9 minmaxtok 49.3 vs plain 47.5 vs teacher 46.8 (Tables 3/5, arXiv:2609.04565); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1; IDA-OPD remains the entropy-shrink plug-in.

### 2026-09-08 — ingest method:opd-then-rlvr (active stacking order; does not supersede method:opd / method:cispo / method:opdvr)
- Added paper:opd-then-rlvr (2609.04108), method:opd-then-rlvr, recipe:opd-then-rlvr. Wired to task:student-distillation and task:math-code-rl-dense; related mention on task:distill-reasoner-verifier. Code: StringNLPLAB/opd-rlvr.
- Status active. OPD then RL beats pure OPD, pure GRPO, and joint one-step fusion. Not a graph supersession of the algorithms.
- Evidence: logic pass@1 mean 80.6 vs GRPO 49.4 vs OPD 53.9 vs KDRL 62.8; math 31.8 vs OPD 31.0 vs GRPO 28.4 (Table 2, arXiv:2609.04108); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1 RLVR (paper RL stage is GRPO); OPDVR remains single-step gated OPD+RLVR.

### 2026-09-08 — ingest 2026-09-08 weekday SOTA sweep (FlowBalance, TGOPD, OT optimizer schedules, Uno)
- Added four methods without stealing CISPO / Muon2 / OPD / OPSA / CANOPY / RISE / GAPO current_sota. Uno is sota only for the new `task:diffusion-augmented-ar`. Per-method receipts follow.
- Skipped (WATCH only): 2608.25936 OPSD critical review; EmbodiedSkills; ENEAS; revision-propagation; training-free MoE expert halving (2609.04575); expert pruning under over-dispersion (2609.04453); mHC residual analysis (2609.05309); Speculative Uncertainty draft-gate (2609.05274). Tue arXiv /new still showed Mon 7 Sep listings at sweep time; HF Daily Papers 2026-09-08 used as extra signal.
- Scope checks: no half supersessions; CISPO, Muon2, OPD remain first hops on their tasks.

### 2026-09-08 — ingest method:flowbalance (active; does not supersede method:cispo / method:opsa / method:opd / method:vista / method:u-opsd / method:rise / method:canopy)
- Added paper:flowbalance (2609.03241), method:flowbalance, recipe:flowbalance. Wired to task:math-code-rl-dense; related mentions on task:teacher-free-on-policy-self-adaptation and task:privileged-teacher-opsd.
- Status active. Privileged same-model token logp-gains aggregated to trajectory self-guidance, sign-gated by verifier group advantage, fitted by profiled trajectory balance. Code: alexhuang13/FlowBalance.
- Evidence: Qwen3-4B five-bench avg 64.26 vs FlowRL 63.22 vs GRPO 62.31; Qwen3-8B 67.61 vs 65.85 / 65.49; AIME24@16 89.33 vs FlowRL 86.67 (Table 1, arXiv:2609.03241); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; OPSA remains supervision-free; VISTA remains privileged-teacher adaptation.

### 2026-09-08 — ingest method:tgopd (active OPD plug-in; does not supersede method:opd / method:cispo / method:opsa / method:open-mopd)
- Added paper:tgopd (2609.02998), method:tgopd, recipe:tgopd (stub; no official code). Wired to task:student-distillation; optional mention on task:math-code-rl-dense.
- Status active. Prompt-level teacher probes then exclusive dense OPD vs GRPO. Sibling of RA-OPD / IDA-OPD / VISTA.
- Evidence: 4B LCB Vanilla OPD 42.3 closes 21% of 39.4→53.3 gap, TGOPD 47.1 closes 55%; 35B LCB TGOPD 64.0 vs base 61.0 vs teacher 62.7 (only positive transfer); 4B SOPD teacher GPU 9.8%→78.9% (Table 1/3, arXiv:2609.02998); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1 RLVR; Open-MOPD remains multi-teacher.

### 2026-09-08 — ingest method:optimizer-memory-schedules (active; does not supersede method:muon2) and thin method:adana
- Added paper:optimizer-memory-schedules (2609.04577), method:optimizer-memory-schedules, recipe:optimizer-memory-schedules (stub; no official code). Wired to task:llm-pretraining-optimization and task:pretrain-dense-7b. Thin method:adana + paper:adana (2602.05298) as the primary ADANA cite; `sota_for: []`.
- Status active. OT horizon changes optimizer rank and optimal LR/WD/memory. WD $\sim\sqrt{\mathrm{OT}}$; LR schedule ranking reverses; longer OT favors longer fixed memory.
- Evidence: 51M $1\times$ linear LR vs $8\times$/$32\times$ cosine; $c_{\mathrm{uniform}}=8\sqrt{f}$; Muon token multiplier vs AdamW $\sim 1.4\times$–$1.7\times$; ADANA equivalent-OT exponent 1.15–1.20 vs AdamW (arXiv:2609.04577); verified: true; evidence_level: preprint. 51M–253M only — not a 7B bake-off.
- Scope checks: Muon2 remains ~7B optimizer; Puro-2B remains consumer ~2B.

### 2026-09-08 — ingest method:uno (new task:diffusion-augmented-ar)
- Added paper:uno (2609.04010), method:uno, recipe:uno, task:diffusion-augmented-ar. Reverse redirects on task:posttrain-diffusion and task:llm-pretraining-optimization.
- Status sota for diffusion-augmented AR serving/train-addon only. Code: ifm-ai/uno.
- Evidence: 8B Uno SWE-Verified 68.4 vs DiffusionGemma 18.7; system throughput 5255 vs 1136 / 1197 tok/s; Uno Qwen 1.6× vs base AR at max H200 batch, >5700 tok/s (Table 1 / §5.2, arXiv:2609.04010); verified: true; evidence_level: preprint.
- Scope checks: does not supersede method:diffusion-opsd, method:self-opd, method:muon2, or method:cispo.

### 2026-09-07 — ingest 2026-09-07 weekday SOTA sweep (GAPO, RISE, layer-dropout, OPD hard-CoT, PTA)
- Added five active/niche methods without stealing current_sota. CISPO, OPD, OPSA, Muon2, CANOPY, SAO, and FoldGRPO remain first hops. Per-method receipts follow.
- Skipped (WATCH only): Iris 2609.04304 (search-agent SFT-RL climbing recipe; domain-specific); ACE expert skipping 2609.05228 (training-free MoE inference); MaxKernel 2609.04523 (TPU kernel agents); mHC residual analysis 2609.05309 (interpretability of existing mHC).
- Scope checks: no half supersessions; cheat-sheet first hops unchanged.

### 2026-09-07 — ingest method:pta (active; does not supersede method:opd / method:cispo / method:canopy / method:sao / method:foldgrpo)
- Added paper:pta (2609.04773, EMNLP 2026 Main), method:pta, recipe:pta. Wired to task:student-distillation; related mentions on task:long-horizon-tool-agent and task:agentic-async-rl.
- Status active. OPKD for tool-using agents: student-induced but teacher-committed rollouts; chunk-level verification + turn-level commitment; persistent lookahead. No official GitHub.
- Evidence: Search-R1 PTA+RL macro best@4 34.59 vs OPKD+RL 32.07; DeepEyes 70.00 vs 67.20; lookahead 0.644 vs 0.519 samples/s (arXiv:2609.04773); verified: true; evidence_level: preprint (EMNLP accept noted).
- Scope checks: OPD remains text distill; CISPO remains Pass@1 RLVR; CANOPY remains outcome-only agent RL; SAO remains async policy train; FoldGRPO remains folding.

### 2026-09-07 — ingest method:gapo (active plug-in; does not supersede method:cispo)
- Added paper:gapo (2609.00444, EMNLP 2026 Main), method:gapo, recipe:gapo. Wired to task:math-code-rl-dense.
- Status active. Adapts GRPO/GSPO IS-ratio clip to rollout advantage (reverse-KL trust-region). No reward shaping. Code: Sheng-J/GAPO.
- Evidence: R1-Distill-Qwen-1.5B AIME24 Pass@1/16 GAPO 44.0/76.7 vs GSPO 41.3/73.3; DeepCoder LCB-v5 24.8 vs 22.4 (arXiv:2609.00444); verified: true; evidence_level: preprint (EMNLP accept noted).
- Scope checks: CISPO remains Pass@1 default; OPD / OPSA / CANOPY unchanged.

### 2026-09-07 — ingest method:rise (active; does not supersede method:opd / method:cispo / method:opsa)
- Added paper:rise (2609.05295), method:rise, recipe:rise. Wired to task:student-distillation; related mentions on task:math-code-rl-dense and task:teacher-free-on-policy-self-adaptation.
- Status active. Synthetic teacher from the model's own RLVR trajectory via param/logit extrapolation. No official GitHub.
- Evidence: Qwen3-8B Math Avg RISE (weight) 62.7 vs GRPO 60.0; OLMo3-7B 56.4 vs 47.6; ALFWorld 84.4 vs 75.0 (arXiv:2609.05295); verified: true; evidence_level: preprint.
- Scope checks: OPD remains single-teacher distill; CISPO remains labeled RLVR; OPSA remains supervision-free; VISTA remains privileged-gold OPSD.

### 2026-09-07 — ingest method:layer-dropout (active; does not supersede method:muon2)
- Added paper:dont-drop-dropout (2609.05275, ICML 2026 extended), method:layer-dropout, recipe:layer-dropout. Wired to task:llm-pretraining-optimization, task:pretrain-dense-7b; optional note on task:budget-consumer-pretrain.
- Status active. Structured layer dropout with $r_{\mathrm{train}}=1/\rho$. Practical code: torchtune layer_dropout.py / fairseq LayerDrop (override residual scale).
- Evidence: 1.8B val 1.836 vs dense 1.849 at 15% FLOP save; 8.2B 25% FLOP save; ~1.5× self-speculative inference (arXiv:2609.05275); verified: true; evidence_level: peer-reviewed.
- Scope checks: Muon2 remains ~7B optimizer; Puro-2B remains consumer ~2B recipe.

### 2026-09-07 — ingest method:opd-hard-cot-selection (niche; does not supersede method:opd or method:opd-one-example)
- Added paper:opd-hard-cot-selection (2609.05198), method:opd-hard-cot-selection, recipe:opd-hard-cot-selection. Wired to task:student-distillation; cross-linked with method:opd-one-example.
- Status niche. Hard/long-CoT selection on OPD (not high token entropy); 8 hard examples match 17K. Sibling to OPD-II's diversity-vs-volume finding.
- Evidence: R1-Distill-Qwen-1.5B 8-hard avg 53.6 vs 17K 53.7; 7B 8-shot 59.5 vs 59.6 (arXiv:2609.05198); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; OPD-II remains the diversity/volume note.

### 2026-09-04 — ingest 2026-09-04 weekday SOTA sweep (OPD-II, Cliff, CANOPY, DIEM, IDA-OPD, Self-Routing, DRACO, spurious-advantage gotcha)
- Added task:outcome-only-long-horizon-agent-rl (CANOPY current_sota; DRACO active sibling). Plug-ins wired beside CISPO/OPD/VeriGate without stealing current_sota. `paper:spurious-advantage-grpo` is a gotcha only (no new method). Per-method receipts follow.
- Does not supersede method:cispo, method:opd, method:sao, method:opsa, method:mini-swe-agent, method:verigate, method:foldgrpo, method:open-mopd, method:ra-opd, or method:omp2-harness.
- Scope checks: new agent-RL task redirects async → agentic-async-rl, folding → long-horizon-tool-agent, dense math/code → math-code-rl-dense, harness → software-engineering-agent-harness, kernel → agent-harness-runtime. Reverse redirects added on those tasks.

### 2026-09-04 — ingest method:opd-one-example (niche; does not supersede method:opd)
- Added paper:opd-one-example (2609.04172), method:opd-one-example, recipe:opd-one-example. Wired to task:student-distillation; Part-II pointer on method:opd / recipe:opd.
- Status niche. OPD is data-overfed but algorithm-starved: one query recovers most full-data gain; ~16 semantically diverse queries match full-data / MOPD.
- Evidence: R1-Distill-1.5B math avg@16 one-shot 68.5 vs full-data 69.8 at step 300; state coverage 71.5% / 98.9% at 1 / 16 queries (arXiv:2609.04172); verified: true; evidence_level: preprint. Code: Thinking-Space/One-Shot-OPD.
- Scope checks: does not supersede method:opd, method:cispo, method:opsa, method:open-mopd, or method:ra-opd.

### 2026-09-04 — ingest method:cliff (active plug-in; does not supersede method:cispo)
- Added paper:cliff (2609.02817), method:cliff, recipe:cliff. Wired to task:math-code-rl-dense, task:reasoning-rl-alignment, task:all-zero-verifier-groups.
- Status active. First-mistake Pitfall Step → token advantages on GRPO/DAPO-style trainers. Not a PRM. Default λ=0. No public code.
- Evidence: Qwen3-4B math avg Cliff 65.66 vs GRPO 61.68 vs OPD 58.17; abstract +15% vs OPD / +7% vs GRPO across 12 scenarios (arXiv:2609.02817); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; VeriGate remains gated-PRM default; OPD remains distill default.

### 2026-09-04 — ingest method:canopy (new task:outcome-only-long-horizon-agent-rl)
- Added paper:canopy (2609.01245), method:canopy, recipe:canopy, task:outcome-only-long-horizon-agent-rl.
- Status sota for outcome-only long-horizon agent RL when a programmatic checker exists. Code listed: AlibabaResearch/SignalCoverageRL.
- Evidence: AppWorld Feb 2026 leaderboard Qwen3-14B TGC 86.9 / 67.6; SWE-bench Verified Qwen3.5-9B mean@4 31.3 → 47.9 (+16.6) (arXiv:2609.01245); verified: true; evidence_level: preprint.
- Scope checks: does not supersede method:sao, method:foldgrpo, method:cispo, method:mini-swe-agent, method:omp2-harness, or method:draco.

### 2026-09-04 — ingest method:diem (active example-reweight; does not supersede method:cispo)
- Added paper:diem (2608.29252), method:diem, recipe:diem. Wired to task:math-code-rl-dense / task:reasoning-rl-alignment.
- Status active. Gradient-alignment importance + constrained batch reweight. Like GMTS: optional. Code: hrtan/DIEM.
- Evidence: Qwen3-4B five-bench avg 40.66 vs GRPO 37.30; Qwen2.5-VL-7B six-bench 61.8 vs RFT 59.1 (arXiv:2608.29252); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; GMTS remains the token-filter plug-in.

### 2026-09-04 — ingest method:ida-opd (niche sampled-token entropy plug-in; does not supersede method:opd)
- Added paper:ida-opd (2608.29846), method:ida-opd, recipe:ida-opd. Wired to task:student-distillation beside ra-opd / opsa / opd.
- Status niche. Keep entropy-expanding A_y; shrink I_H(y)<0 by |q-p|/(q+p). No public code.
- Evidence: Qwen3-8B pass@16 AIME24/25 83.3/76.7 vs OPD 79.1/70.7; Qwen3-4B AIME24 pass@16 83.3 vs OPD 78.7 (arXiv:2608.29846); verified: true; evidence_level: preprint.
- Scope checks: does not replace CISPO or OPD.

### 2026-09-04 — ingest method:self-routing (active recipe router; does not supersede method:cispo or method:opsa)
- Added paper:self-routing (2609.01422), method:self-routing, recipe:self-routing. Wired to task:math-code-rl-dense / task:reasoning-rl-alignment / task:teacher-free-on-policy-self-adaptation (neighbor only).
- Status active. Sample-level GRPO / OPSD / REG / skip from rollout correctness+confidence. No external teacher. ms-swift code planned, not released.
- Evidence: Qwen3-4B six-bench avg 73.7 vs GRPO 66.8 vs OPSD 70.4; Qwen3.5-4B 86.6 vs 79.8 / 83.0 (arXiv:2609.01422); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; OPSA remains teacher-free unlabeled default (Self-Routing's OPSD branch needs gold answers).

### 2026-09-04 — ingest method:draco (active outcome-blind sibling; does not supersede method:canopy)
- Added paper:draco (2609.04094), method:draco, recipe:draco. Wired to task:outcome-only-long-horizon-agent-rl beside CANOPY.
- Status active. Dynamic rubrics + closed-form step credit when no programmatic checker. Code: IBM/draco.
- Evidence: Qwen3.6-27B AppWorld TN TGC p^1 85.3 vs base 69.4 vs outcome-reward GRPO 80.0; τ-bench SR 20.4 vs base 15.8 (arXiv:2609.04094); verified: true; evidence_level: preprint.
- Scope checks: does not supersede method:sao, method:cispo, method:canopy, or method:foldgrpo. Different backbone/protocol than CANOPY's 86.9; not a bake-off.

### 2026-09-04 — ingest paper:spurious-advantage-grpo (gotcha only; no new method)
- Added paper:spurious-advantage-grpo (2609.04063). Updated Gotchas on method:grpo, method:cispo, recipe:cispo, recipe:grpo-trl-training.
- SignBalance is documented in the paper node and is **not** a library method. current_sota unchanged (CISPO).
- Evidence: Qwen2.5-0.5B Avg-8 SignBalance 36.61 vs GRPO 34.24, lift on bounded-answer benches; MATH-7.5K 55.95% bounded answer shapes (arXiv:2609.04063); verified: true; evidence_level: preprint.

### 2026-09-02 — ingest method:omp2-harness (new task:agent-harness-runtime)
- Added paper:harness-playbook (Stencil blog, Can Bölük; no arXiv), method:omp2-harness, recipe:omp2-harness, task:agent-harness-runtime.
- Status sota for production harness-runtime architecture only. Does not supersede method:mini-swe-agent, method:cca, method:openhands-codeact, method:sao, method:foldgrpo, method:rlm, method:magic, method:cispo, method:muon2, method:mcp, or method:ace. omp/Pi are informal predecessors, not library nodes.
- Evidence: Pi official examples 2/78 correct (Appendix A); 5-tool median wall 36.6s vs Codex 42.2s vs Pi 37.0s on task sol (6-run median); renderer 267s → 90ms; speculative compaction ~10% before limit. verified: false; evidence_level: self-reported.
- Scope checks: new agents-shelf task; redirects issue-to-patch/locked eval → software-engineering-agent-harness, train agent RL → agentic-async-rl, dumped long prompt → long-context-prompt-offload, tool protocol → agent-communication. Reverse redirect on the SWE harness task for production engines; that task's current_sota stays mini-swe-agent.

### 2026-09-01 — ingest Agents shelf (harness, RLM, comms)
- Added domain `agents` and method categories `agent-harness`, `agent-protocol`, `agent-memory`, `agent-recursion`.
- New tasks: software-engineering-agent-harness (mini-swe-agent), long-context-prompt-offload (rlm), long-horizon-tool-agent (foldgrpo), agent-communication (mcp), agent-memory (ace), computer-use-agent (claude-computer-use / OSWorld 2.0 paper protocol), multi-agent-orchestration (single-agent-plus-tools; default do not).
- Evidence: official SWE-bench Verified JSON mini+Claude 4.5 Opus (high) 76.8% (2026-02-17); vals.ai locked mini Claude Opus 5 97.00% / DeepSeek V4 Pro 0813 96.40% (2026-09, different snapshot); RLM GPT-5 OOLONG-Pairs d=1 58.0 vs compaction 0.1 (2512.24601); FoldGRPO Seed-OSS-36B BrowseComp-Plus 0.620 vs ReAct 327K+GRPO 0.540 (2510.11967); ACE AppWorld 59.4 vs ReAct 42.4 (2510.04618); OSWorld 2.0 Opus 4.8 20.6% binary / 54.8% partial (2606.29537). Do not mix vals.ai 97% with official JSON 79.2%; do not mix OSWorld 2.0 paper 20.6% with aggregator 70.6%.
- Scope checks: does not retarget CISPO, Muon2, OPD, OLMo-3, poolside-model-factory, BMSSP, OPSA, SAE, MAGIC/Bergson, or SAO (`task:agentic-async-rl` remains SAO). AutoMixer `sota_for` empty. `task:agentic-async-rl` gained a redirect to the harness task for build-not-train; current_sota unchanged.

### 2026-09-01 — ingest method:bergson shelf (new task:training-data-attribution)
- Added task:training-data-attribution; paper:bergson (2606.11660), paper:magic (2504.16430), paper:trackstar (2410.17413), paper:source-tda (2405.12186), paper:ek-fac (2308.03296); method:bergson (active, sota_for empty), method:magic (sota for the new task only), method:trackstar (active), method:ek-fac (active), method:source-unrolling (niche); recipe:bergson-magic-gpt2-wikitext, recipe:bergson-trackstar.
- MAGIC is current_sota for training-data-attribution only (GPT-2 WikiText LDS 0.983). Bergson does not supersede MAGIC (library vs algorithm). No method in this shelf supersedes another. Training defaults unchanged: CISPO, Muon2, OPD family, OLMo-3, factory process, BMSSP, OPSA, SAE (sasa/circuitsteer/fega). AutoMixer pattern: optional factory component, not mix/kernel SOTA.
- Evidence: Bergson Table 1 GPT-2 WikiText FT LDS (50 queries, N=400, Adam) MAGIC 0.983 ± 0.005 vs SOURCE 0.387 vs EK-FAC 0.257 vs TrackStar 0.184; sorted-subset MAGIC 1.000 / EK-FAC 0.865 / TrackStar 0.803; Appendix C 8×A100 grad-dot 72B / EK-FAC 7B (Kronfluence EK-FAC 14B); WMDP bio token reweight +4.61 pp vs unweighted FT +3.11 pp. verified: true; evidence_level: preprint.
- Scope checks: new diagnostic task in interpretability / category data-attribution; redirects mix search → open-data-recipe, SAE → mechanistic-interpretability-dictionaries, factory → industrial-model-building. 405B intro scale recorded as design, not verified.

### 2026-09-01 — receipt: OPSA sweep #12 (4a8406e1)
- Squash-merged ingest of OPSA, NoRA, GMTS, RA-OPD, Qwen3.8-Next, CE-MoE, and GradCodeS, plus new tasks `task:teacher-free-on-policy-self-adaptation` (OPSA) and `task:full-lowbit-finetune` (GradCodeS). Training defaults unchanged: CISPO, Muon2, OPD family, OLMo-3, factory process, BMSSP. Per-method receipts follow.

### 2026-09-01 — integrity: mirror supersedes for method:muon-optimizer
- `method:muon-scalable.supersedes` now includes `method:muon-optimizer` so the existing `superseded_by` pointer is bidirectional. No SOTA retarget.

### 2026-09-01 — ingest method:opsa (new task:teacher-free-on-policy-self-adaptation)
- Added paper:opsa, method:opsa, recipe:opsa, task:teacher-free-on-policy-self-adaptation.
- Status sota for teacher-free / label-free on-policy self-adaptation only. Does not supersede method:cispo, method:opd, method:u-opsd, method:ttpo, method:self-opd, method:vista, or method:j-zero.
- Evidence: Qwen3-1.7B AIME24 Avg@32 48.85 vs base 13.44 vs OPD 32.08 (arXiv:2608.31046); verified: true; evidence_level: preprint.
- Scope checks: new niche; redirects for labeled RLVR, teacher distillation, consensus unlabeled, test-time, data-free, and flow matching.

### 2026-09-01 — ingest method:nora (active; does not supersede method:lr-matters-lora)
- Added paper:nora, method:nora, recipe:nora. Wired to task:parameter-efficient-fine-tuning and task:lora-quality-tuning.
- Status active. Recommended RLVR-stable LoRA upgrade. 24GB quality default remains vanilla LoRA + rsLoRA + LR sweep.
- Evidence: Llama-3.2-3B SFT avg 43.37 vs LoRA 37.93 vs RSLoRA 41.28; RLVR avg 44.4 vs LoRA 42.8 with PiSSA/MiLoRA collapse (arXiv:2608.31036); verified: true; evidence_level: preprint.
- Scope checks: PEFT shelf; no supersession because the paper does not rerun the library LR-sweep protocol of 2602.04998.

### 2026-09-01 — ingest method:gmts (niche token-filter; does not supersede method:cispo)
- Added paper:gmts, method:gmts, recipe:gmts. Wired to task:math-code-rl-dense.
- Status niche. Optional plug-in for GRPO/DAPO/CISPO-family token truncation via |E·ω|.
- Evidence: Qwen2.5-Math-7B DAPO+GMTS 50.14 vs DAPO+ETS 48.81; Qwen3-8B DAPO+GMTS 56.08 vs 53.71 (arXiv:2608.30632); verified: true; evidence_level: preprint.
- Scope checks: in-scope as train-rlvr add-on; CISPO remains Pass@1 default.

### 2026-09-01 — ingest method:ra-opd (niche teacher-OPD filter; does not supersede method:opd or method:opsa)
- Added paper:ra-opd, method:ra-opd, recipe:ra-opd. Wired to task:student-distillation.
- Status niche. Keep trajectories with (2R−1)G≥0; no extra rollouts.
- Evidence: Qwen3-8B-Base math avg@k 49.43 vs OPD 44.34 vs ExOPD 46.95; DeepSeek-R1-Distill-Qwen-7B 69.34 vs OPD 64.43 (arXiv:2608.27960); verified: true; evidence_level: preprint.
- Scope checks: modular filter on teacher OPD; tension with OPSA teacher-noise finding documented, not a supersession.

### 2026-09-01 — ingest method:qwen38-next (active architecture recipe; does not supersede method:muon2 or method:deepseek-v4)
- Added paper:qwen38-next, method:qwen38-next, recipe:qwen38-next. Wired to task:pretrain-moe-frontier, task:pretrain-dense-7b, task:linear-time-sequence-modeling.
- Status active. GDN hybrid + Gated Residual + QSA CPT + off-accelerator n-gram + Muon/AdamW split. Public code is FlashQLA.
- Evidence: 125B-A6B leads 397B-A17B on 8/14 benches at ~1/9 FLOPs; GDN hybrid avg 53.81 vs full attn 49.87; FlashQLA 2–3× forward (arXiv:2608.30320); verified: true; evidence_level: preprint.
- Scope checks: adjacent mHC/AttnRes/GDN; Muon2 and DeepSeek-V4/Kimi-K3 defaults unchanged.

### 2026-09-01 — ingest method:ce-moe (niche MoE layout; does not supersede method:deepseek-v4)
- Added paper:ce-moe, method:ce-moe. No public code; no recipe.
- Status niche. Concentrate experts in fewer routed layers.
- Evidence: 2B–31.5B matched params; 33.3% fewer GPU-hours at 31.5B with better downstream and throughput (arXiv:2608.28511 abstract); verified: true; evidence_level: preprint.
- Scope checks: optional train-moe layout; DeepSeek-V4 / Kimi-K3 remain architecture defaults.

### 2026-09-01 — ingest method:gradcodes (new task:full-lowbit-finetune)
- Added paper:gradcodes, method:gradcodes, recipe:gradcodes, task:full-lowbit-finetune.
- Status sota for fully low-bit code-space fine-tune only. Does not supersede method:aqlora-q or method:quartet-ii.
- Evidence: Llama-3.2-1B-Instruct GSM8K fully 4-bit GradCodeS Full 41.63 vs PV-Tuning 36.92 vs QLoRA-4Merge 24.79 (arXiv:2608.30908); verified: true; evidence_level: preprint.
- Scope checks: new niche; redirects for mixed-precision 4-bit PEFT, native FP4 hardware train, and 24GB quality LoRA.
