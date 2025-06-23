from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id='math_sequence_dag_with_taskflowap',
    start_date=datetime(2025,6,23),
    schedule='@once',
    catchup=False,
) as dag:
    @task
    def start_number():
        initial_number=10
        print(f"Starting with number: {initial_number}")
        return initial_number
    
    @task
    def add_5(number):
        result=number+5
        print(f"Added 5: {number} + 5 = {result}")
        return result
    
    @task
    def multiply_by_2(number):
        result=number*2
        print(f"Multiplied by 2: {number} * 2 = {result}")
        return result
    
    @task
    def subtract_3(number):
        result=number-3
        print(f"Subtracted 3: {number} - 3 = {result}")
        return result
    
    @task
    def compute_square(number):
        result=number**2
        print(f"Computed square: {number} ^ 2 = {result}")
        return result
    
    ## set the task dependencies
    start_value=start_number()
    add_5_value=add_5(start_value)
    multiply_by_2_value=multiply_by_2(add_5_value)
    subtract_3_value=subtract_3(multiply_by_2_value)
    compute_square_value=compute_square(subtract_3_value)

