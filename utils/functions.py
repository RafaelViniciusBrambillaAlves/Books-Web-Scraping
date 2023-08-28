# Funcoes 

## Importando Bibliotecas
import requests
from bs4 import BeautifulSoup
#Por conta da URL não ter um esquema (como "http://" ou "https://"), é necessário construir a URL completa
from urllib.parse import urljoin
#Pandas para melhor visualização dos dados 
import pandas as pd 
#Biblioteca para conexão com o banco de dados
import psycopg2
from psycopg2 import OperationalError

## CONEXAO COM O BANCO
def connect():
    try:
        conn = psycopg2.connect (
            host = "26.189.184.161",
            database = "books",
            user = "postgres",
            password = "root",
            port = "5432"  
        )
        print("Conexao Bem-Sucedida")
        return conn

    except OperationalError as error:
        print(f"Erro ao Conectar: {error}")
        return None
    
## PROXIMA PAGINA  
def nextPage(soup_main, base_url):
    #Usando o método find para encontrar o elemento HTML (Botão Next),
    next_button = soup_main.find('a', href=True, string='next')
    #Condição para verificar se o botão foi encontrado na página
    if next_button:
        next_url = urljoin(base_url, next_button['href'])
        return next_url
    else:
        return None

## TITULO
def _title(soup_books):
    #Encontrar o elemento h1 e pegar o texto
    title = soup_books.find('h1').get_text()
    return title 

## PRECO
def _price(soup_books):
    #Encontrar o elemento e pegar o texto do elemento classe e retirar o £ do texto
    price = soup_books.find("p", class_="price_color").get_text().replace("£", "")
    return price

## SITUACAO e QUANTIDADE
def _situation(soup_books):
    #Encontrar o elemento e pegar o texto do elemento classe
    stock_element = soup_books.find("p", class_="instock availability")
    #Extrair o texto do elemento e remover espacos brancos extras no inicio e fim
    availability_text = stock_element.get_text().strip()
    # Dividir a string para obter "situacao" e "quantidade", baseada no '('
    parts = availability_text.split('(')
    #Separando situacao e quantidade, baseadado no vetor
    situation = parts[0].strip()
    return situation

## QUANTIDADE
def _quantity(soup_books):
    #Encontrar o elemento e pegar o texto do elemento classe
    stock_element = soup_books.find("p", class_="instock availability")
    #Extrair o texto do elemento e remover espacos brancos extras no inicio e fim
    availability_text = stock_element.get_text().strip()
    # Dividir a string para obter "situacao" e "quantidade", baseada no '('
    parts = availability_text.split('(')
    #Separando situacao e quantidade, baseadado no vetor
    quantity = parts[1].replace(')', '').strip().split()[0]
    return quantity
    
## AVALIACAO
def _score(soup_books):
    class_value = {  "One": 1,"Two": 2, "Three": 3, "Four": 4,"Five": 5  }
    # Encontrando todos os elementos <p> com a classe "star-rating"
    star_rating_elements = soup_books.find_all("p", class_="star-rating")
    # Percorra os elementos encontrados e atribua os valores com base na classe
    for element in star_rating_elements:
        class_name = element["class"][1]  # Obtém o segundo valor da lista de classes,  0 - (star-rating) 1 - (One)
        #Associa valores baseados no dicionário 
        score = class_value.get(class_name)
        return score

## Codigo de Produto
def _code(soup_books):
    #Encontrar a table e o <td> 
    table_code = soup_books.find("table", class_="table table-striped").find("td")
    #Pegar o texto de dentro do <td>
    code = table_code.get_text(strip=True)
    return code 
