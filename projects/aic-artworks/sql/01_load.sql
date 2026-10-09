-- Load AIC artwork JSON files into DuckDB. Run from the repo root.
-- Field names follow the AIC API artwork schema; confirm against the first load with DESCRIBE.
CREATE OR REPLACE TABLE artworks AS
SELECT *
FROM READ_NDJSON(
    'projects/aic-artworks/data/raw/artworks.jsonl',
    sample_size = -1,
    maximum_object_size = 4194304
);

CREATE OR REPLACE VIEW artworks_typed AS
SELECT
    id AS artwork_id,
    title,
    artist_display,
    date_start,
    date_end,
    department_title AS department,
    artwork_type_title AS artwork_type,
    classification_title AS classification,
    place_of_origin,
    medium_display AS medium,
    is_public_domain
FROM artworks;
