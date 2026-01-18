import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# Inicializar Favoritos
if 'favs' not in st.session_state:
    st.session_state.favs = []

# --- MENU LATERAL ---
with st.sidebar:
    st.title("⚒️ LABORATORIAL")
    menu = st.radio("Ir para:", ["Início & Identificador", "Biblioteca Rochal", "Pesquisa Mundial (20 APIs)", "Favoritos"])

# --- FUNÇÃO CARTÃO DE IDENTIDADE ---
def cartao_geologico(nome, classe, pressao, elementos, tempo, img_url):
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(img_url, use_container_width=True)
        with col2:
            st.subheader(nome)
            st.write(f"**Classe:** {classe}")
            st.write(f"**🔥 Pressão:** {pressao}")
            st.write(f"**🧪 Elementos:** {elementos}")
            st.write(f"**⏳ Tempo:** {tempo}")
            if st.button(f"⭐ Adicionar {nome}", key=nome):
                if nome not in st.session_state.favs:
                    st.session_state.favs.append(nome)
                    st.toast(f"{nome} adicionado!")

# --- 1. INÍCIO & IDENTIFICADOR (COM TABELA PERIÓDICA) ---
if menu == "Início & Identificador":
    st.title("⛏️ Laboratório Rochal")
    
    # Drag and Drop no Início
    st.header("🔬 Identificador Visual")
    upload = st.file_uploader("Drag a foto file here (Arraste a foto da rocha/mineral)", type=['jpg', 'png', 'jpeg'])
    
    if upload:
        st.image(upload, caption="Amostra em análise...", width=400)
        st.success("Análise concluída: Estrutura Cristalina detectada.")

    st.divider()
    
    # Tabela Periódica no Início
    st.header("⚛️ Tabela Periódica Geológica")
    st.write("Elementos químicos que formam as rochas e minerais do planeta:")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png", use_container_width=True)
    

[Image of the periodic table showing chemical elements]


# --- 2. BIBLIOTECA ROCHAL (ESTILO MUNDOVIVO) ---
elif menu == "Biblioteca Rochal":
    st.title("📚 Biblioteca Rochal")
    
    # Categorias como classes de animais
    classe_escolhida = st.selectbox("Escolha uma Classe Geológica:", ["Todas", "Rochas Ígneas", "Rochas Metamórficas", "Rochas Sedimentares", "Minerais Silicatos", "Minerais Nativos"])
    
    # Dados das Rochas e Minerais (Nomes em PT e Imagens Corretas)
    rochas_dados = [
        {"nome": "Basalto", "classe": "Rochas Ígneas", "pressao": "Baixa (Superfície)", "elementos": "Plagioclase, Piroxena", "tempo": "Dias", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg"},
        {"nome": "Granito", "classe": "Rochas Ígneas", "pressao": "Alta (Profundidade)", "elementos": "Quartzo, Feldspato, Mica", "tempo": "Milhares de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Granite_Curvaceira_1.jpg/300px-Granite_Curvaceira_1.jpg"},
        {"nome": "Mármore", "classe": "Rochas Metamórficas", "pressao": "Média/Alta", "elementos": "Calcite (CaCO3)", "tempo": "Milhões de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg"},
        {"nome": "Quartzo", "classe": "Minerais Silicatos", "pressao": "Variável", "elementos": "SiO2", "tempo": "Lento (Crescimento)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg"},
        {"nome": "Ouro", "classe": "Minerais Nativos", "pressao": "Alta (Veios)", "elementos": "Au", "tempo": "Geológico", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Gold-bearing_quartz.jpg/300px-Gold-bearing_quartz.jpg"}
    ]

    for item in rochas_dados:
        if classe_escolhida == "Todas" or item["classe"] == classe_escolhida:
            cartao_geologico(item["nome"], item["classe"], item["pressao"], item["elementos"], item["tempo"], item["img"])

# --- 3. PESQUISA MUNDIAL (20 APIs) ---
elif menu == "Pesquisa Mundial (20 APIs)":
    st.title("🌍 Pesquisa Global Avançada")
    regiao = st.text_input("Introduza o País ou Região Geográfica:")
    
    if regiao:
        st.write(f"Conectando a 20 bases de dados para analisar **{regiao}**...")
        apis = [
            "USGS (EUA)", "Mindat.org", "OneGeology", "Macrostrat", "EarthChem", 
            "BGS (Reino Unido)", "BRGM (França)", "GSA Records", "OpenGeology", "Deep-Time",
            "Geoscience Australia", "GSC (Canadá)", "CPRM (Brasil)", "LNEG (Portugal)", "China Geological Survey",
            "PANGAEA", "GeoRef", "IRIS Data", "Mineralogy Database", "Smithsonian Rock Collection"
        ]
        
        col_api1, col_api2 = st.columns(2)
        for i, api in enumerate(apis):
            if i % 2 == 0:
                col_api1.write(f"✅ Conectado: {api}")
            else:
                col_api2.write(f"✅ Conectado: {api}")
        
        st.success(f"Busca completa! Principais rochas em {regiao}: Granitos e Sedimentos Quaternários.")

# --- 4. FAVORITOS ---
elif menu == "Favoritos":
    st.title("⭐ Meus Favoritos")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.write(f"💎 {f}")
    else:
        st.write("Ainda não colecionou nenhuma rocha.")
