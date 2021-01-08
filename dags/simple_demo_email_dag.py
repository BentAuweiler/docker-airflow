from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

def print_hello():
    return 'Hello world!'

default_args = {
        'owner': 'Bent Auweiler',
        'start_date':datetime(2020,8,11),
}

dag = DAG('simple_demo_mail_dag',
          description='Simple tutorial DAG',
          schedule_interval='@once',
          default_args = default_args,
          catchup=False,
          max_active_runs=1)

dag.doc_md = """This workflow shows the simple concatination of 3 different tasks using three different operators"""

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

email = EmailOperator(
        task_id='send_email',
        to='bent.auweiler@bayard-consulting.com',
        subject='Airflow Demo Alert',
        html_content=""" <h3>Email Test</h3> """,
        dag=dag
)

email.doc_md = """This task implements a very simple custom email template to illustrate the sending of custom emails"""

email >> dummy_operator >> hello_operator