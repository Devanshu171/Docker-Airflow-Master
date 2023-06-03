from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from bots.python_helper import call

default_args={
  "owner":"dev",
  "start_date":datetime(2023,6,2)
}

with DAG(
  dag_id="pythonOpertor",
  default_args=default_args,
  schedule_interval=None,
  ) as dag:
  start_dag=PythonOperator(
    task_id="start_id",
    python_callable=call
  )
  
  start_dag