# Higgsfield Skills Analysis for REVIEW²

Status: research / adoption blueprint  
Date: 2026-09-17  
Target system: REVIEW² / Reviewing Reviews  

## 0. Source pin

Higgsfield upstream is stored separately and must remain unchanged.

- Reference repo: `yeungseung/connect-ai`
- Reference path: `external-reference/higgsfield-skills`
- Reference note: `external-reference/HIGGSFIELD_REFERENCE.md`
- Upstream: `higgsfield-ai/skills`
- Pinned commit: `d071406147a37b835bed09543d85ab3e9bd85c7d`
- Upstream version at pin: `0.12.0`

Policy:

```text
Higgsfield upstream
= reference implementation

REVIEW² docs / schemas / code
= our canonical system
```

Do not edit or fork logic directly inside the pinned Higgsfield source. Extract only patterns that are useful to REVIEW².

---

# 1. Executive conclusion

Higgsfield is most useful to REVIEW² not as a video-generation backend, but as a reference architecture for an AI-operated production system.

The strongest reusable ideas are:

1. thin decision contracts + on-demand reference knowledge
2. explicit capability routing with `Use when / NOT for / Chain`
3. typed handoff between stages instead of hidden implicit state
4. persistent human approval state
5. dependency-aware invalidation
6. live capability discovery instead of hard-coded tool assumptions
7. deterministic execution for exact text/layout/state work
8. targeted repair instead of full regeneration
9. explicit checkpoints before downstream stages
10. behavior evals in addition to schema validation

The largest fit is not Source Acquisition or Story logic itself. The largest fit is the cross-cutting orchestration layer around Production, Presentation, Render, QA, and Human Gates.

Therefore Higgsfield should influence a new REVIEW² **Control Plane**, while the existing REVIEW² data/story pipeline remains the domain architecture.

---

# 2. Important warning: do not copy Higgsfield wholesale

Higgsfield itself demonstrates documentation drift.

At the pinned revision:

- repository `VERSION` and marketplace manifest are `0.12.0`
- marketplace manifest lists 8 active skills
- `CLAUDE.md` still contains older descriptions such as 7 skills, older version wording, and a retired `game-generation` structure

This means even a system with CI checks can drift when the same architectural truth is duplicated in prose.

REVIEW² should therefore use:

```text
Schema / Manifest / State
= canonical truth

Human-readable docs
= explanation / generated view / validated projection
```

Do not let multiple Markdown files independently define the same runtime truth.

---

# 3. Higgsfield pattern map

## 3.1 Thin decision contract + lazy reference loading

Higgsfield explicitly keeps `SKILL.md` small enough to hold only information required to decide the next action. Detailed tables, troubleshooting, prompt libraries, and long references live under `references/` and are loaded only when needed.

### REVIEW² adaptation

Create a distinction between:

```text
Stage Contract
= what this stage is for
= required inputs
= output contract
= routing conditions
= blocking conditions
= human gate requirements
= failure policy

Knowledge Pack
= large research rules
= examples
= edge cases
= implementation details
= prompt libraries
= renderer notes
```

This is useful later for Story, Production, Scene, Renderer, QA agents because loading all project documentation into every agent context would become expensive and noisy.

Rating: **DIRECT ADOPT**

---

## 3.2 Explicit routing boundaries

Higgsfield skills declare:

```text
Use when
NOT for
Chain with
```

and individual skills often include tie-breakers when multiple modes are plausible.

Product Photoshoot is a good example: it routes by user intent rather than a single keyword and has explicit precedence rules when multiple modes match.

### REVIEW² adaptation

Future REVIEW² capabilities should have machine-readable routing metadata such as:

```text
capability_id
stage
use_when
not_for
requires
produces
human_gate
priority
conflicts_with
fallback_policy
```

Example:

```text
ConflictSplit
use_when:
  Finding.type == conflict

not_for:
  conditional disagreement

use_instead:
  ConditionSplit
```

