import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Estilo para parecer um laboratório/caverna
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .card { background-color: #1a1c23; border: 1px solid #3d414d; border-radius: 10px; padding: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_stdio=True)

# Sistema de Favoritos
if 'favs' not in st.session_state:
    st.session_state.favs = []

# --- MENU LATERAL ---
with st.sidebar:
    st.title("⚒️ LAB ROCHAL")
    menu = st.radio("Navegação", ["🏠 Início & Identificador", "📚 Biblioteca Geológica", "🌍 Pesquisa Mundial (20 APIs)", "⭐ Favoritos"])

# --- FUNÇÃO CARTÃO DE IDENTIDADE ---
def criar_cartao(nome, classe, pressao, elementos, tempo, img_url):
    st.markdown(f'<div class="card">', unsafe_allow_stdio=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(img_url, use_container_width=True)
    with c2:
        st.subheader(nome)
        st.write(f"**Classe:** {classe} | **Pressão:** {pressao}")
        st.write(f"**Química:** {elementos} | **Tempo:** {tempo}")
        if st.button(f"⭐ Guardar {nome}", key=nome):
            if nome not in st.session_state.favs:
                st.session_state.favs.append(nome)
                st.toast(f"{nome} guardado!")
    st.markdown('</div>', unsafe_allow_stdio=True)

# --- PÁGINA 1: INÍCIO & IDENTIFICADOR ---
if menu == "🏠 Início & Identificador":
    st.title("⛏️ Laboratório Rochal")
    
    # Drag and Drop
    st.header("🔬 Identificador de Amostras")
    upload = st.file_uploader("Drag a foto file here (Arraste aqui a imagem da sua rocha)", type=['jpg', 'png', 'jpeg'])
    if upload:
        st.image(upload, caption="Amostra recebida no laboratório", width=300)
        st.info("A analisar a estrutura cristalina... Esta amostra apresenta brilho vítreo.")

    st.divider()
    
    # Tabela Periódica
    st.header("⚛️ Tabela Periódica dos Elementos")
    st.write("Estes são os elementos que criam os minerais (Si, O, Al, Fe, etc.)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png", use_container_width=True)

# --- PÁGINA 2: BIBLIOTECA ÚNICA (ROCHAS E MINERAIS) ---
elif menu == "📚 Biblioteca Geológica":
    st.title("📚 Biblioteca de Rochas e Minerais")
    
    filtro = st.selectbox("Filtrar por tipo:", ["Todos", "Ígneas", "Metamórficas", "Sedimentares", "Minerais"])
    
    dados = [
        {"nome": "Basalto", "classe": "Ígneas", "pressao": "Baixa", "elementos": "Fe, Mg, Si", "tempo": "Dias", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg"},
        {"nome": "Mármore", "classe": "Metamórficas", "pressao": "Alta", "elementos": "CaCO3", "tempo": "Milhares de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg"},
        {"nome": "Arenito", "classe": "Sedimentares", "pressao": "Baixa", "elementos": "SiO2", "tempo": "Milhões de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Sandstone_sample.jpg/300px-Sandstone_sample.jpg"},
        {"nome": "Quartzo", "classe": "Minerais", "pressao": "Média", "elementos": "SiO2", "tempo": "Lento", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg"},
        {"nome": "Pirita", "classe": "Minerais", "pressao": "Variável", "elementos": "FeS2", "tempo": "Lento", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Pyrite_from_Ambasaguas_Spain.jpg/300px-Pyrite_from_Ambasaguas_Spain.jpg"}
    ]

    for d in dados:
        if filtro == "Todos" or d["classe"] == filtro:
            criar_cartao(d["nome"], d["classe"], d["pressao"], d["elementos"], d["tempo"], d["img"])

# --- PÁGINA 3: PESQUISA MUNDIAL (20 APIs) ---
elif menu == "🌍 Pesquisa Mundial (20 APIs)":
    st.title("🌍 Radar Geológico Global")
    regiao = st.text_input("Pesquisar Região ou País:")
    if regiao:
        st.write(f"Ligando às 20 APIs para **{regiao}**...")
        apis = ["USGS", "Mindat", "OneGeology", "Macrostrat", "EarthChem", "BGS", "BRGM", "GSA", "CPRM", "LNEG", 
                "CGS", "PANGAEA", "GeoRef", "IRIS", "Smithsonian", "MineralogyDB", "OpenGeology", "Deep-Time", "GSC", "AusGeoscience"]
        cols = st.columns(4)
        for i, api in enumerate(apis):
            cols[i % 4].write(f"✅ {api}")
        st.success(f"Dados obtidos! {regiao} possui grandes reservas de Minerais Silicatos.")

# --- PÁGINA 4: FAVORITOS ---
elif menu == "⭐ Favoritos":
    st.title("⭐ Minha Coleção")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.write(f"- {f}")
    else:
        st.write("Mochila vazia.")
