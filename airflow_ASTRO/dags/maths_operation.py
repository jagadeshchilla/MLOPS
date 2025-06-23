"""
we'll define a DAG that the tasks are as follows:
Task1:start with an initial number
Task2:Add 5 to the number
Task3:Multiply the result by 2
Task4:Subtract 3 from the result
Task5:compute the square of the result
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

## define function for each task

def start_number(** context):

    context['ti'].xcom_push(key='current_val',value=10)
    print("Starting with number 10")

def add_5(** context):
    current_val=context['ti'].xcom_pull(key='current_val',task_ids='start_task')
    new_values=current_val+5
    context['ti'].xcom_push(key='current_val',value=new_values)
    print(f"Added 5: {current_val} + 5 = {new_values}")

def multiply_by_2(** context):
    current_val=context['ti'].xcom_pull(key='current_val',task_ids='add_5_task')
    new_values=current_val*2
    context['ti'].xcom_push(key='current_val',value=new_values)
    print(f"Multiplied by 2: {current_val} * 2 = {new_values}")

def subtract_3(** context):
    current_val=context['ti'].xcom_pull(key='current_val',task_ids='multiply_by_2_task')
    new_values=current_val-3
    context['ti'].xcom_push(key='current_val',value=new_values)
    print(f"Subtracted 3: {current_val} - 3 = {new_values}")

def compute_square(** context):
    current_val=context['ti'].xcom_pull(key='current_val',task_ids='subtract_3_task')
    new_values=current_val**2
    context['ti'].xcom_push(key='current_val',value=new_values)
    print(f"Computed square: {current_val} ^ 2 = {new_values}")


#define the dag
with DAG(
    dag_id='maths_operation',
    start_date=datetime(2025,6,23),
    schedule='@once',
    catchup=False,
) as dag:
    ## define the tasks
    start_task=PythonOperator(
        task_id='start_task',
        python_callable=start_number
    )
    add_5_task=PythonOperator(
        task_id='add_5_task',
        python_callable=add_5
    )
    multiply_by_2_task=PythonOperator(
        task_id='multiply_by_2_task',
        python_callable=multiply_by_2
    )
    subtract_3_task=PythonOperator(
        task_id='subtract_3_task',
        python_callable=subtract_3
    )
    compute_square_task=PythonOperator(
        task_id='compute_square_task',
        python_callable=compute_square
    )

    ## define the task dependencies
    start_task >> add_5_task >> multiply_by_2_task >> subtract_3_task >> compute_square_task
    