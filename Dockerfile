FROM quay.io/astronomer/astro-runtime:11.3.0

# 1. Cria o virtualenv para o dbt e instala as dependências lá dentro
# Isso isola o protobuf 6.x do dbt do protobuf 4.x do Airflow
RUN python -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-bigquery dbt-core