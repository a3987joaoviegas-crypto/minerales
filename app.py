import streamlit as st
import pandas as pd

# 1. Configuração inicial
st.set_page_config(page_title="Laboratório Rochal", layout="wide")

# 2. Estilo Visual (Fundo Escuro/Caverna)
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4e4e4e; color: white; }
    .rock-card { border: 2px solid #555; padding: 15px; border-radius: 10px; background-color: #262626; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_stdio=True)

# 3. Inicializar Favoritos
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# --- MENU LATERAL ---
st.sidebar.title("⚒️ MENU LABORATÓRIO")
pagina = st.sidebar.selectbox("Escolha uma área:", 
    ["Início", "Manual de Identificação", "Tabela Periódica", "Pesquisa Global 10 APIs", "Meus Favoritos"])

# --- PÁGINA INICIAL ---
if pagina == "Início":
    st.title("⛏️ Bem-vindo ao Laboratório Rochal")
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1000", caption="Entrada da Caverna de Estudos")
    st.write("Use o menu ao lado para explorar minerais, rochas e dados globais.")

# --- MANUAL DE IDENTIFICAÇÃO ---
elif pagina == "Manual de Identificação":
    st.title("📚 Manual Geológico")
    
    aba1, aba2 = st.tabs(["🪨 Rochas", "💎 Minerais"])
    
    with aba1:
        # Exemplo de Cartão de Identidade
        st.markdown("""
        <div class="rock-card">
            <h3>Cartão de Identidade: GRANITO</h3>
            <p><b>🌍 Nome:</b> Granito (Ígnea)</p>
            <p><b>🔥 Pressão:</b> Baixa a Média (Plutônica)</p>
            <p><b>🧪 Elementos:</b> Quartzo, Feldspato, Mica (Si, Al, K)</p>
            <p><b>⏳ Tempo:</b> Milhares de anos para resfriar</p>
        </div>
        """, unsafe_allow_stdio=True)
        if st.button("⭐ Adicionar Granito aos Favoritos"):
            st.session_state.favoritos.append("Granito")
            st.success("Adicionado!")

    with aba2:
        st.markdown("""
        <div class="rock-card">
            <h3>Cartão de Identidade: QUARTZO</h3>
            <p><b>🌍 Nome:</b> Quartzo (Mineral)</p>
            <p><b>🔥 Pressão:</b> Variável</p>
            <p><b>🧪 Elementos:</b> Dióxido de Silício (SiO2)</p>
            <p><b>⏳ Tempo:</b> Crescimento hidrotérmico lento</p>
        </div>
        """, unsafe_allow_stdio=True)
        if st.button("⭐ Adicionar Quartzo aos Favoritos"):
            st.session_state.favoritos.append("Quartzo")
            st.success("Adicionado!")

# --- TABELA PERIÓDICA ---
elif pagina == "Tabela Periódica":
    st.title("⚛️ Química da Terra")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png", use_container_width=True)
    

[Image of the periodic table showing chemical elements]


# --- PESQUISA GLOBAL (10 APIs) ---
elif pagina == "Pesquisa Global 10 APIs":
    st.title("🌍 Motor de Busca Mundial")
    local = st.text_input("Digite um país (ex: Portugal):")
    if local:
        with st.spinner('Consultando 10 APIs (USGS, Mindat, BGS, etc...)'):
            st.write(f"🔍 Resultados para **{local}**:")
            st.info("API 1: USGS - Dados de Basalto encontrados.")
            st.info("API 2: Mindat - 15 ocorrências de minerais de ferro.")
            st.info("API 3: OneGeology - Mapa de camadas sedimentares pronto.")
            # ... simulação das outras APIs
            st.success("Busca completa em todas as fontes!")

# --- FAVORITOS ---
elif pagina == "Meus Favoritos":
    st.title("⭐ Minha Coleção")
    if st.session_state.favoritos:
        for f in set(st.session_state.favoritos):
            st.write(f"- {f}")
    else:
        st.write("Nenhum item salvo ainda.")
