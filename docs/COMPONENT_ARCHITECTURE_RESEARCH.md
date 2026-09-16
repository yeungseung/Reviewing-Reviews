# REVIEW² Component Architecture Research

Research date: 2026-09-16

## 1. Goal

REVIEW²의 Component Architecture를 처음부터 독자적으로 발명하지 않는다.

이미 검증된 component registry / composition / video rendering 구조를 조사하고,
우리의 목적에 맞는 부분만 조합한다.

---

## 2. Reference systems

### HyperFrames

가장 직접적으로 참고할 대상.

현재 HyperFrames registry는 크게 다음을 분리한다.

- Block: standalone sub-composition
- Component: host composition에 삽입되는 effect / snippet

Block은 자체 dimensions / duration / timeline을 가진다.
Component는 host의 dimensions / duration을 상속한다.

또한 registry item은 다음과 같은 metadata를 가진다.

- name
- type
- title
- description
- tags
- license
- registryDependencies
- files
- preview
- dimensions / duration where applicable

HyperFrames catalog에는 실제 선택을 돕기 위한 다음 개념도 존재한다.

- use_when
- avoid_when
- pairs_with
- variables
- slots
- cues
- final-frame hold
- elastic duration

### shadcn/ui

핵심 참고점:

- compiled black-box package보다 source registry
- registry item metadata
- dependencies / registryDependencies
- files
- registry include
- copied source ownership

REVIEW²는 Mac Studio + Codex가 실제 구현을 수정하는 구조이므로
source registry 방식이 매우 잘 맞는다.

### Magic UI

Magic UI는 component source와 registry artifact를 분리하고
registry build step을 둔다.

참고점:

- authored source
- generated registry
- registry validation
- installable component source

### Motion Primitives

core component source와 registry generation script가 분리되어 있다.

참고점:

- small reusable motion primitives
- source first
- registry metadata generated separately
- motion behavior와 demo/documentation 분리

### Cult UI

registry schema에서 다음을 명확히 분리한다.

- ui
- component
- example
- block
- lib
- hook
- page
- theme
- style

또한 category / subcategory / chunks / dependency를 metadata로 가진다.

REVIEW²에서는 모든 종류를 그대로 가져오지 않고,
video system에 필요한 taxonomy만 사용한다.

### components.build

핵심 원칙:

- Composition over Configuration
- 큰 component 하나에 수십 개의 option을 넣기보다 작은 책임으로 분리
- clear API
- slot / sub-component composition
- design token 기반 styling

### Storybook

Args는 component state를 JSON-serializable object로 표현한다.

REVIEW²에서는 Storybook 자체가 필수는 아니지만,
각 component에 다음 fixture를 두는 방식을 채택한다.

- default
- long Japanese text
- dense data
- missing optional asset
- category theme variations

즉 "component + fixture"를 반복 가능한 preview 단위로 사용한다.

### Design Tokens Community Group

DTCG 2025.10 stable format을 장기적인 token interoperability 기준으로 참고한다.

현재 REVIEW² v1 token JSON은 유지하되,
향후 token compiler가 DTCG-compatible source를 읽을 수 있도록 resolver boundary를 둔다.

### Remotion

REVIEW²의 main renderer는 HyperFrames지만,
Remotion의 다음 설계 원칙은 참고 가치가 있다.

- composition은 typed props를 받는다
- render input은 serializable data여야 한다
- schema를 통해 visual editing / validation이 가능하다
- composition과 timeline sequence가 분리된다

따라서 REVIEW²도 renderer에 함수를 넘기는 방식이 아니라
JSON-serializable contract를 canonical input으로 사용한다.

---

## 3. Adopted conclusions

### A. Registry-first

Component는 folder convention만으로 발견하지 않는다.

각 component에 machine-readable manifest를 둔다.

### B. Semantic scene and render implementation are separate

Story/analysis 단계는 x/y/font/color를 알지 않는다.

```text
ScenePlan
→ Component Resolution
→ Asset Binding
→ RenderPlan
```

으로 분리한다.

### C. HyperFrames vocabulary와 충돌하지 않게 taxonomy를 맞춘다

REVIEW²:

- Primitive
- Pattern
- Scene Block
- FX Component
- Vendor Source

HyperFrames mapping:

- Scene Block → HyperFrames Block
- FX Component → HyperFrames Component

### D. use_when / avoid_when

AI가 component 이름을 감으로 고르지 않는다.

모든 reusable scene은:
- 무엇을 위해 존재하는가
- 언제 써야 하는가
- 언제 쓰면 안 되는가
- 어떤 data shape가 필요한가

를 manifest에 기록한다.

### E. Copy source, not dependency lock-in

REVIEW²의 실제 개발은 local Mac Studio에서 Codex가 수행한다.

따라서 third-party UI는 가능하면 source를 가져와
REVIEW² token / motion / renderer contract에 맞게 normalize한다.

### F. Human visual judgment remains authoritative

Asset selection / trim / crop / framing은
Component Architecture가 자동으로 결정하지 않는다.

Component는 필요한 slot만 선언한다.

---

## 4. REVIEW² architecture formula

```text
shadcn-style source registry
+ HyperFrames block/component model
+ components.build composition rules
+ Storybook-like fixtures
+ JSON Schema contracts
+ DTCG-compatible token boundary
+ Human editorial asset gate
= REVIEW² Component Architecture v1
```
