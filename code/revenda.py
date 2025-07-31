import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def revenda():  # Configuração das notas de revenda
    st.sidebar.subheader("Nota para revenda")
    descProduto = st.sidebar.text_input("Descrição do produto:")
    valorUnit = st.sidebar.number_input(
    "Valor unitário do produto:", min_value=0.0, step=0.01, key="valor_unitario_revenda"
    )
    qntProd = st.sidebar.number_input(
    "Quantidade de produto:", min_value=0.0, step=0.01, key="qnt_produto_revenda"
    )
    valorIPI = st.sidebar.number_input(
    "Valor do IPI:", min_value=0.0, step=0.01, key="valor_ipi_revenda"
    )
    valorICMS = st.sidebar.number_input(
    "Valor do ICMS:", min_value=0.0, step=0.01, key="valor_icms_revenda"
    )
    valorTotal = st.sidebar.number_input(
    "Valor total contábil:", min_value=0.0, step=0.01, key="valor_total_revenda"
    )
    totalNota = (valorUnit * qntProd) + valorIPI + valorICMS

    # Verifica se todos os campos foram preenchidos
    if st.sidebar.button("Adicionar produto") and (
    descProduto
    and valorUnit > 0
    and qntProd > 0
    and valorIPI > 0
    and valorICMS > 0
    and valorTotal > 0  
    ):

        novo_produto = {
        "descricao": descProduto,
        "valor_unitario": valorUnit,
        "quantidade": qntProd,
        "valor_ipi": valorIPI,
        "valor_icms": valorICMS,
        "valor_total": valorTotal,
        "total_produto": totalNota,
        }

        # Adiciona o produto à lista
        if "produtos" not in st.session_state:
            st.session_state.produtos = []
            st.session_state.produtos.append(novo_produto)
            st.sidebar.success("Produto adicionado com sucesso!")
        else:
            st.sidebar.error("Por favor, preencha todos os campos.")

    