-- Each check returns the number of offending rows; 0 is a pass.

SELECT
    'object_id_null' AS check_name,
    COUNT(*) AS failures
FROM objects_typed
WHERE object_id IS NULL
UNION ALL
SELECT
    'object_id_duplicate',
    COUNT(*) - COUNT(DISTINCT object_id)
FROM objects_typed
WHERE object_id IS NOT NULL
UNION ALL
SELECT
    'end_year_before_begin_year',
    COUNT(*)
FROM objects_typed
WHERE end_year < begin_year
UNION ALL
SELECT
    'year_outside_plausible_range',
    COUNT(*)
FROM objects_typed
WHERE begin_year < -10000 OR end_year > 2100
UNION ALL
SELECT
    'title_missing',
    COUNT(*)
FROM objects_typed
WHERE title IS NULL OR title = ''
UNION ALL
SELECT
    'department_missing',
    COUNT(*)
FROM objects_typed
WHERE department IS NULL OR department = '';
