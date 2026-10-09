# 0001: Use bulk snapshots instead of live APIs

Status: Accepted

## Context
Both sources offer APIs and bulk exports. The Met API serves one object per call (~470k calls for the full set). The AIC API is capped at 60 requests/minute and 10k search results, and AIC states its data dumps are intended for analysis and large-scale use.

## Decision
Use the official bulk exports: Met Open Access CSV and the AIC `api-data` JSON dump. Take a one-time, manually triggered, pinned snapshot per dataset.

## Consequences
- No API keys, credentials, or rate-limit exposure.
- Reproducible: URL, retrieval date, and SHA-256 recorded in a manifest.
- Results describe the data "as of" the snapshot date; refresh is a manual re-run.
- No scheduled jobs or automated downloads.
