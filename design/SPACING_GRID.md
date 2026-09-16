# REVIEW² Spacing & Grid v1

## 1. Source philosophy

REVIEW²는 새로운 spacing 체계를 발명하지 않는다.

기본값은 Atlassian의 8px spacing system과 12-column grid를 참고하고,
IBM Carbon의 8px mini-unit 원칙을 함께 참고한다.

영상은 앱 화면보다 넓고 고정된 16:9 canvas를 사용하므로,
1080p master에 맞는 layout-only spacing을 추가한다.

---

## 2. Base unit

```text
Base unit = 8px
Micro unit = 4px
```

4px은 optical adjustment와 작은 glyph 내부 간격에만 사용한다.

가능하면 임의의 raw pixel 값을 만들지 않고 token을 사용한다.

---

## 3. Core spacing scale

```text
space.025   2px
space.050   4px
space.075   6px
space.100   8px
space.150  12px
space.200  16px
space.250  20px
space.300  24px
space.400  32px
space.500  40px
space.600  48px
space.800  64px
space.1000 80px
```

REVIEW² layout extension:

```text
layout.1200  96px
layout.1600 128px
layout.2000 160px
```

이 확장 값은 scene-level whitespace에만 사용한다.

---

## 4. Master canvas

Primary master:

```text
1920 × 1080
16:9
```

### Working safe area

```text
Horizontal outer margin: 96px
Vertical outer margin:   64px
```

중요 headline과 수치는 가능하면 이 안에 둔다.

더 강한 title-safe가 필요할 때:

```text
Horizontal: 128px
Vertical:    96px
```

---

## 5. Horizontal grid

```text
Columns: 12
Gutter: 24px
Outer margin: 96px
```

12 columns를 기본으로 하는 이유:

- 12
- 8 + 4
- 7 + 5
- 6 + 6
- 4 + 4 + 4
- 3 + 3 + 3 + 3

등 영상에서 자주 쓰는 분할을 쉽게 구성할 수 있다.

---

## 6. Grid rule

Grid에는 **top-level container만 맞춘다**.

예:
- Product hero
- Text block
- Chart
- Review wall
- Comparison panel
- Image/video frame

버튼, icon, chip, card 내부 요소는 column에 억지로 맞추지 않고
spacing token으로 정렬한다.

---

## 7. Vertical rhythm

기본 rhythm:

```text
Label → value           8~12px
Title → description    16~24px
Card internal groups   24~32px
Card → card            24~40px
Section group          48~64px
Major visual break     80~128px
```

화면의 중요도가 높을수록 주변 whitespace도 늘린다.

---

## 8. Density modes

### Focus
한 가지 정보에 집중.

- 큰 whitespace
- 1~2개의 주요 object
- 80~160px major spacing

### Standard
대부분의 설명 장면.

- 2~4개의 정보 group
- 24~64px spacing

### Dense
스펙표 / 비교표 / review cluster 등에서만 사용.

- 4~8px micro
- 12~24px internal
- 한 장면에서 오래 유지하지 않는다

---

## 9. Optical adjustment

8px grid는 기준이지 감옥이 아니다.

특히:
- 원형 icon
- 큰 숫자
- 일본어 glyph
- 제품 실루엣

등은 시각적 무게가 달라질 수 있으므로
2px / 4px 수준의 optical adjustment를 허용한다.

단, 구조적 layout은 grid를 유지한다.
