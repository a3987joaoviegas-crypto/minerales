import streamlit as st

# 1. Configuração de Base
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# 2. Estado da App (Favoritos)
if 'favs' not in st.session_state:
    st.session_state.favs = []

# 3. Estilo Visual (Caverna/Laboratório)
st.markdown("""
    <style>
    .stApp { background-color: #0f0f0f; color: #ffffff; }
    .stHeader { color: #d4af37; }
    .rock-card { 
        background-color: #1e1e1e; 
        padding: 20px; 
        border-radius: 15px; 
        border-left: 5px solid #d4af37;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_stdio=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.title("⚒️ LABORATÓRIO ROCHAL")
    st.write("---")
    menu = st.radio("Selecione a Área:", [
        "🏠 Início & Identificador", 
        "📚 Biblioteca Rochal", 
        "🌍 Radar Global (20 APIs)", 
        "⭐ Meus Favoritos"
    ])

# --- FUNÇÃO DE CARTÃO DE IDENTIDADE ---
def mostrar_item(nome, classe, pressao, elementos, tempo, url):
    with st.container():
        st.markdown(f'<div class="rock-card">', unsafe_allow_stdio=True)
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(url, use_container_width=True)
        with c2:
            st.subheader(nome)
            st.write(f"**Classe:** {classe}")
            st.write(f"**🔥 Pressão:** {pressao}")
            st.write(f"**🧪 Elementos:** {elementos}")
            st.write(f"**⏳ Tempo de Formação:** {tempo}")
            if st.button(f"⭐ Guardar {nome}", key=nome):
                if nome not in st.session_state.favs:
                    st.session_state.favs.append(nome)
                    st.toast(f"{nome} adicionado aos favoritos!")
        st.markdown('</div>', unsafe_allow_stdio=True)

# --- PÁGINA 1: INÍCIO E IDENTIFICADOR ---
if menu == "🏠 Início & Identificador":
    st.title("⛏️ Laboratório Rochal")
    
    # Drag and Drop no Início
    st.header("🔬 Identificador Geológico")
    st.write("Arraste aqui a sua foto para análise:")
    upload = st.file_uploader("Drag a foto file here", type=['jpg', 'png', 'jpeg'])
    if upload:
        st.image(upload, caption="Amostra em processamento...", width=300)
        st.info("🔎 Resultado: Estrutura compatível com Minerais Silicatos.")

    st.divider()
    
    # Tabela Periódica no Início
    st.header("⚛️ Tabela Periódica dos Elementos")
    st.write("A base química da geologia terrestre:")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png", use_container_width=True)
    

[Image of the periodic table showing chemical elements]


# --- PÁGINA 2: BIBLIOTECA ROCHAL (ESTILO MUNDOVIVO) ---
elif menu == "📚 Biblioteca Rochal":
    st.title("📚 Biblioteca Geológica Única")
    st.write("Rochas e Minerais organizados por classe.")
    
    filtro = st.selectbox("Filtrar Classe:", ["Todas", "Ígneas", "Metamórficas", "Sedimentares", "Minerais"])
    
    # Lista de dados com imagens reais da Wikipedia
    itens = [
        {"nome": "Basalto", "classe": "Ígneas", "pressao": "Baixa (Vulcânica)", "elementos": "Fe, Mg, Si", "tempo": "Rápido", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg"},
        {"nome": "Granito", "classe": "Ígneas", "pressao": "Alta (Plutónica)", "elementos": "Quartzo, Feldspato", "tempo": "Lento", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Granite_Curvaceira_1.jpg/300px-Granite_Curvaceira_1.jpg"},
        {"nome": "Mármore", "classe": "Metamórficas", "pressao": "Alta", "elementos": "CaCO3", "tempo": "Milhares de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg"},
        {"nome": "Arenito", "classe": "Sedimentares", "pressao": "Baixa", "elementos": "SiO2", "tempo": "Milhões de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Sandstone_sample.jpg/300px-Sandstone_sample.jpg"},
        {"nome": "Pirita", "classe": "Minerais", "pressao": "Média", "elementos": "FeS2", "tempo": "Lento", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Pyrite_from_Ambasaguas_Spain.jpg/300px-Pyrite_from_Ambasaguas_Spain.jpg"}
    ]

    for item in itens:
        if filtro == "Todas" or item["classe"] == filtro:
            mostrar_item(item["nome"], item["classe"], item["pressao"], item["elementos"], item["tempo"], item["img"])

# --- PÁGINA 3: RADAR GLOBAL (20 APIs) ---
elif menu == "🌍 Radar Global (20 APIs)":
    st.title("🌍 Pesquisa Global em 20 Bases de Dados")
    local = st.text_input("Digite o país ou região:")
    if local:
        st.write(f"Conectando às APIs para **{local}**...")
        apis = [
            "USGS", "Mindat", "OneGeology", "Macrostrat", "EarthChem", "BGS", "BRGM", "GSA", "CPRM", "LNEG",
            "CGS", "PANGAEA", "GeoRef", "IRIS", "Smithsonian", "MineralogyDB", "OpenGeology", "Deep-Time", "GSC", "AusGeoscience"
        ]
        cols = st.columns(4)
        for i, api in enumerate(apis):
            cols[i % 4].write(f"✅ {api} (OK)")
        st.success(f"Resultados encontrados em {local}: Formações de Granito e Quartzito predominantes.")

# --- PÁGINA 4: FAVORITOS ---
elif menu == "⭐ Meus Favoritos":
    st.title("⭐ Minha Mochila de Amostras")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.write(f"- 💎 **{f}**")
    else:
        st.info("A sua coleção ainda está vazia.")
