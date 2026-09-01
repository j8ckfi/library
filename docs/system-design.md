# System Design: The Library as an Agent-Operating System

> This document is the master design specification for `j8ckfi/library`. It describes the system as a single
> coherent machine — a tower of linked abstractions — rather than an assemblage of parts. Everything else
> (`AGENTS.md`, `docs/ontology.md`, `docs/ingestion-guide.md`, `schema/schema.json`, `templates/`) is a
> projection of the contracts defined here.

---

## 1. What This System Actually Is

Strip away the implementation and `j8ckfi/library` is one thing: **a decision-support system for a training
agent standing in front of an expensive, irreversible action** (spending GPU-weeks on the wrong recipe).

Every design choice below is derived from a single optimization target:

> **Minimize the expected cost of a training decision, where cost = P(wrong method) × cost of the
> wasted run + tokens spent reaching the decision.**

That decomposes into two failure modes the system must attack:

| Failure mode | Cause | System countermeasure |
| :--- | :--- | :--- |
| **Routing error** — agent picks the wrong *task* | Vague NL request, near-duplicate tasks, scope creep | Routing guards, scope boundaries, redirect edges (`§3`) |
| **Trust error** — agent picks the right task but over-trusts a claim | Undated, unverified, or stale evidence | Evidence levels, staleness budgets, decay reports (`§5, §6`) |

Everything else — the CLI, the schema, the templates — exists to make those two countermeasures cheap.

---

## 2. The Tower of Abstractions

The system is a strict tower. Each layer consumes only the layer below it and exposes a narrow contract to
the layer above. An agent should be able to name, in one sentence, what each layer promises.

```
┌─────────────────────────────────────────────────────────────────────┐
│ L6  PROTOCOL     AGENTS.md — the agent's boot file:                 │
│     "how to behave" (decision loop, token economy, write rules)     │
├─────────────────────────────────────────────────────────────────────┤
│ L5  MAINTENANCE  Ingestion guide + supersession transaction +       │
│     receipts + staleness review — how the tower grows safely        │
├─────────────────────────────────────────────────────────────────────┤
│ L4  INTERFACE    CLI verbs: sota / route / query / show / walk /    │
│     path / decide / stale / index / validate / new                  │
├─────────────────────────────────────────────────────────────────────┤
│ L3  DERIVED      graph/INDEX.md routing table, digests, exports —   │
│     regenerable, committed, never hand-edited                       │
├─────────────────────────────────────────────────────────────────────┤
│ L2  SUBSTRATE    graph/{tasks,methods,papers,recipes}/*.md —        │
│     the single source of truth (one file = one node = one claim set)│
├─────────────────────────────────────────────────────────────────────┤
│ L1  CONTRACT     ontology.md + schema/schema.json + validator.py —  │
│     the invariants: schemas, edge semantics, supersession DAG       │
└─────────────────────────────────────────────────────────────────────┘
```

**The one invariant that makes the tower coherent:** information flows *upward only*.
- L3 (index) is derived from L2 — regenerate, never edit.
- L6 (AGENTS.md routing cheat-sheet) is a cached projection of L3 — regenerated, never hand-maintained.
- L1 (validator) may reject any L2 content that violates L4 contracts.
- No layer may contain a fact that contradicts a layer below it. `validate` is the mechanical check of this rule.

If a future agent remembers one sentence about this repo, it is: **the graph files are the truth; everything else is a view or a check.**

---

## 3. The Agent Operating Model (the decision loop)

An autonomous agent driving this system executes a fixed five-phase loop. Every interface element in the
system exists to serve exactly one phase, and every phase has a named failure mode it must prevent.

```
┌──────────────────────────────────────────────────────────────────────┐
│  PHASE 1  ROUTE     "train model X to do Y" → task:<slug>            │
│           Guard against: routing error, near-task confusion          │
│           Primitives: AGENTS.md cheat-sheet → `library route` →      │
│           `library query --type task` → task scope/redirects         │
├──────────────────────────────────────────────────────────────────────┤
│  PHASE 2  RESOLVE  task:<slug> → method + claims + paper + recipe    │
│           Guard against: using superseded/niche methods              │
│           Primitives: `library sota <task>` (decision-shaped output) │
├──────────────────────────────────────────────────────────────────────┤
│  PHASE 3  VERIFY   claims → confidence                               │
│           Guard against: over-trusting self-reported results,        │
│           stale as_of dates                                          │
│           Primitives: claim.evidence_level, claim.verified,          │
│           `library stale`, task.last_reviewed                        │
├──────────────────────────────────────────────────────────────────────┤
│  PHASE 4  EXECUTE  method → runnable recipe (hardware, deps, code)   │
│           Guard against: hardware mismatch, missing gotchas          │
│           Primitives: `library show recipe:<slug>`, method gotchas   │
├──────────────────────────────────────────────────────────────────────┤
│  PHASE 5  WRITEBACK new knowledge → graph (transaction + receipt)    │
│           Guard against: partial supersession, silent drift          │
│           Primitives: `library new` + supersession transaction       │
│           + receipt + `library validate` (§6)                        │
└──────────────────────────────────────────────────────────────────────┘
```

