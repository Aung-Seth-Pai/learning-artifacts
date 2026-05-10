{{ config(materialized='table') }}

select 
    date_trunc('day', pickup_datetime) as pickup_day,
    count(*) as total_cc_riders
    
from {{ ref('stg_taxi_rides') }}

-- Payment type 1 equals Credit Card based on the data dictionary
where payment_type = 1

group by 1