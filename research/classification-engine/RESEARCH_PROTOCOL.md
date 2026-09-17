# Research Protocol

이 문서는 R01~R10에 공통으로 적용할 연구 기록 규칙이다. 아래 필드와 상태는 추적을 위한 protocol의 개념이며, REVIEW²의 최종 schema나 채택 결정을 뜻하지 않는다.

## Source Priority

핵심 결론은 가능한 한 높은 우선순위 출처로 재검증한다. 하위 출처는 개념 발견에는 사용할 수 있지만, 그 자체만으로 핵심 결론을 확정하지 않는다.

1. 국제/산업 표준 기관의 공식 문서
2. 원논문 / peer-reviewed academic paper
3. 정부기관 / 공공기관 / 전문 시험기관의 methodology
4. 공식 기술 문서
5. systematic review / survey paper
6. 상용 시스템의 공식 공개 documentation
7. 신뢰할 수 있는 2차 자료
8. 일반 블로그/게시물

## Source Classification

각 source에는 가능한 경우 아래 정보를 기록한다.

| 항목 | 의미 |
| --- | --- |
| `source_id` | 이 작업공간 안에서 source를 식별하는 ID |
| `title` | 문서 또는 자료 제목 |
| `author` 또는 `organization` | 저자 또는 발행 기관 |
| `publication_date` | 발행일 |
| `version_or_edition` | 가능한 경우 기록하는 버전, 판본, edition 또는 revision; `publication_date`와 별도로 기록 |
| `url` | 원문 또는 공식 접근 주소 |
| `accessed_at` | 실제 접근 시각 |
| `source_type` | 우선순위 판단에 쓰는 출처 유형 |
| `original_or_secondary` | 원출처인지 2차 설명인지 |
| `source_origin` | 알려진 원출처 또는 원출처를 식별할 수 있는 reference |
| `source_relation` | mirror, summary, quotation, syndicated copy 등 다른 source와의 알려진 관계 |
| `same_origin_chain` | 다른 source와 동일 원출처 chain에 속하는지에 대한 기록 |
| `independence_note` | 독립성 판단 근거, 불확실성 또는 확인하지 못한 관계에 대한 주석 |
| `research_id` | R01~R10 중 연결되는 연구 |
| `notes` | 접근 제한, 해석 주의 등 위 항목으로 분리하지 않은 주석 |

표준, taxonomy, methodology, technical documentation은 발행일만으로 식별하지 않는다. 가능한 경우 `version_or_edition`으로 판본 또는 revision을 별도 기록한다.

## Source Independence and Derivation

복제 관계는 `notes`에만 자유 서술로 남기지 않는다. 가능한 경우 `source_origin`, `source_relation`, `same_origin_chain`, `independence_note`를 함께 기록해 provenance와 독립성을 추적한다.

- mirror, summary, quotation, syndicated copy처럼 같은 원출처에서 파생된 자료는 관계와 동일 origin chain 여부를 기록한다.
- 독립성을 확인하지 못했으면 독립이라고 가정하지 않고 그 상태와 이유를 `independence_note`에 남긴다.
- 동일 origin chain의 여러 자료는 독립 evidence strength로 중복 계산하지 않는다.

이 규칙은 연구 provenance를 기록하기 위한 protocol이다. 기존 REVIEW² Source Relation schema를 복제하거나 수정하는 것이 아니며, 최종 schema를 정의하지 않는다.

## Evidence Rules

Evidence는 Source 전체가 아니라 특정 Research Finding을 지지하는 검증 가능한 단위다. `evidence.jsonl`의 각 기록은 가능한 경우 다음 개념을 포함한다.

| 항목 | 의미 |
| --- | --- |
| `evidence_id` | finding 단위의 추적 ID |
| `research_id` | 연결되는 R-ID |
| `source_id` | 근거가 나온 source ID |
| `source_type` | source의 유형 |
| `locator` | 페이지, 절, 표, figure, paragraph 등 위치 |
| `evidence_summary` | 확인 가능한 근거 요약 |
| `short_excerpt_if_needed` | 필요한 경우에만 쓰는 짧은 인용 |
| `supports` | 지지하는 finding 또는 질문 |
| `limitations` | 적용 범위, 표본, 버전, 접근성 등의 한계 |
| `confidence` | 근거의 강도에 대한 판단과 이유 |
| `notes` | 복제 관계, 해석 주의 등 추가 정보 |

Evidence ID는 연구별로 `R01-E001`, `R01-E002`, `R02-E001`처럼 부여한다. 긴 원문 전체를 복사하지 않으며, 필요한 경우 위치 정보와 짧은 excerpt만 기록한다.

## Search Ledger Rules

모든 주요 검색 과정은 `search-ledger.jsonl`에 기록한다. 각 기록은 최소한 다음 개념을 포함한다.

| 항목 | 의미 |
| --- | --- |
| `search_id` | 검색 과정 식별자 |
| `research_id` | 연결되는 R-ID |
| `query` | 실제 사용한 질의 |
| `search_engine_or_database` | 검색 엔진 또는 데이터베이스 |
| `searched_at` | 실제 검색 시각 |
| `purpose` | 질문 또는 공백을 메우려는 목적 |
| `useful_sources_found` | 유용하다고 판단한 source ID 또는 빈 결과 |
| `rejected_sources` | 제외한 등록 source ID, 또는 source ID가 없으면 title / URL / candidate reference |
| `rejection_reason` | 각 제외 자료를 제외한 이유; 반드시 기록 |
| `gap_or_followup` | 남은 공백과 후속 검색 |

검색하지 않았는데 검색한 것처럼 기록하면 안 된다. 탈락한 자료는 아직 source ID를 받지 않았을 수 있으므로, `rejected_sources`에는 등록 source ID뿐 아니라 title, URL, candidate reference를 기록할 수 있다. 각 탈락 이유는 `rejection_reason`에 반드시 남긴다. 결과가 없었던 검색도 중요한 경우에는 결과 없음과 이유를 기록한다.

## Research Report Common Structure

실제 연구가 시작된 뒤 각 `REPORT.md`는 아래 구조를 사용한다.

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

각 finding에는 `evidence_id`를 연결하고, 사실·연구자 해석·REVIEW² 적용 추론을 구분한다. reusable structure와 domain-specific structure, 범용 개념과 category 종속 개념도 구분한다.

## Candidate Fields Rules

Candidate Fields는 최종 schema가 아니다. 외부 연구에서 반복적으로 등장하거나 REVIEW²에서 검토할 가치가 있는 필드를 후보로만 기록한다.

예시는 `property_type`, `value_type`, `unit`, `context_dimension`, `measurement_condition`이다. 이 예시는 채택된 필드가 아니며, 실제 연구 결과가 뒷받침할 때에만 후보로 기록한다.

각 후보는 다음 상태 중 하나로 표시할 수 있다.

- `strong_candidate`
- `candidate`
- `domain_specific`
- `unclear`
- `reject_candidate`

어느 상태도 최종 채택을 뜻하지 않는다. 근거가 부족하면 `unclear`, 발견하지 못했으면 `not_found` 또는 `unresolved`로 남긴다.

## Conflict and Uncertainty Rules

- 독립성이 없는 복제 source는 별도 evidence strength로 합산하지 않는다.
- 상충하는 evidence는 출처 우선순위, 적용 domain, 방법론, Context / Condition 차이를 함께 기록한다.
- Context가 다른 Claim은 자동으로 Conflict가 아니다. 비교 가능한지와 condition mismatch 가능성을 먼저 검토한다.
- uncertainty, limitation, unresolved question을 결론과 분리해 보존한다.
