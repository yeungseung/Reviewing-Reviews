# REVIEW² Source Desk v1

## Purpose

Source Desk는 "검색 도구"가 아니라
Human Source Gate를 빠르고 정확하게 수행하기 위한 작업면이다.

사람이 직접 해야 하는 판단은 남기고,
기계가 대신할 수 있는 기록 작업은 제거한다.

---

## Primary screen

```text
┌───────────────────────────────────────────────────────────────┐
│ Product / Buyer Question / Query                     SEARCH   │
├────────────────┬──────────────────────────────────────────────┤
│ Candidate List │ Source Inspector                             │
│                │                                              │
│ tier / kind    │ title / publisher / author / published date │
│ product match  │ canonical URL / platform IDs                │
│ original?      │ product model / region                      │
│ duplicate?     │                                              │
│ status         │ ┌─ Evidence focus ────────────────────────┐  │
│                │ │ relevant text/video                     │  │
│                │ │ context before / after                  │  │
│                │ │ suggested locator                       │  │
│                │ └─────────────────────────────────────────┘  │
│                │                                              │
│                │ lineage graph                               │
│                │ candidate → possible origin                │
│                │                                              │
│                │ ACCEPT  REJECT  DUPLICATE  LINK ORIGIN      │
│                │ CAPTURE  CREATE EVIDENCE  MORE RESEARCH     │
└────────────────┴──────────────────────────────────────────────┘
```

---

## Human interaction principle

Bad workflow:

```text
human copies URL
human types title
human types author
human saves screenshot
human creates filename
human hashes file
human writes source id
human writes timestamp
```

Target workflow:

```text
human judges
↓
button
↓
system records everything else
```

---

## Capture action

When human selects CAPTURE:

system should:

1. freeze final URL
2. record access time
3. collect metadata
4. capture selected tier
5. save raw artifact
6. extract text/transcript
7. create screenshot/frame
8. calculate SHA-256
9. create Snapshot record
10. offer locator creation

Human then verifies evidence focus.

---

## Create Evidence action

System drafts:

- source_id
- snapshot_id
- exact quote / observation
- prefix / suffix
- text position or timestamp
- product match
- independence group
- origin type
- usable_for_claim
- usable_for_video

Human confirms/edits.

---

## Lineage panel

Show:

```text
ORIGIN
  ↓
DERIVED
  ↓
CURRENT SOURCE
```

Actions:

- confirm origin
- mark probable
- unlink
- same independence group
- new independent source

---

## Coverage panel

Source Desk should expose a matrix:

```text
Question                 Official  Expert  User
Noise                       ✓        ✓       ✓
Maintenance                 ✓        -       ✓
Long-term failure           -        ?       ✓
Filter cost                 ✓        -       ✓
```

This helps the human decide when research is good enough.

---

## Search gap panel

Never hide failure.

Examples:

- blocked
- removed
- paywalled
- no independent expert test found
- wrong model dominates results
- only marketing-derived coverage found

A visible gap is better than silent false confidence.
