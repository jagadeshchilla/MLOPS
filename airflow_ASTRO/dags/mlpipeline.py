from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


## define our task 1
def preprocess_data():
    print("Preprocessing data")

## define our task 2
def train_model():
    print("Training model...")

# define our task 3
def evaluate_model():
    print("Evaluating model...")


## define the dag
with DAG(
    "ml_pipeline",
    start_date=datetime(2025, 6, 23),
    schedule='@weekly',
) as dag:
    preprocess_data_task = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_data,
    )
    train_model_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
    )
    evaluate_model_task = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_model,
    )

    preprocess_data_task >> train_model_task >> evaluate_model_task


## define the task dependencies
