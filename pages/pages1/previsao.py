import streamlit as st
import cv2
import numpy as np
from src.predict import predict

def show_previsao(model):
    st.header("Previsão de Logotipos")
    st.info("Certifique-se de que a imagem do logotipo esteja bem clara e centralizada.")
    st.warning("Classes suportadas: Audi, Ford, Honda, Subaru, Volkswagen.")
    uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.image(image, channels="BGR")

        if st.button("Fazer Previsão"):
            st.write("Realizando previsão...")
            progress_bar = st.progress(0)
            progress_bar.progress(50)

            pred, confidence = predict(image, model)

            progress_bar.progress(100)
            st.success(f"A marca do carro é: {pred.title()} com {confidence:.2%} de confiança.")
