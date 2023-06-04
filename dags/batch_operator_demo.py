from datetime import datetime
from airflow import DAG

from airflow.operators.bash_operator import BashOperator


default_args={ 
  "owner":"dev",
  "start_date":datetime(2023,6,3),
  
  }

with DAG(
  dag_id="batchOperatorDemo0.0",
  default_args=default_args,
  schedule_interval=None
  ) as dag:
  
  start_dag=BashOperator(
    task_id="start_dag",
    bash_command="date"
  )
  
  start_dag