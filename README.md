# Semiotic Velocity Tool

Implementation and technical specification for **Project Master File: Semiotic Velocity Tool (v5.3)**.

The project measures *semiotic velocity*: the rate at which a visual sign's dominant meaning shifts across political and temporal contexts. Its proof of concept traces visual derivatives and nominal deployments of Jan Matejko's *Stańczyk* (1862), with particular attention to Polish digital culture since 2010.

## v5.3 architecture

- **Visual stream (Tiers A–D):** dHash/pHash thresholds for direct and derivative images; advanced Tier D routing for SIFT, pose estimation, OCR, and contextual analysis.
- **Linguistic stream (Tier E):** Polish morphological matching, primary and secondary anchors, and false-positive exclusions.
- **Bibliometric ingest:** Google Books Ngram CSV data for the pre-digital longitudinal baseline.
- **Unified output:** database and visualization layer for temporal and political interpretation.

See [SPEC_v5.3.md](SPEC_v5.3.md) for the taxonomy, ingestion design, historical baseline, and GDPR controls.

## Repository layout

- `main.py` — core v5.3 visual and linguistic pipeline
- `config/grammar_v1_stanczyk.yaml` — canonical target configuration
- `requirements.txt` — pinned Python dependencies
- `SPEC_v5.3.md` — repository version of the master technical specification

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```python
from main import SemioticVelocityPipeline

pipeline = SemioticVelocityPipeline("config/grammar_v1_stanczyk.yaml")
```

## Research context

The broader project, *The Unstable Icon: Semiotic Velocity in the 160-Year Ontogeny of Jan Matejko's Stańczyk (1862–Present)*, combines cultural semiotics, visual analysis, and computational methods. The instrument is a scalable proof of concept intended for extension to additional visual and cinematic objects.

The theoretical framework draws on Lotman's semiosphere and invariant core, the Derrida–Laclau spectrum, Warburg's *Pathosformel*, and Visual Aesopian Language. Planned outputs include a monograph, journal articles, and a methodological paper on multimodal intent analysis.

## Implementation status

The checked-in Python module implements the core dHash classifier and Tier E contextual matching described in v5.3. Advanced image analysis, automated ingestion, database persistence, privacy transformations, bibliometric processing, and the visualization engine are documented requirements and future implementation work; they are not represented as completed features.
