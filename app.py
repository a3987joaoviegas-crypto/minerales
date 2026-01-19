import streamlit as st

st.set_page_config(page_title="Mundo Rochal", layout="wide")

# Inicializar favoritos
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# Navegação entre Telas
tela = st.sidebar.radio("Ir para:", ["Tela Principal", "Laboratório Rochal", "Favoritos"])

# --- TELA PRINCIPAL: EXPLORAÇÃO E REGIÕES ---
if tela == "Tela Principal":
    st.title("🌍 Mundo Rochal: Exploração")
    st.write("Explore as rochas por regiões e classes, tal como no Mundo Vivo.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Mapa Geológico Global")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/World_geology_map_full.png/1200px-World_geology_map_full.png", caption="Distribuição Global de Rochas")
    
    with col2:
        st.subheader("Biblioteca por Regiões")
        regiao = st.selectbox("Escolha uma Região:", ["Europa", "América do Sul", "África", "Ásia", "Oceânia"])
        # Aqui podes listar rochas específicas da região escolhida

# --- LABORATÓRIO ROCHAL: ANÁLISE E PESQUISA ---
elif tela == "Laboratório Rochal":
    st.title("⚒️ Laboratório Rochal")
    
    st.subheader("⚛️ Referência Química")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_Table_by_Merck.png/1200px-Periodic_Table_by_Merck.png")
    
    st.divider()
    
    st.subheader("🔍 Pesquisa Global (Filtro Geo-Rigoroso)")
    busca = st.text_input("Escreve o nome da rocha (ex: Obsidian, Basalt):")
    
    if busca:
        # Filtro técnico automático para evitar imagens irrelevantes nas APIs
        query = f"{busca} rock mineral specimen geology"
        st.write(f"Resultados técnicos para: **{busca}**")
        
        # Exemplo de 3 das 20 APIs com filtro rígido
        c1, c2, c3 = st.columns(3)
        c1.link_button("Mindat (Fotos Reais)", f"https://www.mindat.org/search.php?search={query}")
        c2.link_button("Smithsonian (Museu)", f"https://collections.nmnh.si.edu/search/minerals/?q={query}")
        c3.link_button("WebMineral (Dados)", f"http://www.webmineral.com/search.php?search={query}")

# --- FAVORITOS ---
elif tela == "Favoritos":
    st.title("⭐ Meus Favoritos")
    if st.session_state.favoritos:
        for item in st.session_state.favoritos:
            st.write(f"✅ {item}")
    else:
        st.write("Ainda não guardaste nenhuma rocha.")
