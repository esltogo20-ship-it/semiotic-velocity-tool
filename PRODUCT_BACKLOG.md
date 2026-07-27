# Product Backlog

## Product goal

Develop a reproducible, human-validated research instrument for identifying, coding and analysing changes in the meaning and circulation of culturally persistent visual signs.

This is an ordered Scrum product backlog. Story points are relative estimates, not measures of scientific progress.

| Order | Product backlog item | Priority | Points | Acceptance criteria |
|---:|---|---|---:|---|
| 1 | Define the v6 coding manual | P0 | 8 | Visual A–E and nominal N1–N3 categories have definitions, inclusion rules, exclusions and examples. |
| 2 | Finalize the research database | P0 | 8 | Versioned migrations implement provenance, coding, adjudication, ΔS/Δt and F1–F3 tables. |
| 3 | Implement record persistence | P0 | 5 | Candidate records can be created, retrieved, updated and exported without losing provenance. |
| 4 | Build the human-review interface | P0 | 13 | Reviewers can inspect candidates, assign codes, record confidence and leave evidence notes. |
| 5 | Add double coding and adjudication | P0 | 8 | Two independent coders and an adjudicator can produce an auditable final classification. |
| 6 | Create the validation corpus | P0 | 13 | A manually coded reference set covers every visual and nominal category, including difficult negatives. |
| 7 | Calibrate dHash thresholds | P0 | 5 | Thresholds are evaluated against the validation corpus and reported with precision, recall and F1. |
| 8 | Implement pHash retrieval | P1 | 5 | pHash produces candidate similarities while retaining raw scores and algorithm versions. |
| 9 | Implement CLIP retrieval | P1 | 8 | CLIP retrieves candidates without treating embedding similarity as semantic classification. |
| 10 | Add OCR and caption extraction | P1 | 8 | Extracted text is stored separately and can enter the linguistic pipeline. |
| 11 | Implement structural retrieval | P1 | 13 | SIFT/ORB or pose methods identify candidates for remote visual echoes. |
| 12 | Add compliant corpus ingestion | P1 | 13 | Approved sources are ingested with rate limits, provenance and platform controls. |
| 13 | Implement privacy transformations | P1 | 8 | User identifiers are pseudonymized and unnecessary personal information is excluded. |
| 14 | Calculate circulatory velocity | P1 | 5 | Reproduction frequency is calculated independently from semantic displacement. |
| 15 | Calculate semiotic velocity | P1 | 8 | Velocity is calculated from human-coded ΔS and explicit Δt values. |
| 16 | Implement F1–F3 analysis | P1 | 8 | Performative, institutional and technological friction variables can be coded and compared. |
| 17 | Produce research visualizations | P2 | 8 | Publication-quality charts show circulation, displacement, velocity, uncertainty and event windows. |
| 18 | Add CSV/JSON exports | P2 | 5 | Exports include configuration and coding-scheme versions without restricted source material. |
| 19 | Expand automated testing and CI | P1 | 5 | Unit, integration, schema and regression tests run on pull requests. |
| 20 | Prepare reproducibility documentation | P2 | 8 | Installation, coding, limitations, ethics and data-management procedures are documented. |

## First research release

The first defensible research release requires items 1–7, 15, 19 and 20. Advanced retrieval should follow only after the coding system and validation corpus are stable.

## Definition of done

An item is done only when:

- its acceptance criteria are satisfied;
- relevant tests pass;
- assumptions and limitations are documented;
- configuration, provenance and coding-scheme versions are recorded;
- privacy and ethical implications are reviewed;
- another researcher can reproduce or audit the result;
- the README distinguishes implemented and planned functionality accurately.

Software completion does not constitute methodological or empirical validation.
