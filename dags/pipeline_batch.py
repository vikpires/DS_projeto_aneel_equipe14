from datetime import datetime
from airflow.sdk import dag, task
from src.data import run_extract_data, run_transform_data, run_validation


# DAG de orquestração Batch para ingestão, consolidação e auditoria das bases de dados da ANEEL.
@dag(
    dag_id="aneel_energy_ingestion_batch",
    description="Pipeline de ingestão, consolidação e auditoria das bases de dados da ANEEL.",
    schedule=None,  # Execução manual / batch sob demanda
    start_date=datetime(2024, 1, 1),
    catchup=False,
    max_active_runs=1,
    tags=[
        "aneel",
        "data_ingestion",
        "batch",
        "data_processing",
        "data_quality",
        "audit",
        "elt",
    ],
)
def pipeline_batch():

    # 1. Ingestão de dados
    @task
    def task_run_extractor():
        run_extract_data()

    # 2. Processamento via DuckDB
    @task
    def task_run_transformer():
        run_transform_data()

    # 3. Validação de qualidade dos dados
    @task
    def task_run_validation():
        run_validation()

    # Definindo a ordem de execução das tarefas
    task_run_extractor() >> task_run_transformer() >> task_run_validation()


pipeline_dag = pipeline_batch()
