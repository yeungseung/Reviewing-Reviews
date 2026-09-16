# REVIEW² Component Catalog v1

This is the planned v1 shelf.

The shelf is intentionally small.
Prototype #001 determines what gets promoted into the permanent library.

## Patterns

### metric-card
use_when: One metric needs a compact label + value + context.
avoid_when: The number itself is the entire scene; use big-number-focus.

### review-card
use_when: One user/expert review excerpt must be shown with source context.
avoid_when: More than a short readable excerpt is required.

### quote-card
use_when: One statement is the focal evidence.
avoid_when: Many quotes need to be scanned together; use review-wall.

### source-badge
use_when: Evidence tier or source identity must stay visible.
avoid_when: Never use it as decorative branding.

### comparison-bar
use_when: Two to seven values need direct comparison.
avoid_when: Time change is the point; use a line/timeline treatment.

### spec-grid
use_when: A small set of technical specs must be scanned together.
avoid_when: The narrative depends on only one spec.

### product-stage
use_when: Product image/video needs a stable presentation frame.
avoid_when: Evidence capture itself must remain visually untouched.

---

## Scene Blocks

### product-hero
scene_types: product_intro, hook.
mechanics: introduce, focus.
use_when: The product itself must become the visual subject.
avoid_when: The scene is primarily evidence or comparison.

### big-number-focus
scene_types: hook, consensus, complaint_cluster.
mechanics: focus, show-proof.
use_when: One number is the story.
avoid_when: The number requires comparison context.

### review-wall
scene_types: review_wall, consensus, complaint_cluster.
mechanics: accumulate.
use_when: Many independent reviews must visibly become a pattern.
avoid_when: Individual review text needs careful reading.

### claim-cluster
scene_types: consensus, complaint_cluster.
mechanics: cluster, accumulate.
use_when: Repeated claims need to collapse into topics.
avoid_when: Only two opposing groups exist; use conflict-split.

### conflict-split
scene_types: review_conflict.
mechanics: reveal-conflict, compare.
use_when: Two materially different evaluations need equal visual weight.
avoid_when: The reason for the conflict is already known and should be the main point; use condition-split.

### condition-split
scene_types: condition_split, review_conflict.
mechanics: resolve-conflict, show-condition.
use_when: Opposing reviews can be explained by environment or usage conditions.
avoid_when: Evidence for the condition is weak.

### expert-vs-user
scene_types: expert_test, spec_vs_reality.
mechanics: compare, show-proof.
use_when: Controlled measurement and lived experience need parallel comparison.
avoid_when: One evidence tier clearly lacks usable data.

### spec-vs-reality
scene_types: spec_vs_reality.
mechanics: compare, reveal-conflict.
use_when: Official specification and observed experience materially diverge.
avoid_when: The official claim and user observation measure different concepts.

### price-compare
scene_types: price_compare.
mechanics: compare, rank.
use_when: Price or total ownership cost changes the purchase decision.
avoid_when: Price is a passing fact rather than decision evidence.

### timeline
scene_types: timeline.
mechanics: show-timeline, show-trend.
use_when: Release, update, price, failure, or review history matters.
avoid_when: Ordering in time adds no explanatory value.

### buyer-fit
scene_types: who_fits, who_avoids.
mechanics: show-fit, show-condition.
use_when: Product value depends on buyer/use conditions.
avoid_when: It would merely restate generic pros and cons.

### final-checklist
scene_types: final_check.
mechanics: summarize.
use_when: The viewer needs a small set of purchase checks before leaving.
avoid_when: New evidence is still being introduced.

---

## FX policy

Do not create FX because a name sounds useful.

Before authoring a new FX:

1. Search HyperFrames catalog.
2. Check Motion Primitives.
3. Check Magic UI / Cult UI / React Bits when relevant.
4. Wrap or adapt an existing implementation when possible.
5. Create REVIEW²-original FX only when no suitable mechanic exists.
