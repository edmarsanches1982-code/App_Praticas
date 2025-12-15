import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
fom datetime import date
st.header("Introduzindo os elementos do streamlit")
menu = option_menu(menu_title="menu",
                   options=["Início","Gráficos Estátisticos", "Gráficos Dinamicos", "wiggets","Formulario"],
                   icons=["house", "bar-chat","bar-chat-line", "toggles","bar-chat"],
                   menu_icon="cast",
                   default_index=0,
                   orientation="horizontal"
                   
  )
