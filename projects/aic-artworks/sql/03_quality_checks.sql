-- Each check returns the number of offending rows; 0 is a pass.

SELECT 'artwork_id_null' AS check_name, COUNT(*) AS failures
FROM artworks_typed WHERE artwork_id IS NULL
UNION ALL
SELECT 'artwork_id_duplicate', COUNT(*) - COUNT(DISTINCT artwork_id)
FROM artworks_typed WHERE artwork_id IS NOT NULL
UNION ALL
SELECT 'date_end_before_date_start', COUNT(*)
FROM artworks_typed WHERE date_end < date_start
UNION ALL
SELECT 'year_outside_plausible_range', COUNT(*)
FROM artworks_typed WHERE date_start < -10000 OR date_end > 2100
UNION ALL
SELECT 'title_missing', COUNT(*)
FROM artworks_typed WHERE title IS NULL OR title = ''
UNION ALL
SELECT 'department_missing', COUNT(*)
FROM artworks_typed WHERE department IS NULL OR department = '';
