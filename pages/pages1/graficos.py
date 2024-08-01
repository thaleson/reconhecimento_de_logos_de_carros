import streamlit as st
from src.plots import generate_plots

def show_graficos():
    st.header("Gráficos")
    st.write("Visualizações e análises dos dados de treinamento e desempenho do modelo.")
    generate_plots()
