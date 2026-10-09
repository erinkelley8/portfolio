# 0003: Raw data is never committed

Status: Accepted

## Context
Source files are large and owned by third parties with specific terms. Git history is permanent.

## Decision
`data/raw/` and `data/processed/` are gitignored in every project. Only code, SQL, documentation, manifests, and small aggregate reports are committed. CI verifies no data files are tracked.

## Consequences
- Small repo; no redistribution of third-party content.
- Anyone can rebuild from the source using the manifest and runbook.