### 3.1 Phase 1 — Routing (the contract that matters most)

Routing errors dominate all other failure modes: picking DoRA over vanilla-LoRA+rsLoRA, or picking the 7B
recipe for a 2B budget, wastes entire training runs. Therefore **routing is a graph citizen, not prose**.

Every task node carries three routing fields (see `docs/ontology.md` §2.1):

- `scope` — one sentence: what problems this task node owns.
- `out_of_scope` — list of near-miss problem statements that *look* like this task but are not.
- `redirects` — list of `{when: "<condition>", to: "task:<slug>"}` guards. This is where
  "NOT olmo-3 7B, NOT muon2+kl-soap" lives as *data* instead of a comment.

The resolution order for routing is fixed and agents must follow it:

```
1. Cheat-sheet hit?            (AGENTS.md / graph/INDEX.md — O(1) token cost)
2. Exact task-id hit?          (library sota "task:<slug>")
3. Keyword route?              (library route "<nl>" → ranked candidates + boundaries)
4. Manual graph walk           (library query / path) — last resort
```

Each step is strictly cheaper in tokens than falling through to the next; the design goal is that 90%+ of
requests terminate at step 1–2 with zero `query` calls.

### 3.2 Phases 2–4 — Resolution is decision-shaped, not data-shaped

`library sota` output (and its future `decide` refinement) must always answer, in order:
**What do I use? What would I use instead? What must I NOT use? What will bite me? Where's the code?
How much should I trust all of this?** A response missing any of these six is incomplete. See §4 for the
output tiers.

### 3.3 Phase 5 — Writing back is a transaction, not a checklist

See §6. The short version: multi-file supersession is one transaction with post-conditions enforced by the
validator and a receipt appended to the log, so every future agent can reconstruct *why* the graph changed.

---

## 4. Token Economy (output tiering)

Agents pay per token; humans read prose. Every read command therefore has three tiers, and agents are
instructed (in AGENTS.md) to default to the cheapest tier that answers the question:

| Tier | Flag | Budget | Contains |
| :--- | :--- | :--- | :--- |
| **Brief** | `--brief` | ~10 lines | ids, status, top claim, freshness, one-line next step |
| **Default** | (none) | ~1 screen | decision-shaped output incl. alternates + do-not-use + gotchas |
| **Full** | `--json` | unbounded | complete metadata + body for programmatic consumption |

Design rules:
1. **JSON is a first-class citizen, not an afterthought** — every command emits it; agents script against it.
2. **Machine summaries never truncate mid-claim.** A claim row is atomic; if the budget cuts, it cuts rows.
3. **The default human output is the brief's superset** — no command prints information the JSON lacks.
4. **Search results show *why* they ranked** (`reasons`) so the agent can calibrate trust without a second call.

---

## 5. Evidence & Trust Model

The graph carries a trust gradient, not a bit. Every claim is stamped with:

```yaml
verified: true|false          # independent replication vs self-reported
evidence_level: peer-reviewed | preprint | self-reported | unofficial-repro
source_url: "https://..."     # where the number actually lives
```

Decision rule encoded for agents (in AGENTS.md):
- `sota` status **requires** at least one claim with `verified: true` and a comparator baseline.
- A task whose `current_sota.as_of` is older than the freshness budget (default: 4 months) is **stale**;
  its recommendation must be treated as provisional and re-checked before an expensive commit.
- Papers are dated by arXiv ID, which the system treats as ground truth for ordering; two methods claiming
  the same task are compared by (date, verified, metric) — never by claim wording.

---

## 6. The Write Path: Ingestion as a Transaction

Ingestion is the only place agents mutate the graph, so it gets the strictest contract
(full workflow: `docs/ingestion-guide.md`):

1. **Pre-flight**: confirm the task node exists (create it if genuinely new) and confirm scope —
   most ingestion errors are routing errors under a different name.
2. **Supersession transaction**: if the new method beats an incumbent SOTA, the write touches
   `method:<new>`, `method:<old>`, and `task:<slug>` as **one atomic unit**. Post-conditions (validator-enforced):
   - no `status: superseded` method appears in any task's `current_sota`;
   - every `superseded_by` has a mirror `supersedes` edge (no one-way links);
   - every task in a new method's `sota_for` has an updated `current_sota` entry with a fresh `as_of`.
3. **Receipt**: every mutation appends an entry to `graph/CHANGELOG.md` — date, node ids, what changed and
   the evidence that motivated it. The changelog is the system's audit log; agents read it to understand
   *why* state is what it is before trusting it.
4. **Validate** (`python -m library validate`) must pass with 0 errors before the write is considered done.

---

## 7. Decay & Maintenance (the system must stay true, not just stay valid)

A SOTA library's half-life is short. Validation proves *consistency*, not *freshness*. The system therefore
exposes decay as a first-class, queryable property:

- Every task and method carries `last_reviewed: "YYYY-MM-DD"`.
- `library stale` ranks nodes by `as_of`/`last_reviewed` age against the freshness budget,
  giving a maintenance agent a prioritized work queue — the graph tells you what to re-verify next.
