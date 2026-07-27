# Semiotic Velocity Tool — Technical Specification v5.3

## Purpose

The instrument operationalizes **semiotic velocity**: the rate at which a visual sign's dominant meaning shifts across political and temporal contexts. The proof of concept tracks derivatives and nominal deployments of Jan Matejko's *Stańczyk* (1862) across Polish digital platforms from 2010 to the present.

## System architecture

The system uses three coordinated modules:

1. **Visual stream (Tiers A–D):** dHash and pHash cluster direct and close image variants. Tier D routes high-level abstractions to SIFT feature matching, pose mapping, and contextual NLP.
2. **Linguistic stream (Tier E):** Polish declension matching and contextual anchors identify nominal deployments while filtering false positives.
3. **Bibliometric ingest:** Google Books Ngram Viewer CSV data provides a pre-digital longitudinal baseline.

All accepted records flow into a unified database and visualization engine.

## Data ingestion and compliance

- Automated, rate-limited collection targets Demotywatory.pl, Kwejk.pl, and Wykop only where permitted by each platform's current `robots.txt` and terms.
- X/Twitter records are manually captured unless paid institutional API access is secured.
- The v5.3 baseline contains 75 historical records. Legacy imports use a `legacy_record` flag.
- Historical anchors include the 1969 *Śmiejmy się przez cały rok* annual, the Ossolineum/Muzeum Książąt Lubomirskich *Wesele* postcard cluster (1905–1936), and Kazimierz Sichulski's *Apoteoza* (1938).
- ZNiO material requires the applicable copyright attribution.
- Usernames are pseudonymized using SHA-256 with a rotating salt.
- Personally identifiable information is removed from captions during ingest.
- Non-public faces encountered in Tier D pose processing are blurred.

## Taxonomy

| Tier | Label | Description | Identification |
|---|---|---|---|
| A | Direct reproduction | Original canvas unaltered | dHash distance ≤ 5 |
| B | Close derivative | Composition retained; one item replaced or caption added | Distance ≤ 12 plus secondary check |
| C | Loose derivative | Posture or scene partly altered, overlaid, or cropped | Distance ≤ 20 plus OCR |
| D | Grammar-only / intertextual | Structural grammar reproduced without direct copying | SIFT, pose mapping, and contextual NLP |
| E | Nominal | Meaning carried solely by language | Polish morphology plus anchor validation |

In the recalibrated 75-row v5.3 baseline, Tier B accounts for 24% and Tier C for 37%.

## Canonical configuration

The v5.3 configuration defines:

- target ID `stanczyk_1862`;
- National Museum in Warsaw metadata and inventory `MP 434`;
- visual thresholds of 5, 12, and 20, with Tier D SIFT threshold 40;
- Tier D grammar-only, intertextual, and stylistic-derivative subtypes;
- Polish inflectional roots and the `STAŃ` fragment;
- primary, secondary, and exclusion anchors;
- Wyspiański, *Wesele*, and Wajda as intertextual entities;
- the 2010 Smolensk air disaster and 2023 Polish parliamentary election as event markers.

## Repository implementation

- `main.py` implements the core dHash visual classifier and contextual nominal classifier.
- `config/grammar_v1_stanczyk.yaml` is the canonical visual-grammar configuration.
- `requirements.txt` pins the v5.3 Python dependencies.

Advanced SIFT, pose estimation, OCR, bibliometric ingestion, persistence, privacy automation, and visualization remain specified extension points rather than completed components of the core example pipeline.
