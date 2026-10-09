-- Cleaning rules (non-destructive: the raw table is untouched).
--   1. A year outside -10000..2100 is treated as unreliable and set to NULL in the *_clean column.
--   2. Rows where end year is before begin year are flagged, not altered; the cause is not knowable from the data.
CREATE OR REPLACE VIEW objects_clean AS
SELECT
    t.*,
    CASE WHEN t.begin_year BETWEEN -10000 AND 2100 THEN t.begin_year END AS begin_year_clean,
    CASE WHEN t.end_year BETWEEN -10000 AND 2100 THEN t.end_year END AS end_year_clean,
    COALESCE(t.begin_year NOT BETWEEN -10000 AND 2100, FALSE)
    OR COALESCE(t.end_year NOT BETWEEN -10000 AND 2100, FALSE) AS year_out_of_range,
    COALESCE(t.end_year < t.begin_year, FALSE) AS year_order_issue
FROM objects_typed AS t;

-- What the rules changed
SELECT
    COUNT(*) AS records,
    SUM(year_out_of_range::INT) AS year_out_of_range,
    SUM(year_order_issue::INT) AS year_order_issue,
    SUM((begin_year IS NOT NULL AND begin_year_clean IS NULL)::INT) AS begin_year_nulled,
    SUM((end_year IS NOT NULL AND end_year_clean IS NULL)::INT) AS end_year_nulled
FROM objects_clean;

-- Post-clean check: no out-of-range values remain in the cleaned columns (0 is a pass)
SELECT COUNT(*) AS remaining_out_of_range
FROM objects_clean
WHERE begin_year_clean NOT BETWEEN -10000 AND 2100 OR end_year_clean NOT BETWEEN -10000 AND 2100;
