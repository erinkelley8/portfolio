# Profile report: Met Open Access

Snapshot: 2026-10-09 (UTC), `MetObjects.csv`, 317,650,992 bytes, SHA-256 `de617b9c...0b9183` (full value in `manifest.json`).
Source: The Metropolitan Museum of Art Open Access dataset (CC0). Results describe the collection as of this snapshot and were produced by transforming the source data with `sql/`.

## Size
| Measure | Value |
|---|---|
| Records | 484,956 |
| Columns | 54 |

## Open-access coverage
| Public domain | Records | Share |
|---|---|---|
| True | 248,472 | 51.24% |
| False | 236,484 | 48.76% |

Public-domain share varies widely by department: highest in Ancient Near Eastern Art (99.5%), The Cloisters (97.0%) and Medieval Art (96.9%); lowest in Modern and Contemporary Art (1.4%), Photographs (17.1%) and Costume Institute (26.3%).

## Largest departments
Drawings and Prints (172,630), European Sculpture and Decorative Arts (43,051), Photographs (37,459), Asian Art (37,000), Greek and Roman Art (33,726).

## Completeness (blank rate)
| Field | Blank |
|---|---|
| Medium | 1.49% |
| Title | 5.91% |
| Classification | 16.23% |
| Artist display name | 41.74% |
| Culture | 57.07% |

## Quality checks
| Check | Failures | Note |
|---|---|---|
| Object ID missing | 0 | pass |
| Object ID duplicated | 0 | pass |
| Department missing | 0 | pass |
| End year before begin year | 205 | needs review; likely BCE/CE entry conventions |
| Year outside -10,000..2,100 | 47 | includes extreme values such as -400,000 |
| Title missing | 28,664 | 5.91% of records |

## Caveats
- Year fields are free-form in the source and were parsed with `TRY_CAST`; unparseable values become null.
- "Blank" counts treat empty strings and nulls the same.
- No personal-data concerns were identified in the fields profiled.

## Cleaning (`sql/04_clean.sql`)
Non-destructive: the raw table is unchanged and a view `objects_clean` adds cleaned columns and flags.

| Rule | Effect |
|---|---|
| Years outside -10,000..2,100 set to NULL in `*_clean` columns | 47 begin years and 15 end years nulled; 49 records flagged `year_out_of_range` |
| End year before begin year is flagged, not altered | 205 records flagged `year_order_issue` |
| Post-clean check: out-of-range values remaining | 0 |

Century analysis (`sql/05_analysis.sql`) uses the cleaned begin year; records with an out-of-range year are grouped as "unknown".
