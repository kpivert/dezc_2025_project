{{ config(materialized='table') }}

with medicare_providers as (
    select * from `dezc-final-project-medicare`.`medicare`.`providers`
)

SELECT
  CAST(REGEXP_EXTRACT(filename, r'(\d{4})') AS INT64) AS year,
  COUNT(*) AS providers
FROM medicare_providers
GROUP BY year
ORDER BY year;