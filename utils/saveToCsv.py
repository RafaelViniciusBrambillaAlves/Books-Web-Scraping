#Banco de Dados 

#Biblioteca para conexão com o banco de dados
import psycopg2
from psycopg2 import OperationalError
#Data e hora 
from datetime import datetime
data_hora_atual = datetime.now()
#Formato da data
formato = "%Y-%m-%d_%H-%M-%S"
#Arquivo csv
import csv
#Importando funcoes 
from .functions import connect
#Caminho para salvar o csv
import os 


def save_To_Csv():
    #Funcao
    #   Conectando no Banco 
    conn = connect()

    #Criacao do Cursor 
    cursor = conn.cursor()

    cursor.execute('''
                SELECT * FROM books
    ''')

    todos_os_dados = cursor.fetchall()

    #Fechando a conexão 
    cursor.close()
    conn.close()

    #Nome do arquivo
    nome_arquivo = data_hora_atual.strftime(formato) + '.csv'
    #Caminho do arquivo 
    caminho_completo = os.path.join(os.path.dirname(__file__), "csv", nome_arquivo)
    print("Caminho completo:", caminho_completo)

    #Escrever os dados no arquivo CSV
    with open(caminho_completo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        #Escrevendo os dados
        writer.writerows(todos_os_dados)