import numpy as np
import os
import cv2

directorio = "Datasets"
categorias = ["Gatos", "Perros"]

for categoria in categorias:
    path = os.path.join(directorio, categoria)

    for image in os.listdir
