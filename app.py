
import streamlit as st
from modelo import carregar_modelo

# Configuração da página
st.set_page_config(
    page_title="Gerador de Histórias com IA",
    page_icon="📖",
    layout="centered"
)

st.title("📖 Gerador de Histórias com IA")

st.write(
    "Crie histórias com Inteligência Artificial! "
    "Projeto da Fase 4 da Pós-Tech FIAP."
)

st.divider()

# Carregar o modelo uma única vez
@st.cache_resource
def obter_modelo():
    return carregar_modelo()

# Formulário
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
    placeholder="Ex.: Uma jovem encontra uma chave mágica..."
)

# Função de geração
def gerar_historia(genero, tema):

    modelo = obter_modelo()

    mensagens = [
        {
            "role": "system",
            "content": (
                "Você é um escritor brasileiro especializado "
                "em histórias criativas. Continue narrativas "
                "com coerência e personagens consistentes."
            )
        },
        {
            "role": "user",
            "content": (
                f"Gênero: {genero}\n"
                f"Continue a seguinte história:\n\n{tema}"
            )
        }
    ]

    resposta = modelo.create_chat_completion(
        messages=mensagens,
        max_tokens=250,
        temperature=0.7,
        top_p=0.9,
        repeat_penalty=1.1
    )

    return resposta["choices"][0]["message"]["content"]


# Botão principal
if st.button("✨ Gerar história", type="primary"):

    if not tema.strip():
        st.warning("Digite um tema para sua história.")

    else:
        with st.spinner("Nossa IA está criando sua história..."):
            try:
                historia = gerar_historia(genero, tema)

                st.subheader("📖 Sua história")
                st.write(tema.strip() + "\n\n" + historia)

            except Exception as erro:
                st.error("Erro ao gerar a história.")
                st.exception(erro)

st.divider()

st.caption(
    "FIAP — Pós-Tech | Machine Learning Engineering | Fase 4"
)
