# REVIEW² ENGINE

> 리뷰를 리뷰하다 — 여러 공개 리뷰와 근거를 재분석해 구매 판단을 돕는 검색형 롱폼 제작 시스템

## Core idea

이 프로젝트의 목적은 단순한 리뷰 요약이 아니다.

`PRODUCT → SOURCE → CLAIM → FINDING → STORY → SCENE → VIDEO`

각 단계의 데이터를 구조화해서, 제품별 리서치 자산을 재사용하고 영상 제작을 반자동화한다.

## Principles

1. 기본 단위는 리뷰가 아니라 **Claim(주장)** 이다.
2. 근거는 **Official / Expert / User** 3계층으로 추적한다.
3. 단순 긍·부정 비율보다 **반복 합의 / 반복 불만 / 의견 충돌 / 조건부 평가 / 증거 부족** 을 찾는다.
4. 영상은 리뷰 순서가 아니라 **구매 질문** 순서로 구성한다.
5. 화면은 정지 슬라이드가 아니라 **Scene JSON → 모션 컴포넌트** 로 렌더링한다.
6. 최종 의사결정은 사람이 한다. AI는 수집·분해·분석·구성·렌더링을 보조한다.

## Human gates

- Product Gate — 이 제품을 만들 가치가 있는가
- Evidence Gate — 근거가 충분하고 편향되지 않았는가
- Story Gate — 이번 영상의 핵심 질문은 무엇인가
- Final Gate — 사실·뉘앙스·완성도가 공개 가능한가

## Planned renderer stack

- **HyperFrames**: 메인 모션/프레젠테이션 렌더러
- **srt-whiteboard-animation**: 원리·구조 설명용 서브 렌더러
- 실제 제품 영상/이미지/리뷰 캡처: 증거 시각화 소스

자세한 내용은 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) 참고.
