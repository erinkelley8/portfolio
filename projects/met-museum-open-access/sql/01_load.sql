-- Load the Met Open Access snapshot into DuckDB. Run from the repo root.
CREATE OR REPLACE TABLE objects AS
SELECT *
FROM read_csv(
    'projects/met-museum-open-access/data/raw/MetObjects.csv',
    header = true,
    all_varchar = true,
    sample_size = -1
);

-- Typed view used by the later steps
CREATE OR REPLACE VIEW objects_typed AS
SELECT
    TRY_CAST("Object ID" AS BIGINT) AS object_id,
    "Is Public Domain" = 'True' AS is_public_domain,
    "Is Highlight" = 'True' AS is_highlight,
    "Department" AS department,
    "Object Name" AS object_name,
    "Title" AS title,
    "Culture" AS culture,
    "Artist Display Name" AS artist_display_name,
    TRY_CAST("Object Begin Date" AS INTEGER) AS begin_year,
    TRY_CAST("Object End Date" AS INTEGER) AS end_year,
    "Classification" AS classification,
    "Medium" AS medium,
    "Link Resource" AS link_resource
FROM objects;
