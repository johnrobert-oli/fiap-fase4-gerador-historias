
# 📖 Gerador de Histórias Criativas com IA

Projeto desenvolvido para o Tech Challenge — Fase 4 da Pós-Tech em Machine Learning Engineering da FIAP.

## 🌐 Aplicação publicada

Acesse o Gerador de Histórias:

https://fiap-fase4-gerador-historias.streamlit.app/

O usuário pode selecionar um gênero literário, inserir o início de uma narrativa e solicitar que a inteligência artificial continue a história.

## 🎯 Objetivo

Desenvolver uma aplicação de geração de texto criativo utilizando modelos de linguagem, técnicas de fine-tuning e uma interface web interativa.

## 🧠 Modelo utilizado

- Modelo base: Qwen/Qwen2.5-1.5B-Instruct
- Biblioteca de treinamento: Hugging Face Transformers
- Técnica de adaptação: LoRA (PEFT)
- Idioma principal: português brasileiro
- Formato de implantação: GGUF
- Quantização: Q4_K_M

O modelo base foi adaptado para a tarefa de continuação de histórias e posteriormente convertido para um formato mais leve, adequado à inferência em CPU.

## 📚 Dataset

Dataset utilizado:

https://huggingface.co/datasets/benjleite/FairytaleQA-translated-ptBR

O conjunto contém narrativas de contos de fadas traduzidas para português brasileiro.

Durante o pré-processamento, foram realizadas etapas de limpeza, remoção de duplicatas e preparação dos exemplos para treinamento.

## ⚙️ Treinamento

O treinamento foi realizado no Google Colab utilizando GPU.

A adaptação foi feita com LoRA, reduzindo o número de parâmetros treináveis em relação ao fine-tuning completo.

Configurações principais:

- LoRA rank: 8
- LoRA alpha: 16
- Módulos adaptados: q_proj, k_proj, v_proj e o_proj
- Treinamento inicial seguido de uma etapa adicional de ajuste
- Comprimento de sequência ampliado na segunda etapa

Na segunda etapa, foram utilizados aproximadamente:

- 2.931 exemplos de treinamento
- 351 exemplos de validação

As perdas finais dessa etapa ficaram aproximadamente em:

- Training loss: 2,14
- Validation loss: 2,10

## 📊 Avaliação

A avaliação combinou a análise das perdas de treinamento e validação com testes qualitativos de geração de histórias.

O modelo demonstrou capacidade de produzir continuações em português, incluindo personagens, cenários e acontecimentos criativos.

Entretanto, foram observadas limitações:

- Inconsistências na continuidade narrativa
- Mudanças inesperadas de acontecimentos
- Repetições ocasionais
- Histórias interrompidas antes de uma conclusão

Essas limitações são importantes para compreender o desempenho real do modelo e possíveis melhorias futuras.

## 📦 Modelos publicados

Adaptador LoRA treinado:

https://huggingface.co/johnrobert21/fiap-fase4-gerador-historias

Modelo compactado GGUF:

https://huggingface.co/johnrobert21/fiap-fase4-historias-gguf

O modelo adaptado foi combinado com os pesos do modelo base e convertido para GGUF, utilizando quantização Q4_K_M.

O arquivo resultante possui aproximadamente 986 MB.

## 💻 Tecnologias utilizadas

- Python
- Google Colab
- Hugging Face Transformers
- PEFT / LoRA
- PyTorch
- llama.cpp
- llama-cpp-python
- Hugging Face Hub
- Streamlit
- GitHub

## 🚀 Como executar

Clone o repositório:

    git clone https://github.com/johnrobert-oli/fiap-fase4-gerador-historias.git

Entre na pasta:

    cd fiap-fase4-gerador-historias

Recomenda-se utilizar Python 3.11 e instalar as dependências compatíveis com o sistema operacional.

Inicie a aplicação:

    python -m streamlit run app.py

Na primeira geração, a aplicação baixa o modelo GGUF do Hugging Face, caso ainda não esteja disponível localmente.

## 🏗️ Estrutura do projeto

- app.py — Interface Streamlit e geração de histórias
- modelo.py — Download e carregamento do modelo GGUF
- requirements.txt — Dependências da aplicação
- README.md — Documentação do projeto

## ☁️ Deploy

A aplicação foi publicada utilizando Streamlit Community Cloud, com código hospedado no GitHub e pesos do modelo armazenados no Hugging Face.

Essa arquitetura permite executar o modelo compactado em CPU, sem necessidade de uma GPU dedicada na hospedagem.

## 🔮 Melhorias futuras

- Ampliar e diversificar o dataset
- Melhorar a coerência entre personagens e acontecimentos
- Avaliar diferentes estratégias de fine-tuning
- Implementar geração de histórias mais longas
- Adicionar controles de criatividade e comprimento
- Realizar avaliações automáticas e humanas mais abrangentes

## 🎓 Projeto acadêmico

FIAP — Pós-Tech em Machine Learning Engineering

Tech Challenge — Fase 4

Desenvolvido por John Robert Marreiro de Oliveira.
