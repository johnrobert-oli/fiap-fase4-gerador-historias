
import streamlit as st

# Configuração da aplicação
st.set_page_config(
    page_title="Gerador de Histórias com IA",
    page_icon="📖",
    layout="centered"
)

# Título e apresentação
st.title("📖 Gerador de Histórias com IA")

st.write(
    "Crie histórias utilizando Inteligência Artificial! "
    "Um projeto desenvolvido para a Fase 4 "
    "da Pós-Tech em Machine Learning Engineering da FIAP."
)

st.divider()

# Formulário de criação
genero = st.selectbox(
    "Escolha o gênero da história:",
    [
        "Fantasia",
        "Aventura",
        "Mistério",
        "Ficção científica",
        "Suspense",
        "Conto de fadas"
    ]
)

tema = st.text_area(
    "Sobre o que será sua história?",
    placeholder="Ex.: Uma jovem encontra uma chave mágica em uma floresta..."
)

if st.button("✨ Gerar história", type="primary"):
    if not tema.strip():
        st.warning("Digite um tema para sua história.")
    else:
        st.info(
            "Interface preparada! "
            "Em breve conectaremos nosso modelo Qwen 1.5B."
        )

st.divider()

st.caption(
    "FIAP — Pós-Tech | Machine Learning Engineering | Fase 4"
)
