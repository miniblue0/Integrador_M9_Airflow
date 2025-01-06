
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_data(**context):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

    context['ti'].xcom_push(key='raw_data', value=data)


def transform_data(**context):

    raw_data = context['ti'].xcom_pull(key='raw_data', task_ids='extract_data')  
    promedio = sum(raw_data) / len(raw_data)  

    context['ti'].xcom_push(key='promedio', value=promedio) 



def print_data(**context):

    promedio = context['ti'].xcom_pull(key='promedio', task_ids='transform_data') 
    print(f"el promedio final es: {promedio}")


default_args = {
    'start_date': days_ago(1),
    'retries': 1
}

with DAG(
    dag_id='dag_integrador',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    task_01_extract= PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        provide_context=True,
    )

    task_02_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True,
    )

    task_03_print= PythonOperator(
        task_id='print_data',
        python_callable=print_data,
        provide_context=True,
    )


    task_01_extract >> task_02_transform >> task_03_print

