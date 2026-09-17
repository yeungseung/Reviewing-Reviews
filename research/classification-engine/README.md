# REVIEW² Classification Engine Research Workspace

## 프로젝트 목적

이 프로젝트는 REVIEW² Classification Engine을 즉시 설계하기 위한 프로젝트가 아니다.

목적은 기존 학술 연구, 산업 표준, 제품 분류 체계, 전문 테스트 방법론 등을 조사하여 다음과 같은 선행 구조를 발견하는 것이다.

- 제품을 어떤 단위로 분류하는가
- 제품 속성을 어떤 구조로 표현하는가
- 리뷰의 Claim을 어떤 단위로 쪼개는가
- Context / Condition을 어떻게 표현하는가
- 객관적 측정과 주관적 경험을 어떻게 구분하는가
- Claim끼리 언제 비교 가능한가
- Conflict와 Condition 차이를 어떻게 판단할 수 있는가
- Evidence reliability와 uncertainty를 어떻게 표현하는가

이후 연구 결과는 다음 순서로 연결될 예정이다.

```text
External Research
→ Classification Requirements
→ Claim Classification Architecture
→ Schema
```

현재 단계에서는 Architecture나 Schema를 확정하지 않는다.

## 현재 범위

Phase 1은 R01~R03의 연구 질문과 기록 체계를 준비하는 단계다. 이 초기화에는 실제 외부 검색, 출처 수집, finding, candidate field 채택, 설계 결정이 포함되지 않는다.

각 R 폴더는 다음 파일을 가진다.

- `REPORT.md`: 실제 연구가 시작된 뒤 사용할 report 구조와 작성 규칙
- `SOURCES.md`: source index의 목적과 기록 규칙
- `evidence.jsonl`: finding 단위 evidence 기록용 빈 ledger
- `search-ledger.jsonl`: 실제 검색 과정을 기록할 빈 ledger

빈 JSONL은 연구를 시작하기 전에는 항목을 넣지 않는다. 검색하지 않았는데 검색한 것처럼, 발견하지 않았는데 발견한 것처럼 기록하지 않는다.

## 기존 REVIEW²와의 관계

기존 architecture, source acquisition, evidence 문서는 참고할 수 있다. 다만 외부 연구 결과와 충돌 가능성이 보이더라도 기존 문서를 자동으로 변경하지 않는다. 해당 내용은 연구 report의 `Potential Conflict with Existing REVIEW²`에 기록해 후속 검토 대상으로 남긴다.

## 예정된 연구

Phase 1 뒤에는 다음 연구가 예정되어 있다. 이 초기화에서는 상세 설계나 실제 조사를 하지 않는다.

- R04 Professional Product Testing
- R05 Multi-Criteria Decision Making / Kano / QFD
- R06 Review Reliability / Evidence Quality
- R07 Comparability / Conflict / Contradiction
- R08 Knowledge Graph / Claim Data Model
- R09 Cross-category Stress Test
- R10 Synthesis / Classification Requirements
