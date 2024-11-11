import streamlit as st
import pandas as pd
import numpy as np

#Titulo do dashboard
st.title("Meu pequeno Dashboard")

#Cria dados de exemplo
dados = pd.DataFrame(
    np.random.randn(100, 2),
    columns = ['coluna_x', 'coluna_y']
)
#Exibe o dataframe
st.write("Dados gerados:", dados)

#Gráfico simples de linha
st.line_chart(dados)

#Gráfico de barras
st.bar_chart(dados)

'''
Aqui estão as etapas para seguir:

Quando o prompt solicitar seu e-mail, basta pressionar Enter para continuar sem inserir um.
Depois disso, o Streamlit deverá iniciar e exibir no terminal a URL para acessar o dashboard no seu navegador. Algo como:
arduino
Copiar código
Local URL: http://localhost:8501
Network URL: http://<your-ip>:8501
Abra o navegador e acesse o localhost:8501 para visualizar o seu dashboard.

'''