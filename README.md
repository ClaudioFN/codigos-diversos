# Códigos Diversos
Repositório de códigos de assuntos diversos.

Python:
- [AbreProgramasPython](#AbreProgramasPython)
- [CotacaoDolar](#CotacaoDolar) 

**Listagem de códigos**

> 1º Código: AbreProgramasPython.py <a id="AbreProgramasPython"></a>
  
 1. Site com as instruções de instalação do pip de Python para instalação do PyInstaller: [Pypa](https://pip.pypa.io/en/stable/getting-started/)
 2. Após ter o PyInstaller, executar o comando criador de executáveis Python: `pyinstaller --onefile AbreProgramasPython.py`
 3. Em alguns casos é necessário colocar o caminho do PyInstaller para ele entender a execução

> 2º Código: CotacaoDolar.py <a id="CotacaoDolar"></a>

 1. Instalar o pacote requests: `pip install requests`
 2. Link da API em uso no código: [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
 3. O código cria um arquivo com dados do sucesso ou erro de execução (LOG do processo efetuado) na mesma pasta que o código se encontra
 4. Alterar a URL da linha 6 ( variável "url") para outras moedas
