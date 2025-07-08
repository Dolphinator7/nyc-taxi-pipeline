from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 1),
    'retries': 1,
}

with DAG(
    dag_id='ingest_yellow_taxi',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False,
    tags=['ny_taxi'],
) as dag:

    ingest_to_postgres = BashOperator(
        task_id='ingest_csv_to_postgres',
        bash_command=(
            'python /opt/airflow/dags/ingest_data.py '
            '--user=root '
            '--password=root '
            '--host=postgres '
            '--port=5432 '
            '--db=ny_taxi '
            '--table_name=yellow_taxi_data '
            '--csv_file=/opt/airflow/dags/yellow_tripdata_2021-01.csv'
        ),
    )
