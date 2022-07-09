# pip install requests
import requests
from datetime import datetime

# Link publico com o valor atual da cotacao do dolar informado atraves de uma API com retorno em formato JSON
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

# Busca os dados
response = requests.get(url) 

# Retorno 200 = OK = exibir os dados importantes
# USD = raiz do JSON / low = um dos nos do JSON
if response.status_code == 200:
   dolar_value = response.json()['USD']['low']
   # Cria o arquivo de OK
   arquivo = open('arq-' + datetime.today().strftime('%Y-%m-%d') + '.txt','w')
   arquivo.write('Dolar cotado no menor preco em ' + datetime.today().strftime('%d-%m-%Y %H:%M:%S') + ' = ' + dolar_value)
   arquivo.close()
else:
   # Cria o arquivo de NOK
   arquivo = open('arq-erro-' + datetime.today().strftime('%Y-%m-%d') + '.txt','w')
   arquivo.write('Erro ' + response.status_code + ': ' +  response.json()['message'])
   arquivo.close()