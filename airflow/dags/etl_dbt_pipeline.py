from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('etl_dbt_pipeline', start_date=datetime(2025, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    etl = BashOperator(
        task_id='run_etl',
        bash_command='docker run --rm etl-image'
    )

    dbt = BashOperator(
        task_id='run_dbt',
        bash_command='docker run --rm dbt-image dbt run --profiles-dir /app/profiles'
    )

    etl >> dbt
