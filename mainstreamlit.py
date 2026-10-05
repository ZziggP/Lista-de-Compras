import json
import streamlit as st

ARQUIVO = "lista_compras.json"

# ---------- Persistência ----------
def salvar_lista(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

def carregar_lista():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            {"nome": "Arroz", "quantidade": 3, "comprado": True},
            {"nome": "Feijão", "quantidade": 8, "comprado": False},
            {"nome": "Batata", "quantidade": 6, "comprado": False},
        ]

# ---------- Estado ----------
if "lista_produtos" not in st.session_state:
    st.session_state.lista_produtos = carregar_lista()

if "pagina" not in st.session_state:
    st.session_state.pagina = "Mostrar lista"   # página inicial

lista_produtos = st.session_state.lista_produtos

# ---------- Lógica ----------
def adicionar_item(nome, quantidade):
    lista_produtos.append({"nome": nome, "quantidade": quantidade, "comprado": False})
    salvar_lista(lista_produtos)

def marcar_comprado(nome_busca):
    for item in lista_produtos:
        if item["nome"].lower() == nome_busca.lower():
            item["comprado"] = True
            salvar_lista(lista_produtos)
            return True
    return False

def remover_item(nome_busca):
    for item in lista_produtos:
        if item["nome"].lower() == nome_busca.lower():
            lista_produtos.remove(item)
            salvar_lista(lista_produtos)
            return True
    return False

# ---------- Sidebar com botões ----------
st.sidebar.title("Menu")

if st.sidebar.button("📋 Mostrar lista", use_container_width=True):
    st.session_state.pagina = "Mostrar lista"
if st.sidebar.button("➕ Adicionar item", use_container_width=True):
    st.session_state.pagina = "Adicionar item"
if st.sidebar.button("✅ Marcar como comprado", use_container_width=True):
    st.session_state.pagina = "Marcar como comprado"
if st.sidebar.button("🗑️ Remover item", use_container_width=True):
    st.session_state.pagina = "Remover item"

st.sidebar.divider()
st.sidebar.caption(f"Página atual: **{st.session_state.pagina}**")

# ---------- Página principal ----------
st.title("🛒 Lista de Compras")

def mostrar_lista():
    comprados = [i for i in lista_produtos if i["comprado"]]
    pendentes = [i for i in lista_produtos if not i["comprado"]]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Já comprei")
        if comprados:
            for item in comprados:
                st.write(f"- {item['nome']} / {item['quantidade']}")
        else:
            st.write("_Nada comprado ainda._")

    with col2:
        st.subheader("🛒 Para comprar")
        if pendentes:
            for item in pendentes:
                st.write(f"- {item['nome']} / {item['quantidade']}")
        else:
            st.write("_Lista vazia._")

# Decide o que mostrar com base na página
if st.session_state.pagina == "Mostrar lista":
    mostrar_lista()

elif st.session_state.pagina == "Adicionar item":
    mostrar_lista()
    st.subheader("Adicionar item")
    nome = st.text_input("Nome do produto")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)

    if st.button("Adicionar"):
        if nome.strip():
            adicionar_item(nome.strip(), quantidade)
            st.success(f"{nome} adicionado!")
            st.rerun()
        else:
            st.error("Digite um nome válido.")

elif st.session_state.pagina == "Marcar como comprado":
    mostrar_lista()
    st.divider()
    st.subheader("Marcar como comprado")
    nome = st.text_input("Qual produto foi comprado?")

    if st.button("Marcar"):
        if marcar_comprado(nome):
            st.success(f"{nome} marcado como comprado!")
            st.rerun()
        else:
            st.error("Produto não encontrado.")

elif st.session_state.pagina == "Remover item":
    mostrar_lista()
    st.divider()
    st.subheader("Remover item")
    nome = st.text_input("Qual produto deseja remover?")

    if st.button("Remover"):
        if remover_item(nome):
            st.success(f"{nome} removido!")
            st.rerun()
        else:
            st.error("Produto não encontrado.")