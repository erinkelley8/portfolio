---
name: data-profiling
description: Run standard profiling and data-quality checks on a project dataset using DuckDB SQL and write a short report. Use after loading a new snapshot.
---

# Data profiling

Run with `uv run python tools/run_sql.py <project>` (use `--only 02` for one step). Paths in the SQL are relative to the repo root, and the local DuckDB database is never committed.

Checks, each as a query in `02_profile.sql` / `03_quality_checks.sql`:
- Row count and column count; compare to the source's stated size.
- Per-column null/empty rate and distinct count.
- Primary-key uniqueness and duplicate rows.
- Date and numeric sanity (min/max, impossible values, e.g. end before begin).
- Categorical value frequencies for key fields (department, classification, public-domain flag).
- Licence-relevant flags (public domain / open access) and their counts.

Output: update `reports/profile.md` with counts, findings, and the snapshot date from `manifest.json`. Keep the report small; no raw records, no images, no personal data.
