# ConflictSplit → HyperFrames Adapter Contract

## Mapping

```text
REVIEW² kind: review2:scene
HyperFrames target: block / standalone sub-composition
```

The adapter should produce one 1920×1080 composition.

## Upstream reuse candidates

### testimonial-proof-card

Potential reuse:
- quote card internals
- reading-paced reveal
- attribution line
- hold behavior

Do not inherit:
- marketing testimonial semantics
- star ratings
- promotional emphasis assumptions

### comparison-split blueprint

Potential reuse:
- equal two-column staging
- mirrored entrance
- central relationship

### split-tilt-cards rule

Potential reuse:
- side-aware entry direction

Default REVIEW² adaptation:
- remove or greatly reduce 3D tilt
- no continuous floating
- settle to a still evidence frame

---

## Renderer variables

The adapter converts canonical props into renderer-safe values.

Suggested variable groups:

```text
content.*
left.*
right.*
theme.*
timing.*
slots.*
```

Do not expose raw x/y/font size through ScenePlan.

---

## Timeline

Default normalized timeline for ideal 6.5s:

```text
0.00–0.60  headline
0.45–1.30  shared-center evidence entry
1.05–2.00  left/right separation
1.70–2.40  labels + optional metrics
2.15–2.70  center conflict marker
2.40–3.10  source badges
3.10–6.50  hold / narration finish
```

For a shorter scene:
compress entrance modestly.

For a longer scene:
extend hold first.

Never time-stretch all animation proportionally.

---

## Slots

Optional:
- left_media
- right_media

If present:
- evidence media uses contain unless human-approved crop says otherwise
- readable screenshots should preserve source aspect ratio
- media must not obscure source identity

If absent:
- redistribute space to quote/evidence cards
- no placeholder should appear

---

## Determinism

Adapter must not use:
- network fetch during render
- current time
- unseeded randomness

If subtle card variation is used,
seed it with scene_id.

---

## Output validation

Reject render if:
- either side has zero evidence
- quote overflow remains after layout fallback
- a share metric has no basis
- source-required evidence lacks source_id
- final human-required asset binding is pending for a required slot
