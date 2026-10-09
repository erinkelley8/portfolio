-- Public-domain share by department
SELECT department,
       COUNT(*) AS objects,
       SUM(is_public_domain::INT) AS public_domain,
       ROUND(100.0 * AVG(is_public_domain::INT), 1) AS public_domain_pct
FROM objects_typed
GROUP BY 1
ORDER BY objects DESC;

-- Collection by century of creation (begin year)
SELECT
    CASE WHEN begin_year IS NULL THEN 'unknown'
         ELSE CAST(FLOOR(begin_year / 100.0) * 100 AS VARCHAR) END AS century_start,
    COUNT(*) AS objects
FROM objects_typed
GROUP BY 1
ORDER BY TRY_CAST(century_start AS INTEGER) NULLS LAST;

-- Most common classifications
SELECT classification, COUNT(*) AS objects
FROM objects_typed
WHERE classification IS NOT NULL AND classification <> ''
GROUP BY 1
ORDER BY objects DESC
LIMIT 20;
