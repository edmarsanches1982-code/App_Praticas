import streamlit as st
st.header("Introduzindo os elementos do streamlit")
menu = option_menu(menu_title="menu",
                   options=["Início","Gráficos Estátisticos", "Gráficos Dinamicos", "wiggets","Formulario"],
                   icons=["house", "bar-chat","bar-chat-line", "toggles","bar-chat"],
                   menu_icon="cast",
                   default_index=0,
                   orientation="horizontal"
                   
  )
