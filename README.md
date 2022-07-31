# Códigos Diversos
Repositório de códigos de assuntos diversos.

Java:
- [WEBCrowler](#WEBCrowler)

Python:
- [AbreProgramasPython](#AbreProgramasPython)
- [CotacaoDolar](#CotacaoDolar) 
- [CSVtoExcelConverter](#CSVtoExcelConverter)

Typescript:
- [VariableDeclaration](#VariableDeclaration)

**Listagem de códigos**

> WEBCrowler <a id="WEBCrowler"></a>
1. StartWebCrawler.java - classe com o método `main` para executar o código, onde conseguimos definir a URL de partida e o limite de acessos
2. WebCrawler.java - classe com os detalhes da execução do Web Crawler
3. Realizar o import de todos as packages contidas no início de cada classe
4. Executar a classe StartWebCrawler.java (ter Java e o Java JDK instalados)
5. Será gerado arquivo de LOG de todas as URLs encontradas na pesquisa de URLs disponíveis a partir da primeira URL fornecida no método `main`

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
 3. Caso deseje outro nome para o arquivo de Excel, trocar o texto arquivoNovo_ na linha 16 (`nomeArquivoExcel = 'arquivoNovo_' + datetime.today().strftime('%Y-%m-%d') + '.xlsx'`) pelo nome escolhido
 4. Executar o código irá gerar na pasta do código o arquivo convertido e o arquivo de LOG da execução

> VariableDeclaration.ts <a id="VariableDeclaration"></a>
1. Apenas um resumo básico e inicial sobre TypeScript e seus usos para declaração de variáveis