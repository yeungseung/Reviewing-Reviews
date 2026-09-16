# REVIEW² Component Architecture v1

## 1. Purpose

Component Architecture의 목표는
AI가 매번 화면 디자인을 새로 만드는 것을 막고,
검증된 visual grammar를 선택해서 조립하도록 만드는 것이다.

```text
AI should choose a design.
AI should not invent a design every scene.
```

REVIEW²의 canonical unit은 raw HTML/React component가 아니라
**semantic contract를 가진 reusable visual unit**이다.

---

## 2. Core pipeline

```text
Finding / Story Beat
        ↓
     ScenePlan
        ↓
 Component Resolver
        ↓
  SceneResolution
        ↓
 Human Asset Gate
        ↓
   AssetBindings
        ↓
 Presentation Compiler
        ↓
     RenderPlan
        ↓
 Renderer Adapter
        ↓
 HyperFrames / Preview / Future Renderer
```

각 단계는 별도 파일/데이터 contract로 분리한다.

---

## 3. Four canonical artifacts

### 3.1 ScenePlan

스토리와 분석이 만드는 semantic scene.

ScenePlan에는 다음이 들어간다.

- scene type
- narrative purpose
- mechanic
- narration
- data
- evidence references
- asset requirements
- duration hint
- presentation constraints

들어가면 안 되는 것:

- x / y
- font size
- raw hex color
- arbitrary CSS
- raw animation code

### 3.2 SceneResolution

Component Resolver가 만든 presentation decision.

예:

```json
{
  "scene_id": "S14",
  "component": "conflict-split",
  "variant": "condition-aware",
  "theme": "KITCHEN",
  "motion_profile": "resolve"
}
```

이 단계는 아직 renderer-specific code가 아니다.

### 3.3 AssetBindings

Human Editorial Layer에서 확정한 실제 visual assets.

예:

```json
{
  "scene_id": "S14",
  "bindings": {
    "left_media": {
      "asset_id": "A034",
      "trim": {"in": 12.4, "out": 15.8},
      "fit": "contain"
    }
  },
  "status": "approved"
}
```

AI suggestion과 Human approval을 분리한다.

### 3.4 RenderPlan

모든 resolver가 끝난 machine execution artifact.

포함:

- resolved component version
- renderer
- resolved token values
- local asset paths
- timeline cues
- start / duration
- renderer variables
- source/evidence linkage
- git commit / build provenance

RenderPlan은 사람이 직접 작성하는 문서가 아니라 compiler output이다.

---

## 4. Component taxonomy

REVIEW²는 5단계로 나눈다.

### 4.1 Primitive

가장 작은 visual unit.

예:

- Text
- Number
- Icon
- Divider
- CardShell
- MediaFrame
- Chip
- Progress
- Bar
- Line
- Ring

Primitive는 story meaning을 모른다.

### 4.2 Pattern

여러 Primitive를 합친 반복 가능한 information unit.

예:

- MetricCard
- ReviewCard
- QuoteCard
- SourceBadge
- ComparisonBar
- SpecGrid
- ProductStage

Pattern은 한 가지 정보 표현 책임을 가진다.

### 4.3 Scene Block

독립된 scene grammar.

예:

- ProductHero
- ReviewWall
- ClaimCluster
- ConflictSplit
- ConditionSplit
- ExpertVsUser
- SpecVsReality
- PriceCompare
- Timeline
- BuyerFit
- FinalChecklist

Scene Block은 REVIEW²의 핵심 reusable unit이다.

HyperFrames 구현 시 기본적으로 **Block**으로 mapping한다.

### 4.4 FX Component

scene 안에서 재사용되는 motion / effect behavior.

예:

- count-up
- per-word-rise
- sweep-reveal
- card-accumulate
- highlight-pulse
- source-trace
- wipe-compare

HyperFrames 구현 시 기본적으로 **Component**로 mapping한다.

### 4.5 Vendor Source

third-party에서 가져온 source.

예:

- Magic UI
- Motion Primitives
- Cult UI
- React Bits
- HyperFrames catalog item

Vendor code를 REVIEW² core와 직접 섞지 않는다.

가능하면 wrapper / adapter를 통해 사용한다.

---

## 5. Component Contract

모든 Pattern / Scene Block / FX Component는 manifest를 가진다.

필수 contract:

```text
identity
lifecycle
selection
input
slots
layout
theme
motion
timing
dependencies
renderers
fallback
quality
provenance
```

### Identity

- name
- version
- kind
- title
- description
- category
- tags

### Lifecycle

Registry item은 구현 가능 여부를 명시한다.

```text
draft
→ 아이디어 / contract 미완성

specified
→ SPEC / schema / fixture 완료, 구현 전

implemented
→ 코드 구현 완료, validation 전

validated
→ schema / fixture / visual / deterministic test 통과

deprecated
→ 신규 사용 금지, migration 대상
```

