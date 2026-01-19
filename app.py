import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Mundo Rochal", layout="wide")

if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# --- BASE DE DADOS COMPLETA COM FICHA TÉCNICA ---
# Incluindo Rochas e Minerais de vários países
base_dados = [
    {
        "nome": "Basalto",
        "tipo": "Rocha",
        "pais": "Portugal",
        "regiao": "Ilhas (Madeira/Açores)",
        "cientifico": "Rocha Ígnea Vulcânica",
        "formacao": "🌋 Magmática (Cristalização rápida)",
        "quimica": "🧪 Piroxena e Plagioclase (Rica em Fe/Mg)",
        "classe": "⚒️ Ígnea",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/400px-Basalt_sample.jpg"
    },
    {
        "nome": "Diamante",
        "tipo": "Mineral",
        "pais": "África do Sul",
        "regiao": "Kimberley",
        "cientifico": "Carbono Cristalizado",
        "formacao": "⚙️ Metamorfismo de Pressão Extrema",
        "quimica": "🧪 Carbono Puro (C)",
        "classe": "💎 Mineral Nativo",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Rough_diamond.jpg/400px-Rough_diamond.jpg"
    },
    {
        "nome": "Granito",
        "tipo": "Rocha",
        "pais": "Portugal",
        "regiao": "Norte e Centro",
        "cientifico": "Rocha Ígnea Plutónica",
        "formacao": "🏔️ Magmática (Arrefecimento em profundidade)",
        "quimica": "🧪 Quartzo, Feldspato e Micas",
        "classe": "⚒️ Ígnea",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Granite_Yosemite_P1160483.jpg/400px-Granite_Yosemite_P1160483.jpg"
    },
    {
        "nome": "Ametista",
        "tipo": "Mineral",
        "pais": "Uruguai",
        "regiao": "Artigas",
        "cientifico": "Variedade de Quartzo (Roxo)",
        "formacao": "🧪 Cristalização Hidrotérmica em Geodos",
        "quimica": "🧪 SiO2 com traços de Ferro",
        "classe": "💎 Mineral",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Amethyst._Magaliesburg%2C_South_Africa.jpg/400px-Amethyst._Magaliesburg%2C_South_Africa.jpg"
    },
    {
        "nome": "Arenito",
        "tipo": "Rocha",
        "pais": "Brasil",
        "regiao": "Bacia do Paraná",
        "cientifico": "Rocha Sedimentar Detrítica",
        "formacao": "⏳ Deposição e Cimentação de Areias",
        "quimica": "🧪 Grãos de Sílica",
        "classe": "🧱 Sedimentar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Sandstone_USGOV.jpg/400px-Sandstone_USGOV.jpg"
    },
    {
        "nome": "Lápis-lazúli",
        "tipo": "Mineral",
        "pais": "Afeganistão",
        "regiao": "Badakhshan",
        "cientifico": "Rocha/Mineral Metamórfico Azul",
        "formacao": "🌀 Metamorfismo de Contacto",
        "quimica": "🧪 Lazurite, Calcite e Pirite",
        "classe": "💎 Mineral/Gema",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Lapis-lazuli_from_Afghanistan.jpg/400px-Lapis-lazuli_from_Afghanistan.jpg"
    }
]

st.title("⚒️ Centro de Pesquisa Mundo Rochal")

# --- BARRA LATERAL: FILTRO DE PAÍSES ---
with st.sidebar:
    st.header("🌎 Centro de Pesquisa")
    lista_paises = sorted(list(set([r["pais"] for r in base_dados])))
    pais_selecionado = st.selectbox("Escolha o País:", ["Todos os Países"] + lista_paises)

# --- TELA PRINCIPAL: ABAS ---
aba_explorar, aba_lab, aba_favoritos = st.tabs(["🏠 Tela Principal", "🔬 Laboratório Rochal", "⭐ Favoritos"])

# --- TELA 1: EXPLORAÇÃO POR LISTAS (ROCHAS, MINERAIS, TUDO) ---
with aba_explorar:
    st.header(f"📍 Catálogo de Amostras: {pais_selecionado}")
    
    # Filtro de Categoria (Rochas, Minerais ou Tudo)
    categoria = st.radio("Mostrar apenas:", ["Tudo (Rochas + Minerais)", "Rochas", "Minerais"], horizontal=True)
    
    # Filtragem Lógica
    amostras_filtradas = base_dados
    if pais_selecionado != "Todos os Países":
        amostras_filtradas = [r for r in amostras_filtradas if r["pais"] == pais_selecionado]
    
    if categoria == "Rochas":
        amostras_filtradas = [r for r in amostras_filtradas if r["tipo"] == "Rocha"]
    elif categoria == "Minerais":
        amostras_filtradas = [r for r in amostras_filtradas if r["tipo"] == "Mineral"]

    # Exibição em Cartões com Ficha Técnica
    cols = st.columns(2)
    for i, r in enumerate(amostras_filtradas):
        with cols[i % 2]:
            with st.container(border=True):
                st.image(r["img"], use_container_width=True)
                st.subheader(f"{r['nome']} ({r['pais']})")
                st.write(f"**NOME CIENTÍFICO**\n\n{r['cientifico']}")
                st.write(f"**MÉTODO DE FORMAÇÃO**\n\n{r['formacao']}")
                st.write(f"**ALIMENTAÇÃO REAL (Química)**\n\n{r['quimica']}")
                st.write(f"**CLASSE GEOLÓGICA**\n\n{r['classe']}")
                if st.button(f"⭐ Favoritar {r['nome']}", key=f"f_{r['nome']}"):
                    if r['nome'] not in st.session_state.favoritos:
                        st.session_state.favoritos.append(r['nome'])
                        st.toast(f"{r['nome']} guardado!")

# --- TELA 2: LABORATÓRIO (TABELA E PESQUISA LIVRE) ---
with aba_lab:
    st.header("🔬 Laboratório de Análise Geológica")
    
    # Tabela Periódica
    st.subheader("⚛️ Tabela Periódica (Composição dos Minerais)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_Table_by_Merck.png/1200px-Periodic_Table_by_Merck.png", use_container_width=True)
    

[Image of the periodic table showing chemical elements]


    st.divider()
    
    st.subheader("🔍 Pesquisa de Amostras Certificadas")
    busca = st.text_input("Introduza o nome da amostra:")
    
    if busca:
        resultados = [r for r in base_dados if busca.lower() in r["nome"].lower()]
        if resultados:
            for res in resultados:
                with st.container(border=True):
                    c1, c2 = st.columns([1, 2])
                    with c1: st.image(res["img"], use_container_width=True)
                    with c2:
                        st.subheader(res["nome"])
                        st.write(f"**ORIGEM:** {res['pais']} - {res['regiao']}")
                        st.write(f"**CIENTÍFICO:** {res['cientifico']}")
                        st.write(f"**FORMAÇÃO:** {res['formacao']}")
                        st.write(f"**QUÍMICA:** {res['quimica']}")
        else:
            st.warning("Amostra não encontrada na base de dados.")

with aba_favoritos:
    st.header("⭐ Minha Mochila Geológica")
    if st.session_state.favoritos:
        for f in st.session_state.favoritos:
            st.write(f"✅ Amostra de **{f}** pronta para estudo.")
    else:
        st.write("A tua coleção está vazia.")
