-- Row and column counts
SELECT COUNT(*) AS row_count FROM objects;
SELECT COUNT(*) AS column_count FROM (DESCRIBE objects);

-- Share of records by public-domain flag
SELECT is_public_domain, COUNT(*) AS n,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct
FROM objects_typed
GROUP BY 1
ORDER BY 1;

-- Records by department
SELECT department, COUNT(*) AS n
FROM objects_typed
GROUP BY 1
ORDER BY n DESC;

-- Blank rate for key fields
SELECT
    ROUND(100.0 * AVG((title IS NULL OR title = '')::INT), 2) AS title_blank_pct,
    ROUND(100.0 * AVG((culture IS NULL OR culture = '')::INT), 2) AS culture_blank_pct,
    ROUND(100.0 * AVG((artist_display_name IS NULL OR artist_display_name = '')::INT), 2) AS artist_blank_pct,
    ROUND(100.0 * AVG((classification IS NULL OR classification = '')::INT), 2) AS classification_blank_pct,
    ROUND(100.0 * AVG((medium IS NULL OR medium = '')::INT), 2) AS medium_blank_pct
FROM objects_typed;
