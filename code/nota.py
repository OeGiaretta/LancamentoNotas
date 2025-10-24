import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class NotaEntrada:

    def __init__(self):
        self.totalGeralIPI = 0
        self.totalGeralUnit = 0
        self.totalNota = 0
        self.totalUser = 0
        
    # Calcula os dados da nota de entrada (Uso)
    def calculo(self):        
        
        self.totalGeralIPI = round(
            sum(
                novo_produto["valor_ipi"]
                for novo_produto in st.session_state.produtos
            ),2,
        )
        self.totalGeralUnit = round(
            sum(
                novo_produto["valor_unitario"]
                for novo_produto in st.session_state.produtos
            ),2,
        )
        self.totalUser = round(
                    sum(
                        novo_produto["valor_total"]
                        for novo_produto in st.session_state.produtos
                    ),2,
                )
        
        self.totalNota = round(self.totalGeralUnit + self.totalGeralIPI, 2)
        return self.totalGeralIPI, self.totalGeralUnit, self.totalUser, self.totalNota
        
    #Calcula o total informado pelo cliente
    def calculo_cliente(self):
        totalUser = round(
            sum(
                novo_produto["valor_total"]
                for novo_produto in st.session_state.produtos
            ),2,
        )
        self.totalGeralIPI, self.totalGeralUnit, self.totalUser, self.totalNota = self.calculo()

    # Mostra tabela de resultados
    def resultado(self):
        st.subheader("Resultado do cálculo dos produtos:")

        st.session_state.resultados = []
        resultados = {
            "total IPI": self.totalGeralIPI,
            "Total Unitário": self.totalGeralUnit,
            "Total informado pelo cliente": self.totalUser,
            "Total calculado pelo sistema": self.totalNota,
        }
        st.session_state.resultados.append(resultados)
        df_resultados = pd.DataFrame(st.session_state.resultados)
        st.dataframe(
            df_resultados,
        )
        if self.totalNota == self.totalUser:
            st.success("O valor total da nota está correto.")
        else:
            st.error("O valor total da nota não confere com o calculado pelo sistema.")
    

    def revenda(self):  
        # Configuração das notas de revenda
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
