import streamlit as st


def show_home():
    st.markdown('<div class="home-title">', unsafe_allow_html=True)
    st.title("Bem-vindo ao Classificador de Logotipos de Carros")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="home-content">', unsafe_allow_html=True)

    st.header("Sobre o Algoritmo")

    st.write(
        """
        Este projeto utiliza técnicas avançadas de visão computacional para identificar logotipos de carros em imagens. O algoritmo é baseado na análise de características de textura e forma dos logotipos, usando o Histograma de Gradientes Orientados (HOG) combinado com um classificador de máquina de vetores de suporte (SVM).

        ### Como Funciona:
        1. **Pré-processamento da Imagem**: A imagem do logotipo é convertida para escala de cinza e redimensionada para garantir uma análise consistente.
        2. **Extração de Características**: Utiliza-se o HOG para extrair características da imagem, que captura informações sobre as bordas e contornos.
        3. **Classificação**: As características extraídas são então usadas para prever a classe do logotipo usando um modelo de SVM treinado previamente.

        ### Precisão do Modelo:
        O modelo foi treinado com um conjunto de dados diversificado para reconhecer logotipos de marcas conhecidas, incluindo Audi, Ford, Honda, Subaru e Volkswagen. No entanto, a precisão pode variar dependendo da qualidade da imagem e das condições de iluminação.

        **Nota Importante**: Apesar de sua eficácia, o modelo pode cometer erros, especialmente quando a imagem do logotipo está borrada, mal iluminada ou parcialmente obstruída. A taxa de erro pode ser influenciada por fatores como:
        - **Qualidade da Imagem**: Imagens com baixa resolução ou com ruído podem reduzir a precisão da previsão.
        - **Variedade dos Logotipos**: Logotipos que são semelhantes entre si ou têm variações significativas podem ser mais difíceis de distinguir.
        - **Condições de Captura**: Diferenças na iluminação, ângulo e perspectiva da imagem podem impactar o desempenho do modelo.

        O objetivo é proporcionar uma ferramenta útil para a identificação de logotipos, mas é sempre bom considerar a margem de erro e verificar as previsões com base em outras fontes, se possível.
        """
    )

    st.write(
        """
        Utilize as abas laterais para explorar outras funcionalidades do sistema, como a **Previsão de Logotipos** e a visualização de **Gráficos** com análises detalhadas do desempenho do modelo.
        """
    )

    st.markdown('</div>', unsafe_allow_html=True)
