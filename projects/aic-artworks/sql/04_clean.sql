-- Cleaning rules (non-destructive: the raw table is untouched).
--   1. A year outside -10000..2100 is treated as unreliable and set to NULL in the *_clean column.
--   2. Rows where end date is before start date are flagged, not altered; the cause is not knowable from the data.
CREATE OR REPLACE VIEW artworks_clean AS
SELECT
    t.*,
    CASE WHEN t.date_start BETWEEN -10000 AND 2100 THEN t.date_start END AS date_start_clean,
    CASE WHEN t.date_end BETWEEN -10000 AND 2100 THEN t.date_end END AS date_end_clean,
    COALESCE(t.date_start NOT BETWEEN -10000 AND 2100, FALSE)
    OR COALESCE(t.date_end NOT BETWEEN -10000 AND 2100, FALSE) AS year_out_of_range,
    COALESCE(t.date_end < t.date_start, FALSE) AS year_order_issue
FROM artworks_typed AS t;

-- What the rules changed
SELECT
    COUNT(*) AS records,
    SUM(year_out_of_range::INT) AS year_out_of_range,
    SUM(year_order_issue::INT) AS year_order_issue,
    SUM((date_start IS NOT NULL AND date_start_clean IS NULL)::INT) AS date_start_nulled,
    SUM((date_end IS NOT NULL AND date_end_clean IS NULL)::INT) AS date_end_nulled
FROM artworks_clean;

-- Post-clean check: no out-of-range values remain in the cleaned columns (0 is a pass)
SELECT COUNT(*) AS remaining_out_of_range
FROM artworks_clean
WHERE date_start_clean NOT BETWEEN -10000 AND 2100 OR date_end_clean NOT BETWEEN -10000 AND 2100;