This should extend the current Component Resolver philosophy rather than replace it.

Rating: **ADAPT**

---

## 3.3 Explicit return values, not implicit cross-stage memory

Higgsfield states that skills chain through return values, not implicit state. Example: Soul ID creates a stable reference ID; another skill consumes that reference explicitly.

### REVIEW² adaptation

Every stage should emit typed artifacts that downstream stages consume explicitly.

```text
Evidence Packet
→ Claim
→ Finding
→ Argument Structure
→ Story Plan
→ Story Lock
→ Script Plan
→ Scene Plan
→ Asset Binding
→ Render Plan
→ Render Artifact
→ QA Result
```

No downstream stage should rely on “the agent remembers what happened earlier” as canonical state.

Rating: **DIRECT ADOPT**

---

## 3.4 Persistent approval state

Higgsfield Brandkit persists user approvals in durable local state and explicitly forbids inferring approval from silence or successful generation.

It also records dependencies between approved foundation elements and downstream artifacts.

### REVIEW² adaptation

This is highly relevant to the existing Human Gate design.

Proposed future entity:

```text
Approval State
├─ gate_id
├─ subject_type
├─ subject_id
├─ revision
├─ status
├─ approved_by
├─ approved_at
├─ input_revision_ids
├─ notes
└─ invalidated_by
```

Likely gate families:

```text
SOURCE_GATE
DISCOVERY_GATE
STORY_SOFT_LOCK
STORY_HARD_LOCK
VISUAL_ASSET_GATE
PRODUCTION_LOCK
FINAL_GATE
```

Rules:

```text
approval is explicit
approval is revision-specific
changed upstream data can invalidate approval
invalidated approval never silently survives
```

Rating: **DIRECT ADOPT**

---

## 3.5 Dependency-aware invalidation

Brandkit has one of the most valuable patterns in the repository:

```text
change foundation slot
→ invalidate only downstream outputs that depend on that slot
```

It does not blindly regenerate the whole project.

### REVIEW² adaptation

Introduce a dependency graph across production artifacts.

Examples:

```text
Evidence Packet EP-014 changed
→ Claim C-22 potentially invalid
→ Finding F-04 potentially invalid
→ Story Beat B-07 depends on F-04
→ Scene S-12 depends on B-07
```

or:

```text
Asset A-31 replaced
→ only Scene S-12 / S-13 render plans invalid
→ Story remains valid
```

or:

```text
Story Hard Lock revision changes
→ Script / Scene / Presentation / Render descendants invalid
→ Source / Evidence remain valid
```

This is likely one of the most important future orchestration structures in REVIEW².

Rating: **DIRECT ADOPT**

---

## 3.6 Live capability discovery

Higgsfield repeatedly distinguishes live system state from static reference documentation.

Examples include querying the current model catalog, workflow catalog, presets, and voices before execution.

### REVIEW² adaptation

Renderer/model/tool availability should eventually be discovered through adapters instead of assumed from documentation.

```text
Capability Registry
      ↓
Live Adapter Discovery
      ↓
Available capability set
      ↓
Resolver
```

Static docs should describe intent and selection policy, not claim that a provider/model is currently available.

Rating: **DIRECT ADOPT for adapters, not needed for core research data**

---

## 3.7 Structured intent → compiler → provider command

Several Higgsfield skills do not let the agent freely compose the final provider prompt. The skill gathers structured intent, and a dedicated enhancer/compiler owns the final prompt or command contract.

### REVIEW² adaptation

Do not let Scene/Story agents directly freehand renderer prompts.

Proposed separation:

```text
Story
↓
Scene Plan
↓
Presentation Intent
↓
Asset Binding
↓
Execution Compiler
├─ HyperFrames compiler
├─ image generation compiler
├─ video generation compiler
├─ TTS compiler
└─ overlay compiler
↓
Provider / Renderer Adapter
```

This preserves the existing rule:

