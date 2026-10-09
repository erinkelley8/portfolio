# Profile report: AIC artworks

Snapshot: 2026-10-09 (UTC), `artic-api-data.tar.bz2` (130,131,744 bytes), SHA-256 `8af7838a...6edd50c` (full value in `manifest.json`).
Source: Art Institute of Chicago public data dump, artworks only. Metadata is CC0; the `description` field is CC BY 4.0 and is not reproduced here. Results describe the collection as of this snapshot and were produced by transforming the source data with `sql/`.

## Size
| Measure | Value |
|---|---|
| Artwork records | 139,699 |
| Columns (after load) | 99 |

## Public-domain flag
| `is_public_domain` | Records | Share |
|---|---|---|
| True | 62,072 | 44.43% |
| False | 77,627 | 55.57% |

This is a metadata flag about the artwork. It is not a statement about image rights, which are handled separately by the source.

Share varies by department: Arts of Greece, Rome, and Byzantium 93.5%, Applied Arts of Europe 90.0%, Painting and Sculpture of Europe 85.2%; Contemporary Art and AIC Archives 0%; Photography and Media 16.9%.

## Largest departments
Prints and Drawings (53,816), Photography and Media (24,793), Arts of Asia (17,024), Textiles (11,736), Architecture and Design (6,172). 6,805 records (4.9%) have no department.

## Completeness (blank rate)
| Field | Blank |
|---|---|
| Title | 0.00% |
| Artist display | 0.06% |
| Medium | 0.87% |
| Classification | 2.08% |
| Place of origin | 7.56% |

## Quality checks
| Check | Failures | Note |
|---|---|---|
| Artwork ID missing | 0 | pass |
| Artwork ID duplicated | 0 | pass |
| End date before start date | 0 | pass |
| Year outside -10,000..2,100 | 17 | includes values such as -1,824,528,600 |
| Title missing | 1 | |
| Department missing | 6,805 | 4.9% of records; 43 of these are flagged public domain |

## Caveats
- Source schema is nested (arrays and structs); the analysis uses a flat typed view of selected fields.
- Records were streamed from the archive into one JSON Lines file for loading; content is otherwise unchanged.
- No personal-data concerns were identified in the fields profiled.

## Cleaning (`sql/04_clean.sql`)
Non-destructive: the raw table is unchanged and a view `artworks_clean` adds cleaned columns and flags.

| Rule | Effect |
|---|---|
| Years outside -10,000..2,100 set to NULL in `*_clean` columns | 13 start dates and 6 end dates nulled; 17 records flagged `year_out_of_range` |
| End date before start date is flagged, not altered | 0 records flagged `year_order_issue` |
| Post-clean check: out-of-range values remaining | 0 |

Century analysis (`sql/05_analysis.sql`) uses the cleaned start date; records with an out-of-range year are grouped as "unknown".
