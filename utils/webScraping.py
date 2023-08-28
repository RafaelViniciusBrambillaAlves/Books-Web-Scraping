#Importando Bibliotecas
import requests
from bs4 import BeautifulSoup
#Por conta da URL não ter um esquema (como "http://" ou "https://"), é necessário construir a URL completa
from urllib.parse import urljoin
#Pandas para melhor visualização dos dados 
import pandas as pd 
#Importando funcoes 
from .functions import connect, nextPage, _title, _price, _situation, _quantity, _score, _code
#Biblioteca para conexão com o banco de dados
import psycopg2
from psycopg2 import OperationalError
from psycopg2 import extras

#WEB SCRAPING

def web_Scraping():
    #DataFrame vazio
    data = {'title':[], 'price':[], 'situation':[], 'quantity':[], 'score':[], 'code':[]}
    df = pd.DataFrame(data)


    #My User Agent no Google
    headers =   {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
                }

    #Definindo a URL base do site
    base_url = "http://books.toscrape.com/catalogue/"
    #Primeira página
    next_url = "http://books.toscrape.com/catalogue/page-1.html"

    #Requisicao do site e análise do conteudo do site, de acordo com a solicitação anterior 
    site = requests.get(next_url, headers=headers)
    soup_main = BeautifulSoup(site.content, 'html.parser')

    #Condição, enquanto houver próximas páginas, ele continua no loop
    while True:
        if next_url:
            #Imprime próxima página
            print("PROXIMA PAGINA: ", next_url)
            #Requisicao do site e análise do conteudo do site, de acordo com a solicitação anterior 
            response = requests.get(next_url, headers=headers)
            soup_main = BeautifulSoup(response.content, 'html.parser')
            #Encontra todos os elementos <a> - Links dos livros
            book_links = soup_main.find_all('a', href=True, title=True)

            # Para cada link do livro, concatenando para formar o link completo e retira os dados necessarios 
            for link_element in book_links:
                link = link_element['href']
                full_link = ("http://books.toscrape.com/catalogue/" + link)

                #Requisicao do site e análise do conteudo do site, de acordo com a solicitação anterior para acessar os dados de cada livro
                response_books = requests.get(full_link, headers=headers)
                soup_books = BeautifulSoup(response_books.content, 'html.parser')

                ## Titulo, Preco, Situacao, quantidade, nota, codigo
                title = _title(soup_books)
                price = _price(soup_books)
                situation = _situation(soup_books)
                quantity = _quantity(soup_books)
                score = _score(soup_books)
                code = _code(soup_books)

                #Imprimir Informacoes
                print('Titulo:', title, '- Preco:', price, '- Situacao:', situation, '- Quantidade:', quantity, '- Avaliacao:', score, '- Codigo:', code )
                #Inserir informações em um Dataframe
                novo_registro = {'title': title, 'price': price, 'situation': situation, 'quantity': quantity, 'score': score, 'code': code}
                df = df._append(novo_registro, ignore_index=True)

        else:
            #Imprime que não há mais páginas
            print("NAO HA MAIS PAGINAS")
            break
        #Chama a função novamente para passar de página
        next_url = nextPage(soup_main, base_url)
    return df 

