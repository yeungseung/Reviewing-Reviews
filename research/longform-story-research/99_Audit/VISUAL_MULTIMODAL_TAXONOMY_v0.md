# VISUAL & MULTIMODAL TAXONOMY v0

> Purpose: separate evidence classes before converting visual research into Story Engine rules.

## 1. Visual function taxonomy

A visual element should have one or more explicit functions:

| Code | Function | Example |
|---|---|---|
| VF1 | Evidence | original document, product test, archive |
| VF2 | Causal explanation | diagram, process animation |
| VF3 | Context | location, time, environment |
| VF4 | Human consequence | face, behavior, lived detail |
| VF5 | Comparison | before/after, A vs B |
| VF6 | Attention orienting | highlight, reframing, deliberate cut |
| VF7 | Emotional response | reaction shot, expressive imagery |
| VF8 | Continuity | spatial/temporal orientation |
| VF9 | Abstraction reduction | concrete visual example |
| VF10 | Provenance | source label, archive status, reenactment label |

A cut/animation without a function is a candidate for removal, but this is a production heuristic—not a proven cognitive law.

---

## 2. Evidence classes

### E1 — Experimental media processing
Best for:
- resource allocation
- edits/formal features
- memory/attention

### E2 — Basic visual cognition
Best for:
- gaze
- selective attention
- inattentional blindness

### E3 — Multimedia learning
Best for:
- diagrams
- text + narration
- animation
- split attention
- educational information processing

### E4 — Film/craft theory
Best for:
- continuity
- framing
- editing grammar
- narrative aesthetics

### E5 — Information design
Best for:
- tables
- charts
- hierarchy
- visual comparison

### E6 — Affective cinema/neuroscience
Best for:
- camera movement
- embodied response
- emotional shot design

### E7 — Provenance/trust
Best for:
- archive
- reenactment
- stock
- AI-generated media
- labels/authenticity

Do not flatten E1–E7 into one "Tier 1 scientific proof" category.

---

## 3. Timing policy for the future engine

Current corpus contains many hard timings:
- 2.5 s
- 4–8 s
- 12 s
- 3.5 s reaction
- 6–9 s proof dwell
- 5–8 s fact phase
- 4–6 s emotion phase

Audit disposition:
**UNVERIFIED PRODUCTION PRIORS**

Future engine should represent them as parameters:

```
cut_interval_prior
evidence_dwell_prior
text_read_time
reaction_dwell_prior
motion_budget
audio_ducking_prior
```

Each parameter should be adjustable by:
- amount of information
- text length
- visual complexity
- genre
- emotional intensity
- audience
- platform
- observed retention/skip behavior

No fixed number should be promoted to a scientific law without comparable direct evidence.

---

## 4. Candidate visual decision sequence

```
WHAT must the viewer understand/feel?
        ↓
WHAT visual function is needed?
        ↓
WHAT evidence class supports this design?
        ↓
HOW complex is the visual?
        ↓
HOW long is needed for comprehension?
        ↓
DOES motion/editing help or compete?
        ↓
OBSERVE actual audience behavior
        ↓
UPDATE timing prior
```

This is a more suitable architecture for a Story Engine than fixed editing-frequency rules.
