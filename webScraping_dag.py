from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator
from utils.webScraping import web_Scraping
from utils.insertData import insert_Data
from utils.saveToCsv import save_To_Csv

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'webScraping_dag',
    default_args=default_args,
    description='DAG para Web Scraping',
    schedule_interval=timedelta(days=1),
)

# Criação das tarefas
web_scraping_task = PythonOperator(
    task_id='web_scraping_task',
    python_callable=web_Scraping,  # Chamando a função correta: webScraping.webScraping
    dag=dag,
)

def pass_df_to_insert_data_function(**kwargs):
    ti = kwargs['ti']
    df = ti.xcom_pull(task_ids='web_scraping_task')
    insert_Data(df)

insert_data_task = PythonOperator(
    task_id='insert_data_task',
    python_callable=pass_df_to_insert_data_function,
    provide_context=True,  # Isso permite passar o contexto para a função
    dag=dag,
)

save_to_csv_task = PythonOperator(
    task_id='save_to_csv_task',
    python_callable=save_To_Csv,  # Chamando a função correta: saveToCsv.saveToCsv
    dag=dag,
)

# Definição do fluxo de dependência das tarefas
web_scraping_task >> insert_data_task >> save_to_csv_task

