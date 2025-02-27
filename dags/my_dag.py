from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': datetime(2018, 11, 1),
    'provide_context': True
}

with DAG('Hello-world', description='Hello-world', schedule_interval='*/1 * * * *', catchup=True, default_args=args) as dag:
    t1 = BashOperator(
        task_id='task_1',
        bash_command='echo hello world from task 1',
    )
    t2 = BashOperator(
        task_id='task_2',
        bash_command='echo hello world from task 2',
    )
    t3 = BashOperator(
        task_id='task_3',
        bash_command='echo hello world from task 3',
    )
    t4 = BashOperator(
        task_id='task_4',
        bash_command='echo hello world from task 4',
    )

    t1 >> t2
    t1 >> t3
    t2 >> t4
    t3 >> t4
