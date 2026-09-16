# ConflictSplit Architecture Dry Run

## Scenario

Story finding:

```text
Some users describe the product as quiet.
Others describe the same product as distracting at night.
The cause has not yet been established in this scene.
```

Expected semantic scene:

```text
type: review_conflict
mechanic: reveal-conflict
```

---

## 1. ScenePlan

```json
{
  "schema_version": "1.0.0",
  "scene_id": "S14",
  "type": "review_conflict",
  "intent": {
    "mechanic": "reveal-conflict",
    "importance": "high",
    "density": "standard"
  },
  "duration_hint": 6.5,
  "narration": "ところが 音についての評価はきれいに二つに分かれました",
  "data": {
    "headline": "同じ製品なのに 音の評価が真っ二つでした",
    "topic": "運転音",
    "left": {
      "label": "気にならない",
      "summary": "リビングでは十分静かという声",
      "evidence": [
        {
          "text": "テレビを見ていてもほとんど気になりません",
          "source_id": "S_USER_014",
          "source_tier": "user"
        }
      ]
    },
    "right": {
      "label": "気になる",
      "summary": "寝室では低い音が気になるという声",
      "evidence": [
        {
          "text": "夜は低いモーター音が思ったより耳に残ります",
          "source_id": "S_USER_031",
          "source_tier": "user"
        }
      ]
    }
  },
  "finding_ids": ["F018"],
  "claim_ids": ["C114", "C172"],
  "source_ids": ["S_USER_014", "S_USER_031"],
  "asset_requirements": [],
  "presentation_constraints": {
    "preferred_component": null,
    "forbidden_components": [],
    "preferred_theme": "AIR_CARE"
  },
  "human_notes": ""
}
```

Result:
PASS.

No visual coordinates or renderer code leaked into ScenePlan.

---

## 2. Resolver

Hard filter:

```text
scene type     review_conflict     PASS
mechanic       reveal-conflict     PASS
evidence       both sides present  PASS
density        standard            PASS
duration       6.5s                PASS
assets         no required media   PASS
```

Candidate score:

```text
scene type match        35/35
mechanic match          25/25
data shape fit          15/15
asset compatibility     10/10
duration fit             5/5
density fit              5/5
category affinity        5/5
────────────────────────────
TOTAL                  100/100
```

Resolution:

```json
{
  "schema_version": "1.0.0",
  "scene_id": "S14",
  "component": "conflict-split",
  "component_version": "0.1.0",
  "variant": "balanced",
  "theme": "AIR_CARE",
  "motion_profile": "conflict-separate",
  "score": 100,
  "reason": [
    "exact scene type match",
    "exact mechanic match",
    "both sides contain traceable evidence",
    "no required media slots"
  ],
  "fallback_chain": ["comparison-bar", "quote-card"],
  "status": "validated"
}
```

Result:
PASS.

---

## 3. Human Asset Gate

No media is required.

```json
{
  "schema_version": "1.0.0",
  "scene_id": "S14",
  "status": "approved",
  "bindings": {},
  "approved_by": "human-editor"
}
```

Result:
PASS.

Important finding:
Human Asset Gate can legitimately approve an empty binding.
This proves the architecture does not force decorative media into evidence scenes.

---

## 4. Presentation Compiler

Compiler responsibilities:

- validate props against props.schema.json
- resolve AIR_CARE theme tokens
- resolve typography / spacing
- resolve motion profile
- convert source tier to SourceBadge
- build HyperFrames variables
- assign start/duration/track

The compiler does NOT rewrite story evidence.

Result:
PASS.

---

## 5. RenderPlan

Expected shape:

```json
{
  "schema_version": "1.0.0",
  "renderer": "hyperframes",
  "canvas": {
    "width": 1920,
    "height": 1080
  },
  "fps": 30,
  "scenes": [
    {
      "scene_id": "S14",
      "component": "conflict-split",
      "component_version": "0.1.0",
      "adapter": "components/scenes/conflict-split/adapters/hyperframes",
      "start": 41.2,
      "duration": 6.5,
      "track": 1,
      "variables": {},
      "assets": {},
      "cues": [0.6, 1.3, 2.0, 2.7, 3.1],
      "source_ids": ["S_USER_014", "S_USER_031"]
    }
  ],
  "provenance": {
    "git_commit": "<resolved-at-build>",
    "design_system_version": "v1",
    "token_revision": "<resolved-at-build>"
  }
}
```

Result:
PASS.

---

# Stress tests

## Long Japanese copy

Fixture:
`long-ja.json`

Risk:
quote card height and line wrapping.

Expected response:
- reduce visible evidence count before reducing font below minimum
- switch to quote-led variant
- if still overflow: split scene

PASS as architecture:
the component has a defined failure strategy.

## Dense evidence

Fixture:
`dense.json`

Risk:
three evidence items on each side create dashboard-like clutter.

Expected response:
- data may contain 3 items
- visible scene uses max 2 per side
- remaining evidence contributes to metric/context but is not simultaneously displayed

PASS.

## No media

Fixture:
`no-media.json`

Expected:
layout remains intentional,
not empty.

PASS.

## Known cause of conflict

Input:
```text
living room users are positive
bedside users are negative
cause is already strongly evidenced
```

Resolver result:
REJECT ConflictSplit via `avoid_when`.
Prefer `ConditionSplit`.

PASS.

## Weak right-side evidence

Input:
left = 18 independent claims
right = 1 ambiguous comment

Resolver result:
REJECT because evidence does not deserve balanced conflict framing.

Fallback:
QuoteCard or another asymmetric evidence scene.

PASS.

---

# Architecture findings

## Finding 1 — taxonomy works

Primitive → Pattern → Scene Block → FX maps cleanly to the real ConflictSplit need.

## Finding 2 — Scene / Mechanic separation is necessary

`review_conflict` alone is not enough.

When the cause is known,
same story domain should resolve to ConditionSplit instead.

## Finding 3 — optional Human Asset Gate works

AssetBindings can be empty and still approved.

This is important for evidence-first scenes.

## Finding 4 — visual symmetry needs semantic guardrails

Equal 6+6 layout can accidentally imply 50:50 evidence.

Therefore the SPEC explicitly states:
symmetry = two positions exist,
not equal prevalence or credibility.

## Finding 5 — upstream reuse is viable

HyperFrames already has testimonial and comparison mechanics.

REVIEW² should own:
- evidence semantics
- source traceability
- resolver rules

and reuse/adapt:
- quote rendering
- split staging
- timing mechanics

## Finding 6 — one schema improvement is needed

Current component manifest has no lifecycle field.

Recommended addition:

```text
status:
draft
specified
implemented
validated
deprecated
```

Without this,
a registry cannot distinguish a spec-only component from production-ready code.

---

# Verdict

Architecture is implementable without forcing renderer details into semantic data.

No structural redesign is required after this dry run.

One immediate schema change is recommended:
**component lifecycle status**.

Next useful validation target:
`ConditionSplit`

Why:
it tests whether one scene can consume the output of conflict analysis
and whether semantic routing between two similar components remains clean.
