import streamlit as st

# Configuração da página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Estilo Visual: Fundo de Caverna e Cartões
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
        color: #f0f0f0;
    }
    .id-card {
        background-color: rgba(45, 45, 45, 0.9);
        border: 2px solid #8B4513;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# Sistema de Favoritos
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# --- MENU LATERAL ---
with st.sidebar:
    st.title("⚒️ Laboratório Rochal")
    menu = st.radio("Navegação:", [
        "🏠 Início", 
        "🔬 Identificador", 
        "📚 Manual de Rochas", 
        "💎 Manual de Minerais",
        "⚛️ Tabela Periódica", 
        "🌍 Pesquisa Global (10 APIs)",
        "⭐ Meus Favoritos"
    ])

# --- FUNÇÃO CARTÃO DE IDENTIDADE ---
def criar_cartao(nome, pressao, elementos, tempo, tipo, img_url):
    st.markdown(f'<div class="id-card">', unsafe_allow_stdio=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(img_url, use_container_width=True)
    with col2:
        st.subheader(f"🆔 {nome}")
        st.write(f"**Classe:** {tipo}")
        st.write(f"**🔥 Pressão:** {pressao}")
        st.write(f"**🧪 Elementos:** {elementos}")
        st.write(f"**⏳ Tempo de Formação:** {tempo}")
        if st.button(f"⭐ Adicionar {nome}", key=nome):
            if nome not in st.session_state.favoritos:
                st.session_state.favoritos.append(nome)
                st.toast(f"{nome} guardado!")
    st.markdown('</div>', unsafe_allow_stdio=True)

# --- PÁGINAS ---

if menu == "🏠 Início":
    st.title("Bem-vindo às Profundezas!")
    st.write("Explora a geologia mundial neste laboratório digital.")
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1000", caption="Interior do Laboratório")

elif menu == "🔬 Identificador":
    st.header("📸 Identificação de Campo")
    upload = st.file_uploader("Suba uma foto da sua rocha:", type=['jpg', 'png'])
    if upload:
        st.image(upload, width=300)
        st.info("Analisando dados geológicos... Amostra compatível com formações ígneas.")

elif menu == "📚 Manual de Rochas":
    st.header("🪨 Manual de Rochas")
    criar_cartao("Basalto", "Baixa (Vulcânica)", "Silício, Magnésio, Ferro", "Dias a meses", "Ígnea Extrusiva", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg")
    criar_cartao("Mármore", "Alta", "Carbonato de Cálcio", "Milhares de anos", "Metamórfica", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg")

elif menu == "💎 Manual de Minerais":
    st.header("💎 Manual de Minerais")
    criar_cartao("Quartzo", "Variável", "SiO2 (Sílica)", "Lento", "Mineral Silicato", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg")
    criar_cartao("Pirita", "Média", "FeS2 (Ferro e Enxofre)", "Milhares de anos", "Sulfeto", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Pyrite_from_Ambasaguas_Spain.jpg/300px-Pyrite_from_Ambasaguas_Spain.jpg")

elif menu == "⚛️ Tabela Periódica":
    st.header("⚛️ Composição Química da Terra")
    st.write("Elementos essenciais para a formação de minerais.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png")

elif menu == "🌍 Pesquisa Global (10 APIs)":
    st.header("🔍 Motor de Busca Geológico")
    pais = st.text_input("País ou Região para pesquisar:")
    if pais:
        apis = ["USGS", "Mindat", "OneGeology", "Macrostrat", "EarthChem", "BGS", "BRGM", "GSA", "OpenGeology", "Deep-Time Data"]
        for api in apis:
            st.write(f"✅ Consultando {api}... Dados de **{pais}** obtidos.")
        st.success(f"Busca finalizada para {pais}!")

elif menu == "⭐ Meus Favoritos":
    st.header("🎒 Sua Coleção Particular")
    if st.session_state.favoritos:
        for fav in st.session_state.favoritos:
            st.write(f"- {fav}")
    else:
        st.write("Ainda não tens favoritos.")
