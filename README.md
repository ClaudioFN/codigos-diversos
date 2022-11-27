# Códigos Diversos
Repositório de códigos de assuntos diversos.

<a id="inicio"></a>

Java (<a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosJava" target="_blank" rel="noopener noreferrer">Pasta Códigos Java</a>):
- Acessar Resumo: [WEBCrowler](#WEBCrowler) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosJava/WEBCrowler" target="_blank" rel="noopener noreferrer">WEBCrowler</a>

Python  (<a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosPython" target="_blank" rel="noopener noreferrer">Pasta Códigos Python</a>):
- Acessar Resumo: [AbreProgramasPython](#AbreProgramasPython) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/AbreProgramasPython.py" target="_blank" rel="noopener noreferrer">AbreProgramasPython</a>
- Acessar Resumo: [CotacaoDolar](#CotacaoDolar) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/CotacaoDolar.py" target="_blank" rel="noopener noreferrer">CotacaoDolar</a>
- Acessar Resumo: [CSVtoExcelConverter](#CSVtoExcelConverter) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/CSVtoExcelConverter.py" target="_blank" rel="noopener noreferrer">CSVtoExcelConverter</a>
- Acessar Resumo: [GraficoInterativo](#GraficoInterativo) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/GraficoInterativo.py" target="_blank" rel="noopener noreferrer">GraficoInterativo</a>
- Acessar Resumo: [IoTMachineLeaning](#IoTMachineLeaning) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/" target="_blank" rel="noopener noreferrer">IoTMachineLeaning</a>
- Acessar Resumo: [IoTFacialRecognition](#IoTFacialRecognition) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/" target="_blank" rel="noopener noreferrer">IoTFacialRecognition</a>

Typescript (<a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosTypeScript" target="_blank" rel="noopener noreferrer">Pasta Códigos Typescript</a>):
- Acessar Resumo: [VariableDeclaration](#VariableDeclaration) | Acessar Código:  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosTypeScript/VariableDeclaration.ts" target="_blank" rel="noopener noreferrer">VariableDeclaration</a>

**Listagem de códigos**

> WEBCrowler <a id="WEBCrowler"></a> [Voltar ao Início](#inicio)

1. StartWebCrawler.java - classe com o método `main` para executar o código, onde conseguimos definir a URL de partida e o limite de acessos
2. WebCrawler.java - classe com os detalhes da execução do Web Crawler
3. Realizar o import de todos as packages contidas no início de cada classe
4. Executar a classe StartWebCrawler.java (ter Java e o Java JDK instalados)
5. Será gerado arquivo de LOG de todas as URLs encontradas na pesquisa de URLs disponíveis a partir da primeira URL fornecida no método `main`

> AbreProgramasPython.py <a id="AbreProgramasPython"></a> [Voltar ao Início](#inicio)
  
 1. Site com as instruções de instalação do pip de Python para instalação do PyInstaller: [Pypa](https://pip.pypa.io/en/stable/getting-started/)
 2. Após ter o PyInstaller, executar o comando criador de executáveis Python: `pyinstaller --onefile AbreProgramasPython.py`
 3. Em alguns casos é necessário colocar o caminho do PyInstaller para ele entender a execução

> CotacaoDolar.py <a id="CotacaoDolar"></a> [Voltar ao Início](#inicio)

 1. Instalar o pacote requests: `pip install requests`
 2. Link da API em uso no código: [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
 3. O código cria um arquivo com dados do sucesso ou erro de execução (LOG do processo efetuado) na mesma pasta que o código se encontra
 4. Alterar a URL da linha 6 (variável "url") para outras moedas

> CSVtoExcelConverter.py <a id="CSVtoExcelConverter"></a> [Voltar ao Início](#inicio)
 1. Instalar pacotes numpy e pandas: `pip install numpy` e `pip install pandas`
 2. Trocar o texto arquivo.csv na linha 10 (`arquivoCSV = pd.read_csv('arquivo.csv')`) pelo nome do arquivo que se deseja converter
 3. Caso deseje outro nome para o arquivo de Excel, trocar o texto arquivoNovo_ na linha 16 (`nomeArquivoExcel = 'arquivoNovo_' + datetime.today().strftime('%Y-%m-%d') + '.xlsx'`) pelo nome escolhido
 4. Executar o código irá gerar na pasta do código o arquivo convertido e o arquivo de LOG da execução
 
 > GraficoInterativo.py <a id="GraficoInterativo"></a> [Voltar ao Início](#inicio)

 Obs.: inspirado no vídeo: YouTube: youtu.be/Qxm5QEEKHqE
 1. Instalar o pacote no computador: `pip install plotly-express`
 2. Instalar os pacotes relacionados ao Streamlit: `pip install streamlit`
 3. Streamlit não é obrigatório. Descomentar trechos do código e comentar os que fazem referência ao Streamlit tratam o assunto localmente

> IoTMachineLeaning.py <a id="IoTMachineLeaning"></a> [Voltar ao Início](#inicio)
 1. Instalar o pacote de audio: `pip install SpeechRecognition`
 2. Instalar arquivo baixado no site [UCI - PACOTES DE ÁUDIO](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Baixar de acordo com seu chipset (x32 | x64) e versão do Python: `pip install <DIRETORIO DO DOWNLOAD SEM ESPAÇOS COM NOME DO ARQUIVO BAIXADO>`
 3. Criar executável do código (executar comando na pasta onde o arquivo está, depois de já ter o PyInstaller no computador): `pyinstaller --onefile IoTMachineLeaning.py`

IoTFacialRecognition.py <a id="IoTFacialRecognition"></a> [Voltar ao Início](#inicio)
 1. Obrigatório ter uma webcam para operar esse programa.
 2. Programa pronto para executar. Apenas use de preferência o [Google Colaboratory](https://colab.research.google.com) para executar o código.
 3. Carregar o programa no ambiente do Google Colab e executar tudo de uma vez. 

> VariableDeclaration.ts <a id="VariableDeclaration"></a> [Voltar ao Início](#inicio)
1. Apenas um resumo básico e inicial sobre TypeScript e seus usos para declaração de variáveis