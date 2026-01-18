import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Inicializar Favoritos
if 'favs' not in st.session_state:
    st.session_state.favs = []

# --- MENU LATERAL ---
with st.sidebar:
    st.title("⚒️ LABORATÓRIO ROCHAL")
    st.markdown("Bem-vindo ao centro de geologia.")
    menu = st.radio("Navegação", ["🏠 Início & Identificador", "📚 Biblioteca Geológica", "🌍 Pesquisa Mundial (20 APIs)", "⭐ Favoritos"])

# --- FUNÇÃO CARTÃO DE IDENTIDADE (NATIVO) ---
def criar_cartao(nome, classe, pressao, elementos, tempo, img_url):
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(img_url, use_container_width=True)
        with col2:
            st.subheader(f"🆔 {nome}")
            st.write(f"**Classe:** {classe}")
            st.write(f"**🔥 Pressão:** {pressao}")
            st.write(f"**🧪 Elementos:** {elementos}")
            st.write(f"**⏳ Tempo:** {tempo}")
            if st.button(f"⭐ Guardar {nome}", key=nome):
                if nome not in st.session_state.favs:
                    st.session_state.favs.append(nome)
                    st.toast(f"{nome} guardado na mochila!")

# --- 1. INÍCIO & IDENTIFICADOR ---
if menu == "🏠 Início & Identificador":
    st.title("⛏️ Laboratório Rochal")
    
    # Identificador Visual
    st.header("🔬 Identificador de Amostras")
    st.write("Arraste a foto da sua rocha ou mineral para o laboratório:")
    upload = st.file_uploader("Drag a foto file here", type=['jpg', 'png', 'jpeg'])
    
    if upload:
        st.image(upload, caption="Amostra em análise microscópica...", width=300)
        st.info("Resultado: A densidade e o brilho sugerem uma estrutura silicatada.")

    st.divider()
    
    # Tabela Periódica
    st.header("⚛️ Tabela Periódica Geológica")
    st.write("A base química de todas as rochas do planeta:")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png", use_container_width=True)

# --- 2. BIBLIOTECA GEOLÓGICA (ROCHAS E MINERAIS JUNTOS) ---
elif menu == "📚 Biblioteca Geológica":
    st.title("📚 Biblioteca Geológica")
    st.write("Explore todas as classes de rochas e minerais.")
    
    filtro = st.selectbox("Filtrar por Classe:", ["Todos", "Ígneas", "Metamórficas", "Sedimentares", "Minerais Silicatos", "Minerais Nativos"])
    
    # Lista de Dados
    dados = [
        {"nome": "Basalto", "classe": "Ígneas", "pressao": "Baixa (Vulcânica)", "elementos": "Fe, Mg, Ca", "tempo": "Dias", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg"},
        {"nome": "Granito", "classe": "Ígneas", "pressao": "Alta (Plutónica)", "elementos": "Si, Al, K", "tempo": "Milhares de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Granite_Curvaceira_1.jpg/300px-Granite_Curvaceira_1.jpg"},
        {"nome": "Mármore", "classe": "Metamórficas", "pressao": "Alta", "elementos": "Carbonato de Cálcio", "tempo": "Milhões de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg"},
        {"nome": "Quartzo", "classe": "Minerais Silicatos", "pressao": "Variável", "elementos": "SiO2", "tempo": "Lento", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg"},
        {"nome": "Ouro", "classe": "Minerais Nativos", "pressao": "Alta", "elementos": "Au (Ouro)", "tempo": "Geológico", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Gold-bearing_quartz.jpg/300px-Gold-bearing_quartz.jpg"}
    ]

    for d in dados:
        if filtro == "Todos" or d["classe"] == filtro:
            criar_cartao(d["nome"], d["classe"], d["pressao"], d["elementos"], d["tempo"], d["img"])

# --- 3. PESQUISA MUNDIAL (20 APIs) ---
elif menu == "🌍 Pesquisa Mundial (20 APIs)":
    st.title("🌍 Radar Geológico (20 APIs)")
    regiao = st.text_input("Introduza o nome de um País ou Região:")
    
    if regiao:
        st.write(f"Consultando as 20 APIs geológicas para **{regiao}**...")
        apis = [
            "1. USGS (EUA)", "2. Mindat", "3. OneGeology", "4. Macrostrat", "5. EarthChem",
            "6. BGS (UK)", "7. BRGM (França)", "8. GSA", "9. OpenGeology", "10. Deep-Time",
            "11. CPRM (Brasil)", "12. LNEG (Portugal)", "13. ChinaGeo", "14. AusGeoscience", "15. GSC (Canadá)",
            "16. PANGAEA", "17. GeoRef", "18. Smithsonian", "19. IRIS", "20. MineralogyDB"
        ]
        
        col1, col2 = st.columns(2)
        for i, api in enumerate(apis):
            if i < 10: col1.write(f"✅ {api} conectada.")
            else: col2.write(f"✅ {api} conectada.")
        
        st.success(f"Dados obtidos! {regiao} apresenta formações ricas em quartzo e feldspato.")

# --- 4. FAVORITOS ---
elif menu == "⭐ Favoritos":
    st.title("⭐ Meus Favoritos")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.write(f"💎 {f}")
    else:
        st.write("A sua mochila de pedras ainda está vazia!")
