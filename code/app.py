import streamlit as st
import pandas as pd
import numpy as np
import telaInicial as ti
import nota as nt
import uso as so

from utils import Utils as ut

# Seleção de nota e criação da lista de produtos
opcao = st.sidebar.selectbox(
    "Selecione uma métrica",
    [
        "Tela Inicial",
        "Nota de entrada",
        #"Nota de saída",
    ],
)

# Verifica se a opção selecionada é "nota de entrada"
if opcao == "Tela Inicial":
    ti.tela_inicial()

elif opcao == "Nota de entrada":
    utilizado_Para = st.sidebar.selectbox(
        "Selecione o tipo de nota",
        [
            "Uso",
            "Revenda",
        ],
    )

    titulo = st.title("Entrada de dados: " + utilizado_Para)

    # Verifica se a opção selecionada é "uso" ou "revenda"
    if utilizado_Para == "Uso":
        so.uso()

    # Deixar tabela visível
    ut.tabela_visivel()

    # Alinha os botões na mesma linha
    ut.alinhar_botoes()

    # Limpar produtos da lista
    with ut.col1:
        ut.limpar_produtos()
        
    # Excluir produtos da lista
    with ut.col2:
        ut.excluir_produto()
        
    # Calcula os dados da nota de entrada (Uso)
    with ut.col3:
        if st.button("Calcular Nota de Entrada"):
            nt.calculo()
            nt.calculo_cliente()

    # Mostra o resultado dos cálculos
    ut.resultado()

    # Verifica se a opção selecionada é "revenda"
    if utilizado_Para == "Revenda":
        nt.revenda()