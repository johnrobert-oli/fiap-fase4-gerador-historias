
from llama_cpp import Llama
from huggingface_hub import hf_hub_download
import os

# Repositório do nosso modelo compactado
REPOSITORIO = "johnrobert21/fiap-fase4-historias-gguf"

ARQUIVO_MODELO = "qwen15b_historias_Q4_K_M.gguf"


def carregar_modelo():
    """Carrega nosso Qwen 1.5B ajustado e compactado."""

    # Procurar primeiro o modelo local
    caminho_local = os.path.join(
        "modelos",
        ARQUIVO_MODELO
    )

    if os.path.isfile(caminho_local):
        caminho = caminho_local
    else:
        # Baixar automaticamente do Hugging Face
        caminho = hf_hub_download(
            repo_id=REPOSITORIO,
            filename=ARQUIVO_MODELO
        )

    # Carregar a IA compactada
    modelo = Llama(
        model_path=caminho,
        n_ctx=1024,
        n_threads=4,
        n_gpu_layers=0,
        verbose=False
    )

    return modelo
