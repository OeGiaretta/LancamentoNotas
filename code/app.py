import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nota as npy

# Seleção de nota e criação da lista de produtos
produtos = []
titulo = st.title("Entrada de dados")
opcao = st.sidebar.selectbox(
    "Selecione uma métrica",
    [
        "nota de entrada",
        "nota de saída",
    ],
)

# Configuração do título da aplicação
st.title("Cálculo de Notas Fiscais")


# Função para adicionar produtos à lista
def adicionarProd(descProduto, valorUnit, valorIPI, valorTotal):
    novo_produto = {
        "descricao": descProduto,
        "valor_unitario": valorUnit,
        "valor_ipi": valorIPI,
        "valor_total": valorTotal,
    }
    st.session_state.produtos.append(novo_produto)
    df = pd.DataFrame(produtos)
    st.sidebar.write("Produtos cadastrados:")
    st.sidebar.dataframe(df, use_container_width=True)
    st.session_state.produtos = []


# Verifica se a opção selecionada é "nota de entrada"
if opcao == "nota de entrada":
    opcao2 = st.selectbox(
        "Selecione o tipo de nota",
        [
            "uso",
            "revenda",
        ],
    )

    # Verifica se a opção selecionada é "uso" ou "revenda"
    if opcao2 == "uso":

        # Configuração das notas de uso
        st.subheader("Nota para uso")
        descProduto = st.text_input("Descrição do produto:")
        valorUnit = st.number_input(
            "Valor unitário do produto:", min_value=0.0, step=0.01, key="valor_unitario"
        )
        qntProd = st.number_input(
            "Valor unitário do produto:", min_value=0.0, step=0.01, key="qnt_produto"
        )
        valorIPI = st.number_input(
            "Valor do IPI:", min_value=0.0, step=0.01, key="valor_ipi"
        )
        valorTotal = st.number_input(
            "Valor total contábil:", min_value=0.0, step=0.01, key="valor_total"
        )

        # Verifica se todos os campos foram preenchidos
        if (
            st.button("Adicionar produto", key="B1") and descProduto
            and valorUnit
            and valorIPI
            and valorTotal
        ):
            st.button("Adicionar produto", key="B1,")
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

        # Botão para calcular os valores
        st.button("Calcular valores", key="B2")
        npy.calculoAtributos()
