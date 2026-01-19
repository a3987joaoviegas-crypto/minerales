import streamlit as st

# Configuração da página
st.set_page_config(page_title="Laboratório Rochal", layout="wide")

# Inicializar favoritos
if 'colecao' not in st.session_state:
    st.session_state.colecao = []

st.title("⚒️ Laboratório Rochal")

# 1. TABELA PERIÓDICA (No início)
st.header("⚛️ Tabela Periódica dos Elementos")
st.write("Estes são os elementos químicos que formam os minerais e as rochas.")
st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png", use_container_width=True)


[Image of the periodic table showing chemical elements]


st.divider()

# 2. BIBLIOTECA E IDENTIFICADOR (Estilo Classes de Animais)
st.header("📚 Identificador e Biblioteca Rochal")

# Lista de Classes (como nos animais)
classe = st.selectbox("Selecione a Classe Geológica:", 
                     ["Todas", "Rochas Ígneas", "Rochas Metamórficas", "Rochas Sedimentares", "Minerais Silicatos"])

# Dados (Minerais e Rochas juntos)
dados = [
    {"nome": "Basalto", "classe": "Rochas Ígneas", "pressao": "Baixa", "elementos": "Fe, Mg", "tempo": "Dias", "img": "https://images.unsplash.com/photo-1515462277126-2dd0c162007a?w=400"},
    {"nome": "Mármore", "classe": "Rochas Metamórficas", "pressao": "Alta", "elementos": "Ca, C, O", "tempo": "Milhões de anos", "img": "https://images.unsplash.com/photo-1620215175664-cb9a6f5b6103?w=400"},
    {"nome": "Arenito", "classe": "Rochas Sedimentares", "pressao": "Baixa", "elementos": "Si, O", "tempo": "Longo", "img": "https://images.unsplash.com/photo-1590218121117-0824961547a4?w=400"},
    {"nome": "Quartzo", "classe": "Minerais Silicatos", "pressao": "Média", "elementos": "SiO2", "tempo": "Lento", "img": "https://images.unsplash.com/photo-1567095761054-7a02e69e5c43?w=400"}
]

# Filtragem e Exibição
for item in dados:
    if classe == "Todas" or item["classe"] == classe:
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(item["img"], use_container_width=True)
            with col2:
                st.subheader(item["nome"])
                st.write(f"**Classe:** {item['classe']}")
                st.write(f"**Composição:** {item['elementos']}")
                st.write(f"**Tempo de Formação:** {item['tempo']}")
                if st.button(f"Adicionar à Coleção: {item['nome']}", key=item['nome']):
                    if item['nome'] not in st.session_state.colecao:
                        st.session_state.colecao.append(item['nome'])
                        st.success(f"{item['nome']} guardado!")

st.divider()

# 3. MINHA COLEÇÃO (Favoritos)
st.header("⭐ Minha Coleção Particular")
if st.session_state.colecao:
    st.write(", ".join(st.session_state.colecao))
else:
    st.write("Nenhum exemplar selecionado.")
