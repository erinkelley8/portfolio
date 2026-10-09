# 0002: DuckDB with SQL-first analysis

Status: Accepted

## Context
Datasets are hundreds of thousands of records in CSV and JSON. The goal is transparent, reviewable analysis without running a database server.

## Decision
Use DuckDB (embedded, local, queries CSV/JSON directly). Analysis lives in numbered `.sql` files. Python is limited to download, load, and run orchestration.

## Consequences
- Analysis is readable by anyone who knows SQL.
- No server, credentials, or cloud dependency; data stays local.
- Single-machine scale, which is sufficient for these datasets.
