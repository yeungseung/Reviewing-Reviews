# R02 — Aspect-Based Sentiment Analysis / Opinion Mining Report

## 이 파일의 목적

이 파일은 실제 R02 연구가 시작된 뒤 리뷰 문장의 Claim, Aspect, Opinion, polarity, comparison, certainty 및 Context 처리 구조에 관한 finding을 기록하는 report다. 현재는 작업공간 초기화 단계이므로 실제 외부 리서치 결과, source, evidence, candidate field는 기록하지 않는다.

## 작성 규칙

- 각 중요한 finding에는 `R02-E001` 형식의 `evidence_id`를 연결한다.
- Aspect Term, Aspect Category, Opinion, Claim을 source가 구분하는 방식과 연구자의 해석을 섞지 않는다.
- sentiment polarity만으로 제품 평가를 단순화하지 않으며, intensity, certainty, comparison, implicit 표현의 한계를 함께 기록한다.
- Context가 다른 동일 Aspect를 자동으로 Conflict로 판단하지 않는다.
- 재사용 가능한 구조와 특정 dataset, 언어, 제품 category에만 종속된 구조를 구분한다.
- Candidate Fields는 검토 후보일 뿐 최종 schema나 채택 결정이 아니다.

## 실제 연구 시작 후 사용할 구조

1. 분야 정의
2. 이 분야가 해결하려는 문제
3. 대표 표준 / 프레임워크 / 연구 계보
4. 핵심 Entity
5. 핵심 Classification Dimensions
6. Entity 간 관계
7. Context / Condition 표현 방식
8. 비교 가능성 / Conflict 처리
9. Reliability / Uncertainty 처리
10. 실제 데이터 구조 또는 필드 사례
11. REVIEW²에 직접 참고 가능한 구조
12. 수정해서 참고해야 하는 구조
13. 가져오면 안 되는 구조 / 한계
14. Candidate Fields
15. Unresolved Questions
16. Evidence Map
17. 주요 Sources
18. Potential Conflict with Existing REVIEW²
