# REVIEW² Components

This directory is the source registry for reusable REVIEW² visual units.

## Taxonomy

```text
primitives/
patterns/
scenes/
fx/
vendor/
```

### primitives
Small visual building blocks with no story meaning.

### patterns
Reusable information groups.

### scenes
Standalone REVIEW² scene grammar.
These normally map to HyperFrames blocks.

### fx
Reusable motion/effect behaviors.
These normally map to HyperFrames components.

### vendor
Third-party source retained with provenance and license information.

## Canonical item structure

```text
<kind>/<name>/
  manifest.json
  props.schema.json
  SPEC.md
  examples/
  adapters/
```

Actual implementation source will be added during Mac Studio / Codex development.

Do not put raw asset binaries or rendered video outputs here.
