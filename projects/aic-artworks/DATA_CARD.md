# Data card: AIC artworks

| Field | Value |
|---|---|
| Publisher | Art Institute of Chicago |
| Source | https://github.com/art-institute-of-chicago/api-data (full archive linked from its README) |
| Download URL used | `https://artic-api-data.s3.amazonaws.com/artic-api-data.tar.bz2` |
| Size | ~115 MB compressed, ~2.5 GB extracted (only artworks are extracted here) |
| Licence | Metadata CC0 1.0; `description` field CC BY 4.0; see each record's `info`/licence fields. Images and media may have different terms and are not downloaded. |
| Content | Artwork metadata in the API's JSON schema, one file per record |
| Method | One-time bulk snapshot, manually triggered. The API is not used. |
| Snapshot date / checksum | See `manifest.json` |
| Update behaviour | Source dump is refreshed by AIC (monthly per source docs); this repo does not auto-refresh |

## Intended use
Descriptive analysis of collection composition, public-domain coverage, and metadata completeness.

## Known limits
- Not all artworks or images are public domain; flag is analysed, not assumed.
- JSON schema may evolve; field names in `sql/01_load.sql` are confirmed with `DESCRIBE` on first load.
- Results describe the collection as of the snapshot date only.

## Privacy check
Records describe artworks and their makers. No personal data about living private individuals is expected. If any is found, document it here and stop.

## If the API is ever used
Follow the documented limits (anonymous: 60 requests/minute, max 100 per page, no parallel scraping) and send an identifying `AIC-User-Agent` header.
