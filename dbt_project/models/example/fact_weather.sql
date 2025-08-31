-- models/fact_weather.sql
-- This model is a view in dbt, but it queries a pre-existing view in PostgreSQL.

-- It's a good practice to use the `ref` function to refer to other models
-- or the `source` function to refer to pre-existing data.
-- Since you're using a view as your base, let's treat it as a source.

{{ config(
    materialized='table'
) }}

SELECT
    timestamp_utc,
    temperature,
    humidity,
    -- Add more transformations here if needed
    (temperature * 9/5) + 32 AS temperature_fahrenheit
FROM
    {{ source('weather_data', 'your_postgresql_view_name') }}