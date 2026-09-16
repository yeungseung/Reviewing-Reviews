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

Result: PASS.

No visual coordinates or renderer code leak into ScenePlan.

The semantic payload is sufficient to route the scene.

---

## 2. Resolver

Hard-filter result:

```text
scene type     review_conflict     PASS
mechanic       reveal-conflict     PASS
evidence       both sides present  PASS
density        standard            PASS
duration       6.5s                PASS
assets         no required media   PASS
```

ConflictSplit is a valid semantic match.

Important:
the component lifecycle is currently `specified`,
so it is a development target, not a production-render candidate.

---

## 3. Human Asset Gate

Media slots are optional.

A valid approval may contain:

```json
{
  "schema_version": "1.0.0",
  "scene_id": "S14",
  "status": "approved",
  "bindings": {},
  "approved_by": "human-editor"
}
```

Result: PASS.

The architecture does not force decorative media into evidence scenes.

---

## 4. Presentation Compiler

Compiler responsibilities:

- validate props
- resolve category theme
- resolve typography / spacing
- resolve motion profile
- map source tier to source badge
- assign render variables / timing

The compiler does not rewrite story evidence.

Result: PASS.

---

## 5. RenderPlan

The semantic contract maps cleanly to a renderer execution plan.

Result: PASS.

---

# Fixture stress tests

## default.json

Balanced qualitative conflict.

PASS.

## long-ja.json

Tests long Japanese wrapping and mixed expert/user evidence.

Expected fallback behavior:
- reduce simultaneously visible evidence count
- prefer quote-led layout
- split scene before violating minimum text size

PASS at contract level.

## dense.json

Three evidence items per side plus metrics.

Expected behavior:
- input may retain three items
- visible frame normally shows at most two per side
- remaining evidence supports context rather than becoming dashboard clutter

PASS.

## no-media.json

No visual asset supplied.

Expected:
layout remains complete and intentional.

PASS.

---

# Machine contract validation

2026-09-16 validation pass:

```text
Contract checks   94 PASS
Errors             0
Warnings           1
Fixtures           4
```

Warning:

```text
specified component has unresolved internal dependencies:
text
number
divider
media-frame
review-card
source-badge
```

This warning is expected because ConflictSplit is currently a specification,
not an implemented production component.

---

# Architecture findings

## Finding 1 — taxonomy works

Primitive → Pattern → Scene Block → FX maps cleanly to the real ConflictSplit requirement.

## Finding 2 — Scene / Mechanic separation is necessary

`review_conflict` alone is insufficient.

When the cause is already known,
the resolver should route to `ConditionSplit`.

## Finding 3 — Human Asset Gate can be empty

This is useful and intentional.

Evidence scenes do not require visual filler.

## Finding 4 — visual symmetry needs a semantic guardrail

Equal 6+6 columns can accidentally look like statistical 50:50.

Rule:

```text
visual symmetry
= both positions deserve representation

NOT
= equal frequency
= equal credibility
= equal sample size
```

## Finding 5 — upstream reuse is viable

HyperFrames already provides useful quote/comparison mechanics.

REVIEW² owns:
- evidence semantics
- source traceability
- selection rules
- visual meaning

Existing libraries may provide:
- quote rendering mechanics
- entry motion
- split staging
- typography effects

## Finding 6 — lifecycle status was required

Added:

```text
draft
specified
implemented
validated
deprecated
```

Production resolver uses `validated` components only.

## Finding 7 — dependency and provenance must remain separate

A runtime/build dependency is not the same as a design reference.

Therefore:

```text
dependencies
= code/build items actually required

provenance / adapted_from
= reference, inspiration, copied/adapted origin
```

For ConflictSplit,
HyperFrames comparison/testimonial patterns are currently provenance references,
not declared runtime dependencies.

## Finding 8 — dependency maturity needs a gate

Recommended rule:

```text
draft / specified
→ unresolved internal dependencies allowed

implemented
→ every required internal dependency must exist and be at least implemented

validated
→ every required internal dependency must be validated

deprecated
→ may depend on deprecated items only for legacy reproducibility
```

Cycles in required internal dependencies are forbidden.

---

# Verdict

No fundamental redesign was required.

The architecture successfully separates:

```text
semantic story
component selection
human asset judgment
presentation compile
renderer execution
```

The first real component test produced two useful architecture improvements:

1. component lifecycle state
2. dependency-vs-provenance separation + dependency maturity gate

ConflictSplit remains:

```text
status: specified
```

until code, static preview, motion, deterministic rendering and visual QA are completed.

Next high-value architecture test:
`ConditionSplit`.
