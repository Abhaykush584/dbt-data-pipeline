from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A DAG to ingest weather data and run dbt models.',
    schedule_interval=timedelta(days=1), # or '0 8 * * *' for 8 AM daily
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['dbt', 'postgres'],
) as dag:
    # Task to ingest data from API
    ingest_task = BashOperator(
        task_id='ingest_weather_data',
        bash_command='python C:/Users/abhay/dbt_pipeline_project/data/ingest_api_data.py',
    )

    # Task to run dbt models
    dbt_run_task = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd C:/Users/abhay/dbt_pipeline_project/dbt_project && dbt run',
    )

    # Set the task dependencies
    ingest_task >> dbt_run_task