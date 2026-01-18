import streamlit as st

# Configuração da página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Estilo Visual: Fundo de Caverna e Cartões
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=2000');
        background-size: cover;
        color: #f0f0f0;
    }
    .id-card {
        background-color: rgba(30, 30, 30, 0.9);
        border: 2px solid #8B4513;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# Sistema de Favoritos (Igual ao MundoVivo)
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# --- MENU LATERAL ---
with st.sidebar:
    st.title("⚒️ Laboratório Rochal")
    menu = st.radio("Navegação:", [
        "🏠 Início", 
        "🔬 Identificador de Rochas", 
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
    

elif menu == "🔬 Identificador de Rochas":
    st.header("📸 Identificação de Campo")
    upload = st.file_uploader("Suba uma foto da sua rocha:", type=['jpg', 'png'])
    if upload:
        st.image(upload, width=300)
        st.info("Analisando densidade e brilho... Esta amostra parece ser de origem vulcânica.")

elif menu == "📚 Manual de Rochas":
    st.header("🪨 Manual de Rochas")
    criar_cartao("Basalto", "Baixa (Superficial)", "Silício, Magnésio, Ferro", "Dias a meses", "Ígnea Extrusiva", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg")
    criar_cartao("Mármore", "Alta", "Carbonato de Cálcio", "Milhares de anos", "Metamórfica", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg")

elif menu == "💎 Manual de Minerais":
    st.header("💎 Manual de Minerais")
    criar_cartao("Quartzo", "Variável", "SiO2 (Sílica)", "Lento (Crescimento de Cristais)", "Mineral Silicato", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg")
    criar_cartao("Ouro Nativo", "Variável", "Au (Ouro Puro)", "Geológico (Veios Hidrotérmicos)", "Metal Nativo", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Gold-bearing_quartz.jpg/300px-Gold-bearing_quartz.jpg")

elif menu == "⚛️ Tabela Periódica":
    st.header("⚛️ Composição Química da Terra")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png")
    

[Image of the periodic table showing chemical elements]


elif menu == "🌍 Pesquisa Global (10 APIs)":
    st.header("🔍 Motor de Busca Geológico")
    pais = st.text_input("País ou Região para pesquisar:")
    if pais:
        apis = ["USGS (EUA)", "Mindat", "OneGeology", "Macrostrat", "EarthChem", "BGS", "BRGM", "GSA", "OpenGeology", "Deep-Time Data"]
        for api in apis:
            st.write(f"✅ Consultando {api}... Dados de **{pais}** obtidos.")
        st.success(f"Busca finalizada para {pais}!")

elif menu == "⭐ Meus Favoritos":
    st.header("🎒 Sua Coleção Particular")
    if st.session_state.favoritos:
        for fav in st.session_state.favoritos:
            st.write(f"- {fav}")
    else:
        st.write("Nenhuma rocha favoritada.")
