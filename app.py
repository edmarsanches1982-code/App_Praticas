import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
import openpyxl
from datetime import date
st.header("Introduzindo os elementos do streamlit")
menu = option_menu(menu_title="menu",
                   options=["Início","Gráficos Estátisticos", "Gráficos Dinamicos", "Widgets","Formulario"],
                   icons=["house", "bar-chart","bar-chart-line", "toggles","bar-chart"],
                   menu_icon="cast",
                   default_index=0,
                   orientation="horizontal"                 
  )

with st.sidebar:
  st.success("**UPLOAD DE DADOS**")
  dados = st.file_uploader(
      "carregue...", 
      type=["xlsx","xls"])
  if dados:
    def carregar_dados(dados):
      try:
        df = pd.read_excel(dados)
        return df
      except FileNotFoundError:
        return pd.DataFrame()
    df = carregar_dados(dados)
    st.table(df)
  else:
    st.info("carregue um ficheiro excel para começar")

# INICIO
if menu == "Início":
    with st.expander("**Sobre o Instituto Nacional de Estatística**"):
        st.write("Acesse o site www.ine.cv")
        st.image("Ine.jpg")  # Certifique-se de que a imagem está na mesma pasta

# Widgets
if menu == "Widgets":
    bt = st.button("Dê um clique!")

    if bt:
        st.info("Clicaste num botão acima!")

    sd = st.slider(
        "Novo ponto do slider!",
        min_value=25,
        max_value=35,
        value=30,
        step=1
    )

    texto = f"Eu tenho {sd} anos!"
    st.success(texto)

if menu == "Gráficos Estátisticos":
  col1, col2, col3 = st.columns([0.3, 0.1, 0.6])

with col1:
    st.subheader("coluna 1")
    dados_hist = [3, 9, 5, 12, 6, 7, 5, 6, 10]
    fig, ax = plt.subplots()
    ax.hist(dados_hist, bins=5, color="skyblue" , edgecolor="black")
    ax.set_title("Histograma")
    st.pyplot(fig)
  
with col3:
    st.subheader("coluna 2")
    lab = ["python", "java", "C++", "javaScript"]
    pop = [45, 25, 15, 15]
    fig, ax = plt.subplots()
    ax.pie(pop, labels=lab, autopct="%1.1f%%", startangle=90)
    ax.set_title("Gráfico circular")
    ax.axis("equal")
    st.pyplot(fig)
    


    
