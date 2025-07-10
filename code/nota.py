# Classe para calcular os atributos da nota fiscal
class calculoAtributos:
    def calculoAtributos(self):
        totalGeralIPI = round(apy.valorIPI, 2)
        totalGeralUnit = round(apy.valorUnit, 2)
        totalUser = round(apy.valorTotal, 2)
        totalNota = round(totalGeralUnit + totalGeralIPI, 2)
        st.write("Resultado do cálculo dos produtos:")
        st.write(f"Total IPI: {apy.totalGeralIPI}")
        st.write(f"Total Unitário: {apy.totalGeralUnit}")
        st.write(f"Cálculo do total informado pelo usuário: {totalUser}")
        st.write(f"Total da Nota calculado pelo sistema: {totalNota}")
        if totalNota == totalUser:
            st.success("O valor total da nota está correto.")
        else:
            st.error("O valor total da nota não confere com o calculado pelo sistema.")




# # Classe para adicionar produtos à lista - não utilizada

    #class adicionarProd:
    #   def adicionarProd(descProduto, valorUnit, valorIPI, valorTotal):
    #      global produtos
    #     produtos = []
        #    produtos.append(
        #       {
        #          "descricao": descProduto,
        #         "valor_unitario": valorUnit,
            ##       "valor_total": valorTotal,
            #  }
            #)
        