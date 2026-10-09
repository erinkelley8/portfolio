# Portfolio

A working portfolio demonstrating **technology leadership, data analysis, data governance, and AI-agent governance** through reproducible, well-documented projects on open datasets.

## What this repo shows

| Capability | Where to look |
|---|---|
| Data analysis (SQL-first, DuckDB) | `projects/*/sql/`, `projects/*/reports/` |
| Data governance (licensing, lineage, quality, privacy) | `docs/governance/`, `projects/*/DATA_CARD.md`, `projects/*/LICENSE_NOTES.md` |
| AI-agent governance (scope, permissions, oversight) | `CLAUDE.md`, `.claude/`, `docs/governance/ai-agent-governance.md` |
| Engineering leadership (decisions, standards, CI) | `docs/decisions/`, `.github/`, `CONTRIBUTING.md` |

## Projects

| Project | Source | License | Method |
|---|---|---|---|
| [met-museum-open-access](projects/met-museum-open-access/) | The Met Open Access CSV | CC0 | Bulk snapshot |
| [aic-artworks](projects/aic-artworks/) | Art Institute of Chicago data dump | CC0 metadata (descriptions CC BY 4.0) | Bulk snapshot |

## Principles

- **Reproducible**: every project pins its source, retrieval date, and checksum in a manifest.
- **Safe by default**: no secrets, no raw third-party data or images in git, least-privilege agent permissions.
- **Documented decisions**: architecture decision records in [docs/decisions](docs/decisions/).
- **Governed AI use**: AI agents operate under written rules in [CLAUDE.md](CLAUDE.md).

## Getting started

See [docs/runbook.md](docs/runbook.md).

## License

Code is MIT licensed (see [LICENSE](LICENSE)). Data licences are per-project; see each project's `LICENSE_NOTES.md`.
