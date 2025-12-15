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

    
