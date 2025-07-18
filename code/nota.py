import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


totalGeralIPI = 0
totalGeralUnit = 0
totalNota = 0
totalUser = 0


# Calcula os dados da nota de entrada (Uso)
def calculo():        
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
            return totalGeralIPI, totalGeralUnit, totalUser, totalNota
