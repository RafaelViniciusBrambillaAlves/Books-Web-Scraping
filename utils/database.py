#Banco de Dados 

#Biblioteca para conexão com o banco de dados
import psycopg2
from psycopg2 import OperationalError
#Importando funcoes 
import functions

#Conectando no Banco 
conn = functions.connect()

#Criacao do Cursor 
cursor = conn.cursor()

#Excluindo tabela 
cursor.execute(''' 
 DROP TABLE books         
''')

#Criacao da tabela
cursor.execute(''' 
CREATE TABLE books (
             id SERIAL PRIMARY KEY,
             title TEXT,
             price FLOAT, 
             situation VARCHAR(20),
             quantity INT,
             score INT,
             code VARCHAR(30)
)
''')
print("Tabela criada")

#Confirmanado as mudancas 
conn.commit()
#Fechando a conexão 
conn.close()