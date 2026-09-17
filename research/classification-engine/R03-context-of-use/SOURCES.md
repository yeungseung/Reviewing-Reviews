# R03 — Source Index

## 이 파일의 목적

이 파일은 실제 R03 연구에서 확인한 source를 식별하고 출처 성격을 기록하는 index다. 현재는 작업공간 초기화 단계이므로 실제 source는 아직 기록하지 않는다.

## 기록 규칙

- 가능한 경우 `source_id`, `title`, `author` 또는 `organization`, `publication_date`, `url`, `accessed_at`, `source_type`, `original_or_secondary`, `research_id`, `notes`를 기록한다.
- 국제 표준, 정부·공공기관, 전문 시험기관의 usability 또는 test methodology와 원논문을 우선한다.
- 실제 사용 조건을 설명하지 않는 일반적 요약은 핵심 Context 결론의 단독 근거로 사용하지 않는다.
- 같은 methodology를 요약한 여러 문서는 원출처와의 관계를 표시하고 독립 evidence로 중복 계산하지 않는다.
- Source는 문서 단위로, Evidence는 finding과 locator 단위로 구분해 `evidence.jsonl`에 기록한다.