```text
Component decides how meaning is shown
Renderer decides how pixels are produced
```

Rating: **DIRECT ADOPT concept / REVIEW²-specific implementation**

---

## 3.8 Deterministic tools for exact work

Brandkit deliberately separates generative work from deterministic SVG/HTML/PPTX construction. It does not ask an image model to perform exact editable layout tasks when code can guarantee them.

The YouTube Thumbnail skill similarly prefers deterministic overlay handling for exact headline text.

### REVIEW² adaptation

Strong fit with HyperFrames.

Use deterministic code for:

```text
exact copy
numbers
charts
tables
source badges
subtitles
safe areas
product tags
layout
animation timing
scene assembly
```

Use generative models for:

```text
illustrative assets
backgrounds
concept visuals
image/video transformations
non-deterministic visual material
```

Rating: **DIRECT ADOPT**

---

## 3.9 Checkpoint barriers

Video Explainer defines hard barriers: do not start a later phase until the required artifacts for the previous phase exist and are valid.

### REVIEW² adaptation

Turn important stage transitions into executable preconditions.

Example:

```text
Story-driven Research cannot finish unless:
- required Beat research requirements resolved or explicitly marked gap
- SUPPORT search complete
- CHALLENGE search complete
- ALTERNATIVE search complete
- Human Gate 3 passed
```

```text
Render cannot start unless:
- Story Hard Lock valid
- ScenePlan valid
- required assets bound
- required component status == validated
- renderer capabilities available
```

Rating: **DIRECT ADOPT**

---

## 3.10 Targeted repair instead of whole-pipeline regeneration

Higgsfield repeatedly prefers retrying or regenerating only the failing block/output. Thumbnail editing is explicitly surgical; Brandkit repairs only the failing downstream element; Explainer regenerates only a failed clip.

### REVIEW² adaptation

QA should return a repair target, not merely pass/fail.

Proposed result:

```text
QA Finding
├─ severity
├─ artifact_id
├─ failure_type
├─ repair_scope
├─ invalidates
└─ recommended_action
```

Example:

```text
subtitle overflow
→ repair Scene S-18 subtitle layout only
→ do not regenerate narration/story
```

Rating: **DIRECT ADOPT**

---

## 3.11 Behavioral evals

Higgsfield has separate eval scenarios because Markdown behavior rules can regress even if files parse correctly.

Their eval concept records:

```text
commit SHA
date
scenario score
failure mode
time-to-result
```

### REVIEW² adaptation

REVIEW² already has schema/contract validation. Add a second category later:

```text
STRUCTURAL TEST
= schema validity / references / contract links

BEHAVIOR TEST
= does the system actually make the correct decision for a realistic case
```

Possible scenario groups:

```text
Source Gate scenarios
product identity mismatch scenarios
origin contamination scenarios
conflict vs condition routing scenarios
Story challenge-search scenarios
Component Resolver scenarios
Visual Asset Gate scenarios
QA repair-scope scenarios
```

Rating: **DIRECT ADOPT**

---

# 4. What should NOT be adopted directly

## 4.1 Higgsfield Story / Explainer structure

The fixed 10-second block model is implementation-specific.

REVIEW² Story Engine is being researched as an Audience State / State Transition system and must not be replaced by Higgsfield's explainer sequencing.

Use Explainer only as a reference for:

```text
ordered artifact pairing
checkpoint barriers
assembly manifests
partial recovery
```

Rating: **REFERENCE ONLY**

---

## 4.2 Provider-specific model defaults

Do not encode Higgsfield's preferred models or provider names into REVIEW² architecture.

Model choice belongs in adapters/capability data and can change independently.

Rating: **REJECT AS ARCHITECTURE**

---

## 4.3 Duplicated reference documents inside every skill

Higgsfield intentionally accepts some duplicated reference files so each skill can install independently.

That tradeoff is not ideal for REVIEW² canonical truth because REVIEW² relies heavily on shared Source / Evidence / Claim / Finding definitions.

