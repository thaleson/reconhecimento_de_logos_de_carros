import matplotlib.pyplot as plt
import streamlit as st


def generate_plots():
    # Exemplo de gráfico fictício
    st.write("Desempenho do modelo.")
    fig, ax = plt.subplots()
    ax.bar(["Audi", "Ford", "Honda", "Subaru", "Volkswagen"], [80, 70, 90, 60, 85])
    ax.set_ylabel('Acurácia (%)')
    ax.set_title('Desempenho do Modelo por Classe')
    st.pyplot(fig)
