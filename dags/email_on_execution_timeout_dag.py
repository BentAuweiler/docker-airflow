from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Bent Auweiler',
    'depends_on_past': False,
    'email': ['bent.auweiler@bayard-consulting.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0,
    'start_date': datetime(2018, 8, 17, 0, 0),
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(seconds=5),
    'execution_timeout': timedelta(seconds=5),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG('email_on_execution_timeout_dag',
          default_args=args,
          max_active_runs=1,
          schedule_interval="@once")

t1 = BashOperator(
    task_id='timeout',
    sla=timedelta(seconds=5),
    execution_timeout=timedelta(seconds=5),
    bash_command='sleep 10',
    retries=0,
    dag=dag,
)

t1.doc_md = """This task demonstrates the sending of an email if an execution timeout is set and reached during the execution"""