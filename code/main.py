import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nota.py as npy

titulo = st.title("Entrada de dados")
opcao = st.sidebar.selectbox(
    "Selecione uma métrica",
    [
        "nota de entrada",
        "nota de saída",
    ],
)
st.title("Cálculo de Notas Fiscais")

if opcao == "nota de entrada":
    opcao2 = st.selectbox(
        "Selecione o tipo de nota",
        [
            "uso",
            "revenda",
        ],
    )
    if opcao2 == "uso":
        st.subheader(
            "Nota para uso"
        )
        descProduto = st.text_input(
            "Descrição do produto:"
        )
        valorUnit = st.number_input(
            "Valor unitário do produto:", min_value=0.0, step=0.01
        )
        valorIPI = st.number_input(
        "Valor do IPI:", min_value=0.0, step=0.01
        )
        valorTotal = st.number_input(
            "Valor total contábil:", min_value=0.0, step=0.01
        )

        if st.button("Adicionar produto"):
            st.success(
                f"Produto {descProduto} adicionado com sucesso!"
            )

        st.button("Calcular valores")
        npy.calculoAtributos()

        produtos = []
        produtos.append(
            {
                "descricao": descProduto,
                "valor_unitario": valorUnit,
                "valor_ipi": valorIPI,
                "valor_total": valorTotal,
            }
        )



      

     