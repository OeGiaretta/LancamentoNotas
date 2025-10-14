import streamlit as st
import pandas as pd
import numpy as np

from nota import NotaEntrada as ne

class Utils:
    def alinhar_botoes():
        # Alinhar botões
        col1, col2, col3 = st.columns(3)

    # Limpar produtos da lista
    def limpar_produtos():
        if st.button("limpar produtos"):
            if "produtos" in st.session_state:
                del st.session_state.produtos
                st.write("Limpar lista de produtos?")
            else:
                st.write("Nenhum produto para limpar.")

    # Excluir produtos da lista
    def excluir_produto():
        if st.button("Excluir produto"):
            if "produtos" in st.session_state and st.session_state.produtos:
                st.sidebar.text_input(
                    "Digite a descrição do produto a ser excluído:",
                    key="produto_excluir",
                    placeholder="Descrição do produto",
                )
                produto_excluir = st.session_state.produto_excluir
                if produto_excluir:
                    st.session_state.produtos = [
                        produto
                        for produto in st.session_state.produtos
                        if produto["descricao"] != produto_excluir
                    ]
                    st.sidebar.write(f"Produto '{produto_excluir}' excluído.")
            else:
                st.sidebar.write("Nenhum produto para excluir.")

    # Deixar tabela visível
    def tabela_visivel():
        if "produtos" in st.session_state and st.session_state.produtos:
            st.write("Lista de produtos:")
            df = pd.DataFrame(st.session_state.produtos)
            st.dataframe(df, use_container_width=True)
        else:
            st.write("Nenhum produto cadastrado.")

    # Mostra tabela de resultados
    def resultado():
        st.subheader("Resultado do cálculo dos produtos:")

        st.session_state.resultados = []
        resultados = {
            "total IPI": ne.totalGeralIPI,
            "Total Unitário": ne.totalGeralUnit,
            "Total informado pelo cliente": ne.totalUser,
            "Total calculado pelo sistema": ne.totalNota,
        }
        st.session_state.resultados.append(resultados)
        df_resultados = pd.DataFrame(st.session_state.resultados)
        st.dataframe(
            df_resultados,
        )
        if ne.totalNota == ne.totalUser:
            st.success("O valor total da nota está correto.")
        else:
            st.error("O valor total da nota não confere com o calculado pelo sistema.")
            