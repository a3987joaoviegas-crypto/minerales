import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Mundo Rochal", layout="wide")

# Inicializar favoritos na memória do navegador
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# --- 1. BARRA LATERAL (BIBLIOTECA ESTILO MUNDO VIVO) ---
with st.sidebar:
    st.header("📚 Biblioteca Geológica")
    
    # Base de Dados com Fichas Técnicas idênticas ao teu modelo
    rochas = [
        {
            "nome": "Basalto",
            "cientifico": "Rocha Ígnea Mafica",
            "formacao": "🧬 Magmática (Vulcânica)",
            "composicao": "🍴 Rica em Magnésio e Ferro",
            "classe": "🏷️ Ígnea",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg"
        },
        {
            "nome": "Quartzo",
            "cientifico": "Dióxido de Silício (SiO2)",
            "formacao": "🧬 Cristalização Hidrotérmica",
            "composicao": "🍴 Silício e Oxigénio",
            "classe": "🏷️ Mineral",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Quartz_Crystal.jpg/300px-Quartz_Crystal.jpg"
        },
        {
            "nome": "Mármore",
            "cientifico": "Calcário Recristalizado",
            "formacao": "🧬 Metamorfismo Regional",
            "composicao": "🍴 Carbonato de Cálcio",
            "classe": "🏷️ Metamórfica",
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Marble-textures.jpg/300px-Marble-textures.jpg"
        }
    ]

    for r in rochas:
        with st.expander(f"💎 {r['nome']}"):
            st.image(r["img"], use_container_width=True)
            st.write(f"**NOME CIENTÍFICO**\n\n{r['cientifico']}")
            st.write(f"**MÉTODO DE FORMAÇÃO**\n\n{r['formacao']}")
            st.write(f"**ALIMENTAÇÃO REAL** (Composição)\n\n{r['composicao']}")
            st.write(f"**CLASSE GEOLÓGICA**\n\n{r['classe']}")
            if st.button(f"⭐ Favoritar {r['nome']}", key=f"fav_{r['nome']}"):
                if r['nome'] not in st.session_state.favoritos:
                    st.session_state.favoritos.append(r['nome'])
                    st.toast(f"{r['nome']} guardado!")

# --- 2. TELA PRINCIPAL (ABAS DE NAVEGAÇÃO) ---
st.title("⚒️ Mundo Rochal")

aba1, aba2, aba3 = st.tabs(["🏠 Tela Principal", "🔬 Laboratório Rochal", "⭐ Favoritos"])

with aba1:
    st.header("🌍 Exploração por Regiões")
    st.write("Consulta a geodiversidade mundial por continente.")
    # Link estável para o Mapa Geológico
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/World_geology_map_full.png/1200px-World_geology_map_full.png", caption="Mapa de Regiões Geológicas", use_container_width=True)
    
    regiao = st.selectbox("Escolha uma Região:", ["Portugal", "Brasil", "Islândia", "Grand Canyon"])
    st.info(f"A mostrar amostras típicas da região: {regiao}")

with aba2:
    st.header("🔬 Laboratório de Análise")
    
    # Tabela Periódica (Referência Química)
    st.subheader("⚛️ Tabela Periódica dos Elementos")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_Table_by_Merck.png/1200px-Periodic_Table_by_Merck.png", use_container_width=True)

    st.divider()
    
    # Pesquisa Profissional (Filtro para não aparecer imagens erradas)
    st.subheader("🔍 Pesquisa Global (20 APIs)")
    busca = st.text_input("Nome da rocha para pesquisa profunda:")
    
    if busca:
        # O filtro técnico evita "lixo" nos resultados
        query_limpa = f"{busca} geology specimen rock mineral professional"
        st.success(f"Pesquisa filtrada ativa para: {busca}")
        
        apis = {
            "Mindat (Fotos Reais)": f"https://www.mindat.org/search.php?search={query_limpa}",
            "USGS (Oficial)": f"https://www.usgs.gov/search?keywords={query_limpa}",
            "Smithsonian": f"https://collections.nmnh.si.edu/search/minerals/?q={query_limpa}",
            "WebMineral": f"http://www.webmineral.com/search.php?search={query_limpa}",
            "Mineral Atlas": f"http://www.mineralatlas.eu/search.php?search={query_limpa}"
        }
        
        cols = st.columns(3)
        for i, (nome, url) in enumerate(apis.items()):
            cols[i % 3].link_button(nome, url, use_container_width=True)

with aba3:
    st.header("⭐ Amostras Favoritas")
    if st.session_state.favoritos:
        for f in st.session_state.favoritos:
            st.write(f"💎 **{f}**")
    else:
        st.write("Ainda não tens rochas guardadas nos favoritos.")
