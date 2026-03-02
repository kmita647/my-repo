from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Dataformと同じリポジトリで管理するサンプルのDAG
with DAG(
    "sample_composer_dag",
    description="A sample DAG in the same repo as Dataform",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["dataform_repo"],
) as dag:

    t1 = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello! This DAG lives happily alongside Dataform.'",
    )