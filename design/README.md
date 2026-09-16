# REVIEW² Design System

이 폴더는 Reviewing Reviews 영상 생성 시스템의 시각 언어를 정의한다.

## Foundation

- [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) — 전체 철학 / 카테고리 시각 언어
- [REFERENCES.md](REFERENCES.md) — Apple / Atlassian / Carbon / Material 참고 기준
- [SPACING_GRID.md](SPACING_GRID.md) — 8px spacing / 12-column video grid
- [TYPOGRAPHY.md](TYPOGRAPHY.md) — Inter / Noto Sans JP / Pretendard
- [UI_PRIMITIVES.md](UI_PRIMITIVES.md) — icon / button / card / chip
- [MOTION.md](MOTION.md) — duration / easing / choreography

## Composition

- [LAYOUT_GRAMMAR.md](LAYOUT_GRAMMAR.md) — scene layout patterns
- [DATA_VISUALIZATION.md](DATA_VISUALIZATION.md) — chart rules + REVIEW² custom visualizations
- [ASSET_TREATMENT.md](ASSET_TREATMENT.md) — Human Editorial Layer / asset selection rules

## Tokens

- [color-tokens.json](color-tokens.json)
- [category-themes.json](category-themes.json)
- [ui-tokens.json](ui-tokens.json)
- [typography-tokens.json](typography-tokens.json)
- [spacing-tokens.json](spacing-tokens.json)
- [motion-tokens.json](motion-tokens.json)
- [data-viz-tokens.json](data-viz-tokens.json)

## v1 design formula

```text
Brand structure
+ Category familiarity
+ Quiet UI
+ Evidence-first data visualization
+ Controlled motion
+ Human visual judgment
= REVIEW²
```

## Automation boundary

AI는 asset을 찾고, 분류하고, 후보를 좁히고, scene 요구사항과 연결할 수 있다.

하지만 최종 clip / crop / framing / rhythm / visual emphasis는 사람이 결정한다.

```text
AI = assistant
Human = editor
```

## Status

v1은 Prototype 제작을 위한 기준안이다.

실제 영상 렌더링 이후 다음 값을 조정한다.

- spacing density
- typography scale
- category color saturation
- motion duration
- chart label size
- safe area
- card radius / padding
- human asset selection workflow
