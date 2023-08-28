#Importando Bibliotecas
import requests
from bs4 import BeautifulSoup
#Por conta da URL não ter um esquema (como "http://" ou "https://"), é necessário construir a URL completa
from urllib.parse import urljoin
#Pandas para melhor visualização dos dados 
import pandas as pd 
#Importando funcoes 
from .functions import connect
#Biblioteca para conexão com o banco de dados
import psycopg2
from psycopg2 import OperationalError
from psycopg2 import extras

# INSERIR NO BANCO DE DADOS 
def insert_Data(df):

    #Conectando no Banco 
    conn = connect()
    #Criacao do Cursor 
    cursor = conn.cursor()

    # Inserir os dados do DataFrame na tabela
    columns = df.columns.tolist()
    values = df.values.tolist()

    # Gerar a string SQL para inserção
    #INSERT INTO books (coluna1, coluna2, coluna3, ...) VALUES %s
    insert_query = f"INSERT INTO books ({','.join(columns)}) VALUES %s"

    # Usar a função execute_values para inserir os dados
    extras.execute_values(cursor, insert_query, values)

    # Commit das alterações e fechamento da conexão
    conn.commit()
    conn.close()