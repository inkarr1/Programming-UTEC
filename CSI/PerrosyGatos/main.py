import numpy as np
import os
import cv2
import random

DIRECTORIO = "Datasets"
CATEGORIAS = ["Gatos", "Perros"]
conjunto = []

for categoria in CATEGORIAS:

    indice = CATEGORIAS.index(categoria)
    ruta = os.path.join(DIRECTORIO, categoria)

    for img in os.listdir(ruta):
        img_array = cv2.imread(os.path.join(ruta, img), cv2.IMREAD_GRAYSCALE)
        print(img_array)
        print(img_array.shape)
        print("archivo:", img)
        print("------")
        nuevo_arreglo = cv2.resize(img_array, (100,100))
        #print(nuevo_arreglo)
        #print(nuevo_arreglo.shape)
        conjunto.append([nuevo_arreglo, indice])
print(len(conjunto))
#print(conjunto)
random.shuffle(conjunto)

X = []
y = []

for matriz, etiqueta in conjunto:
    X.append(matriz)
    y.append(etiqueta)

X = np.array(X).reshape(-1,100,100,1)
y = np.array(y)

print("---- estamos listos ----")

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPool2D

X = X/255.0

print(X.shape)

model = Sequential()

# en el primer Conv2D especificamos
model.add(Conv2D(64,(5,5), input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

#La salida es un solo nodo
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics= ['accun'])

model.fit(X,y, batch_size=32, epochs=12, validation_split=0.2)

def preparar(ruta_de_una_image):
    img_array = cv2.imread(ruta_de_una_image, cv2.IMREAD_GRAYSCALE)
    nuevo_arreglo = cv2.resize(img_array, (100,100))
    return nuevo_arreglo.reshape(-1,100,100,1)

prediccion = model.predict([preparar("Predecir/prueba1.jpg")])
print("La imagen prueba!.jpg es un", CATEGORIAS[int(prediccion[0,0])])