import os
import sys
import yaml
import datetime
from pathlib import Path
from google.cloud import bigquery
from google.cloud import storage


def yaml_loader():
    # Loads a yaml config file
    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    sys.path.append(parent)
    dag_bucket = Path(__file__).parent
    config_filepath = f'{dag_bucket}/bikeshare_etl.yaml'

    with open(config_filepath, 'r') as file_descriptor:
        config = yaml.safe_load(file_descriptor)
    return config


config = yaml_loader()
yesterday = datetime.datetime.now(datetime.UTC).date() - datetime.timedelta(days=1)

project_id = config['gcp']['project_id']
dataset_id = config['gcp']['dataset_id']
gcs_bucket = config['gcp']['gcs_bucket']
file_path = str(config['gcp']['file_path']).format(yesterday)
external_table_name = config['gcp']['external_table_name']


def run_bq_qry():
    sql = """
        SELECT 
            trips.*
            , DATE(start_time) day_partition
            , EXTRACT(HOUR FROM start_time) hour_partition
        FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` trips 
        WHERE 
          start_time >= TIMESTAMP_TRUNC(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY), DAY)
          AND start_time <  TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), DAY)
        ORDER BY 
          day_partition, 
          hour_partition
        """

    bqclient = bigquery.Client()
    qry_result = bqclient.query(sql)
    df_res = qry_result.to_dataframe()

    return df_res


def upload_files_to_gcs(qry_df):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(gcs_bucket)

    for hour in qry_df['hour_partition'].unique():
        df = qry_df[qry_df['hour_partition'] == hour]
        gcs_path = f'{file_path}{str(hour).zfill(2)}/data.parquet'

        #df.to_parquet(f'gs://{gcs_bucket}/{gcs_path}', engine='pyarrow')
        bucket.blob(f'{gcs_path}').upload_from_string(df.to_parquet(index=False))


def extract_data_from_bq():
    df_res = run_bq_qry()
    upload_files_to_gcs(df_res)


def create_external_table():
    bqclient = bigquery.Client()

    gcs_urls = f'gs://{gcs_bucket}/bikeshare/{yesterday}/*/data.parquet'
    ext_config = bigquery.ExternalConfig('PARQUET')
    ext_config.source_uris = [gcs_urls]
    ext_config.options.hive_partitioning_mode = 'AUTO'
    ext_config.options.hive_partitioning_source_uri_prefix = f'gs://{gcs_bucket}/bikeshare/'

    table_ref = f'{project_id}.{dataset_id}.{external_table_name}'

    try:
        bqclient.delete_table(table_ref)
    except Exception as e:
        print(f"Cant delete the table {table_ref} since its not exist. {e}")

    table = bigquery.Table(table_ref)
    table.external_data_configuration = ext_config

    table = bqclient.create_table(table, exists_ok=True)
