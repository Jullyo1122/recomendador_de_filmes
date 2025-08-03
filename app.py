import streamlit as st
from utils.loader import carregar_filmes

filmes = carregar_filmes()
st.title("Olá, cinéfilo!")
st.write("Aqui está uma lista de filmes populares, selecione apenas os filmes que você gostou de ter assistido:")
st.dataframe(filmes)
