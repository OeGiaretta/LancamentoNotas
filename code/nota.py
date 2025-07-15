import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import app as apy
import nota as noty
from app import col3

totalGeralIPI = 0
totalGeralUnit = 0
totalUser = 0
totalNota = 0


# Calcula os dados da nota de entrada (Uso)
def calculo():
    with col3:
        if st.button("Calcular Nota de Entrada"):
            totalGeralIPI = round(
                sum(
                    novo_produto["valor_ipi"]
                    for novo_produto in st.session_state.produtos
                ),2,
            )
            totalGeralUnit = round(
                sum(
                    novo_produto["valor_unitario"]
                    for novo_produto in st.session_state.produtos
                ),2,
            )
            totalUser = round(
                sum(
                    novo_produto["valor_total"]
                    for novo_produto in st.session_state.produtos
                ),2,
            )
            totalNota = round(totalGeralUnit + totalGeralIPI, 2)
            st.write("Resultado do cálculo dos produtos:")
            st.write(f"Total IPI: {totalGeralIPI}")
            st.write(f"Total Unitário: {totalGeralUnit}")
            st.write(f"Cálculo do total informado pelo usuário: {totalUser}")
            st.write(f"Total da Nota calculado pelo sistema: {totalNota}")
            if totalNota == totalUser:
                st.success("O valor total da nota está correto.")
            else:
                st.error(
                    "O valor total da nota não confere com o calculado pelo sistema."
                )
