import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Mundo Rochal", layout="wide")

if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# --- BASE DE DADOS COM EMOJIS GEOLÓGICOS REAIS ---
base_geologica = [
    {
        "nome": "Basalto",
        "regiao": "Portugal (Madeira/Açores)",
        "cientifico": "Rocha Ígnea Vulcânica",
        "formacao": "🌋 Magmática (Cristalização em superfície)",
        "composicao": "🧪 Piroxena e Plagioclase (Rica em Fe/Mg)",
        "classe": "⚒️ Ígnea",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/400px-Basalt_sample.jpg"
    },
    {
        "nome": "Granito",
        "regiao": "Portugal (Norte e Centro)",
        "cientifico": "Rocha Ígnea Plutónica",
        "formacao": "🏔️ Magmática (Arrefecimento lento em profundidade)",
        "composicao": "🧪 Quartzo, Feldspato e Micas",
        "classe": "⚒️ Ígnea",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Granite_Yosemite_P1160483.jpg/400px-Granite_Yosemite_P1160483.jpg"
    },
    {
        "nome": "Arenito",
        "regiao": "Brasil (Bacia do Paraná)",
        "cientifico": "Rocha Sedimentar Detrítica",
        "formacao": "⏳ Deposição e Cimentação de Sedimentos",
        "composicao": "🧪 Grãos de Sílica e Óxidos",
        "classe": "🧱 Sedimentar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Sandstone_USGOV.jpg/400px-Sandstone_USGOV.jpg"
    },
    {
        "nome": "Xisto",
        "regiao": "Portugal (Trás-os-Montes / Douro)",
        "cientifico": "Rocha Metamórfica Foliada",
        "formacao": "⚙️ Metamorfismo de alta pressão e temperatura",
        "composicao": "🧪 Silicatos Lamelares e Micas",
        "classe": "🌀 Metamórfica",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Schist_P1040669.jpg/400px-Schist_P1040669.jpg"
    }
]

st.title("⚒️ Laboratório Mundo Rochal")

aba_explorar, aba_lab, aba_favoritos = st.tabs(["🌍 Tela Principal", "🔬 Laboratório Rochal", "⭐ Favoritos"])

# --- TELA 1: EXPLORAÇÃO POR REGIÕES ---
with aba_explorar:
    st.header("📍 Amostras por País e Região")
    escolha_regiao = st.selectbox("Filtrar Localização:", ["Todas", "Portugal", "Brasil"])
    
    cols = st.columns(2)
    contador = 0
    for r in base_geologica:
        if escolha_regiao == "Todas" or escolha_regiao in r["regiao"]:
            with cols[contador % 2]:
                with st.container(border=True):
                    st.image(r["img"], use_container_width=True)
                    st.subheader(f"💎 {r['nome']}")
                    st.write(f"**📍 REGIÃO:** {r['regiao']}")
                    st.write(f"**NOME CIENTÍFICO:**\n{r['cientifico']}")
                    st.write(f"**MÉTODO DE FORMAÇÃO:**\n{r['formacao']}")
                    st.write(f"**ALIMENTAÇÃO REAL (Química):**\n{r['composicao']}")
                    st.write(f"**CLASSE GEOLÓGICA:**\n{r['classe']}")
                    if st.button(f"⭐ Favoritar {r['nome']}", key=f"fav_{r['nome']}"):
                        if r['nome'] not in st.session_state.favoritos:
                            st.session_state.favoritos.append(r['nome'])
                            st.toast("Adicionado à coleção!")
            contador += 1

# --- TELA 2: LABORATÓRIO ROCHAL ---
with aba_lab:
    st.header("🔬 Laboratório de Análise")
    
    st.subheader("⚛️ Tabela Periódica (Referência de Composição)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_Table_by_Merck.png/1200px-Periodic_Table_by_Merck.png", use_container_width=True)
    
    st.divider()
    
    st.subheader("🔍 Pesquisa Global de Cartões")
    termo = st.text_input("Escreva o nome da rocha para abrir a ficha técnica:")
    
    if termo:
        encontrado = False
        for r in base_geologica:
            if termo.lower() in r["nome"].lower():
                encontrado = True
                with st.container(border=True):
                    c1, c2 = st.columns([1, 2])
                    with c1: st.image(r["img"], use_container_width=True)
                    with c2:
                        st.subheader(r["nome"])
                        st.write(f"**NOME CIENTÍFICO:** {r['cientifico']}")
                        st.write(f"**FORMAÇÃO:** {r['formacao']}")
                        st.write(f"**ALIMENTAÇÃO REAL:** {r['composicao']}")
        if not encontrado:
            st.warning("Rocha não encontrada na base local.")

# --- TELA 3: FAVORITOS ---
with aba_favoritos:
    st.header("⭐ A Minha Coleção")
    if st.session_state.favoritos:
        for f in st.session_state.favoritos:
            st.write(f"✅ Amostra de **{f}** certificada no laboratório.")
    else:
        st.write("A tua mochila está vazia.")
