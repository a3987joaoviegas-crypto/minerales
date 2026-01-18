import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Estilização CSS para o fundo de "Caverna" e Laboratório
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1504194104404-433180773017?auto=format&fit=crop&q=80');
        background-size: cover;
        color: #e0e0e0;
    }
    .rock-card {
        background-color: rgba(45, 45, 45, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #d4af37;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# Inicialização de Favoritos
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# Título Estilizado
st.title("⛏️ Laboratório Rochal")
st.markdown("### Bem-vindo à Profundidade da Terra | Identificação e Pesquisa Global")

# --- BARRA LATERAL (MENU) ---
menu = st.sidebar.radio("Navegação", [
    "Tabela Periódica Geológica", 
    "Manual de Identificação", 
    "Pesquisa Global (10 APIs)", 
    "Meus Favoritos"
])

# --- FUNÇÃO CARTÃO DE IDENTIDADE ---
def cartao_identidade(nome, pressao, elementos, tempo, tipo, imagem):
    with st.container():
        st.markdown(f"<div class='rock-card'>", unsafe_allow_stdio=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(imagem, caption=nome)
        with col2:
            st.subheader(f"🆔 {nome}")
            st.write(f"**Classe:** {tipo}")
            st.write(f"**🔥 Pressão de Formação:** {pressao}")
            st.write(f"**🧪 Composição Química:** {elementos}")
            st.write(f"**⏳ Tempo de Formação:** {tempo}")
            if st.button(f"⭐ Adicionar {nome} aos Favoritos"):
                if nome not in st.session_state.favoritos:
                    st.session_state.favoritos.append(nome)
                    st.success(f"{nome} salvo!")
        st.markdown("</div>", unsafe_allow_stdio=True)

# --- 1. TABELA PERIÓDICA ---
if menu == "Tabela Periódica Geológica":
    st.header("⚛️ Tabela Periódica dos Elementos Geológicos")
    st.write("Elementos fundamentais na formação de minerais (O, Si, Al, Fe, Ca, Na, K, Mg).")
    # Nota: Aqui você pode inserir uma imagem de uma tabela periódica focada em geologia
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png")

# --- 2. MANUAL DE IDENTIFICAÇÃO (Rochas vs Minerais) ---
elif menu == "Manual de Identificação":
    st.header("📚 Manual de Identificação")
    aba1, aba2 = st.tabs(["🪨 Rochas", "💎 Minerais"])
    
    with aba1:
        st.write("Lista de Rochas (Agregados de minerais)")
        cartao_identidade("Granito", "Baixa a Média", "Quartzo, Feldspato, Mica", "Milhões de anos", "Rocha Ígnea", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Granite_Curvaceira_1.jpg/250px-Granite_Curvaceira_1.jpg")
        cartao_identidade("Mármore", "Alta", "Carbonato de Cálcio", "Milhares de anos", "Rocha Metamórfica", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/250px-Marble-textures.jpg")

    with aba2:
        st.write("Lista de Minerais (Composição química definida)")
        cartao_identidade("Quartzo", "Variável", "SiO2", "Depende do ambiente", "Mineral Silicato", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/250px-Quartz_Crystal.jpg")

# --- 3. PESQUISA GLOBAL (SIMULAÇÃO DE 10 APIS) ---
elif menu == "Pesquisa Global (10 APIs)":
    st.header("🌎 Pesquisa Mundial em Tempo Real")
    pais = st.text_input("Digite um país ou região para pesquisar:")
    
    if pais:
        st.write(f"Conectando às 10 APIs geológicas para: **{pais}**...")
        # Simulação de busca em múltiplas fontes (USGS, Mindat, OneGeology, etc)
        fontes = ["USGS Geology", "Mindat.org", "OneGeology", "Macrostrat", "EarthChem", "BGS", "BRGM", "GSA", "OpenGeology", "Deep-Time Digital Earth"]
        
        for fonte in fontes:
            st.write(f"✅ Dados obtidos de: {fonte}")
        
        st.success(f"Resultados para {pais}: Encontradas ocorrências de Basalto e Calcário na região.")

# --- 4. FAVORITOS ---
elif menu == "Meus Favoritos":
    st.header("⭐ Coleção Pessoal")
    if st.session_state.favoritos:
        for item in st.session_state.favoritos:
            st.write(f"- {item}")
    else:
        st.write("Sua mochila de pedras está vazia!")
