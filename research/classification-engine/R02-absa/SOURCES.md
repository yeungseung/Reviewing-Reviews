# R02 — Source Index

## 이 파일의 목적

이 파일은 실제 R02 연구에서 확인한 source를 식별하고 출처 성격을 기록하는 index다. 현재는 작업공간 초기화 단계이므로 실제 source는 아직 기록하지 않는다.

## 기록 규칙

- 가능한 경우 `source_id`, `title`, `author` 또는 `organization`, `publication_date`, `url`, `accessed_at`, `source_type`, `original_or_secondary`, `research_id`, `notes`를 기록한다.
- 원논문, peer-reviewed paper, systematic review, 공식 benchmark 또는 공식 documentation의 원자료를 우선한다.
- 2차 요약과 블로그는 원개념의 단서가 될 수 있지만 원논문이나 공식 표준으로 취급하지 않는다.
- 같은 dataset, 논문, benchmark를 재서술한 source는 독립 evidence로 중복 계산하지 않는다.
- Source와 finding 단위 Evidence를 구분하고, locator가 있는 evidence는 `evidence.jsonl`에 기록한다.