Resolver는 기본적으로 `validated`만 production render 후보로 사용한다.

개발/preview 모드에서는 `implemented`를 opt-in으로 사용할 수 있다.

### Selection

- supported scene types
- supported mechanics
- use_when
- avoid_when
- hard constraints

### Input

각 component의 data props는 별도 JSON Schema로 검증한다.

### Slots

미디어/콘텐츠를 넣을 수 있는 named slot.

예:

```text
product_media
left_media
right_media
review_cards
source_label
chart
```

Slot은 asset을 선택하지 않는다.

필요한 역할만 선언한다.

### Layout

기존 LAYOUT_GRAMMAR의 ID를 참조한다.

예:

- full-focus
- hero-split
- equal-compare
- insight-evidence
- triple-compare

Component 내부에서 임의 grid system을 새로 만들지 않는다.

### Theme

raw color를 받지 않는다.

Theme Resolver를 통해 semantic token을 소비한다.

### Motion

motion code를 ScenePlan이 직접 전달하지 않는다.

component는 motion role을 선언한다.

예:

- reveal
- compare
- accumulate
- focus
- resolve
- exit

### Timing

각 scene block은 다음을 선언한다.

- minDuration
- idealDuration
- maxDuration
- elastic
- holdFinal

추가 시간이 생기면 animation을 느리게 늘이지 않고
가능하면 final hold로 사용한다.

### Dependencies

- primitives
- patterns
- fx
- vendor
- external packages

### Renderers

지원 renderer와 adapter를 선언한다.

### Fallback

component validation 실패 시 사용할 대체 component.

### Quality

- max item count
- max text length
- required evidence
- supported density
- asset requirements

### Provenance

- origin
- upstream
- license
- attribution
- adapted_from
- internal owner

---

## 6. Registry architecture

shadcn / HyperFrames와 비슷한 source registry 방식을 사용한다.

```text
components/
  registry.json

  primitives/
  patterns/
  scenes/
  fx/

  vendor/
```

각 reusable item:

```text
components/scenes/conflict-split/
  manifest.json
  props.schema.json
  SPEC.md
  examples/
    default.json
    long-ja.json
    dense.json
    no-media.json
  adapters/
    hyperframes.*
    preview.*
```

실제 implementation file은 Mac Studio 개발 단계에서 추가한다.

---

## 7. Registry item selection

AI가 component 이름을 직접 생성하지 않는다.

### Phase 0 — Lifecycle gate

Production mode:
- validated only

Development mode:
- validated
- implemented (explicit opt-in)

draft / specified는 선택 후보가 아니라 설계·개발 대상이다.

### Phase 1 — Hard filter

다음이 맞지 않으면 후보에서 제거한다.

- scene type
- mechanic
- renderer support
- item count
- evidence requirement
- asset requirement
- duration range

### Phase 2 — Avoid rules

`avoid_when` 조건과 충돌하면 reject.

### Phase 3 — Score

초기 v1 score:

```text
scene type match       35
mechanic match         25
data shape fit         15
asset compatibility    10
duration fit            5
density fit             5
category affinity       5
──────────────────────────
total                  100
```

### Phase 4 — Human / author override

ScenePlan에 명시적 preferred component가 있으면
validation을 통과하는 한 override한다.

### Phase 5 — Fallback

최종 binding 후 overflow / missing asset / invalid data가 발견되면
fallback chain을 사용한다.

---

## 8. Semantic mechanics

Scene type와 Component를 1:1로 고정하지 않는다.

Scene은 "무엇을 말하는가",
Mechanic은 "어떻게 이해시키는가"다.

초기 mechanic:

```text
introduce
focus
compare
accumulate
cluster
rank
show-proof
show-trend
show-distribution
reveal-conflict
resolve-conflict
show-condition
trace-origin
show-timeline
show-fit
summarize
```

예:

```text
scene type: review_conflict
mechanic: resolve-conflict
→ ConflictSplit

scene type: expert_test
mechanic: compare
→ ExpertVsUser or ComparisonBar
```

이 분리가 component library의 재사용성을 크게 높인다.

---

## 9. Theme ownership

ScenePlan은 theme name 정도만 요청할 수 있다.

예:

```text
TECH
KITCHEN
CLEANING
AIR_CARE
AUDIO
```

실제:

- colors
- radius
- material
- line style
- chart accent
- motion modifier

는 Theme Resolver가 결정한다.

Component 안에 category-specific hex를 하드코딩하지 않는다.

---

## 10. Motion ownership

Motion은 3층으로 나눈다.

### Core motion token

duration / easing / stagger.

### Component motion grammar

해당 component의 고정 choreography.

### Category modifier

TECH / KITCHEN / CLEANING 등의 personality.

