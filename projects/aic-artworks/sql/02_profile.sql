SELECT COUNT(*) AS row_count FROM artworks;
SELECT COUNT(*) AS column_count FROM (DESCRIBE artworks);

SELECT is_public_domain, COUNT(*) AS n,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct
FROM artworks_typed
GROUP BY 1
ORDER BY 1;

SELECT department, COUNT(*) AS n
FROM artworks_typed
GROUP BY 1
ORDER BY n DESC;

SELECT
    ROUND(100.0 * AVG((title IS NULL OR title = '')::INT), 2) AS title_blank_pct,
    ROUND(100.0 * AVG((artist_display IS NULL OR artist_display = '')::INT), 2) AS artist_blank_pct,
    ROUND(100.0 * AVG((classification IS NULL OR classification = '')::INT), 2) AS classification_blank_pct,
    ROUND(100.0 * AVG((medium IS NULL OR medium = '')::INT), 2) AS medium_blank_pct,
    ROUND(100.0 * AVG((place_of_origin IS NULL OR place_of_origin = '')::INT), 2) AS place_blank_pct
FROM artworks_typed;
