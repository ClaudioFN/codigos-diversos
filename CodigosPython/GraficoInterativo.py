# This Python file uses the following encoding: iso-8859-15 -*-
import pandas as pd
import plotly.express as px
import streamlit as st

"""
pip install plotly-express -> instalar o pacote no computador
pip install streamlit -> instalar os pacotes relacionados ao Streamlit

Video explicativo do assunto -> YouTube: youtu.be/Qxm5QEEKHqE

streamlit é usado junto com a plataforma online e tem sincronização com o GitHub. Criar conta, sincronizar o Streamlit com o GitHub e colocar o projeto em um 
repositório para ser executado nele.
"""

# Ler o Dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Nomenclatura de colunas
df = df.rename(columns={'newDeaths': 'Novos Óbitos', 'newCases': 'Novos Casos', 'deaths_per_100k_inhabitants': 'Óbitos a Cada 100 mil Habitantes', 'totalCases_per_100k_inhabitants': 'Casos a Cada 100 mil Habitantes'})

# Selecao de Estados
# state = 'RJ' -- comentado para adicionar a linha 18
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual Estado Gostaria de Ver?', estados)

# Selecao de Colunas
# column = 'Casos a Cada 100 mil Habitantes' -- comentado para adicionar a linha 23
colunas = ['Novos Óbitos', 'Novos Casos', 'Óbitos a Cada 100 mil Habitantes', 'Total de Casos a cada 100 mil Habitantes']
column = st.sidebar.selectbox('Qual Informação Gostaria de Ver?', colunas)

# Selecao das linhas do estado selecionado
df = df[df['state'] == state] 

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

# print('DADOS COVID - BRASIL') -- comentado para adicionar a linha 32
st.title('DADOS COVID - BRASIL')

#print('Nessa aplicação, o usuário escolhe o estado e a informação que deseja ter acesso. Para isso, verifique o menu lateral.')  -- comentado para adicionar a linha 35
st.write('Nessa aplicação, o usuário escolhe o estado e a informação que deseja ter acesso. Para isso, verifique o menu lateral.')

# fig.show() -- comentado para adicionar a linha 38
st.plotly_chart(fig, use_container_width=True)

# Rodape
st.caption('Dados de WCOCA - GitHub https://github.com/wcota/covid19br')