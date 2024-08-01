import argparse
import imutils
import cv2
from sklearn.neighbors import KNeighborsClassifier
from skimage import exposure
from skimage import feature
from imutils import paths
import os
import joblib

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
for imagePath in paths.list_images(args["training"]):
    make = os.path.basename(os.path.dirname(imagePath))
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = imutils.auto_canny(gray)

    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)

    (x, y, w, h) = cv2.boundingRect(c)
    logo = gray[y:y + h, x:x + w]
    logo = cv2.resize(logo, (200, 100))

    H = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2), transform_sqrt=True)

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
