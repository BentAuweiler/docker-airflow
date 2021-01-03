from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Bent Auweiler',
    'depends_on_past': False,
    'start_date': datetime(2018, 8, 17, 0, 0),
    'retries': 0,
    'email': ['bent.auweiler@bayard-consulting.com'],
    'email_on_failure': True,
    'email_on_retry': True
}

dag = DAG('email_on_sla_miss_dag',
          default_args=args,
          max_active_runs=1,
          schedule_interval="@once")

t1 = BashOperator(
    task_id='timeout',
    sla=timedelta(seconds=5),
    bash_command='sleep 10',
    retries=0,
    dag=dag,
)