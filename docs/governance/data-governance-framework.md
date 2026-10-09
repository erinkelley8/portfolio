# Data governance framework

Lightweight framework applied to every project in this repo.

## Principles
1. **Provenance**: every dataset has a documented source, licence, retrieval date and checksum.
2. **Minimisation**: collect metadata only; no images; keep only fields needed for the analysis.
3. **Lawful and licensed use**: usage follows the source licence and terms; attribution is recorded.
4. **Quality is measured**: each snapshot is profiled and issues are listed, not hidden.
5. **Reproducibility**: transformations are versioned SQL; raw data is re-obtainable from the source.
6. **Security by default**: no secrets or third-party data in git; least-privilege tooling.

## Roles (single-maintainer repo)
| Role | Responsibility |
|---|---|
| Data owner | Maintainer: approves sources, licences, and downloads |
| Data steward | Maintainer: maintains data cards, dictionaries, quality reports |
| AI agent | Executes scoped tasks under `CLAUDE.md`; cannot approve its own downloads or pushes |

## Lifecycle controls
| Stage | Control | Evidence |
|---|---|---|
| Intake | Source and licence assessed | `DATA_CARD.md`, `LICENSE_NOTES.md` |
| Acquisition | HTTPS, pinned URL, checksum, manual trigger | `manifest.json` |
| Storage | Local only, gitignored | `.gitignore`, `git ls-files` check in CI |
| Processing | Numbered SQL, no hidden steps | `sql/` |
| Quality | Profiling + checks per snapshot | `reports/profile.md` |
| Publication | Aggregates and code only; attribution kept | project README |
| Retention | Raw data deleted at will; re-fetchable | `DATA_CARD.md` |

## Review
Run the `data-governance-review` skill before merging a new or changed project.
