import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Laboratório Rochal", layout="wide")

# Inicializar a coleção (favoritos)
if 'colecao' not in st.session_state:
    st.session_state.colecao = []

st.title("⚒️ Laboratório Rochal")

# 2. TABELA PERIÓDICA (No topo, conforme pedido)
st.header("⚛️ Tabela Periódica dos Elementos")
st.write("Base química de todos os minerais e rochas.")
st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Periodic_Table_by_Merck.png", use_container_width=True)

st.divider()

# 3. BIBLIOTECA GEOLÓGICA (Ordem por Classes)
st.header("📚 Biblioteca e Identificador")

# Seletor de Classe (Igual à app dos animais)
classe_selecionada = st.selectbox("Selecione a Classe:", 
                                 ["Todas", "Rochas Ígneas", "Rochas Metamórficas", "Rochas Sedimentares", "Minerais"])

# Dados Unificados (Rochas e Minerais na mesma biblioteca)
dados = [
    {"nome": "Basalto", "classe": "Rochas Ígneas", "pressao": "Baixa", "elementos": "Ferro e Magnésio", "tempo": "Dias", "img": "https://images.unsplash.com/photo-1515462277126-2dd0c162007a?w=400"},
    {"nome": "Mármore", "classe": "Rochas Metamórficas", "pressao": "Alta", "elementos": "Carbonato de Cálcio", "tempo": "Milhões de anos", "img": "https://images.unsplash.com/photo-1620215175664-cb9a6f5b6103?w=400"},
    {"nome": "Arenito", "classe": "Rochas Sedimentares", "pressao": "Baixa", "elementos": "Silício e Oxigénio", "tempo": "Longo", "img": "https://images.unsplash.com/photo-1590218121117-0824961547a4?w=400"},
    {"nome": "Quartzo", "classe": "Minerais", "pressao": "Média", "elementos": "SiO2", "tempo": "Lento", "img": "https://images.unsplash.com/photo-1567095761054-7a02e69e5c43?w=400"},
    {"nome": "Pirita", "classe": "Minerais", "pressao": "Variável", "elementos": "FeS2", "tempo": "Geológico", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Pyrite_from_Ambasaguas_Spain.jpg/320px-Pyrite_from_Ambasaguas_Spain.jpg"}
]

# Exibição dos Cartões
for item in dados:
    if classe_selecionada == "Todas" or item["classe"] == classe_selecionada:
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(item["img"], use_container_width=True)
            with col2:
                st.subheader(item["nome"])
                st.write(f"**Classe:** {item['classe']}")
                st.write(f"**Composição Química:** {item['elementos']}")
                st.write(f"**Pressão de Formação:** {item['pressao']}")
                st.write(f"**Tempo Estimado:** {item['tempo']}")
                
                if st.button(f"⭐ Adicionar {item['nome']} à Coleção", key=item['nome']):
                    if item['nome'] not in st.session_state.colecao:
                        st.session_state.colecao.append(item['nome'])
                        st.toast(f"{item['nome']} adicionado!")

st.divider()

# 4. MINHA COLEÇÃO (Favoritos no final)
st.header("⭐ Minha Coleção Particular")
if st.session_state.colecao:
    st.info(f"Itens na mochila: {', '.join(st.session_state.colecao)}")
else:
    st.write("A tua mochila geológica está vazia.")
