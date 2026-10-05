# 🛒 Lista de Compras (Lista de Feira)

Um aplicativo simples e interativo feito em Python utilizando **Streamlit**. O objetivo é ajudar a gerenciar sua lista de compras de supermercado ou feira, permitindo adicionar, remover e marcar produtos como comprados.

## 🚀 Funcionalidades

- **📋 Mostrar lista:** Visualiza todos os itens separados por "Já comprei" e "Para comprar".
- **➕ Adicionar item:** Permite adicionar novos produtos à lista com suas respectivas quantidades.
- **✅ Marcar como comprado:** Altera o status de um item para comprado, movendo-o para a lista de "Já comprei".
- **🗑️ Remover item:** Remove completamente um item da sua lista.
- **💾 Persistência de Dados:** Todos os itens são salvos localmente em um arquivo `lista_compras.json`, garantindo que você não perca os dados ao fechar a aplicação.

## 🛠️ Tecnologias Utilizadas

- **Python** 
- **[Streamlit](https://streamlit.io/)** - Para a interface gráfica interativa.
- **JSON (built-in)** - Para o armazenamento e persistência dos dados localmente.

## ⚙️ Como executar o projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale a biblioteca Streamlit (caso ainda não possua):
   ```bash
   pip install streamlit
   ```
3. Navegue até a pasta do projeto (onde está o arquivo `mainstreamlit.py`).
4. Execute o comando:
   ```bash
   streamlit run mainstreamlit.py
   ```
5. O seu navegador abrirá automaticamente com o aplicativo rodando!

## 📁 Estrutura dos Arquivos

- `mainstreamlit.py` - Contém todo o código principal da aplicação Streamlit (interface e lógica).
- `lista_compras.json` - Arquivo gerado automaticamente que funciona como banco de dados para armazenar os itens da sua lista.
