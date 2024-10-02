from airflow import DAG
from airflow.operators.python.PythonOperator import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

def extrair():
    url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv/data.csv'
    df = pd.read_csv(url)
    df.to_csv('data/dados_covid_extraidos.csv', sep=';', index=False)
    
def transformar():
    df = pd.read_csv('data/dados_covid_extraidos.csv', delimiter=';')
    df['dateRep'] = pd.to_datetime(df['dateRep'], format='%d/%m/%Y', errors='coerce')
    df = df.dropna()
    
    df_agrupada = df.groupby('continentExp')[['cases', 'deaths']].sum().reset_index()
    df_agrupada.to_csv('data/dados_transformados.csv', sep=';', index=False)

def carregar():
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/postgres')
    df = pd.read_csv('data/dados_transformados.csv', delimiter=';')
    df.to_sql('dados_covid', engine, if_exists='replace', index=False)
    
default_args = {
    'start_date': datetime(2023, 10, 1),
}

with DAG('etl_covid_europa_pipeline', default_args=default_args, schedule='@daily') as dag:
    extracao = PythonOperator(task_id='extrair', python_callable=extrair)
    transformacao = PythonOperator(task_id='transformar', python_callable=transformar)
    carga = PythonOperator(task_id='carregar', python_callable=carregar)
    
    extracao >> transformacao >> carga
