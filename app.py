import streamlit as st
from utils.loader import carregar_filmes

filmes = carregar_filmes()

if "favoritos" not in st.session_state:
    st.session_state.favoritos = []

st.title("Olá, cinéfilo!")
st.write("Aqui está uma lista de filmes populares, selecione apenas os filmes que você gostou de ter assistido:")

option = st.selectbox('Quais são seus filmes favoritos?', filmes['title'])
select = st.button("Adicionar")
finish = st.button("Finalizar")

if select:
    if option not in st.session_state.favoritos:
        st.session_state.favoritos.append(option)
        st.success(f"Filme '{option}' adicionado aos favoritos!")
    
if finish:
     st.subheader("Seus filmes favoritos:")
     for filmes in st.session_state.favoritos:
         st.write(f"- {filmes}")