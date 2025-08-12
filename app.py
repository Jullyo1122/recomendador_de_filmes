import streamlit as st
from utils.loader import carregar_filmes
from recomender import criar_recomendador, recomendar_filmes

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


cosine_sim, indices = criar_recomendador(filmes)

if finish:
    st.markdown("### 🎬 Seus filmes favoritos:")
    for filme in st.session_state.favoritos:
        st.write(f"- {filme}")

    st.markdown("### 🍿 Recomendações para você:")
    for favorito in st.session_state.favoritos:
        recomendacoes = recomendar_filmes(favorito, filmes, cosine_sim, indices)
        st.subheader(f"Baseado no filme **{favorito}**:")
        for r in recomendacoes:
            st.markdown(f"• {r}")

