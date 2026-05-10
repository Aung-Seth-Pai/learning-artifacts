# dbt Learning Artifacts

Hands-on learning notes and a mini-project for **dbt (data build tool)** — the transformation layer in the modern ELT stack.

## What's Inside

### `dbt_basics.ipynb`
notebook covering core dbt concepts:
- What dbt solves (modular SQL, testing, documentation, lineage)
- Project structure (`dbt_project.yml`, `profiles.yml`, `model_properties.yml`)
- Jinja templates and the `ref()` function
- Medallion Architecture (Bronze → Silver → Gold)
- The `dbt run` lifecycle (compilation → connection → materialization → manifest)
- `dbt test` and `dbt docs`

### `nyc_yellow_taxi/` — Mini-Project
A complete dbt project built on [NYC Yellow Taxi trip data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) using **DuckDB** as the local warehouse.

#### Pipeline Architecture (Medallion)

```
Parquet File (source)
    │
    ▼
┌──────────────────┐
│  taxi_rides_raw  │  ← Bronze: raw ingestion from parquet
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  stg_taxi_rides  │  ← Silver: cleaned column names, filtered bad data
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌─────────┐ ┌─────────────────────┐
│ fct_taxi│ │ agg_daily_cc_riders │  ← Gold: business-ready tables
│_finance │ │                     │
└─────────┘ └─────────────────────┘
```

#### Key Models

| Model | Layer | Materialization | Description |
|-------|-------|-----------------|-------------|
| `taxi_rides_raw` | Bronze | table | Reads the raw parquet file into DuckDB |
| `stg_taxi_rides` | Silver | view | Renames columns, cleans bad passenger counts, filters zero-distance trips |
| `fct_taxi_financials` | Gold | table | Financial columns extracted using Jinja `for` loop |
| `agg_daily_cc_riders` | Gold | table | Daily aggregation of credit-card riders |

#### Data Quality Tests
Defined in `model_properties.yml`:
- `not_null` on `vendorid` and `tpep_pickup_datetime`
- `accepted_values` on `Passenger_count` (1–6)

#### `explore_warehouse.ipynb`
Companion notebook for querying the DuckDB warehouse after `dbt run`:
- Inspecting table schemas and sample data
- Identifying data quality issues (e.g., rides with 0 passengers)
- Dropping orphaned tables from previous model iterations

## Getting Started

### Prerequisites
```bash
# From the repo root, install dbt dependencies
uv sync --extra de_toolbox_dbt_experiments
```

### Download the Data
1. Go to the [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) page.
2. Download the **Yellow Taxi Trip Records** parquet file for the desired month (e.g., January 2026).
3. Place it inside `nyc_yellow_taxi/` as `yellow_tripdata_2026-01.parquet`.

### Run the Project
```bash
cd de_toolbox/dbt_experiments/nyc_yellow_taxi

# Verify your configuration
dbt debug

# Build all models (Bronze → Silver → Gold)
dbt run

# Run data quality tests
dbt test

# Generate documentation and view the lineage DAG
dbt docs generate
dbt docs serve
```

## References
- [Introduction to dbt](https://app.datacamp.com/learn/courses/introduction-to-dbt) — DataCamp course by **Mike Metzger**
- [dbt Documentation](https://docs.getdbt.com/docs/introduction)
- [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [dbt + DuckDB Guide](https://docs.getdbt.com/docs/core/connect-data-platform/duckdb-setup)

