# REVIEW² Data Visualization v1

## 1. Principle

차트는 장식이 아니라 주장에 대한 증거다.

먼저 질문의 종류를 정하고,
그다음 가장 단순한 chart를 선택한다.

---

## 2. Question → chart mapping

### Comparison
기본:
- Horizontal bar
- Grouped bar

예:
- 제품별 가격
- 소음
- 만족도
- 배터리

영상에서는 label 길이를 처리하기 쉬운 horizontal bar를 우선한다.

---

### Trend
기본:
- Line
- Area는 누적/범위 의미가 있을 때만

예:
- 가격 변화
- 장기 배터리 저하
- 리뷰 평점 변화

---

### Part-to-whole
기본:
- Stacked bar

제한적으로:
- Donut

Donut은 segment가 적고 하나의 비율을 강조할 때만 사용한다.

---

### Distribution
기본:
- Histogram
- Dot distribution
- Review sentiment strip

예:
- 평점 분포
- 소음 불만의 범위
- 사용 기간별 평가

---

### Correlation
기본:
- Scatter
- Heatmap

예:
- 가격 vs 성능
- 사용기간 vs 만족도

상관관계를 인과관계처럼 설명하지 않는다.

---

### Timeline
기본:
- Horizontal timeline

예:
- 출시
- 업데이트
- 가격 인하
- 반복 고장 보고
- 장기사용 이슈

---

## 3. REVIEW² custom visualizations

### Review Wall
많은 후기 → 반복 pattern으로 수렴하는 과정을 보여준다.

### Claim Cluster
비슷한 claim이 하나의 topic으로 모이는 장면.

### Conflict Split
같은 항목에서 상반된 평가를 양쪽으로 분리한다.

### Condition Split
평가 충돌이 실제로는 사용 조건 차이인지 보여준다.

### Expert vs User
전문 측정 결과와 실제 체감 평가를 병렬 비교한다.

### Marketing Origin
마케팅 문구가 어디서 시작돼 얼마나 반복되는지 보여준다.

### Evidence Strength
Finding이 얼마나 다양한 독립 source에 의해 지지되는지 표현한다.

### Buyer Fit
제품 특성과 사용자 조건의 match를 보여준다.

---

## 4. Axis rule

### Bar / part-to-whole comparison
Numerical axis는 0에서 시작한다.

### Line chart
작은 변화가 핵심일 경우 non-zero axis를 허용하지만,
축 범위를 명확히 보여준다.

---

## 5. Direct labeling

가능하면 legend 대신 chart 안에 직접 label한다.

예:

```text
Sony   █████████  8.7
Bose   ████████   8.1
```

다음 경우에만 legend 사용:
- series가 많음
- direct label 공간이 부족함
- 동일 series가 여러 chart에 반복됨

---

## 6. Color rule

### Category accent
Primary data series 또는 focus item에 사용.

### Neutral
Comparison series에 사용.

### Semantic colors
의미가 고정된 상태에만 사용.

```text
positive
negative
warning
conflict
official
expert
user
```

여러 series를 구분하기 위해 semantic color를 임의 사용하지 않는다.

---

## 7. Highlight rule

한 chart에서 강한 accent는 기본 1개.

예:
- 5개 제품 중 현재 리뷰 제품만 accent
- 나머지 4개는 neutral gray

이렇게 해야 시선이 자동으로 결론으로 간다.

---

## 8. Labels and numbers

- 단위는 반복하지 말고 축/헤더에서 처리 가능
- 큰 수는 천 단위 구분
- 불필요한 소수점 제거
- %는 비교 의미가 있을 때만
- label은 짧고 직접적으로
- chart title은 데이터 이름보다 insight를 우선

나쁨:
`Noise comparison`

좋음:
`침실에서는 평가가 완전히 갈렸습니다`

---

## 9. Gridline rule

Gridline은 데이터 해석에 필요한 만큼만.

- 기본 low contrast
- border보다 약하게
- animation focus 중에는 더 줄일 수 있음

---

## 10. Motion in charts

차트는 결과가 나타나는 순서대로 움직인다.

예:
1. axis
2. bars
3. values
4. highlight
5. conclusion

모든 bar가 동시에 튀어나오는 방식보다
논리를 따라 reveal한다.

---

## 11. Max complexity

영상 scene에서 한 chart에 권장하는 최대:
- bars: 5~7
- line series: 3
- donut segments: 4
- comparison columns: 4
- strongly emphasized metrics: 1~2

그 이상이면 scene을 나눈다.
