import streamlit as st
import pandas as pd
import numpy as np
import telaInicial as ti
import uso as so

from utils import Utils as ut
from nota import NotaEntrada as ne

nota = ne()
utils = ut()

if __name__ == "__main__":
    st.set_page_config(
        page_title="Lançamento de Notas Fiscais",
        page_icon=":memo:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

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
    col1, col2, col3 = st.columns(3)
    # Limpar produtos da lista
    with col1:
        ut.limpar_produtos()
        
    # Excluir produtos da lista
    with col2:
        ut.excluir_produto()
        
    # Calcula os dados da nota de entrada (Uso)
    with col3:
        button_calcular = st.button("Calcular Nota de Entrada")        
    if button_calcular:
                nota.calculo()
                nota.calculo_cliente()
                nota.resultado()
    
    # Verifica se a opção selecionada é "revenda"
    if utilizado_Para == "Revenda":
        nota.revenda()