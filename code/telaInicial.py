import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def tela_inicial():
    # Configuração do título da aplicação
    st.title("Cálculo de Notas Fiscais")
    st.subheader("Bem-vindo ao sistema de cálculo de notas fiscais!")
    st.write(
        "Selecione uma opção no menu lateral para começar a inserir dados de notas fiscais."
    )
    st.write(
        "Você pode calcular notas de entrada para uso ou revenda, e verificar se os valores informados estão corretos."
    )
    st.write(
        "Para começar, selecione a opção 'nota de entrada' no menu lateral e siga as instruções."
    )  
    st.sidebar.info(
        "Use o menu lateral para navegar entre as opções disponíveis. Se precisar de ajuda, consulte a documentação."
    )
    