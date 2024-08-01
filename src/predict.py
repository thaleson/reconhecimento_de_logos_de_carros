import cv2
import numpy as np
from skimage import feature


def predict(image, model):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    logo = cv2.resize(gray, (200, 100))
    H = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2), transform_sqrt=True)
    probas = model.predict_proba(H.reshape(1, -1))[0]
    max_index = np.argmax(probas)
    pred = model.classes_[max_index]
    confidence = probas[max_index]
    return pred, confidence
