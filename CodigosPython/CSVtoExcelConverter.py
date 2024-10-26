"""
Created Date: 23/07/2023
Last Update: 26/10/2024
Description: Convert CSV to Excel
Observation: Convert CSV to Excel comes with logging to better locate each step
"""
import pandas as pd
import numpy as np
from datetime import datetime
import logging

# Configurando o arquivo de LOG
logging.basicConfig(filename='CSVtoExcelConverter.log', format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
print('INICIO - ', datetime.today().strftime('%d-%m-%Y %H:%M:%S'))
# Ler arquivo CSV
arquivoCSV = pd.read_csv('arquivo.csv')
logging.info('\n')
logging.info('Leu o arquivo')

# Salvar o arquivo para o formato XLSX
logging.info('Antes de criar novo  arquivo para colocar os dados do formato XLSX')
nomeArquivoExcel = 'arquivoNovo_' + datetime.today().strftime('%Y-%m-%d') + '.xlsx'
arquivoExcel = pd.ExcelWriter(nomeArquivoExcel)
logging.info('Arquivo ' + nomeArquivoExcel)

logging.info('Iniciando a escrita do CSV para o XLSX')
arquivoCSV.to_excel(arquivoExcel, index = False)

logging.info('Conversao completa!')

arquivoExcel.save()
logging.info('Arquivo salvo')

print('FIM - ', datetime.today().strftime('%d-%m-%Y %H:%M:%S'))