import os

from dotenv import load_dotenv
import pandas as pd
from google.cloud import bigquery

load_dotenv()

# Uploading the transformed mater data to BigQuery.
def push_to_bigquery(df: pd.DataFrame) -> int:
    project_id = os.getenv("GCP_PROJECT_ID")
    dataset_id = os.getenv("BQ_DATASET_ID")
    table_id = os.getenv("BQ_TABLE_ID")

    if not all([project_id, dataset_id, table_id]):
        raise ValueError(
            "Missing BigQuery environment configuration."
        )

    # GCP Format - project / dataset / table
    full_table_id = f"{project_id}.{dataset_id}.{table_id}"

    client = bigquery.Client(project=project_id)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(
        df,
        full_table_id,
        job_config=job_config,
    )

    job.result()

    table = client.get_table(full_table_id)

    print(
        f"BigQuery upload complete: "
        f"{table.num_rows} rows"
    )

    return table.num_rows