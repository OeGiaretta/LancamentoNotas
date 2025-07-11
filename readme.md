
# Lançamento de Notas Fiscais

Este projeto é uma aplicação web simples desenvolvida com [Streamlit](https://streamlit.io/) para facilitar o **lançamento e validação de notas fiscais**, tanto de entrada quanto de saída.

## 🚀 Funcionalidades

- Seleção de tipo de nota (entrada/saída)
- Subtipos: uso ou revenda
- Entrada de dados:
  - Descrição do produto
  - Valor unitário
  - Valor do IPI
  - Valor total
- Cálculo automático e validação do valor total da nota
- Mensagens de sucesso ou erro em tempo real

## 🧠 Tecnologias Utilizadas

- Python 3.x
- Streamlit
- Pandas
- NumPy

## 🗂 Estrutura do Projeto

```
├── code/
│   ├── app.py         # Interface da aplicação
│   └── nota.py        # Lógica de cálculo da nota fiscal
├── db/                # Scripts SQL para criação de tabelas
│   ├── banco_categorias.sql
│   ├── banco_clientes.sql
│   └── ...
```

## 💡 Melhorias Futuras

- Conexão com banco de dados
- Registro e histórico de notas
- Exportação para PDF ou Excel
- Testes unitários
- Separação mais clara entre lógica e interface

## 📦 Como executar

1. Clone este repositório:

```bash
git clone https://github.com/OeGiaretta/LancamentoNotas.git
cd LancamentoNotas/code
```

2. Instale as dependências:

```bash
pip install streamlit pandas numpy
```

3. Execute o projeto:

```bash
streamlit run app.py
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](../LICENSE) para mais detalhes.
```
