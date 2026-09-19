# PREDICTION TAXONOMY v0

> Audit artifact for LONGFORM STORY RESEARCH  
> Goal: prevent concept collapse around the word "prediction"

## 1. Why this taxonomy exists

The current corpus uses "prediction error" as though one mechanism directly explains:
- event boundaries
- suspense
- curiosity
- surprise
- dopamine reward
- memory updating
- active inference
- counterfactual regret
- Rehook timing
- binge watching

The audit shows these are not interchangeable.

---

## 2. Construct map

| Code | Construct | Typical question | Main outcome | Current Story Engine relevance |
|---|---|---|---|---|
| P1 | Event-model prediction | What happens in the next moment of ongoing activity? | event boundary / event-model update | HIGH |
| P2 | Narrative expectation | What outcome/action/solution will occur in the story? | suspense, curiosity, surprise, comprehension | VERY HIGH |
| P3 | Mnemonic prediction error | Does a familiar expected episode conclude as expected? | memory destabilization/update | HIGH |
| P4 | Reward prediction error | Was reward better/worse than expected? | reinforcement learning / dopamine teaching signal | CONDITIONAL |
| P5 | Predictive processing / FEP | How do generative models explain sensory input/action? | perceptual inference / model optimization | BACKGROUND |
| P6 | Counterfactual simulation | What would have happened if the past were different? | regret, responsibility, causal judgment | HIGH but NOT prediction engine |
| P7 | Epistemic curiosity / complexity | Is there a meaningful, learnable information gap? | information seeking / attention | HIGH, belongs M5 |

---

## 3. P1 Event-model prediction

Evidence:
Zacks et al. Event Segmentation Theory and related work.

Supported:
- continuous activity is parsed into events
- event models guide short-term predictions
- transient increases in prediction error can trigger event-model updating/boundaries
- conceptual changes such as goals/causal relations can correlate with boundaries

Not established:
- 7–10 minute universal boundary cycle
- two simultaneous state dimensions as a universal threshold
- exact retention multipliers
- every scene must end on a prediction-error spike

Research Map:
Merge substantially with M2 Event/State Updating.

---

## 4. P2 Narrative expectation

Direct narrative evidence should become the core of any future Prediction module.

Examples:
- Gerrig & Bernardo: restricted solution paths heighten suspense
- Hoeken & van Vliet: event-order manipulation differentiates suspense, curiosity, surprise and influences processing

Future Claude questions:
- prospective inference during narrative comprehension
- outcome expectation confidence
- fair surprise / retrospective coherence
- foreshadowing and expectation calibration
- suspense under known outcomes
- genre expertise and expectation

Avoid importing numeric rules from infant complexity or primate reward learning.

---

## 5. P3 Mnemonic prediction error

Sinclair et al. (2021) is especially valuable because it used familiar narrative videos.

Supported:
- interrupting expected narrative endings created mnemonic prediction errors
- disrupted sustained hippocampal representations
- disruption predicted memory updating
- basal forebrain activity mattered for the memory relationship

Not supported:
- "bigger twist = more dopamine"
- surprise is always good
- surprise necessarily strengthens accurate memory
- VTA dopamine is the central mechanism

Story Engine interpretation:
A violated expected episode can make an existing representation more updateable.
This is closer to **reframing / memory revision** than to pure entertainment reward.

---

## 6. P4 Reward Prediction Error

Schultz et al. (1997) concerns reward-related prediction signals, primarily in primate dopamine systems.

Supported at broad level:
- dopamine neuron output tracks deviations/errors in predictions of future salient/rewarding events

Do not infer directly:
- a plot twist is a reward
- an unexpected victory always creates a "dopamine explosion"
- expected reward is emotionally flat for human story viewers
- negative RPE equals narrative disappointment in a one-to-one mapping

Required bridge research:
human narrative, music, game, or entertainment reward studies that actually measure expectation/value and dopaminergic/reward outcomes.

---

## 7. P5 Predictive processing / Free-Energy Principle

Use:
- theoretical framing for generative models and prediction-based updating

Do not use as:
- direct audience-retention evidence
- a numeric mystery meter
- proof that 100% predictability causes mind-wandering
- proof that uncertainty makes viewers continue watching
- proof of dopamine reward from information resolution

---

## 8. P6 Counterfactual thinking

Counterfactual thinking is retrospective:
"If X had been different, Y might not have happened."

Likely Story Engine uses:
- regret
- responsibility
- tragedy
- near miss
- causal attribution
- choice/consequence meaning

Research Map:
Move toward M1 causal-model construction and M3 appraisal/emotion.

---

## 9. P7 Epistemic curiosity / complexity

Kidd et al.:
intermediate complexity can sustain infant attention.

Kang et al.:
curiosity relates to information seeking, reward-related caudate activity, and later memory.

Research Map:
This belongs primarily under M5 Curiosity / Managed Uncertainty.

No numeric 30–50% prediction-error target is currently justified.

---

## 10. Provisional Story Engine architecture

Instead of one "Prediction Engine":

```
CURRENT EVENT MODEL
      ↓
LOCAL PREDICTION (P1)
      ↓
EVENT / STATE CHANGE
      ↓
MODEL UPDATE
      ↓
NARRATIVE EXPECTATION (P2)
      ↓
[confirm / delay / violate / reframe]
      ↓
MEMORY UPDATE (P3, when conditions apply)

CURIOSITY (P7) regulates information seeking
REWARD RPE (P4) is a separate value-learning mechanism
FEP (P5) remains theoretical background
COUNTERFACTUAL (P6) operates retrospectively
```

This architecture is provisional and should be stress-tested in precision research.
