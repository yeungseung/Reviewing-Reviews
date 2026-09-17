# ROADMAP v0.1

## Phase 0 — Contract
- [ ] Source schema 확정
- [ ] Claim schema 확정
- [ ] Finding schema 확정
- [ ] Scene schema 확정
- [ ] 프로젝트 폴더 규약 확정

## Phase 1 — Research prototype
- [ ] 제품 1개 선정
- [ ] Official / Expert / User 소스 수집
- [ ] Claim 수동+AI 분해
- [ ] cluster/conflict/conditional 분석
- [ ] Buyer Question 생성

## Phase 2 — Story compiler
- [ ] Finding → Story Beat 변환 규칙
- [ ] 일본어 내레이션 생성 규칙
- [ ] 출처 추적 가능한 문장 단위 provenance

## Phase 3 — Scene compiler
- [ ] Story Beat → Scene JSON
- [ ] 기본 Scene component 10개
- [ ] 모션 디자인 토큰 정의

## Phase 4 — Rendering
- [ ] HyperFrames 통합
- [ ] 자막/TTS word timing 통합
- [ ] whiteboard 서브 렌더러 연동

## Phase 5 — QA
- [ ] claim-source trace 검사
- [ ] unsupported claim 검사
- [ ] 중복/편향 source 검사
- [ ] 자막/화면 overflow 검사

## Phase 6 — Feedback loop
- [ ] 검색어 데이터 저장
- [ ] CTR / retention / comment signal 저장
- [ ] 다음 제품 선정에 반영

---

## Architecture research references

- `docs/HIGGSFIELD_SKILLS_ANALYSIS.md`
  - Higgsfield Skills 구조 분석
  - REVIEW² Control Plane 적용 후보
  - Approval State / dependency invalidation / capability routing / targeted repair / eval harness 참고
  - 실제 적용 전 `yeungseung/connect-ai/external-reference/higgsfield-skills`의 pinned upstream을 함께 확인
