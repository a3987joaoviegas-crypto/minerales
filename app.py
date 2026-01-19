import streamlit as st

# Configuração Profissional
st.set_page_config(page_title="Mundo Rochal", layout="wide")

# Abas de Navegação (Igual ao que pediste)
aba_principal, aba_lab, aba_favoritos = st.tabs(["🏠 Tela Principal (Mundo)", "🔬 Laboratório & Tabela", "⭐ Favoritos"])

# --- 1. TELA PRINCIPAL: CENTRO DE PESQUISA POR REGIÕES ---
with aba_principal:
    st.header("🌍 Centro de Pesquisa Global")
    st.write("Usa as tuas Apps de Geologia para identificar a rocha e regista-a aqui.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📍 Filtro de Região")
        pais = st.text_input("Introduza o País ou Região (ex: Portugal, Brasil, Islândia):")
    
    with col2:
        st.subheader("📂 Tipo de Amostra")
        categoria = st.radio("Listar:", ["Todas", "Rochas", "Minerais"], horizontal=True)

    st.info(f"A explorar {categoria} em: {pais if pais else 'Todo o Mundo'}")
    
    # Espaço para o Mapa Mundi de Geologia
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/World_geology_map_full.png/1200px-World_geology_map_full.png", use_container_width=True)

# --- 2. LABORATÓRIO: TABELA PERIÓDICA E ANÁLISE ---
with aba_lab:
    st.header("🔬 Laboratório de Análise Técnica")
    
    # Tabela Periódica Interativa (Visual)
    st.subheader("⚛️ Tabela Periódica dos Elementos")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_Table_by_Merck.png/1200px-Periodic_Table_by_Merck.png", use_container_width=True)
    
    st.divider()
    
    # Espaço de pesquisa que integra com o que encontras nas Apps
    st.subheader("🔍 Validação de Ficha Técnica")
    st.write("Consulta o **Rock Identifier** ou **Mindat** e valida os dados abaixo:")
    
    nome_rocha = st.text_input("Nome da Amostra encontrada:")
    if nome_rocha:
        st.success(f"Ficha de análise criada para: {nome_rocha}")
        c1, c2 = st.columns(2)
        c1.write("**🧬 Formação:** A aguardar dados da App...")
        c2.write("**🧪 Química:** A consultar Tabela Periódica...")

# --- 3. FAVORITOS ---
with aba_favoritos:
    st.header("⭐ A Minha Mochila Certificada")
    st.write("As rochas guardadas aparecerão aqui para o teu relatório final.")