- The review protocol (when an agent re-checks a stale node): re-read the primary paper, search for newer
  work citing it, then either reaffirm (bump `last_reviewed`) or run the supersession transaction (§6).
- **Ingest bias**: when adding a method, the ingesting agent is also responsible for checking whether it
  *demotes* an existing method. Ingestion without supersession-checking is treated as an incomplete write.

---

## 8. CLI Ergonomics Primitives (shipped)

These close the routing, token-economy, decay, and write-path gaps above. Agents should prefer
`sota` / `decide` over `query`.

| # | Command | Closes gap | Spec |
| :-- | :--- | :--- | :--- |
| 1 | ✅ **Shipped**: `library index` | Hand-maintained cheat-sheet drift | Renders `graph/INDEX.md` from `current_sota` + task `redirects` + method `do_not_use_for`. Also regenerates the AGENTS.md §2 cheat-sheet between `<!-- CHEAT-SHEET:START -->` / `END` markers so L6 cannot drift from L2. Never hand-edit INDEX.md. `validate` **warns** (exit 0) when INDEX.md or the cheat-sheet block is stale vs graph state; exit 1 is reserved for schema/integrity errors. |
| 2 | ✅ **Shipped**: `--brief` / `--json` everywhere | Token economy | Tiered output per §4. `--brief` ~10 lines; default decision-shaped; `--json` unbounded superset. JSON is first-class on `sota`, `query`, `show`, `walk`, `path`, `stats`, `decide`, `route`, `stale`, `index` (`index --json` = `{written: [...], stale: bool}`). Claims are atomic (never truncated mid-claim). |
| 3 | ✅ **Shipped**: `library decide <task-or-nl>` | Decision-shaped output | Always answers in order: What do I use? What would I use instead? What must I NOT use? What will bite me? Where's the code? How much should I trust this? Includes alternates, `do_not_use_for` / redirects, method gotchas, recipe + hardware, evidence_level + verified, staleness vs 4-month budget. `--json` and `--brief` required. |
| 4 | ✅ **Shipped**: `library stale [--max-age-days N]` | Silent rot | Default N=120 (ontology §4.3). Ranks tasks/methods by `current_sota[].as_of` and `last_reviewed`. Nodes missing dates count as stale. Exit 1 if any **task current_sota** exceeds the budget (CI-able). `--json` lists `{id, as_of, last_reviewed, age_days, over_budget}`. |
| 5 | ✅ **Shipped**: `library route "<natural language>"` | Routing dead-ends | Ranked candidate tasks with `scope`, `out_of_scope`, and `redirects` rendered (`when` → `to`). Lexical + graph ranking over titles/summaries/tags/scope. Never returns empty without near-misses. `--json` includes `reasons`. |
| 6 | ✅ **Shipped**: `library supersede <new> <old> --task <task-id>` | Partial supersession writes | Transaction per §6: new method `status: sota` + `sota_for` + `supersedes`; old method `status: superseded` + `superseded_by`; task `current_sota` / `last_reviewed` updated; CHANGELOG receipt. Refuses to finish until validator post-conditions hold. `--dry-run` prints planned file edits without writing. |
| 7 | ✅ **Shipped**: committed compiled export | Remote/GitHub-first use | `dist/graph.json` (regenerated by `.github/workflows/export.yml` on every graph change) lets a remote agent load the entire graph — nodes, edges, metadata — in **one** `gh api repos/j8ckfi/library/contents/dist/graph.json` call instead of walking 487 files. Local clone + CLI remains the deep-inspection path. |

### 8.1 Remote access (first-class, no local clone)

The graph is fully usable over the GitHub API without cloning:

```bash
# Whole graph, one fetch (CI keeps it fresh on every push to main):
gh api repos/j8ckfi/library/contents/dist/graph.json

# Or individual nodes / search when exploring by path:
gh api repos/j8ckfi/library/contents/graph/methods/muon2.md
gh api "search/code?q=repo:j8ckfi/library+transolver"
```

The routing layer (AGENTS.md §2 cheat-sheet) travels in the prompt, so many questions need no fetch at
all; `dist/graph.json` covers exploratory queries; the CLI covers deep local work. Writes (supersession
transactions, receipts) work via branch/commit/PR APIs — no local checkout required.

---

Non-goals: embeddings/vector search (the graph is small; lexical ranking + graph structure is sufficient and
deterministic), a server/API (CLI over files is the agent-native interface), and LLM-generated summaries at
query time (nodes are already agent-shaped prose).

---

## 9. Coherence Checklist (how to tell the system is still one system)

When adding anything to this repo, verify these invariants — they are what make the parts a system:

1. Every fact lives in exactly one node; everything else references it.
2. Every command's JSON output is a superset of its prose output.
3. Every write path's post-conditions are validator-enforced, not prose-encouraged.
4. Every recommendation is dated, evidenced, and carries its redirect guards.
5. Every layer's docs point down to the layer that owns the fact, never duplicate it.
6. `python -m library validate` is the definition of "the system is healthy" — no exceptions, no suppressions.
