{{ config(materialized='table') }}

with source_data as (
    SELECT * FROM read_parquet('yellow_tripdata_2026-01.parquet')
)

SELECT * FROM source_data