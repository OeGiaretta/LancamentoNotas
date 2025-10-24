import streamlit as st
import pandas as pd
import numpy as np

from nota import NotaEntrada as ne

nota = ne()

class Utils:

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