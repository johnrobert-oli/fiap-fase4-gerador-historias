
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Modelo original e nosso adaptador treinado
MODELO_BASE = "Qwen/Qwen2.5-1.5B-Instruct"

MODELO_FIAP = (
    "johnrobert21/fiap-fase4-gerador-historias"
)


def carregar_modelo():
    """Carrega o Qwen e nosso adaptador LoRA."""

    tokenizer = AutoTokenizer.from_pretrained(
        MODELO_FIAP
    )

    modelo = AutoModelForCausalLM.from_pretrained(
        MODELO_BASE,
        dtype=torch.float32
    )

    modelo = PeftModel.from_pretrained(
        modelo,
        MODELO_FIAP
    )

    modelo.eval()

    return tokenizer, modelo
