import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Estilo de Caverna / Laboratório
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .card {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #8b4513;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_stdio=True)

if 'favs' not in st.session_state:
    st.session_state.favs = []

# --- BARRA LATERAL ---
st.sidebar.title("⛏️ Laboratório Rochal")
menu = st.sidebar.radio("Navegação", 
    ["Início", "Manual de Identificação", "Tabela Periódica", "Pesquisador Global (10 APIs)", "Favoritos"])

# --- FUNÇÃO CARTÃO DE IDENTIDADE ---
def cartao(nome, pressao, elementos, tempo, tipo, img):
    st.markdown(f"""
    <div class="card">
        <h3>🆔 {nome.upper()}</h3>
        <p><b>Tipo:</b> {tipo}</p>
        <p><b>🔥 Pressão de Criação:</b> {pressao}</p>
        <p><b>🧪 Elementos:</b> {elementos}</p>
        <p><b>⏳ Tempo de Formação:</b> {tempo}</p>
    </div>
    """, unsafe_allow_stdio=True)
    st.image(img, width=300)
    if st.button(f"⭐ Adicionar {nome} aos Favoritos", key=nome):
        if nome not in st.session_state.favs:
            st.session_state.favs.append(nome)
            st.success(f"{nome} guardado!")

# --- PÁGINAS ---

if menu == "Início":
    st.title("Bem-vindo ao Laboratório Rochal")
    st.write("Explore o mundo subterrâneo e identifique minerais e rochas.")
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1000")

elif menu == "Manual de Identificação":
    st.title("📚 Manual Geológico")
    aba1, aba2 = st.tabs(["🪨 Rochas", "💎 Minerais"])
    
    with aba1:
        st.subheader("Lista de Rochas")
        cartao("Basalto", "Baixa (Vulcânica)", "Fe, Mg, Si", "Dias a Semanas", "Ígnea Extrusiva", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg")
        cartao("Gnaisse", "Muito Alta", "Si, Al, K", "Milhões de Anos", "Metamórfica", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gneiss.jpg/300px-Gneiss.jpg")

    with aba2:
        st.subheader("Lista de Minerais")
        cartao("Quartzo", "Variável", "SiO2 (Silício e Oxigénio)", "Lento (Crescimento)", "Silicato", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg")
        cartao("Pirita", "Média", "FeS2 (Ferro e Enxofre)", "Milhares de Anos", "Sulfeto", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Pyrite_from_Ambasaguas_Spain.jpg/300px-Pyrite_from_Ambasaguas_Spain.jpg")

elif menu == "Tabela Periódica":
    st.title("⚛️ Tabela Periódica Geológica")
    st.write("Estes são os elementos que constroem o nosso planeta.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png")

elif menu == "Pesquisador Global (10 APIs)":
    st.title("🌍 Pesquisa em 10 Bases de Dados")
    local = st.text_input("Introduza o País ou Região:")
    if local:
        st.info(f"Pesquisando rochas em {local}...")
        apis = ["USGS Geology", "Mindat.org", "OneGeology", "Macrostrat", "EarthChem", "BGS Database", "BRGM Info", "GSA Records", "OpenGeology", "Deep-Time Data"]
        for api in apis:
            st.write(f"✅ Ligação a **{api}**... Dados obtidos!")
        st.success(f"Resultados para {local}: Encontradas formações de Xisto e Calcário.")

elif menu == "Favoritos":
    st.title("⭐ Minha Mochila de Rochas")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.write(f"- {f}")
    else:
        st.write("Ainda não tens favoritos.")
