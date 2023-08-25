# 📚 Web Scraping Books 

 Projeto fictício. O site mencionado nesse projeto não é real. A inspiração para este projeto veio do [blog](https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823)📝 
 O link para o [site](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction?resource=download)🔎 em que foi feito a coleta de dados.

## 🚀 Descrição do projeto 
- Coleta de Dados:
O código desenvolvido em Python é responsável por extrair informações de um site que vende livros, incluindo títulos, preços, situações, quantidades, notas e códigos de produtos.

- Armazenamento no Banco de Dados:
Uma vez que os dados são coletados, eles são cuidadosamente organizados e armazenados em um banco de dados Postgresql.

- Cópia em Formato CSV:
Para garantir a preservação dos dados coletados e a rastreabilidade das informações, uma cópia é criada em um formato universalmente reconhecido: o arquivo CSV. Esse arquivo contém não apenas os dados da coleta, mas também em seu nome a data e hora exata em que os dados foram adquiridos.

- Automação com Apache Airflow:
A automação integral desse processo é alcançada por meio da plataforma Apache Airflow. Uma configuração é estabelecida dentro do Airflow para agendar a execução do código de coleta e armazenamento de dados em intervalos regulares. Com isso, é garantido que o processo ocorra automaticamente todos os dias, sempre no mesmo horário pré-determinado.

### 🔨 Linguagens, Tecnologias e Bibliotecas Utilizadas
  <div style="display: flex; flex-direction: row;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Descrição da Imagem" width="40">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png" width="90">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" width="100">
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png" width="90">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/2560px-Google_Colaboratory_SVG_Logo.svg.png" width="72">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" width="40">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/993px-Postgresql_elephant.svg.png" width="40">
</div>
