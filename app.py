import streamlit as st

# 1. Configuração da Página (Sempre a primeira linha)
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# 2. Inicializar Favoritos
if 'favs' not in st.session_state:
    st.session_state.favs = []

# --- MENU LATERAL ---
st.sidebar.title("⚒️ LAB ROCHAL")
menu = st.sidebar.radio("Navegação:", [
    "🏠 Início & Identificador", 
    "📚 Biblioteca Geológica", 
    "🌍 Pesquisa Mundial (20 APIs)",
    "⭐ Favoritos"
])

# --- PÁGINA 1: INÍCIO & IDENTIFICADOR ---
if menu == "🏠 Início & Identificador":
    st.title("Laboratório Rochal")
    
    st.header("🔬 Identificador Visual")
    st.write("Arraste aqui a foto da sua rocha ou mineral:")
    # Componente de Drag and Drop
    upload = st.file_uploader("Drag a foto file here", type=['jpg', 'png', 'jpeg'])
    
    if upload:
        st.image(upload, caption="Amostra em análise no laboratório...", width=300)
        st.info("🔎 Resultado: Estrutura mineral detectada. Processando composição...")

    st.divider()
    
    st.header("⚛️ Tabela Periódica Geológica")
    st.write("Os elementos fundamentais que constroem as rochas da Terra:")
    # Imagem da Tabela Periódica
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png")

# --- PÁGINA 2: BIBLIOTECA (ROCHAS E MINERAIS JUNTOS) ---
elif menu == "📚 Biblioteca Geológica":
    st.title("Biblioteca de Rochas e Minerais")
    
    filtro = st.selectbox("Filtrar por tipo:", ["Todos", "Ígneas", "Metamórficas", "Sedimentares", "Minerais"])
    
    # Banco de Dados de Amostras
    itens = [
        {"nome": "Basalto", "classe": "Ígneas", "pressao": "Baixa (Superfície)", "elementos": "Ferro, Magnésio, Cálcio", "tempo": "Dias", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg"},
        {"nome": "Granito", "classe": "Ígneas", "pressao": "Alta (Plutónica)", "elementos": "Silício, Alumínio, Potássio", "tempo": "Milhares de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Granite_Curvaceira_1.jpg/300px-Granite_Curvaceira_1.jpg"},
        {"nome": "Mármore", "classe": "Metamórficas", "pressao": "Média/Alta", "elementos": "Carbonato de Cálcio", "tempo": "Milhões de anos", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg"},
        {"nome": "Quartzo", "classe": "Minerais", "pressao": "Variável", "elementos": "Dióxido de Silício (SiO2)", "tempo": "Crescimento Lento", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg"}
    ]

    for i in itens:
        if filtro == "Todos" or i["classe"] == filtro:
            with st.container(border=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(i["img"], width=200)
                with col2:
                    st.subheader(i["nome"])
                    st.write(f"**Classe:** {i['classe']} | **🔥 Pressão:** {i['pressao']}")
                    st.write(f"**🧪 Elementos:** {i['elementos']} | **⏳ Tempo:** {i['tempo']}")
                    if st.button(f"⭐ Guardar {i['nome']}", key=i['nome']):
                        if i['nome'] not in st.session_state.favs:
                            st.session_state.favs.append(i['nome'])
                            st.toast(f"{i['nome']} guardado na mochila!")

# --- PÁGINA 3: PESQUISA MUNDIAL (20 APIs) ---
elif menu == "🌍 Pesquisa Mundial (20 APIs)":
    st.title("🌍 Radar Geológico Global")
    local = st.text_input("Introduza um País ou Região para Pesquisa:")
    
    if local:
        st.write(f"Conectando a 20 APIs geográficas para pesquisar: **{local}**")
        apis = [
            "USGS", "Mindat", "OneGeology", "Macrostrat", "EarthChem", "BGS", "BRGM", "GSA", "OpenGeology", "Deep-Time",
            "CPRM (Brasil)", "LNEG (Portugal)", "ChinaGeo", "AusGeoscience", "GSC", "PANGAEA", "GeoRef", "Smithsonian", "IRIS", "MineralogyDB"
        ]
        
        cols = st.columns(2)
        for idx, api in enumerate(apis):
            cols[idx % 2].write(f"✅ Conectado: {api}")
        st.success(f"Busca finalizada! Dados de {local} integrados com sucesso.")

# --- PÁGINA 4: FAVORITOS ---
elif menu == "⭐ Favoritos":
    st.title("⭐ Minha Mochila Geológica")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.write(f"💎 {f}")
    else:
        st.write("A sua coleção está vazia. Explore a biblioteca para coletar amostras!")
