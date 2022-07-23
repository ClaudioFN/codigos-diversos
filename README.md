# Códigos Diversos
Repositório de códigos de assuntos diversos.

Python:
- [AbreProgramasPython](#AbreProgramasPython)
- [CotacaoDolar](#CotacaoDolar) 
- [CSVtoExcelConverter](#CSVtoExcelConverter)

**Listagem de códigos**

> AbreProgramasPython.py <a id="AbreProgramasPython"></a>
  
 1. Site com as instruções de instalação do pip de Python para instalação do PyInstaller: [Pypa](https://pip.pypa.io/en/stable/getting-started/)
 2. Após ter o PyInstaller, executar o comando criador de executáveis Python: `pyinstaller --onefile AbreProgramasPython.py`
 3. Em alguns casos é necessário colocar o caminho do PyInstaller para ele entender a execução

> CotacaoDolar.py <a id="CotacaoDolar"></a>

 1. Instalar o pacote requests: `pip install requests`
 2. Link da API em uso no código: [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
 3. O código cria um arquivo com dados do sucesso ou erro de execução (LOG do processo efetuado) na mesma pasta que o código se encontra
 4. Alterar a URL da linha 6 ( variável "url") para outras moedas

> CSVtoExcelConverter.py <a id="CSVtoExcelConverter"></a>
 1. Instalar pacotes numpy e pandas: `pip install numpy` e `pip install pandas`
 2. Trocar o texto arquivo.csv na linha 10 (`arquivoCSV = pd.read_csv('arquivo.csv')`) pelo nome do arquivo que se deseja converter
 3. Caso deseje outro nome para o arquivo de Excel, trocar o texto arquivoNovo_ na linha 16 (`nomeArquivoExcel = 'arquivoNovo_' + datetime.today().strftime('%Y-%m-%d') + '.xlsx'`) pelo nome escolido
 4. Executar o código irá gerar na pasta do código o arquivo convertido e o arquivo de LOG da execução
