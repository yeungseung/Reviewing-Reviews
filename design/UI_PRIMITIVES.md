# REVIEW² UI Primitives v0.1

## 1. Reference direction

Reviewing Reviews의 버튼, 아이콘, 카드, 토글, 배지 등 UI 요소는
Apple 계열 인터페이스가 잘하는 다음 원칙을 참고한다.

목표는 Apple UI를 복제하는 것이 아니라,
**정돈된 위계 / 높은 가독성 / 절제된 시각 노이즈 / 자연스러운 인터랙션**을 가져오는 것이다.

---

## 2. Core principles

### Restraint
장식보다 정보가 먼저 보인다.

- 불필요한 테두리 제거
- 한 화면에 강조색 남발 금지
- 그림자 최소화
- 버튼은 필요한 순간에만 존재
- 아이콘은 가능한 한 단일 의미

### Hierarchy
크기, 굵기, 명도, 여백으로 우선순위를 만든다.

- Primary action은 한 화면에 1개
- Secondary action은 시각적으로 한 단계 낮게
- Tertiary action은 text/icon 중심
- 위험/경고는 semantic color로만 강조

### Consistency
같은 의미는 항상 같은 형태와 움직임을 사용한다.

---

## 3. Icon language

### Shape
- 단순한 선형 아이콘 우선
- stroke 굵기 통일
- 가능한 한 24x24 기반
- 작은 크기에서 알아볼 수 있어야 함
- 디테일보다 실루엣 우선

### Stroke
- Default: 1.75px
- Emphasis: 2px
- Hairline 사용 금지

### Corner / Cap
- round cap
- round join
- 급격한 각보다 부드러운 연결

### Usage
아이콘 단독으로 의미가 불명확하면 반드시 라벨과 함께 사용한다.

### Avoid
- 서로 다른 아이콘 스타일 혼합
- filled / outline 무작위 혼용
- 장식용 아이콘 남발
- 제품 카테고리를 너무 직접적으로 묘사하는 픽토그램 남발

---

## 4. Buttons

### Primary
가장 중요한 행동 하나.

- 높은 대비
- category accent 사용 가능
- radius: 14~18px
- 높이: 44~52px
- padding-x: 18~24px
- font-weight: 600

### Secondary
- surface 계열
- 얇은 border 또는 tonal fill
- Primary보다 대비를 낮춘다

### Ghost
- 투명 배경
- 텍스트 또는 아이콘 중심
- hover/focus에서만 surface 표시

### Icon Button
- 최소 터치 영역 44x44
- 실제 glyph 크기 18~22px
- 원형 또는 rounded square

---

## 5. Cards

카드는 화면을 나누기 위한 박스가 아니라
관련 정보를 하나의 단위로 묶기 위해 사용한다.

### Default
- radius: 20px
- padding: 20~28px
- border: 1px / low contrast
- shadow: 거의 사용하지 않음

### Elevated
필요한 경우에만 한 단계 밝은 surface 사용.

### Category card
카테고리별 geometry token을 적용할 수 있다.

예:
- TECH: radius 10~14px
- KITCHEN: radius 22~28px
- CLEANING: radius 18~24px
- BEAUTY: radius 24~32px

브랜드 shell 안에서만 변주한다.

---

## 6. Pills / Chips

용도:
- Source type
- Product attribute
- Filter
- Category
- Review sentiment

규칙:
- 너무 많은 색 사용 금지
- 최대 1개의 강조색
- 나머지는 neutral surface
- height: 28~34px
- radius: full

---

## 7. Typography behavior

버튼과 UI 라벨은 최대한 짧게 쓴다.

좋음:
- Compare
- Reviews
- Specs
- Sources
- Details

피함:
- Click here to see detailed specifications
- View all of the available customer reviews

영상 UI에서는 정보 전달 속도가 우선이다.

---

## 8. Motion

모션은 존재감을 과시하기보다
**상태 변화가 자연스럽게 이해되게 하는 역할**을 한다.

### Default
- 160~260ms
- ease-out

### Large transition
- 300~450ms
- spring 또는 smooth ease

### Avoid
- bounce 남발
- 과한 elastic
- 의미 없는 회전
- 긴 fade
- 같은 장면에서 서로 다른 easing 혼용

---

## 9. Interaction visual grammar

### Hover
- 명도 변화 4~8%
- scale 변화는 최대 1~2%

### Press
- scale 0.97~0.99
- 짧은 opacity 변화 가능

### Focus
- 명확한 outline
- category accent 또는 accessibility token 사용

---

## 10. Apple-like reference, not Apple clone

다음은 금지한다.

- Apple UI 화면을 그대로 복제
- Apple 고유 아이콘 자산을 무단으로 전용
- Apple 제품 페이지와 동일한 컴포넌트 구성 재현
- 특정 OS UI를 그대로 모사

우리가 가져오는 것은 자산이 아니라 원칙이다.

```text
clarity
hierarchy
spacing
consistency
restraint
natural motion
```

이 여섯 가지를 Reviewing Reviews의 공통 UI 문법으로 사용한다.
