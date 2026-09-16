# REVIEW² Visual Design System v0.1

## 1. Goal

시청자가 제품명을 읽기 전에 영상의 색, 형태, 움직임만 보고도
대략적인 제품군과 사용 맥락을 직감할 수 있게 한다.

예:

- 밥솥 → 따뜻함 / 주방 / 김 / 둥근 형태
- 청소기 → 청결 / 회전 / 스캔 / 먼지 제거
- PC → 정밀 / 차가움 / 그리드 / 빠른 반응
- 오디오 → 몰입 / 파형 / 어두운 공간 / 리듬

중요한 원칙은 **브랜드 아이덴티티는 고정하고, 제품 카테고리의 친숙함은 변주한다**는 것이다.

---

## 2. Theme hierarchy

디자인은 다음 5단계로 상속된다.

```text
Brand Base
  ↓
Domain
  ↓
Category
  ↓
Product Cue
  ↓
Semantic State
```

### Brand Base
모든 영상에 공통
- Black / Graphite base
- 같은 타이포
- 같은 카드 구조
- 같은 정보 계층
- 같은 전환 문법

### Domain
큰 산업군
- TECH
- HOME
- KITCHEN
- FOOD
- BEAUTY
- FASHION
- SPORT
- WELLNESS
- ENTERTAINMENT

### Category
구체적인 사용 맥락
- COMPUTING
- MOBILE
- AUDIO
- KITCHEN_APPLIANCE
- CLEANING
- LAUNDRY
- AIR_CARE
- COOKWARE
- BEAUTY_DEVICE
- OUTDOOR

### Product Cue
제품 단위의 친숙한 인상
- RICE_COOKER
- ROBOT_VACUUM
- STICK_VACUUM
- AIR_PURIFIER
- WASHING_MACHINE
- LAPTOP
- HEADPHONE
- CAMERA

### Semantic State
정보 의미
- positive
- negative
- warning
- conflict
- official
- expert
- user

---

## 3. Brand shell

기본 프레임은 항상 동일하다.

```text
background        #090909
surface           #171717
surfaceRaised     #242424
textPrimary       #F5F5F2
textSecondary     #A8A8A3
divider           #343434
```

이 레이어가 모든 영상의 REVIEW² 정체성을 유지한다.

---

## 4. Product feel is more than color

카테고리 친숙함은 다음 여섯 요소의 조합으로 만든다.

1. Color
2. Geometry
3. Motion
4. Material / texture
5. Data visualization style
6. Ambient cue

색 하나만으로 제품군을 표현하지 않는다.

---

## 5. Category language examples

### TECH / COMPUTING

**Feeling**
정밀함, 속도, 기술, 논리

**Color**
Cobalt / Off White / Graphite

**Geometry**
- 직선
- 얇은 그리드
- 정렬된 모듈
- 4~8px radius

**Motion**
- 짧고 빠른 이동
- snap
- scan
- panel docking

**Data**
- line chart
- spec matrix
- benchmark bar

**Ambient**
- grid
- cursor-like markers
- tiny technical labels

---

### KITCHEN / RICE COOKER

**Feeling**
따뜻함, 생활, 음식, 포근함

**Color**
Terracotta / Cream / Warm Gray

**Geometry**
- 둥근 카드
- 원형 게이지
- 큰 곡률
- 부드러운 캡슐

**Motion**
- 위로 퍼지는 흐름
- 부드러운 easing
- 증기처럼 올라오는 reveal
- 천천히 차오르는 gauge

**Data**
- cooking-time ring
- heat distribution
- texture comparison
- taste / convenience matrix

**Ambient**
- steam arc
- soft grain
- subtle warm glow

---

### HOME / CLEANING

**Feeling**
청결, 정리, 제거, 시원함

**Color**
Aqua Teal / Mist White / Cool Gray

**Geometry**
- 원형 sweep
- clean edges
- radial layouts
- 넓은 여백

**Motion**
- 좌우 wipe
- circular sweep
- dust particle disappearing
- before → after clean transition

**Data**
- coverage map
- dirt-removal percentage
- path trace
- suction comparison

**Ambient**
- sparkle
- airflow / suction lines
- clean scan

---

### HOME / AIR CARE

**Feeling**
공기, 호흡, 조용함, 투명함

**Color**
Ice Blue / Teal / Soft White

**Geometry**
- 얇은 곡선
- 투명 레이어
- 넓은 원형 공간

**Motion**
- breathing pulse
- floating particles
- airflow stream
- slow transparency fade

**Data**
- AQI ring
- particle density
- noise chart
- room coverage

---

### HOME / LAUNDRY

**Feeling**
회전, 섬유, 깨끗함, 반복

**Color**
Powder Blue / Soft Mint / White

**Geometry**
- circular drum motif
- soft folds
- rounded squares

**Motion**
- rotation
- tumble
- wave
- fabric-like fold transition

**Data**
- cycle time
- energy/water usage
- fabric care matrix

---

### ENTERTAINMENT / AUDIO

**Feeling**
몰입, 리듬, 공간, 감정

**Color**
Deep Violet / Acid Lime / Black

**Geometry**
- waveform
- arcs
- concentric circles
- dark large surfaces

**Motion**
- beat-reactive pulse
- waveform growth
- spatial expansion

**Data**
- frequency response
- ANC comparison
- battery timeline
- codec / feature matrix

---

## 6. Semantic colors are separate

카테고리 분위기 색과 정보 의미 색은 절대 혼합하지 않는다.

```text
positive   #52C878
negative   #FF5C5C
warning    #F5B942
conflict   #8E6CFF
official   #4F8CFF
expert     #45C6D8
user       #D8D8D8
```

예:
밥솥 영상의 메인 컬러가 Terracotta여도
실제 사용자 불만 그래프는 negative red를 사용한다.

---

## 7. Theme resolver

영상 생성 엔진은 제품 메타데이터에서 Theme을 결정한다.

예:

```yaml
product:
  category: KITCHEN_APPLIANCE
  cue: RICE_COOKER
  positioning: PREMIUM
```

Resolver result:

```json
{
  "brand": "review2",
  "domain": "KITCHEN",
  "category": "KITCHEN_APPLIANCE",
  "cue": "RICE_COOKER",
  "positioning": "PREMIUM",
  "palette": "kitchen-warm-premium",
  "geometry": "rounded",
  "motion": "soft-rise",
  "ambient": ["steam", "warm-glow"]
}
```

---

## 8. Familiarity rule

제품군의 상징을 직접 그리는 것이 아니라
사람이 이미 익숙하게 느끼는 시각 패턴을 추상화한다.

예:

- 밥솥 → 쌀알 아이콘 남발 X
- 대신 따뜻한 크림톤 + 둥근 형태 + 김처럼 올라가는 reveal

- 청소기 → 빗자루 아이콘 남발 X
- 대신 sweep motion + particle removal + clean-space expansion

- PC → CPU 아이콘 남발 X
- 대신 grid + fast docking + precise spec layout

목표는 ‘설명’이 아니라 ‘직감’이다.

---

## 9. Design principle

**Brand consistency = structure**
**Category familiarity = mood**
**Information meaning = semantic color**

이 세 레이어를 분리하면,
영상마다 다른 제품을 다루면서도 하나의 채널처럼 보이게 할 수 있다.
