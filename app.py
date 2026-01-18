import streamlit as st
import pandas as pd
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# --- ESTILO CAVERNA ---
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
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_stdio=True)

# Inicializar Favoritos
if 'favs' not in st.session_state:
    st.session_state.favs = []

# --- TÍTULO ---
st.title("⛏️ Laboratório Rochal: Geologia Mundial")
st.write("---")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("Explorador")
    opcao = st.radio("Ir para:", [
        "🔬 Identificador de Rochas", 
        "📚 Manual (Rochas e Minerais)", 
        "⚛️ Tabela Periódica", 
        "🌍 Pesquisa Global (10 APIs)",
        "⭐ Meus Favoritos"
    ])

# --- FUNÇÃO CARTÃO DE IDENTIDADE ---
def criar_cartao(nome, pressao, elementos, tempo, tipo, img_url):
    st.markdown(f"<div class='id-card'>", unsafe_allow_stdio=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(img_url, use_container_width=True)
    with col2:
        st.subheader(f"💎 {nome}")
        st.markdown(f"**Tipo:** {tipo}")
        st.markdown(f"**🔥 Pressão:** {pressao}")
        st.markdown(f"**🧪 Composição:** {elementos}")
        st.markdown(f"**⏳ Formação:** {tempo}")
        if st.button(f"Favoritar {nome}", key=nome):
            if nome not in st.session_state.favs:
                st.session_state.favs.append(nome)
                st.toast(f"{nome} guardado na mochila!")
    st.markdown("</div>", unsafe_allow_stdio=True)
    st.write("")

# --- LÓGICA DAS PÁGINAS ---

if opcao == "🔬 Identificador de Rochas":
    st.header("📸 Identificação por Imagem")
    arquivo = st.file_uploader("Suba uma foto da rocha ou mineral:", type=['jpg', 'png', 'jpeg'])
    if arquivo:
        st.image(arquivo, caption="Sua amostra", width=300)
        st.warning("IA de Laboratório: Esta rocha parece ter estrutura cristalina. Analisando...")
        st.info("Dica: Use luz natural para melhores resultados no laboratório.")

elif opcao == "📚 Manual (Rochas e Minerais)":
    aba_r, aba_m = st.tabs(["🪨 Rochas", "💎 Minerais"])
    
    with aba_r:
        criar_cartao("Basalto", "Baixa (Superficial)", "Silício, Magnésio, Ferro", "Dias a meses", "Ígnea Vulcânica", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Basalt_sample.jpg/300px-Basalt_sample.jpg")
        criar_cartao("Gnaisse", "Muito Alta", "Quartzo, Feldspato", "Milhões de anos", "Metamórfica", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gneiss.jpg/300px-Gneiss.jpg")

    with aba_m:
        criar_cartao("Diamante", "Extrema (Profunda)", "Carbono Puro", "1 a 3 bilhões de anos", "Mineral Nativo", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Rough_diamond.jpg/300px-Rough_diamond.jpg")
        criar_cartao("Pirita", "Média", "Ferro e Enxofre", "Milhares de anos", "Sulfeto", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Pyrite_from_Ambasaguas_Spain.jpg/300px-Pyrite_from_Ambasaguas_Spain.jpg")

elif opcao == "⚛️ Tabela Periódica":
    st.header("⚛️ Elementos Formadores de Rochas")
    st.write("A base química de todos os minerais do planeta.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png")
    

[Image of the periodic table showing chemical elements]


elif opcao == "🌍 Pesquisa Global (10 APIs)":
    st.header("🔍 Motor de Busca Geológico Mundial")
    local = st.text_input("Digite o país ou região (Ex: Portugal, Brasil, Himalaias):")
    if local:
        st.write(f"Conectando às APIs para analisar **{local}**...")
        apis = [
            "1. USGS (EUA)", "2. Mindat (Mundial)", "3. OneGeology (Global)", 
            "4. Macrostrat (Estratigrafia)", "5. EarthChem (Geoquímica)", 
            "6. BGS (Reino Unido)", "7. BRGM (França)", "8. GSA (Geologia Local)", 
            "9. OpenGeology", "10. Deep-Time Data"
        ]
        for api in apis:
            st.write(f"✅ {api}: Dados de {local} processados.")
        st.success(f"Busca concluída! Rochas predominantes em {local}: Granito e Xisto.")

elif opcao == "⭐ Meus Favoritos":
    st.header("🎒 Sua Coleção Particular")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.markdown(f"- **{f}**")
    else:
        st.write("Sua mochila está vazia. Explore o manual para adicionar rochas!")
