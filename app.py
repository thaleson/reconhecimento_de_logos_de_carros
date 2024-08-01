import streamlit as st
import joblib
from pages.pages1 import home, previsao, graficos
from streamlit_option_menu import option_menu

# Função para carregar o CSS
def load_css():
    with open("assets/styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Definir configurações da página
st.set_page_config(
    page_title="Reconhecimento de Logotipos de Carros",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Carregar o CSS personalizado
load_css()

# Carregar o modelo treinado
model = joblib.load("assets/data/model.pkl")

# Menu lateral estilizado com ícones
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Previsão", "Gráficos"],
        icons=["house", "camera", "bar-chart"],
        menu_icon="cast",
        default_index=0,

    )

# Renderizar o conteúdo baseado na seleção do menu
if selected == "Home":
    home.show_home()
elif selected == "Previsão":
    previsao.show_previsao(model)
elif selected == "Gráficos":
    graficos.show_graficos()
