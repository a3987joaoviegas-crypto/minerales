import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Laboratório Rochal", layout="wide", page_icon="⛏️")

# 2. Inicializar Favoritos
if 'favs' not in st.session_state:
    st.session_state.favs = []

# --- MENU LATERAL ---
st.sidebar.title("⚒️ LAB ROCHAL")
menu = st.sidebar.radio("Navegação:", ["🏠 Laboratório", "⭐ Meus Favoritos"])

# --- PÁGINA PRINCIPAL ---
if menu == "🏠 Laboratório":
    st.title("⛏️ Laboratório Rochal")
    
    # Seção 1: Tabela Periódica
    st.header("⚛️ Tabela Periódica Geológica")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Periodic_Table_by_Merck.png/1200px-Periodic_Table_by_Merck.png", use_container_width=True)
    
    st.divider()

    # Seção 2: Biblioteca de Rochas e Minerais
    st.header("📚 Biblioteca Geológica")
    
    itens = [
        {"nome": "Basalto", "classe": "Ígnea", "pressao": "Baixa (Vulcânica)", "elementos": "Fe, Mg, Ca", "tempo": "Rápido", "img": "https://images.unsplash.com/photo-1515462277126-2dd0c162007a?w=600"},
        {"nome": "Granito", "classe": "Ígnea", "pressao": "Alta (Plutónica)", "elementos": "Si, Al, K", "tempo": "Milhares de anos", "img": "https://images.unsplash.com/photo-1533038595788-da570932e604?w=600"},
        {"nome": "Mármore", "classe": "Metamórfica", "pressao": "Alta", "elementos": "Carbonato de Cálcio", "tempo": "Milhões de anos", "img": "https://images.unsplash.com/photo-1620215175664-cb9a6f5b6103?w=600"},
        {"nome": "Quartzo", "classe": "Mineral", "pressao": "Variável", "elementos": "Dióxido de Silício", "tempo": "Lento", "img": "https://images.unsplash.com/photo-1567095761054-7a02e69e5c43?w=600"}
    ]

    # Grelha de Exibição
    for i in range(0, len(itens), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(itens[i]["nome"])
            st.image(itens[i]["img"], use_container_width=True)
            st.write(f"**Classe:** {itens[i]['classe']} | **🔥 Pressão:** {itens[i]['pressao']}")
            st.write(f"**🧪 Química:** {itens[i]['elementos']} | **⏳ Tempo:** {itens[i]['tempo']}")
            if st.button(f"⭐ Guardar {itens[i]['nome']}", key=itens[i]['nome']):
                if itens[i]['nome'] not in st.session_state.favs:
                    st.session_state.favs.append(itens[i]['nome'])
                    st.toast(f"{itens[i]['nome']} guardado!")

        if i+1 < len(itens):
            with col2:
                st.subheader(itens[i+1]["nome"])
                st.image(itens[i+1]["img"], use_container_width=True)
                st.write(f"**Classe:** {itens[i+1]['classe']} | **🔥 Pressão:** {itens[i+1]['pressao']}")
                st.write(f"**🧪 Química:** {itens[i+1]['elementos']} | **⏳ Tempo:** {itens[i+1]['tempo']}")
                if st.button(f"⭐ Guardar {itens[i+1]['nome']}", key=itens[i+1]['nome']):
                    if itens[i+1]['nome'] not in st.session_state.favs:
                        st.session_state.favs.append(itens[i+1]['nome'])
                        st.toast(f"{itens[i+1]['nome']} guardado!")

# --- PÁGINA FAVORITOS ---
elif menu == "⭐ Meus Favoritos":
    st.title("⭐ Minha Coleção")
    if st.session_state.favs:
        for f in st.session_state.favs:
            st.write(f"### 💎 {f}")
    else:
        st.write("Mochila vazia.")
