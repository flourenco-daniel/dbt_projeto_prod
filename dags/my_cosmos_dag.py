from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import GoogleCloudServiceAccountDictProfileMapping # Alterado para BQ
import os
from datetime import datetime

# Configuração do Perfil para BigQuery
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=GoogleCloudServiceAccountDictProfileMapping(
        conn_id="google_cloud_default", # ID da conexão que você criará na UI do Airflow
        profile_args={
            "project": "seu-projeto-id",
            "dataset": "seu_dataset_dbt",
        },
    ),
)

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        "/usr/local/airflow/dags/dbt/projeto_prod",
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        # O caminho que definimos no seu Dockerfile
        dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt",
    ),
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dag_id="my_cosmos_dag",
    default_args={"retries": 2},
)