REVIEW² should prefer:

```text
one canonical schema / rule source
↓
build or package stage-specific context views
```

rather than manually duplicating canonical rules.

Rating: **DO NOT ADOPT DIRECTLY**

---

## 4.4 Markdown prose as runtime truth

The observed Higgsfield documentation drift proves this is unsafe.

Runtime truth should live in structured manifests/schemas/state where possible.

Rating: **REJECT**

---

# 5. Proposed REVIEW² Control Plane

This does not replace the existing content pipeline.

Existing domain pipeline remains:

```text
PRODUCT
↓
SOURCE ACQUISITION
↓
EVIDENCE
↓
ANALYSIS
↓
ARGUMENT / LOGIC
↓
STORY ENGINE
↓
STORY-DRIVEN RESEARCH
↓
STORY HARD LOCK
↓
SCRIPT / PRODUCTION
↓
SCENE
↓
PRESENTATION
↓
RENDER
↓
QA
↓
PUBLISH / FEEDBACK
```

Add a cross-cutting Control Plane:

```text
                    REVIEW² CONTROL PLANE

┌─────────────────────────────────────────────────────────┐
│ Canonical Manifest / Schemas                            │
│ Capability Registry                                     │
│ Stage Contracts                                         │
│ Approval / Lock State                                   │
│ Dependency + Invalidation Graph                         │
│ Context Loader                                          │
│ Execution / Prompt Compiler                             │
│ Run Ledger                                              │
│ Recovery Policy                                         │
│ Eval Harness                                            │
└─────────────────────────────────────────────────────────┘
              │ controls / observes
              ▼
PRODUCT → SOURCE → EVIDENCE → ANALYSIS → STORY → PRODUCTION
                                      → SCENE → PRESENTATION
                                      → RENDER → QA
```

The Control Plane answers:

```text
What stage are we in?
What is allowed to run?
What inputs are valid?
What has the human approved?
What became stale after a change?
Which capability should handle this?
What context does that capability need?
What exact command/render plan should be compiled?
What failed?
What is the smallest valid repair scope?
```

---

# 6. Candidate future entities

Do not implement these yet. They are design candidates extracted from the analysis.

## 6.1 capability-manifest

```text
capability_id
stage
version
use_when
not_for
inputs
outputs
human_gate
priority
conflicts
adapter
reference_packs
```

## 6.2 approval-state

```text
gate_id
subject_id
subject_revision
status
approved_by
approved_at
input_revisions
notes
invalidated_by
```

## 6.3 dependency-edge

```text
from_artifact
from_revision
to_artifact
dependency_type
invalidation_policy
```

## 6.4 run-record

```text
run_id
capability_id
input_artifact_ids
adapter
provider/model
compiled_params
started_at
completed_at
status
output_artifact_ids
retry_of
failure_code
```

## 6.5 qa-finding

```text
artifact_id
failure_type
severity
repair_scope
invalidates
recommended_action
```

These names are provisional until Production Architecture and Story Engine research are further advanced.

---

# 7. REVIEW² layer impact map

| REVIEW² Layer | Higgsfield impact | Main reusable pattern |
|---|---|---|
| Source Acquisition | Low-Medium | explicit gates, durable approvals, stage preconditions |
| Evidence | Medium | revision-aware artifact lineage |
| Analysis | Medium | typed outputs, behavior evals |
| Argument / Logic | Medium | explicit stage contract |
| Story Engine | Low | orchestration only; do not copy story logic |
| Story-driven Research | Medium | checkpoints, dependency tracking, gap state |
| Script / Production | High | thin capability contracts, context loading, compiler separation |
| Scene | High | structured routing, typed handoff |
| Presentation | Very High | deterministic vs generative split, dependency handling |
| Render | Very High | live capability discovery, run ledger, targeted retries |
| QA | Very High | repair scope, behavioral evals, regression testing |
| Publish / Feedback | Medium | run/eval/performance lineage |

