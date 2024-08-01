# 🚗 **Reconhecimento de Logos de Carros Usando HOG e Machine Learning**

## 📜 Descrição

Este projeto visa a detecção e reconhecimento de logos de carros utilizando **Histograma de Gradientes Orientados (HOG)** e um classificador **K-Nearest Neighbors (KNN)**. Utilizamos técnicas avançadas de visão computacional para extrair características visuais dos logos e classificá-los corretamente.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **OpenCV**: Biblioteca de visão computacional
- **scikit-image**: Implementação do HOG
- **scikit-learn**: Classificador KNN
- **imutils**: Utilitários de imagem

## 🚀 Como Usar

### 1. Clonar o Repositório

Clone o repositório para o seu computador:

```bash
git clone https://github.com/thaleson/reconhecimento_de_logos_de_carros
cd seu-repositorio
```

### 2. Configurar o Ambiente

#### Usando `venv` (Virtual Environment)

Crie e ative um ambiente virtual:

- **Windows**:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

- **macOS / Linux**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 3. Preparar o Dataset

- **Treinamento**: Coloque suas imagens de logos de carros em um diretório de treinamento (por exemplo, `car_logos`).
- **Teste**: Coloque suas imagens de teste em um diretório de teste (por exemplo, `test_images`).

### 4. Executar o Código

#### Treinamento e Teste

Execute o script para treinar o classificador e testar o reconhecimento de logos:

```bash
python recognize_car_logos.py --training car_logos --test test_images
```

### 5. Estrutura do Projeto

```
/seu-repositorio
│
├── recognize_car_logos.py  # Script principal para reconhecimento de logos
├── requirements.txt        # Dependências do projeto
├── car_logos/              # Diretório contendo imagens para treinamento
└── test_images/            # Diretório contendo imagens para teste
```

## 📝 Notas

- Certifique-se de que a estrutura do diretório esteja correta e que os diretórios `car_logos` e `test_images` contenham imagens no formato suportado.
- O código está configurado para usar imagens JPEG. Se você usar um formato diferente, ajuste o código e o parâmetro `glob.glob` conforme necessário.

## 🔧 Como Funciona

1. **Extração de Recursos**: O sistema extrai características dos logos usando o descritor HOG.
2. **Treinamento**: Um classificador KNN é treinado com os vetores de características dos logos.
3. **Reconhecimento**: O classificador é utilizado para prever e identificar logos em novas imagens de teste.

## 📚 Documentação

Para mais informações sobre as bibliotecas usadas, consulte a documentação oficial:
- [OpenCV](https://docs.opencv.org/)
- [scikit-image](https://scikit-image.org/docs/)
- [scikit-learn](https://scikit-learn.org/stable/documentation.html)
- [imutils](https://github.com/jrosebr1/imutils)

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões para melhorias, abra uma issue ou envie um pull request.

## 📝 Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

