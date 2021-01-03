

from __future__ import print_function

from airflow import DAG
from airflow.models import Variable
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from pprint import pprint

from airflow.operators.python_operator import PythonOperator

default_arguments = {
    'owner': 'Bent Auweiler',
    'start_date': days_ago(1),
}

max_execution_time = timedelta(hours=1)

# Dependencies used in the python callable (function) need to be defined in the python callable (function) itself
def print_context(ds, **kwargs):
    print('Hello Airflow World!')
    pprint(kwargs)
    print(ds)
    result = 120 / 0
    return result


with DAG(
    'email_on_failure_dag',
    schedule_interval='@once', # cron expression would be 0 0 * * *
    catchup=False,
    description='Demo dag to throw an error on execution and send an email',
    default_args=default_arguments) as dag:

        fetch_items_task = PythonOperator(
            task_id='print_the_context',
            execution_timeout=max_execution_time,
            provide_context=True,
            email_on_failure=True,
            email='bent.auweiler@bayard-consulting.com',
            python_callable=print_context,
            dag=dag
        )



