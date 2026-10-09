-- Public-domain share by department
SELECT
    department,
    COUNT(*) AS artworks,
    SUM(is_public_domain::INT) AS public_domain,
    ROUND(100.0 * AVG(is_public_domain::INT), 1) AS public_domain_pct
FROM artworks_typed
GROUP BY 1
ORDER BY artworks DESC;

-- Artworks by century of creation (cleaned start year; out-of-range years grouped as unknown)
SELECT
    CASE
        WHEN date_start_clean IS NULL THEN 'unknown'
        ELSE ((FLOOR(date_start_clean / 100.0) * 100)::BIGINT)::VARCHAR
    END AS century_start,
    COUNT(*) AS artworks
FROM artworks_clean
GROUP BY 1
ORDER BY TRY_CAST(century_start AS INTEGER) NULLS LAST;

-- Most common artwork types
SELECT
    artwork_type,
    COUNT(*) AS artworks
FROM artworks_typed
WHERE artwork_type IS NOT NULL
GROUP BY 1
ORDER BY artworks DESC
LIMIT 20;
