# R01 — Source Index

## 이 파일의 목적

이 파일은 실제 R01 연구에서 확인한 source를 식별하고 출처 성격을 기록하는 index다. 현재는 작업공간 초기화 단계이므로 실제 source는 아직 기록하지 않는다.

## 기록 규칙

- 가능한 경우 `source_id`, `title`, `author` 또는 `organization`, `publication_date`, `url`, `accessed_at`, `source_type`, `original_or_secondary`, `research_id`, `notes`를 기록한다.
- 국제/산업 표준 기관의 공식 문서, 원논문, 공공·전문 시험기관 methodology를 우선한다.
- 블로그나 2차 요약은 개념 탐색용으로는 사용할 수 있지만, 핵심 결론은 상위 우선순위 source로 재검증한다.
- 동일 원출처를 복제하거나 요약한 여러 문서는 독립 source strength로 세지 않고 관계를 `notes`에 남긴다.
- Source는 문서 단위의 출처이고, Evidence는 특정 finding을 지지하는 위치 가능한 단위다. Evidence는 `evidence.jsonl`에 따로 기록한다.
