-- This model cleans the raw data
{{ config(materialized='view') }}

with source as (
    select * from {{ ref('taxi_rides_raw') }}
)

select
    VendorID as vendor_id,
    tpep_pickup_datetime as pickup_datetime,
    tpep_dropoff_datetime as dropoff_datetime,
    
    -- Here we handle the bad data found in the test
    case 
        when Passenger_count not in (1, 2, 3, 4, 5, 6) then 1 -- Defaulting to 1, or you could keep as is
        else Passenger_count 
    end as passenger_count,
    payment_type,
    trip_distance,
    fare_amount,
    tip_amount, 
    tolls_amount, 
    total_amount
from source
where trip_distance > 0 -- Cleaning out junk trips