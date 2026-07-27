# Semiotic Velocity Tool

Research software for studying the circulation and changing interpretation of Jan Matejko's *Stańczyk* (1862).

## Status

This repository is an **early v6-aligned foundation**, not a complete operational research instrument. It currently provides:

- configurable dHash candidate retrieval;
- a rule-based Polish nominal-invocation candidate stream;
- strict separation of visual A–E candidates from nominal N1–N3 candidates;
- structured machine outputs that require human validation;
- a versioned target/configuration schema;
- an initial SQL schema for provenance, double coding, adjudication, semiotic displacement, Δt, semiotic velocity, and F1–F3 friction variables;
- regression tests for the linguistic-stream safeguards.

CLIP, pHash, SIFT/ORB, pose analysis, OCR, database services, the coder interface, validation-corpus evaluation, exports, and visualisations remain planned work. Machine similarity is not treated as meaning, semantic truth, or semiotic velocity.

## Analytical safeguards

1. **Circulatory velocity and semiotic velocity are separate.** Dated reproduction or invocation counts measure circulation. Semiotic velocity is calculated only from human-coded displacement (ΔS) over an explicit historical interval (Δt).
2. **Visual and linguistic classes are separate.** Images use A–E candidate tiers. Linguistic invocations use N1–N3 candidate classes.
3. **Machine outputs are candidates.** Final classifications require an auditable human decision.
4. **Tier E needs independent evidence.** Computational resemblance alone cannot establish a remote visual echo.
5. **Thresholds are provisional.** The dHash values 5/12/20 must be calibrated against a manually coded validation corpus.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

```python
from semiotic_velocity import SemioticVelocityPipeline

pipeline = SemioticVelocityPipeline("config/targets.yaml")
candidate = pipeline.process_linguistic_stream("Stańczyk Jana Matejki")
print(candidate)
```

## Repository structure

- `semiotic_velocity/pipeline.py` — machine candidate generation;
- `config/targets.yaml` — versioned targets, thresholds, and linguistic rules;
- `schema.sql` — initial research-data schema;
- `tests/` — safeguard regression tests;
- [`PRODUCT_BACKLOG.md`](PRODUCT_BACKLOG.md) — ordered research and development backlog.

## Roadmap

The ordered Scrum backlog, first-release gate and research-oriented definition of done are maintained in [`PRODUCT_BACKLOG.md`](PRODUCT_BACKLOG.md).
## Current proposal alignment (v6.1)

The current UMCS proposal expands the implementation target beyond the original v6 foundation:

- linguistic retrieval must support Polish, Russian and German with language-specific morphology, historical variants, transliteration, contextual anchors and false-positive controls;
- the unit of analysis is a documented derivative or invocation in context, with reposts linked through derivative lineages;
- semantic change is recorded as an evidenced transition between coded states; any ordinal ΔS score is optional, versioned and subject to sensitivity analysis;
- meaning status is coded as `dominant`, `contested` or `indeterminate`, with evidence and confidence;
- comparison periods and source strata are configurable, and exports retain archival survival, digitisation, platform availability and evidential-weight metadata;
- privacy review includes re-identification, search-engine discoverability and identifiable political content.

These are planned requirements until the corresponding backlog items and tests are complete. The software must not represent unimplemented controls as operational.
