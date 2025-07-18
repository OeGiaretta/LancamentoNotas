import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import telaInicial as ti
import nota as nt


# Seleção de nota e criação da lista de produtos
titulo = st.title("Entrada de dados")
opcao = st.sidebar.selectbox(
    "Selecione uma métrica",
    [
        "Tela Inicial",
        "nota de entrada",
        "nota de saída",
    ],
)

# Verifica se a opção selecionada é "nota de entrada"

if opcao == "Tela Inicial":
    ti.tela_inicial()

elif opcao == "nota de entrada":
    opcao2 = st.sidebar.selectbox(
        "Selecione o tipo de nota",
        [
            "uso",
            "revenda",
        ],
    )

    # Verifica se a opção selecionada é "uso" ou "revenda"
    if opcao2 == "uso":

        # Configuração das notas de uso
        st.sidebar.subheader("Nota para uso")
        descProduto = st.sidebar.text_input("Descrição do produto:")
        valorUnit = st.sidebar.number_input(
            "Valor unitário do produto:", min_value=0.0, step=0.01, key="valor_unitario"
        )
        qntProd = st.sidebar.number_input(
            "Quantidade de produto:", min_value=0.0, step=0.01, key="qnt_produto"
        )
        valorIPI = st.sidebar.number_input(
            "Valor do IPI:", min_value=0.0, step=0.01, key="valor_ipi"
        )
        valorTotal = st.sidebar.number_input(
            "Valor total contábil:", min_value=0.0, step=0.01, key="valor_total"
        )
        totalNota = (valorUnit * qntProd) + valorIPI 

        # Verifica se todos os campos foram preenchidos
        if st.sidebar.button("Adicionar produto") and (
            descProduto
            and valorUnit > 0
            and qntProd > 0
            and valorIPI > 0
            and valorTotal > 0
        ):

            novo_produto = {
                "descricao": descProduto,
                "valor_unitario": valorUnit,
                "quantidade": qntProd,
                "valor_ipi": valorIPI,
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

    # Deixar tabela de produtos visível
    if "produtos" in st.session_state and st.session_state.produtos:
        st.write("Lista de produtos:")
        df = pd.DataFrame(st.session_state.produtos)
        st.dataframe(df, use_container_width=True)
    else:
        st.write("Nenhum produto cadastrado.")

    # Alinhar botões
    col1, col2, col3 = st.columns(3)

    # Limpar produtos da lista
    with col1:
        if st.button("limpar produtos"):
            if "produtos" in st.session_state:
                del st.session_state.produtos
                st.write("Lista de produtos limpa.")
            else:
                st.write("Nenhum produto para limpar.")

    # Excluir produtos da lista
    with col2:
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

    # Calcula os dados da nota de entrada (Uso)

    with col3:

        if st.button("Calcular Nota de Entrada"):
            nt.calculo()
            totalUser = round(
                sum(
                    novo_produto["valor_total"]
                    for novo_produto in st.session_state.produtos
                ),2,
            )
            nt.totalGeralIPI, nt.totalGeralUnit, nt.totalUser, nt.totalNota = nt.calculo()
    
    st.subheader("Resultado do cálculo dos produtos:")

    st.session_state.resultados = []
    resultados = {
        "total IPI": nt.totalGeralIPI,
        "Total Unitário": nt.totalGeralUnit,
        "Total informado pelo cliente": nt.totalUser,
        "Total calculado pelo sistema": nt.totalNota,
    }
    st.session_state.resultados.append(resultados)
    df_resultados = pd.DataFrame(st.session_state.resultados)
    st.dataframe(
        df_resultados,
    )
    if nt.totalNota == nt.totalUser:
        st.success("O valor total da nota está correto.")
    else:
        st.error("O valor total da nota não confere com o calculado pelo sistema.")