---

# 8. Highest-value Higgsfield references

When implementation begins, inspect these pinned files first.

## Core architecture

```text
external-reference/higgsfield-skills/CLAUDE.md
external-reference/higgsfield-skills/CONTRIBUTING.md
external-reference/higgsfield-skills/.github/workflows/validate-skills.yml
external-reference/higgsfield-skills/evals/README.md
external-reference/higgsfield-skills/evals/scenarios.md
```

Use for:

```text
skill contract design
context loading
CI rules
behavior eval design
chaining semantics
```

## Orchestration / routing

```text
external-reference/higgsfield-skills/higgsfield-generate/SKILL.md
external-reference/higgsfield-skills/higgsfield-product-photoshoot/SKILL.md
external-reference/higgsfield-skills/higgsfield-marketplace-cards/SKILL.md
```

Use for:

```text
intent routing
mode precedence
live capability discovery
scope/bundle selection
provider abstraction
```

## State / dependencies / human approvals

```text
external-reference/higgsfield-skills/higgsfield-brandkit/SKILL.md
external-reference/higgsfield-skills/higgsfield-brandkit/references/handoff.md
external-reference/higgsfield-skills/higgsfield-brandkit/references/state-payloads.md
external-reference/higgsfield-skills/higgsfield-brandkit/references/qa-and-iteration.md
```

Use for:

```text
approval state
lock state
dependency invalidation
partial regeneration
deterministic output handling
```

## Asset identity / stable reference

```text
external-reference/higgsfield-skills/higgsfield-soul-id/SKILL.md
```

Use only as a pattern for reusable stable asset references.

## Ordered production / checkpoint recovery

```text
external-reference/higgsfield-skills/higgsfield-video-explainer/SKILL.md
```

Use for:

```text
phase barriers
typed block pairing
assembly manifests
partial retry
```

Do not copy its Story grammar or 10-second block rule.

## Visual QA / surgical repair

```text
external-reference/higgsfield-skills/higgsfield-youtube-thumbnail/SKILL.md
external-reference/higgsfield-skills/higgsfield-youtube-thumbnail/references/thumbnail-frameworks.md
```

Use for:

```text
post-render visual inspection
truthfulness checks
variant review
targeted edits
```

---

# 9. Suggested adoption order

## Phase A — now

```text
Keep Higgsfield pinned as reference
Maintain this analysis document
Do not change REVIEW² runtime architecture yet
Continue Longform Story Research
```

## Phase B — when Production Architecture v1 begins

Design:

```text
Stage Contract
Capability Manifest
Approval / Lock State
Dependency Graph
Run Record
```

Then compare the design against Higgsfield Brandkit / Generate / Explainer patterns.

## Phase C — when implementation begins

Implement:

```text
Capability Router
Context Loader
Execution Compiler
Renderer/Provider adapters
Run Ledger
Targeted Recovery
```

## Phase D — before Prototype #001 becomes production-like

Add:

```text
behavior eval scenarios
regression rounds
CI cross-contract checks
stale dependency detection
approval invalidation tests
```

---

# 10. Provisional architecture decision

The current best interpretation is:

```text
Higgsfield does NOT give REVIEW² a better domain pipeline.

Higgsfield DOES provide strong reference patterns for the operating system
around that pipeline.
```

Therefore:

```text
REVIEW² Domain Architecture
= keep and deepen

Higgsfield-derived Control Plane patterns
= add later as orchestration infrastructure
```

Most promising concepts:

```text
1. Approval State
2. Dependency-aware Invalidation
3. Thin Stage Contracts + Lazy Context
4. Typed Stage Handoffs
5. Execution Compiler separation
6. Deterministic vs Generative execution policy
7. Targeted Repair
8. Behavioral Eval Harness
```

This document is a research blueprint, not a locked architecture decision. Final schemas and runtime modules should be designed only when their adjacent REVIEW² layers are mature enough to define stable contracts.
