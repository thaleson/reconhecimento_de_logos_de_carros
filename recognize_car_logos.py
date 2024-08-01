import argparse
import imutils
import cv2
from sklearn.neighbors import KNeighborsClassifier
from skimage import exposure
from skimage import feature
from imutils import paths
import os


# Argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--training", required=True, help="Caminho para o dataset de treino")
ap.add_argument("-t", "--test", required=True, help="Caminho para o dataset de teste")
ap.add_argument("-m", "--model", required=True, help="Caminho para salvar o modelo treinado")

args = vars(ap.parse_args())

# Inicializa a matriz de dados e de labels
print("Extraindo recursos...")
data = []
labels = []

# Loop pelas imagens no dataset de treino
for imagePath in paths.list_images(args["training"])

    # Obtenha o nome da pasta pai

    make = os.path.basename(os.path.dirname(imagePath))
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = imutils.auto_canny(gray)


    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)


    # Encontra contornos no mapa de borda, mantendo apenas o maior que se supõe ser o logotipo do carro
    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)

    # Extrai o logotipo do carro e redimensiona

    (x, y, w, h) = cv2.boundingRect(c)
    logo = gray[y:y + h, x:x + w]
    logo = cv2.resize(logo, (200, 100))


    H = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2), transform_sqrt=True)

    # Extrai Histograma de Gradientes Orientados do logotipo
    H = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2), transform_sqrt=True)

    # Atualiza dados e labels

    data.append(H)
    labels.append(make)

# Treina o Classificador Nearest Neighbors
print("Treinando o Classificador...")
model = KNeighborsClassifier(n_neighbors=1)
model.fit(data, labels)


# Salva o modelo treinado
print("Salvando o modelo...")
joblib.dump(model, args["model"])
print(f"Modelo salvo em {args['model']}")

# Avaliação e visualização podem ser adicionadas aqui, se necessário

# Loop no dataset de teste
print("Avaliando...")
for (i, imagePath) in enumerate(paths.list_images(args["test"])):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logo = cv2.resize(gray, (200, 100))

    # Extrai o Histograma de Gradientes Orientados da imagem de teste e prevê a marca do carro
    H, hogImage = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2), transform_sqrt=True, visualize=True)
    pred = model.predict(H.reshape(1, -1))[0]

    # Visualiza a imagem HOG
    hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
    hogImage = hogImage.astype("uint8")
    cv2.imshow("HOG Image #{}".format(i + 1), hogImage)

    # Print das previsões
    cv2.putText(image, pred.title(), (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
    cv2.imshow("Test Image #{}".format(i + 1), image)
    cv2.waitKey(0)

cv2.destroyAllWindows()

