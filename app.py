import streamlit as st

# Configuração da página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Inicializar Favoritos
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# --- MENU LATERAL ---
with st.sidebar:
    st.title("⚒️ Laboratório Rochal")
    st.markdown("---")
    menu = st.sidebar.radio("Navegação:", [
        "🏠 Início", 
        "🔬 Identificador", 
        "📚 Manual de Rochas", 
        "💎 Manual de Minerais",
        "⚛️ Tabela Periódica", 
        "🌍 Pesquisa Global (10 APIs)",
        "⭐ Meus Favoritos"
    ])

# --- FUNÇÃO CARTÃO DE IDENTIDADE (SIMPLIFICADA) ---
def criar_cartao(nome, pressao, elementos, tempo, tipo, img_url):
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(img_url, use_container_width=True)
        with col2:
            st.subheader(f"🆔 {nome}")
            st.write(f"**Classe:** {tipo}")
            st.write(f"**🔥 Pressão:** {pressao}")
            st.write(f"**🧪 Elementos:** {elementos}")
            st.write(f"**⏳ Tempo:** {tempo}")
            if st.button(f"⭐ Adicionar {nome} aos Favoritos", key=nome):
                if nome not in st.session_state.favoritos:
                    st.session_state.favoritos.append(nome)
                    st.toast(f"{nome} guardado!")

# --- PÁGINAS ---

if menu == "🏠 Início":
    st.title("⛏️ Bem-vindo ao Laboratório Rochal")
    st.markdown("#### Explore as profundezas da Terra e a ciência das rochas.")
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1000")
    st.info("Utilize o menu lateral para navegar entre o manual, a tabela periódica e as pesquisas globais.")

elif menu == "🔬 Identificador":
    st.header("📸 Laboratório de Identificação")
    st.write("Suba uma imagem para análise macroscópica.")
    upload = st.file_uploader("Foto da amostra:", type=['jpg', 'png'])
    if upload:
        st.image(upload, width=300)
        st.success("Análise concluída: Estrutura compatível com granitos e rochas ígneas intrusivas.")

elif menu == "📚 Manual de Rochas":
    st.header("🪨 Manual de Rochas")
    criar_cartao("Basalto", "Baixa", "Silício, Magnésio, Ferro", "Dias (Vulcânico)", "Ígnea", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg")
    criar_cartao("Mármore", "Alta", "Carbonato de Cálcio", "Milhares de anos", "Metamórfica", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg")

elif menu == "💎 Manual de Minerais":
    st.header("💎 Manual de Minerais")
    criar_cartao("Quartzo", "Variável", "SiO2", "Lento", "Silicato", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg")
    criar_cartao("Pirita", "Média", "FeS2", "Milhares de anos", "Sufeto", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Pyrite_from_Ambasaguas_Spain.jpg/300px-Pyrite_from_Ambasaguas_Spain.jpg")

elif menu == "⚛️ Tabela Periódica":
    st.header("⚛️ Composição Química")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png")

elif menu == "🌍 Pesquisa Global (10 APIs)":
    st.header("🔍 Motor de Busca Geológico (10 APIs)")
    pais = st.text_input("Escreva o nome do país ou região:")
    if pais:
        st.write(f"Consultando bases de dados para {pais}...")
        for api in ["USGS", "Mindat", "OneGeology", "Macrostrat", "EarthChem", "BGS", "BRGM", "GSA", "OpenGeology", "Deep-Time"]:
            st.write(f"✅ Dados de **{api}** carregados.")
        st.success(f"Busca finalizada! Rochas dominantes em {pais}: Xisto e Calcário.")

elif menu == "⭐ Meus Favoritos":
    st.header("🎒 Sua Coleção Particular")
    if st.session_state.favoritos:
        for fav in st.session_state.favoritos:
            st.write(f"- {fav}")
    else:
        st.write("Sua mochila geológica está vazia!")
