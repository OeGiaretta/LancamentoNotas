import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Seleção de nota e criação da lista de produtos
titulo = st.title("Entrada de dados")
opcao = st.sidebar.selectbox(
    "Selecione uma métrica",
    [
        "nota de entrada",
        "nota de saída",
    ],
)

# Configuração do título da aplicação
st.title("Cálculo de Notas Fiscais")


# Função para adicionar produtos à lista - não utilizada
#def adicionarProd(descProduto, valorUnit, valorIPI, valorTotal):


# Verifica se a opção selecionada é "nota de entrada"
if opcao == "nota de entrada":
    opcao2 = st.selectbox(
        "Selecione o tipo de nota",
        [
            "uso",
            "revenda",
        ],
    )

    # Verifica se a opção selecionada é "uso" ou "revenda"
    if opcao2 == "uso":

        # Configuração das notas de uso
        st.subheader("Nota para uso")
        descProduto = st.text_input("Descrição do produto:")
        valorUnit = st.number_input(
            "Valor unitário do produto:", min_value=0.0, step=0.01, key="valor_unitario"
        )
        qntProd = st.number_input(
            "Quantidade de produto:", min_value=0.0, step=0.01, key="qnt_produto"
        )
        valorIPI = st.number_input(
            "Valor do IPI:", min_value=0.0, step=0.01, key="valor_ipi"
        )
        valorTotal = st.number_input(
            "Valor total contábil:", min_value=0.0, step=0.01, key="valor_total"
        )
        totalNota_Prod = (valorUnit + valorUnit) * qntProd

        
        
        # Verifica se todos os campos foram preenchidos
        if st.button(
                "Adicionar produto"
            ) and (
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
                "total_produto": totalNota_Prod
            }

            # Adiciona o produto à lista
            if "produtos" not in st.session_state:
                st.session_state.produtos = []
            st.session_state.produtos.append(novo_produto)           
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

    # Deixar tabela de produtos visível
    if "produtos" in st.session_state and st.session_state.produtos:
        st.sidebar.write("Lista de produtos:")
        df = pd.DataFrame(st.session_state.produtos)
        st.sidebar.dataframe(df, use_container_width=True)
    else:
        st.sidebar.write("Nenhum produto cadastrado.")

    # Limpar produtos da lista
    if st.sidebar.button("limpar produtos"):
        if "produtos" in st.session_state:
            del st.session_state.produtos
            st.sidebar.write("Lista de produtos limpa.")
        else:
            st.sidebar.write("Nenhum produto para limpar.")

    # Excluir produtos da lista
    if st.sidebar.button("Excluir produto"):
        if "produtos" in st.session_state and st.session_state.produtos:
            st.sidebar.text_input("Digite a descrição do produto a ser excluído:", 
                                  key="produto_excluir",
                                  placeholder="Descrição do produto"
                                  )
            produto_excluir = st.session_state.produto_excluir
            if produto_excluir:
                st.session_state.produtos = [
                    produto for produto in st.session_state.produtos
                    if produto["descricao"] != produto_excluir
                ]
                st.sidebar.write(f"Produto '{produto_excluir}' excluído.")
        else:
            st.sidebar.write("Nenhum produto para excluir.")

    # Calcula os dados da nota de entrada (Uso)
    if st.button(
        "Calcular Nota de Entrada"
            ):
        totalGeralIPI = round(
            sum(novo_produto["valor_ipi"] for novo_produto in st.session_state.produtos), 2
            )
        totalGeralUnit = round(
            sum(novo_produto["valor_unitario"] for novo_produto in st.session_state.produtos), 2
            )
        totalUser = round(
            sum(novo_produto["valor_total"] for novo_produto in st.session_state.produtos), 2
            )
        totalNota = round(
            totalGeralUnit + totalGeralIPI, 2
            )
        st.write("Resultado do cálculo dos produtos:")
        st.write(f"Total IPI: {totalGeralIPI}")
        st.write(f"Total Unitário: {totalGeralUnit}")
        st.write(f"Cálculo do total informado pelo usuário: {totalUser}")
        st.write(f"Total da Nota calculado pelo sistema: {totalNota}")
        if totalNota == totalUser:
            st.success("O valor total da nota está correto.")
        else:
            st.error("O valor total da nota não confere com o calculado pelo sistema.")
        
        
        
        
      

    
            