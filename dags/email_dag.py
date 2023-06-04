from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from bots.emailhelper import send


default_args={
  "owner":"dev",
  "start_date":datetime(2023,1,3)
}

with DAG(
  dag_id="PythonEmail",
  default_args=default_args,
  schedule_interval=None
  ) as dag:
  
  start_dag=PythonOperator(
    task_id="start_dag",
     python_callable=send
 
  )
  
  start_dag