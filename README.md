# Códigos Diversos
Repositório de códigos de assuntos diversos.

<a id="inicio"></a>

Java (<a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosJava" target="_blank" rel="noopener noreferrer">Pasta Códigos Java</a>):
- WEBCrowler: [Acessar Resumo](#WEBCrowler) |  <a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosJava/WEBCrowler" target="_blank" rel="noopener noreferrer">Acessar Código</a>

Python  (<a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosPython" target="_blank" rel="noopener noreferrer">Pasta Códigos Python</a>):
- AbreProgramasPython: [Acessar Resumo](#AbreProgramasPython) |  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/AbreProgramasPython.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>
- CotacaoDolar: [Acessar Resumo](#CotacaoDolar) |  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/CotacaoDolar.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>
- CSVtoExcelConverter: [Acessar Resumo](#CSVtoExcelConverter) |  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/CSVtoExcelConverter.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>
- GraficoInterativo: [Acessar Resumo](#GraficoInterativo) | <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/GraficoInterativo.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>
- IoTMachineLeaning: [Acessar Resumo](#IoTMachineLeaning) |  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/IoTMachineLeaning.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>
- IoTFacialRecognition: [Acessar Resumo](#IoTFacialRecognition) | <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/IoTFacialRecognition.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>

- ImageCreationWithOpenAI: [Acessar Resumo](#ImageCreationWithOpenAI) |   <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/ImageCreationWithOpenAI.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>

- PhoneNumberID: [Acessar Resumo](#PhoneNumberID) |   <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosPython/PhoneNumberID.py" target="_blank" rel="noopener noreferrer">Acessar Código</a>

Typescript (<a href="https://github.com/ClaudioFN/codigos-diversos/tree/main/CodigosTypeScript" target="_blank" rel="noopener noreferrer">Pasta Códigos Typescript</a>):
- VariableDeclaration: [Acessar Resumo](#VariableDeclaration) |  <a href="https://github.com/ClaudioFN/codigos-diversos/blob/main/CodigosTypeScript/VariableDeclaration.ts" target="_blank" rel="noopener noreferrer">Acessar Código</a>

**Listagem de códigos**

> WEBCrowler <a id="WEBCrowler"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> WEB Crowler que, a partir de uma URL, apresenta todas as URLs acessíveis a partir da URL original.

1. StartWebCrawler.java - classe com o método `main` para executar o código, onde conseguimos definir a URL de partida e o limite de acessos
2. WebCrawler.java - classe com os detalhes da execução do Web Crawler
3. Realizar o import de todos as packages contidas no início de cada classe
4. Executar a classe StartWebCrawler.java (ter Java e o Java JDK instalados)
5. Será gerado arquivo de LOG de todas as URLs encontradas na pesquisa de URLs disponíveis a partir da primeira URL fornecida no método `main`

> AbreProgramasPython.py <a id="AbreProgramasPython"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Informações de como fazer arquivo(s) Python ser(em) executado(s) por um executável.

 1. Site com as instruções de instalação do pip de Python para instalação do PyInstaller: [Pypa](https://pip.pypa.io/en/stable/getting-started/)
 2. Após ter o PyInstaller, executar o comando criador de executáveis Python: `pyinstaller --onefile AbreProgramasPython.py`
 3. Em alguns casos é necessário colocar o caminho do PyInstaller para ele entender a execução

> CotacaoDolar.py <a id="CotacaoDolar"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Vai até uma API e recupera o valor do dia sobre uma moeda monetária específica. 

 1. Instalar o pacote requests: `pip install requests`
 2. Link da API em uso no código: [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
 3. O código cria um arquivo com dados do sucesso ou erro de execução (LOG do processo efetuado) na mesma pasta que o código se encontra
 4. Alterar a URL da linha 6 (variável "url") para outras moedas

> CSVtoExcelConverter.py <a id="CSVtoExcelConverter"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Conversor de arquivos de CSV (extensão CSV) para Excel (extensão XLSX). 

 1. Instalar pacotes numpy e pandas: `pip install numpy` e `pip install pandas`
 2. Trocar o texto arquivo.csv na linha 10 (`arquivoCSV = pd.read_csv('arquivo.csv')`) pelo nome do arquivo que se deseja converter
 3. Caso deseje outro nome para o arquivo de Excel, trocar o texto arquivoNovo_ na linha 16 (`nomeArquivoExcel = 'arquivoNovo_' + datetime.today().strftime('%Y-%m-%d') + '.xlsx'`) pelo nome escolhido
 4. Executar o código irá gerar na pasta do código o arquivo convertido e o arquivo de LOG da execução
 
 > GraficoInterativo.py <a id="GraficoInterativo"></a> [Voltar ao Início](#inicio)

 - <b>Resumo:</b> Teste de criação de gráficos em Python.

 Obs.: inspirado no vídeo: YouTube: youtu.be/Qxm5QEEKHqE
 1. Instalar o pacote no computador: `pip install plotly-express`
 2. Instalar os pacotes relacionados ao Streamlit: `pip install streamlit`
 3. Streamlit não é obrigatório. Descomentar trechos do código e comentar os que fazem referência ao Streamlit tratam o assunto localmente

> IoTMachineLeaning.py <a id="IoTMachineLeaning"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Teste de execução com geração de instalador de programa capaz de transformar áudio em texto.

 1. Instalar o pacote de audio: `pip install SpeechRecognition`
 2. Instalar arquivo baixado no site [UCI - PACOTES DE ÁUDIO](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Baixar de acordo com seu chipset (x32 | x64) e versão do Python: `pip install <DIRETORIO DO DOWNLOAD SEM ESPAÇOS COM NOME DO ARQUIVO BAIXADO>`
 3. Criar executável do código (executar comando na pasta onde o arquivo está, depois de já ter o PyInstaller no computador): `pyinstaller --onefile IoTMachineLeaning.py`

> IoTFacialRecognition.py <a id="IoTFacialRecognition"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Teste de criação de programa capaz de reconhecer faces onde é obrigatório ter uma câmera.

 1. Obrigatório ter uma webcam para operar esse programa.
 2. Programa pronto para executar. Apenas use de preferência o [Google Colaboratory](https://colab.research.google.com) para executar o código.
 3. Carregar o programa no ambiente do Google Colab e executar tudo de uma vez. 

> ImageCreationWithOpenAI.py <a id="ImageCreationWithOpenAI"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Efetuar a chamada da API da OpenAI para tratar de criar uma imagem a partir de outra.

 1. Instalar o pacote OpenAI: `pip install openai`.
 2. Para execução do código, é obrigatório ter uma chave da API da OpenAI no trecho do código com as palavras `YOUR API KEY FROM OPENAI HERE`. Essa chave está disponível no próprio site da [API da OpenAI](https://openai.com/api/).
 3. Para a execução do trecho para o tratamento de imagens, é obrigatório ter a imagem disponível de preferência na mesma pasta onde o arquivo do código se encontra e nomeá-lo em `image.png` (trecho dentro do código). 

> PhoneNumberID.py <a id="PhoneNumberID"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Recebe números de telefone em determinado formato e devolve a Operadora e a Região ao qual o número digitado pertence.

 1. Instalar o pacote PhoneNumbers: `pip install phonenumbers`.
 2. Ao executar o código, será solicitado que se digite o número de telefone do qual se deseja identificar, considerando o padrão +CCAANNNNNNNNN onde o + é o sinal internacional, C é o código do país, A é o código da região e N é o número do telefone com até 9 dígitos.
 3. Serão feitas solicitações consecutivas para digitação do número de telefone. O programa se encerra se ao invés de digitar o número de telefone for digitado a palavra.

> VariableDeclaration.ts <a id="VariableDeclaration"></a> [Voltar ao Início](#inicio)

- <b>Resumo:</b> Prática simples de uso da linguagem de programação TypeScript.

1. Apenas um resumo básico e inicial sobre TypeScript e seus usos para declaração de variáveis