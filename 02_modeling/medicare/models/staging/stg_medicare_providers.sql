
{{
    config(
        materialized='view'
    )
}}

with medicare_providers as
(
  select *,
    row_number() over(partition by unique_row_id, filename) as rn
  from {{ source('staging','providers') }}
)
select
    *,
    CAST(REGEXP_EXTRACT(filename, r'(\d{4})') AS INT64) AS year

from medicare_providers
where rn = 1