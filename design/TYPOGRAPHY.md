# REVIEW² Typography v1

## 1. Direction

Reviewing Reviews의 타이포그래피는
**깔끔함 / 가독성 / 단단함 / 절제**를 우선한다.

서체 자체가 강하게 튀기보다,
크기 / 굵기 / 여백 / 정렬로 위계를 만든다.

카테고리에 따라 폰트를 바꾸지 않는다.

```text
Typography = Reviewing Reviews의 목소리
Color / Motion / Geometry = 제품군의 목소리
```

---

## 2. Font stack

### Primary Latin / Numerals
Inter

### Japanese
Noto Sans JP

### Korean
Pretendard

### CSS stack

```css
font-family:
  Inter,
  "Noto Sans JP",
  Pretendard,
  sans-serif;
```

실제 렌더링 환경에 따라 플랫폼 fallback을 추가할 수 있다.

---

## 3. Weight system

### Japanese
- Main Title: 700
- Subtitle: 600
- Body: 400~500
- UI Label: 500~600

### Latin / Numerals
- Big Number: 700~800
- Main Title: 700
- Subtitle: 600
- Body: 400~500
- UI Label: 500~600

일본어는 획수가 많은 글자가 많으므로
800~900 weight 남용을 피한다.

---

## 4. Tracking

### Big Latin / Numerals
-0.02em ~ -0.04em

### Japanese Title
-0.01em ~ 0

### Japanese Body
0 ~ 0.02em

### Small UI Label
0.01em ~ 0.04em

큰 글자는 살짝 조이고,
작은 글자는 조금 열어준다.

---

## 5. Hierarchy

### Display / Big Number
제품 점수, 가격, 핵심 수치, 순위 등

### H1
영상의 메인 질문 / 핵심 주장

### H2
섹션 제목

### H3
카드 제목 / 비교 항목

### Body
설명문

### Label
버튼 / 태그 / 데이터 라벨

### Caption
출처 / 보조 정보 / 단위

---

## 6. Typography principles

1. 큰 숫자는 강하게
2. 본문은 조용하게
3. 일본어는 과도한 Bold를 피한다
4. 긴 문장은 줄 간격으로 읽기 쉽게 만든다
5. 장식적 폰트는 사용하지 않는다
6. 한 화면에 너무 많은 크기 단계 사용 금지
7. 수치 / 단위 / 라벨의 정렬을 통일한다

---

## 7. v1 status

이 문서는 초기 기준안이다.

실제 HyperFrames 렌더링 결과를 기준으로
다음 항목을 반복 조정한다.

- 숫자 크기
- 일본어 weight
- 자간
- line-height
- 카드 내부 텍스트 밀도
- 모바일/TV 시청 거리에서의 가독성
