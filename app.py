import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Laboratório Rochal", layout="wide")

# Inicializar a coleção na memória
if 'colecao' not in st.session_state:
    st.session_state.colecao = []

st.title("⚒️ Laboratório Rochal")

# 2. TABELA PERIÓDICA NO TOPO
st.header("⚛️ Tabela Periódica Geológica")
st.write("Elementos químicos fundamentais que constituem as rochas e minerais.")
# Link estável para a imagem da tabela
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_Table_by_Merck.png/1200px-Periodic_Table_by_Merck.png", use_container_width=True)

st.divider()

# 3. BIBLIOTECA E IDENTIFICADOR POR CLASSES
st.header("📚 Biblioteca e Identificador")

# Seletor de Classe Geológica
classe_alvo = st.selectbox("Escolha a Classe:", 
                          ["Todas", "Rochas Ígneas", "Rochas Metamórficas", "Rochas Sedimentares", "Minerais"])

# Dados (Rochas e Minerais juntos na mesma lista)
base_dados = [
    {"nome": "Basalto", "classe": "Rochas Ígneas", "compo": "Ferro e Magnésio", "tempo": "Dias", "img": "https://images.unsplash.com/photo-1515462277126-2dd0c162007a?w=400"},
    {"nome": "Mármore", "classe": "Rochas Metamórficas", "compo": "Carbonato de Cálcio", "tempo": "Milhões de anos", "img": "https://images.unsplash.com/photo-1620215175664-cb9a6f5b6103?w=400"},
    {"nome": "Arenito", "classe": "Rochas Sedimentares", "compo": "Silício", "tempo": "Milhares de anos", "img": "https://images.unsplash.com/photo-1590218121117-0824961547a4?w=400"},
    {"nome": "Quartzo", "classe": "Minerais", "compo": "Dióxido de Silício", "tempo": "Lento", "img": "https://images.unsplash.com/photo-1567095761054-7a02e69e5c43?w=400"}
]

# Exibição dos itens filtrados
for r em base_dados:
    if classe_alvo == "Todas" ou r["classe"] == classe_alvo:
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(r["img"], use_container_width=True)
            with col2:
                st.subheader(r["nome"])
                st.write(f"**Classe**: {r['classe']}")
                st.write(f"**Composição**: {r['compo']}")
                st.write(f"**Tempo de Formação**: {r['tempo']}")
                
                if st.button(f"⭐ Guardar {r['nome']}", key=r['nome']):
                    if r['nome'] não em st.session_state.colecao:
                        st.session_state.colecao.append(r['nome'])
                        st.toast(f"{r['nome']} guardado!")

st.divider()

# 4. MINHA COLEÇÃO (Final da página)
st.header("⭐ Minha Coleção Particular")
se st.session_state.colecao:
    st.write("Itens guardados: " + ", ".join(st.session_state.colecao))
