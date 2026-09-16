# ConflictSplit — SPEC v0.1

## 1. Job

ConflictSplit의 역할은 **충돌을 해결하는 것**이 아니라
시청자가 "같은 제품인데 평가가 실제로 갈린다"는 사실을 한눈에 이해하게 만드는 것이다.

```text
ESTABLISH CONFLICT
not
RESOLVE CONFLICT
```

원인이 이미 충분히 밝혀졌다면 이 scene을 오래 쓰지 않고
다음 `ConditionSplit`으로 넘긴다.

---

## 2. Semantic contract

Input:

```text
one review topic
+ left position
+ right position
+ traceable evidence on both sides
```

Output:

```text
viewer understands:
"둘 다 실제로 존재하는 평가다"
```

이 component는 다음을 주장하지 않는다.

- 양쪽의 신뢰도가 동일하다
- 양쪽의 표본 수가 동일하다
- 50:50으로 의견이 갈린다
- 어느 쪽이 맞다

시각적 symmetry는 **논쟁의 존재**를 표현할 뿐,
통계적 동등성을 의미하지 않는다.

---

## 3. Default composition

Layout grammar:

```text
Equal Compare 6 + 6
```

Screen:

```text
┌──────────────────────────────────────────────────────────┐
│                 HEADLINE / TOPIC                         │
│                                                          │
│   LEFT POSITION             │      RIGHT POSITION        │
│   short summary             │      short summary         │
│                             │                            │
│   [review card]             │      [review card]         │
│   [optional metric]         │      [optional metric]     │
│                             │                            │
│          source tier        │      source tier           │
│                                                          │
│                optional neutral takeaway                 │
└──────────────────────────────────────────────────────────┘
```

The center divider uses semantic `conflict` styling,
but the two sides do NOT default to green/red.

Reason:
positive/negative color would imply a verdict.

---

## 4. Variants

### balanced

Default.

Both sides use equal visual weight.

Use when:
- quotes are the primary evidence
- metrics are missing or not directly comparable

### metric-led

A defensible metric exists on both sides.

Use when:
- same basis
- same unit
- comparison is meaningful

Never show two metrics as comparable if their basis differs.

### quote-led

One short quote on each side is the focal point.

Use when:
- qualitative language itself explains the disagreement
- the quotes are concise and source-traceable

---

## 5. Evidence rules

At least one evidence item per side.

Maximum visible:
- 2 evidence cards per side in standard mode
- 1 per side in focus mode

A third evidence item may exist in data but should not normally be displayed simultaneously.

Every visible quote keeps:
- source_id
- source_tier

Source label may be visually shortened,
but source_id remains in project data.

---

## 6. Metrics

Metric is optional.

Allowed:
- count
- share
- score
- measurement

### count

Example:
`217 mentions`

Must not be converted to a percentage without denominator.

### share

Requires a defensible denominator.

The `basis` field should state what the share is based on.

### score

Use only when both sides are genuinely the same scoring construct.

### measurement

Use for controlled measured values.

If the metric becomes the actual story,
the resolver should consider `comparison-bar` or `expert-vs-user` instead.

---

## 7. Asset slots

Optional:

```text
left_media
right_media
```

These are evidence slots, not decorative slots.

Examples:
- two different usage environments
- two screenshots
- two short product-use clips

If no useful media exists,
ConflictSplit must remain fully functional as text/data-only.

This is intentional.

---

## 8. Human Asset Gate

AI can propose:

- source candidate
- timestamp
- quality
- left/right relevance

Human decides:

- whether media adds understanding
- final clip
- trim
- crop
- framing

If media creates false equivalence or distracts from evidence,
leave the slots empty.

---

## 9. Motion grammar

Default profile: `conflict-separate`

Recommended choreography:

```text
0. headline establishes topic
1. evidence cards enter near the shared center
2. cards separate left/right
3. labels and metrics settle
4. center divider / conflict cue appears
5. source badges resolve
6. HOLD
```

The motion should communicate:

```text
same topic
→ different experiences
```

Avoid:
- aggressive collision
- red vs green combat framing
- bouncing
- excessive 3D tilt
- winner/loser motion

---

## 10. HyperFrames reuse strategy

Do not hand-build every visual mechanic from zero.

Useful upstream references:

### testimonial-proof-card
Use as structural reference for:
- quote wrapping
- attribution
- restrained reveal
- hold behavior

### comparison-split blueprint
Use as structural reference for:
- two equal sides
- mirrored entrance logic

### split-tilt-cards
Use only as a motion reference.
REVIEW² default should reduce/remove the theatrical 3D tilt.

The semantic behavior and evidence constraints remain REVIEW²-owned.

---

## 11. Timing

```text
min     4.5s
ideal   6.5s
max     9.0s
```

Extra duration becomes HOLD.

Do not slow the entry sequence merely because narration is longer.

If narration cannot be read within max duration:
- shorten visible text without altering narration
- split to next scene
- or choose another component

---

## 12. Fallback

### comparison-bar

Use if:
- quotes are weak
- the conflict is actually numeric comparison

### quote-card

Use if:
- only one side has sufficiently strong evidence
- the scene should not visually imply two-sided balance

### condition-split

Not technically a fallback.
It is a semantic upgrade when the cause of disagreement is known.

---

## 13. Acceptance criteria

ConflictSplit passes when:

- one topic only
- both sides have traceable evidence
- no statistical equivalence is implied accidentally
- Japanese text remains readable at 1080p
- no content crosses safe area
- no essential evidence is cropped
- theme changes do not change semantic meaning
- same input produces deterministic hold frame
