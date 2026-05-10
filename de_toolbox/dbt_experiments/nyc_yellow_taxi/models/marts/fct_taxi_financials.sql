{{ config(materialized='table') }}

select
    -- loop using jinja
    {% for col in ['fare_amount', 'tip_amount', 'tolls_amount', 'total_amount'] %}
        {{ col}}{% if not loop.last %},{% endif %}
    {% endfor %}
from {{ ref('stg_taxi_rides') }}