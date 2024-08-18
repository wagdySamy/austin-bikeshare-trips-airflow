import datetime
from airflow import DAG, settings
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from utilities import extract_data_from_bq, create_external_table, yaml_loader

yesterday = datetime.datetime.now(datetime.UTC).date() - datetime.timedelta(days=1)

config = yaml_loader()
print('read_config complete for: ')

# Create the DAG
with DAG(**config['dag']) as dag:

    # Start the graph with a dummy task
    start_task = DummyOperator(task_id='start')

    run_bq_qry = PythonOperator(
        task_id="extract-biketrips-data-bq",
        python_callable=extract_data_from_bq
    )

    create_external_table = PythonOperator(
        task_id="create-external-bq-table",
        python_callable=create_external_table
    )

    end_task = DummyOperator(task_id='end')


    start_task >> run_bq_qry >> create_external_table >> end_task

