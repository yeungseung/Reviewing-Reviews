# REVIEW² Motion v1

## 1. Principle

Motion은 장식이 아니라
**관계 / 변화 / 원인 / 순서**를 이해시키기 위해 사용한다.

기본 움직임은 짧고 자연스럽게,
영상의 큰 scene 전환만 조금 더 길게 사용한다.

---

## 2. Duration scale

Material의 desktop motion이 짧고 즉각적인 편이라는 원칙을 참고하되,
REVIEW²는 '사용자가 조작하는 UI'가 아니라 '시청하는 영상'이므로
정보 인지 시간을 위해 일부 구간을 늘린다.

```text
motion.micro       160ms
motion.fast        200ms
motion.ui          240ms
motion.component   300ms
motion.structure   380ms
motion.scene       480ms
motion.emphasis    640ms
```

640ms 이상은 특별한 cinematic transition이 아니면 사용하지 않는다.

---

## 3. Easing

### Standard
화면 안에서 위치/크기가 바뀔 때.

```css
cubic-bezier(0.4, 0.0, 0.2, 1)
```

### Enter
새 object가 들어올 때.

```css
cubic-bezier(0.0, 0.0, 0.2, 1)
```

### Exit
object가 화면 밖으로 나갈 때.

```css
cubic-bezier(0.4, 0.0, 1, 1)
```

---

## 4. Choreography

여러 요소를 동시에 움직이지 않는다.

기본 stagger:

```text
60ms
80ms
120ms
```

### Small group
60ms

### Cards / list
80ms

### Strong sequential explanation
120ms

---

## 5. Continuity

scene이 바뀔 때 가능하면 하나의 object를 유지한다.

예:

```text
Review Card
→ 여러 카드
→ Claim Cluster
→ 하나의 Conflict Bar
```

같은 정보가 형태를 바꾸며 이어지면
시청자는 별도 설명 없이 관계를 이해할 수 있다.

---

## 6. Motion roles

### Reveal
정보 등장

### Transform
같은 정보의 의미 변화

### Compare
A/B 관계 형성

### Accumulate
review / claim이 모임

### Filter
불필요한 요소가 사라짐

### Focus
핵심 데이터만 강조

### Resolve
conflict가 조건 차이로 설명됨

---

## 7. Category modifiers

Core motion token은 동일하게 유지하고
카테고리별로 ±15% 안에서 personality를 준다.

### TECH
- 조금 빠르게
- snap / dock / scan
- 낮은 overshoot

### KITCHEN
- 조금 부드럽게
- rise / fill / steam reveal

### CLEANING
- sweep / wipe / particle remove

### AIR CARE
- breathing / float / transparency

### AUDIO
- pulse / wave / spatial expansion

카테고리가 달라도 easing family와 기본 duration scale은 유지한다.

---

## 8. Avoid

- 의미 없는 bounce
- 과한 elastic
- 같은 scene에서 easing 혼용
- 모든 object 동시 등장
- 긴 fade만 반복
- 회전할 이유가 없는 object 회전
- transition이 content보다 눈에 띄는 상태

---

## 9. Chart motion

추천 순서:

```text
axis
→ mark
→ value
→ highlight
→ takeaway
```

차트 자체가 narration의 논리를 따라가야 한다.

---

## 10. Reduced motion / static fallback

렌더러는 향후 다음 mode를 지원한다.

```text
motion: full
motion: reduced
motion: static
```

QA와 썸네일/정지 프레임 생성에도 유용하다.
