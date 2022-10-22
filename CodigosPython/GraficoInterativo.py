# This Python file uses the following encoding: iso-8859-15 -*-
import pandas as pd
import plotly.express as px
import streamlit as st

"""
streamlit � usado junto com a plataforma online e tem sincroniza��o com o GitHub. Criar conta, sincronizar o Streamlit com o GitHub e colocar o projeto em um 
reposit�rio para ser executado nele.
"""

# Ler o Dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Nomenclatura de colunas
df = df.rename(columns={'newDeaths': 'Novos �bitos', 'newCases': 'Novos Casos', 'deaths_per_100k_inhabitants': '�bitos a Cada 100 mil Habitantes', 'totalCases_per_100k_inhabitants': 'Casos a Cada 100 mil Habitantes'})

# Selecao de Estados
# state = 'RJ' -- comentado para adicionar a linha 18
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual Estado Gostaria de Ver?', estados)

# Selecao de Colunas
# column = 'Casos a Cada 100 mil Habitantes' -- comentado para adicionar a linha 23
colunas = ['Novos �bitos', 'Novos Casos', '�bitos a Cada 100 mil Habitantes', 'Total de Casos a cada 100 mil Habitantes']
column = st.sidebar.selectbox('Qual Informa��o Gostaria de Ver?', colunas)

# Selecao das linhas do estado selecionado
df = df[df['state'] == state] 

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

# print('DADOS COVID - BRASIL') -- comentado para adicionar a linha 32
st.title('DADOS COVID - BRASIL')

#print('Nessa aplica��o, o usu�rio escolhe o estado e a informa��o que deseja ter acesso. Para isso, verifique o menu lateral.')  -- comentado para adicionar a linha 35
st.write('Nessa aplica��o, o usu�rio escolhe o estado e a informa��o que deseja ter acesso. Para isso, verifique o menu lateral.')

# fig.show() -- comentado para adicionar a linha 38
st.plotly_chart(fig, use_container_width=True)

# Rodape
st.caption('Dados de WCOCA - GitHub https://github.com/wcota/covid19br')