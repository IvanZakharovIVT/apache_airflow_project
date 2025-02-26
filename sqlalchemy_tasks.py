import logging

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from database.session import SessionLocal


logger = logging.getLogger(__name__)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def execute_sql_task(task_id, sql_query):
    def _execute_task(**kwargs):
        with SessionLocal() as session:
            result = session.execute(sql_query)
            session.commit()
            return result.fetchall()
    return _execute_task

def execute_logger_task(task_id):
    def _execute_task(**kwargs):
        logger.info(f"executing task {task_id}")
    return _execute_task

dag = DAG(
    'sqlalchemy_dag',
    default_args=default_args,
    schedule_interval='*/30 * * * *',  # каждые 30 минут
    start_date=datetime(2025, 1, 1),
)

task1 = PythonOperator(
    task_id='first_task',
    python_callable=execute_logger_task(task_id='third_task'),
    dag=dag
)

task2 = PythonOperator(
    task_id='second_task',
    python_callable=execute_logger_task(task_id='third_task'),
    dag=dag
)

task3 = PythonOperator(
    task_id='third_task',
    python_callable=execute_logger_task(task_id='third_task'),
    dag=dag
)

task1 >> task2 >> task3