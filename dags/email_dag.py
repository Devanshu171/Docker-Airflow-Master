from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from bots.emailhelper import send


default_args={
  "owner":"dev",
  "start_date":datetime(2023,6,3)
}

with DAG(
  dag_id="PythonEmail1.0",
  default_args=default_args,
  schedule_interval="@daily"
  ) as dag:
  
  send_email=PythonOperator(
    task_id="send_email",
     python_callable=send
 
  )
  
  send_email