Category modifier는 core timing을 크게 깨지 않는다.

---

## 11. Human Asset Gate

Component는 named slot과 requirement만 선언한다.

AI:
- candidate 찾기
- timestamp 후보
- source 연결
- quality metadata

Human:
- approve
- replace
- trim
- crop
- framing
- skip

최종 asset path는 RenderPlan 생성 직전에 resolve한다.

---

## 12. Renderer Adapter

Component semantic contract와 renderer implementation을 분리한다.

```text
Scene Block
    ↓
Renderer Adapter
    ├─ HyperFrames
    ├─ Preview
    └─ Future Renderer
```

### HyperFrames adapter

기본 mapping:

```text
REVIEW² Scene Block
→ HyperFrames Block

REVIEW² FX Component
→ HyperFrames Component
```

Renderer adapter가 담당:
- local source path
- HyperFrames registry dependencies
- data-variable-values
- slots
- start
- duration
- track index
- timeline cues

ScenePlan은 이를 모른다.

---

## 13. Deterministic rendering

같은 RenderPlan은 같은 결과를 내야 한다.

원칙:
- render 중 network fetch 금지
- current time 사용 금지
- unseeded randomness 금지
- 외부 asset은 미리 local staging
- component input은 JSON serializable
- canonical time unit은 seconds
- renderer가 필요하면 frames로 변환

---

## 14. Static-first implementation

새 Scene Block은 motion부터 만들지 않는다.

### Pass 1 — Hero frame
가장 중요한 hold frame을 먼저 구현한다.

### Pass 2 — Motion
hold frame이 승인된 뒤 choreography를 추가한다.

### Pass 3 — Seek / timing test
임의 frame에서도 deterministic한지 확인한다.

---

## 15. Fixtures and preview

각 component는 최소 fixture 4종을 갖는다.

```text
default
long-ja
dense
missing-optional
```

Preview renderer는 fixture를 이용해 정지 프레임 또는 짧은 loop를 만든다.

---

## 16. Test contract

### Schema test
manifest / props / ScenePlan validation.

### Layout test
safe area / overflow / minimum text size.

### Fixture test
default / stress fixture 렌더.

### Theme test
주요 category theme에서 깨지지 않는지.

### Determinism test
동일 input → 동일 frame.

### Fallback test
asset missing / data overflow 시 fallback 동작.

### Evidence test
source-required component가 source ref 없이 render되지 않음.

---

## 17. Versioning

세 종류의 버전을 분리한다.

```text
schema_version
component_version
design_system_version
```

RenderPlan에는 가능하면:
- component versions
- design token revision
- git commit SHA

를 기록한다.

---

## 18. Third-party source policy

Vendor code는 별도 provenance를 유지한다.

```text
components/vendor/<source>/<item>/
```

manifest에:
- upstream URL
- upstream commit/tag
- license
- adaptation notes

를 남긴다.

---

## 19. v1 component set

### Patterns
- MetricCard
- ReviewCard
- QuoteCard
- SourceBadge
- ComparisonBar
- SpecGrid
- ProductStage

### Scene Blocks
- ProductHero
- BigNumberFocus
- ReviewWall
- ClaimCluster
- ConflictSplit
- ConditionSplit
- ExpertVsUser
- SpecVsReality
- PriceCompare
- Timeline
- BuyerFit
- FinalChecklist

### FX

처음부터 전부 새로 만들지 않는다.

HyperFrames catalog / Motion Primitives / Magic UI 등을 먼저 검색하고,
REVIEW² motion grammar에 맞게 wrap한다.

---

## 20. Recommended implementation order

```text
01 schemas
02 registry
03 token/theme resolver interface
04 Primitive contracts
05 Pattern contracts
06 Scene Block manifests
07 preview renderer
08 HyperFrames adapter
09 fixtures + validation
10 Prototype #001
```

Prototype #001 이후 실제로 반복되는 component만 확장한다.

---

## 21. Anti-patterns

금지:

### Raw design instructions in ScenePlan
```json
{"x": 120, "fontSize": 74, "color": "#0047FF"}
```

### Giant god component
```text
UniversalReviewScene
with 47 flags
```

### Scene type = fixed visual
review_conflict가 항상 같은 화면일 필요는 없다.

### Asset auto-selection without human approval
final visual asset은 Human Gate를 통과한다.

### Renderer lock-in
HyperFrames는 v1 main renderer지만
semantic layer가 HyperFrames API 자체가 되어서는 안 된다.

---

## 22. Final architecture rule

```text
DATA decides what is true.
STORY decides what matters.
SCENE PLAN decides what must be understood.
COMPONENT decides how it is shown.
HUMAN decides what visual asset is actually used.
RENDERER decides how pixels are produced.
```

이 경계를 깨지 않는 것이 REVIEW² Component Architecture의 핵심이다.
